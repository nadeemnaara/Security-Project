# global imports
from threading import Thread
import sys

# local imports
from filter_procedure import FilterProcedure
from connection_engine import ConnectionEngine


class PacketHandler(Thread):
    """
    the class inherits Thread, so we can run the filtering procedure in a thread.
    """
    def __init__(self, data, packet_id, host, separator, activate_filtering):
        """
        class constructor.
        :param data: the packet to filter.
        :param packet_id: the id of the packet - given by the server - integer.
        :param host: a tuple (ip, port) of the host to which we will forward the packet in case it passed
                the filtering procedure.
        :param separator: the separator used to separate between the fields of the packet.
        :param activate_filtering: bolean, if set to True, we will activate filtering procedure on
        each received packet.
        """
        Thread.__init__(self)
        self._packet = data
        self._packet_id = packet_id
        self._host = host
        self._separator = separator
        self._activate_filtering = activate_filtering

        # creates a thread to execute run().
        self.start()

    # ------------------------------------------------------------------------

    def run(self):
        """
        this function will apply the filtering rules on the packet if activate_filtering is set to True.
        in case of success, the packet will be forwarded to forward_to_ip.
        """
        if self._activate_filtering:
            filter_procedure = FilterProcedure(self._packet, self._packet_id, self._separator)
            rc = filter_procedure.run()

            if rc != 0:
                sys.exit()  # the packet has been dropped. force the thread to stop.

        # now, we will be forwarding the packet to its destination.
        (dst_ip, dst_port) = self._host

        print('forwarding to c')
        # engine = ConnectionEngine(dst_ip, dst_port)
        # engine.send_data(self._packet)
        # engine.close_connection()

        sys.exit()
    # ------------------------------------------------------------------------






