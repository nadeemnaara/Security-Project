
# global imports
import socket
import sys
import zlib

# local imports
from tools import try_catch_wrapper, safe_call

# global constants
MAX_QUEUED_CONNECTIONS = 1  # the max number of queued connections in the socket.
BUFF_SIZE = 1024


class Server:

    def __init__(self, server_ip, server_port):
        """
        class constructor..
        :param server_ip: the ip of the server.
        :param server_port: the port to which the server will be listening.
        """
        self._ip = server_ip
        self._port = server_port
        self._socket = None   # will be defined when calling run_server().
        self._is_connected = False

    # ------------------------------------------------------------------------

    def run(self):
        """
        creates a socket and binds it to the server's ip and port, and starts listening on the socket.
        upon each socket received the server will handle it in a new thread - this way the server
        will always be available and won't be wasting time in handling the received packets.
        each thread will handle the received packet by executing a filtering rules - this done by
        FilteringProtocol class.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # binding the socket to the ip and port of the server.
        try_catch_wrapper(self._socket.bind, (self._ip, self._port))

        self._socket.listen(MAX_QUEUED_CONNECTIONS)

        print('-INFO- the server is up and listening on port {}\n'.format(self._port))
        self._is_connected = True

        while True:
            received_socket, received_from = self._socket.accept()

            print('-INFO- a socket was received from {}'.format(received_from))

            received_packet = received_socket.recv(BUFF_SIZE)
            #received_packet_decompressed = zlib.decompress(received_packet)

            print('-INFO- the data received : {}\n'.format(received_packet))

    # ------------------------------------------------------------------------

    def terminate(self):
        """
        closes the server's socket - but first should wait for all the threads to finish.
        :raise: an exception of type Exception will be raised in case of an error.
        """
        if self._is_connected:
            print('-INFO- server terminating...\n')
            rc = safe_call(self._socket.close)

        if rc == 0:
            self._is_connected = False
        return rc

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
    server = Server(server_ip=ip, server_port=int(port))
    server.run()





