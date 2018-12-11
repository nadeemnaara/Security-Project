
# global imports
import socket
import sys
import random

# local imports
from tools import try_catch_wrapper, safe_call, Log as log
from packet_handler import PacketHandler

# global constants
MAX_QUEUED_CONNECTIONS = 1  # the max number of queued connections in the socket.
SEPARATOR = ':'
BUFF_SIZE = 200


class Server:

    def __init__(self, server_ip, server_port):
        """
        class constructor..
        :param server_ip: the ip of the server - str.
        :param server_port: the port to which the server will be listening - str.
        """
        self._ip = server_ip
        self._port = int(server_port)
        self._socket = None   # will be defined when calling run_server().
        self._is_connected = False
        self._active_threads = []

    # ------------------------------------------------------------------------

    def run(self, activate_filtering=False):
        """
        creates a socket and binds it to the server's ip and port, and starts listening on the socket.
        upon each socket received the server will handle it in a new thread - this way the server
        will always be available and won't be wasting time in handling the received packets.
        each thread will handle the received packet by executing a filtering rules - this done by
        FilteringProtocol class.
        :param activate_filtering: bolean, if set to True, we will activate filtering procedure on
        each received packet.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # binding the socket to the ip and port of the server.
        try_catch_wrapper(self._socket.bind, (self._ip, self._port))

        self._socket.listen(MAX_QUEUED_CONNECTIONS)

        log.stage('the server is up and listening on port {}'.format(self._port))
        self._is_connected = True

        while True:
            received_socket, received_from = self._socket.accept()
            packet_id = random.randint(100, 1000)
            received_packet = received_socket.recv(BUFF_SIZE)

            log.info('the following socket was received from {}: packet-id={}  packet-data={}.'.format(received_from,
                                                                                                       packet_id,
                                                                                                       received_packet))

            packet_handler = PacketHandler(received_packet, packet_id, ('0','1'), SEPARATOR, activate_filtering)
            self._active_threads.append(packet_handler)

    # ------------------------------------------------------------------------

    def terminate(self):
        """
        closes the server's socket - but first should wait for all the threads to finish.
        :raise: an exception of type Exception will be raised in case of an error.
        """
        if self._is_connected:
            log.stage('server terminating...')

            log.info('waiting for the active threads to finish.')
            for t in self._active_threads:
                t.join()

            rc = safe_call(self._socket.close)

        if rc == 0:
            self._is_connected = False

    # ------------------------------------------------------------------------

    def __del__(self):
        """
        class destructor, closes the server socket if still open.
        """
        if self._is_connected:
            self.terminate()



if __name__ == '__main__':

    ip = sys.argv[1]
    port = sys.argv[2]
    flag = sys.argv[3] == '-f'
    server = Server(server_ip=ip, server_port=int(port))
    server.run(flag)





