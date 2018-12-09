

class PacketParser:

    def __init__(self, packet_data, separator):
        """
        class constructor.
        :param packet_data:
            a string representing the data of the packet.
        :param separator:
            the separator used to separate the fields of the packet.
        """
        # removing leading and trailing separators in packet_data.
        self._packet_data = packet_data.strip(separator)

        self._separator = separator

    # ------------------------------------------------------------------------

    def parse_nth_field(self, n):
        """
        returns the value of the nth field of the packet.
        :param n: the index of the parsed field. starting from 0.
        :return: the value of the nth field - as string.
        :raise: an exception of type Exception will be raised in case of an error.
        """
        packet_fields = self._packet_data.split(self._separator)

        if n + 1 > len(packet_fields):
            raise Exception('too few fields in the packet.')

        nth_field = packet_fields[n]
        if not isinstance(nth_field, str):
            raise Exception('the value of the field need to be of type str.')

        return nth_field

    # ------------------------------------------------------------------------

    def packet_size(self):
        """
        returns the size of the packet in Bytes - not including separators.
        :return: the size of the packet - as integer.
        """
        size = 0
        fields = self._packet_data.split(self._separator)
        for field in fields:
            size += len(field)

        return size

    # ------------------------------------------------------------------------

    def get_nth_field_size(self, n):
        """
        returns the size of the nth field in Bytes - starting from 0.
        :return: the size of the field - as integer.
        :raise: an exception of type Exception will be raised in case of an error.
        """
        # an exception can be raised here.
        nth_field = self.parse_nth_field(n)

        return len(nth_field)

    # ------------------------------------------------------------------------

    def number_of_fields(self):
        """
        returns the number of fields of the packet.
        :return: number of fields - as integer.
        """
        fields = self._packet_data.split(self._separator)

        return len(fields)




if __name__ == '__main__':

    packet = 'aa bb cc '
    pp = PacketParser(packet, ' ')
    field = pp.parse_nth_field(2)
    field_size = pp.get_nth_field_size(2)
    size = pp.packet_size()
    print('field: {}, field size: {} ,packet size: {}'.format(field, field_size, size))

