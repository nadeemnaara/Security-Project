
import sys


class PacketParser:

    def __init__(self, packet_data):
        """
        class constructor.
        :param packet_data:
            a string representing the data of the packet.
        """
        self._packet_data = packet_data

    # ------------------------------------------------------------------------

    def parse_nth_field(self, n, separator):
        """
        returns the value of the nth field of the packet.
        :param n: the index of the parsed field. starting from 0.
        :param separator: the separator used between the field of the packet.
        :return: the value of the nth field - as string.
        :raise: in case of error, an exception of type Exception.
        """
        packet_fields = self._packet_data.split(separator)

        if n + 1 > len(packet_fields):
            raise Exception('Too few fields in the packet.')
        nth_field = packet_fields[n]
        if not isinstance(nth_field, str):
            raise Exception('Nth field has invalid value.')
        return nth_field

    # ------------------------------------------------------------------------


if __name__ == '__main__':

    packet = sys.argv[1]
    pp = PacketParser(packet)
    field = pp.parse_nth_field(4, ' ')
    print(field)

