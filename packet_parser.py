# global imports
import re
import sys


# local imports
from tools import assert_and_raise

#  email domains are hardcoded.


class PacketParser:

    # the expected fields of a packet and the regx of it, based on the op code.
    __packets_structure = {'1': ['opcode', 'fname', 'lname', 'id', 'country', 'email', 'gender', 'dep', 'job_title',
                                 'manager', 'office_loc', 'date', 'items_issued', 'bank_no', 'bank_section',
                                 'bank_acc', 'signature'],
                           '2': ['opcode', 'id', 'name', 'job_title', 'sub_date', 'due_date', 'purpose', 'money_amount',
                                 'bank_no', 'bank_section', 'bank_acc', 'signature'],
                           '3': ['opcode', 'id', 'name', 'job_title', 'dep', 'reason_of_leaving', 'last_day', 'country',
                                 'approval_1', 'approval_2']}

    __fields_regx = {'name': '^[A-Z,a-z]{1,10}$',
                     'id': '^[0-9]{9}$',
                     'country': '^[A-Z]{2,3}$',
                     'email': '^[a-zA-Z][^: ]{5,19}[@](hotmail|gmail|yahoo).(com|co.il)$',
                     'gender': '^(male|female|others)',
                     'job_title': '^[A-Za-z ]{4,18}$',
                     'dep': '^[A-Za-z]{2,14}$',
                     'manager': '^[A-Za-z ]{6,18}$',
                     'office_loc': '^[A-Za-z]{3,7}$',
                     'date': '^[0-3][1-9]/[0-1][0-9]/2018$',
                     'purpose': '^[A-Z]{2}$',
                     'money_amount': '^[1-9]{3,4}$',
                     'reason_of_leaving': '^[A-Z]{2}$',
                     'items_issued': '^[A-Za-z ]{1,50}',
                     'signature': '^[A-Z]{2}$',
                     'approval': '^(HR|FDW|FDL)-^[0-3][1-9]/[0-1][0-9]/2018$'
                     }

    __bank_info_regx = {'USA': ['^[1-9]{2}$', '^[0-9]{3}$', '^[0-9]{5}$'],
                        'IL': ['^[1-9]{2}$', '^[0-9]{3}$', '^[0-9]{5}$'],
                        'ENG': ['^[1-9]{2}$', '^[0-9]{3}-[A-Z]$', '^[0-9]{7}']
                        }

    __max_packet_size = 200

    def __init__(self, packet_data, separator):
        """
        class constructor.
        :param packet_data: a string representing the data of the packet.
        :param separator: the separator used to separate the fields of the packet - str.
        """
        # removing leading and trailing separators in packet_data.
        self._packet_data = packet_data.strip(separator)

        self._separator = separator

    # ------------------------------------------------------------------------

    def _packet_size(self):
        """
        returns the size of the packet in Bytes - not including separators.
        :return: the size of the packet - integer.
        """
        size = 0
        fields = self._packet_data.split(self._separator)
        for field in fields:
            size += len(field)

        return size

    # ------------------------------------------------------------------------

    def parse(self):
        """
        parses the packet and returns dictionary of the following format:
        {<field_name>: <value>, <field_name>: <value>....}.
        the fields are determined by the opcode of the packet.
        if the function didn't fail, we can know that:
        - size - OK.
        - number of fields - OK.
        - opcode - OK.
        - field regx - OK.
        :return: a dictionary as described above.
        :raise: Exception, if the parsing failed.
        """
        assert_and_raise(self._packet_size() < self.__max_packet_size, 'size not valid')
        fields_values = self._packet_data.split(self._separator)
        assert_and_raise((len(fields_values) > 0), 'number of fields not valid')

        opcode = fields_values[0]
        assert_and_raise(opcode in self.__packets_structure.keys(), 'opcode is not valid')

        fields_names = [name for name in self.__packets_structure[opcode]]
        assert_and_raise(len(fields_values) == len(fields_names), 'number of fields not valid')

        parsed_dict = dict(zip(fields_names, fields_values))

        # asserting the value of each field based on its regx.
        validate_banking_info = False
        for field, value in zip(fields_names, fields_values):
            if field ==  'opcode':
                continue
            # problematic keys for the regx
            if re.match('^[f,l]name', field):
                field = 'name'
            elif re.match('^(sub|due)_date', field):
                field = 'date'
            elif re.match('^appoval', field):
                field = 'approval'

            # needed for bank info validation.
            if field == 'country':
                country = value
            if re.match('bank', field) is not None:
                validate_banking_info = True
                break
            else:
                regx = self.__fields_regx[field]

            condition = re.match(regx, value) is not None
            assert_and_raise(condition, 'field -{}- did not satisfy its regx, value:{} regx:{}'.format(field, value, regx))

        # asserting banking info - if exists.
        if validate_banking_info:
            regx_list = self.__bank_info_regx[country]
            for field in ['bank_no', 'bank_section', 'bank_acc']:
                regx = regx_list.pop(0)
                condition = re.match(regx, parsed_dict[field]) is not None
                assert_and_raise(condition, 'field -{}- did not satisfy its regx, value:{} regx:{}'.format(field,
                                                                                                           parsed_dict[field],
                                                                                                           regx))
        field = 'signature'
        if 'signature' in self.__packets_structure[opcode]:
            condition = re.match(self.__fields_regx[field], parsed_dict[field]) is not None
            assert_and_raise(condition, 'field -{}- did not satisfy its regx, value:{} regx:{}'.format(field,
                                                                                                       parsed_dict[field],
                                                                                                       regx))
        return list(zip(fields_names, fields_values))

    # ------------------------------------------------------------------------


if __name__ == '__main__':
    str = sys.argv[1]
    parser = PacketParser('1:nadeem:naara:205496322:IL:nadeemn@hotmail.com:male:Verification:'
                          + 'SW student:john cena:TLV:26/06/2018:AA:12:122:12000:NA', ':')
    print(parser.parse())