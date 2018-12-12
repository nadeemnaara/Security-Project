
# global imports
import re

# local imports
from packet_parser import PacketParser
from database import DataBase
from tools import assert_and_raise


class FilterProcedure(PacketParser):

    __deps = {'dep': [],
              'office_loc': ['dep'],
              'items_issued': ['dep', 'job_title'],
              'job_title': ['dep'],
              'bank_no': [],
              'bank_section': ['bank_no'],
              'money_amount': ['dep', 'job_title']
              }

    def __init__(self, data, packet_id, separator):
        """
        class constructor.
        :param data: the packet to filter.
        :param packet_id: the id of the packet - given by the server - integer.
        :param separator: the separator used to separate between the fields of the packet.
        """
        PacketParser.__init__(self, data, separator)
        self._packet_id = packet_id

    # ------------------------------------------------------------------------

    def run(self):
        """
        applies the filtering rules on the packet.
        in case of failure in one of the rules, the packet will be dropped.
        :return: 0 if the packet passed the filtering procedure, 1 otherwise.
        """
        rc = 0
        action = 'FORWARD'
        err = ''
        try:
            parsed_packet = self.parse()
            opcode = parsed_packet[0][1]

            # variables to be used in the for loop bellow.
            first_and_last_name = []
            dates = []
            helper_dict = {'country': '', 'dep': '', 'bank_no': '', 'job_title': ''}

            for field, value in parsed_packet[1:]:
                # problematic names for dependencies check.
                if re.match('^[f,l]name', field):
                    field = 'name'
                if re.match('^(sub|due)_date', field):
                    field = 'date'
                if re.match('^appoval', field):
                    field = 'approval'

                if field == 'name':
                    first_and_last_name.append(value)
                if field in helper_dict.keys():
                    helper_dict[field] = value

                if field not in self.__deps.keys():
                    continue

                if field == 'date':
                    dates.append(value)
                    if len(dates) == 2:
                        d1, m1, y1 = map(int, dates[0].split('/'))
                        d2, m2, y2 = map(int, dates[1].split('/'))
                        assert_and_raise(y2 >= y1 and m2 >= m1 and d2 >= d1)
                elif field == 'signature' and opcode == '1':
                    expected_sig = first_and_last_name[0][0] + first_and_last_name[1][0]
                    assert_and_raise(value == expected_sig, 'signature is {}, expected: {}'.format(value, expected_sig))

                elif field == 'approval':
                    app_dep = value.split('-')[0]
                    assert_and_raise(app_dep in DataBase.query(helper_dict['country']), 'one of the approval fields not valid.')
                else:
                    deps_values = [helper_dict['country']]
                    for dep in self.__deps[field]:
                        deps_values += [dep, helper_dict[dep]]
                    assert_and_raise(value in DataBase.query(deps_values + [field]), 'field:{} value:{}, expected one of:{}'.format(field,
                                                                                                                          value,
                                                                                                     DataBase.query(deps_values)))

        except Exception as exp:
            err = str(exp)
            raise exp
            action = 'DROP'
            rc = 1

        self._print_table(self._packet_id, action, err)
        return rc

    # ------------------------------------------------------------------------

    def _print_table(self, packet_id, action, reason=''):
        """
        prints the following table
        the format:
        ====================================================================
        ## filtering stats:
        ====================================================================
        | packet id |  action | reason (if not FORWARD)  |
        ====================================================================
        | id        |  DROP   |  size not valid.         |
        ====================================================================

        :param: packet_id: integer.
        :param: action: FORWARD/DROP
        :param reason: string.
        """
        line_format = ''
        for i in range(60):
            line_format += '='
        print(line_format)
        print('## filtering Stats:')
        print(line_format)
        print('| {} |  {}  |  {}  |'.format('packet id', 'action', 'reason (if not FORWARD)'))
        print(line_format)
        print('|  {}      |  {}     |  {}        |'.format(packet_id, action, reason))

    # ------------------------------------------------------------------------

    def _assert_and_drop(self, condition, err_msg):
        """
        asserts the given condition, in case of failure, the packet will be dropped.
        :param condition: the condition to assert.
        :param err_msg: the cause of the failure if assertion failed.
        :return: 0 in case of success, 1 otherwise.
        """
        rc = 0
        if not condition:
            self._print_table(self._packet_id, 'DROP', err_msg)
            rc = 1

        return rc

    # ------------------------------------------------------------------------


if __name__ == '__main__':
    msg = '1:nadeem:naara:205496342:IL:nadeemn@hotmail.com:male:Verification:SW student:john cena:TLV:26/06/2018:AA:12:122:12000:NA'
    fp = FilterProcedure(msg, 777, ':')
    fp.run()
