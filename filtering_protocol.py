
# global imports
from threading import Thread

import re

# local imports
from packet_parser import PacketParser


class Constants:

    # the expected fields of a packet, based on the op code.
    PACKET_FIELDS = {'1': ['fname', 'lname', 'id', 'country', 'email', 'gender', 'job_title', 'dep',
                           'manager', 'office_loc', 'start_date', 'items_issued', 'bank_no', 'bank_section',
                           'bank_acc', 'signature'],
                     '2': ['id', 'fname', 'job_title', 'submit_date', 'due_date', 'purpose', 'money_amount',
                           'bank_no', 'bank_section', 'bank_acc', 'signature'],
                     '3': ['id', 'fname', 'job_title', 'dep', 'reason_of_leaving', 'last_day', 'country',
                           'fiscal_dep', 'admin_dep', 'hr_dep']}

    # max len for each field.
    MAX_LEN_FIELD = {'fname': }


class Rules:

    @staticmethod
    def name_rule(name):
        pass

    @staticmethod
    def date_rule(date):
        pass

    @staticmethod
    def id_rule(id):
        pass

    @staticmethod
    def country_rule(country):
        pass

    @staticmethod
    def email_rule(email):
        pass

    @staticmethod
    def gender(gender):
        pass





class FilteringProtocol(Thread):
    """
    the class inherits Thread, so we can run the filtering procedure in a thread.
    """
    def __init__(self, data: str, forward_to_ip: str, separator: str):
        """
        class constructor.
        :param data: the packet to filter.
        :param forward_to_ip: the ip to which we will forward the packet in case it passed the filtering procedure.
        :param separator: the separator used to separate between the fields of the packet.
        """
        self._packet = data
        self._forward_to_ip = forward_to_ip
        self._separator = separator

        # creates a thread to execute run().
        self.start()

    # ------------------------------------------------------------------------

    def run(self):
        """
        this function will apply the filtering rules on the packet.
        in case of success, the packet will be forwarded to forward_to_ip.
        """
        parser = PacketParser(self._packet, self._separator)

    # ------------------------------------------------------------------------

    def _validate_packet_structure(self, parser: PacketParser):
        """
        -checks if the size of the packet is valid.
        -checks if the packet contains the appropriate number of field.
        :param parser: an instance of PacketParser.
        :raise: an exception of type Exception in case of failure.
        """
        packet_size = parser.packet_size()








