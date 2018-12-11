
# global imports
import socket
import sys

# local imports
from tools import try_catch_wrapper, safe_call, Log as log


class ConnectionEngine:

    def __init__(self, dst_ip, dst_port, timeout=None):
        """
        class constructor, creates a socket connection with the specified ip and port.
        :param dst_ip: the host ip - str.
        :param dst_port: the port used for the connection. - str
        :param timeout: maximum time to establish the connection - integer.
        :raise: an exception of type Exception will be raised in case of connection issues.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._dst_ip = dst_ip
        self._dst_port = int(dst_port)

        # setting maximum time to establish the connection.
        if timeout is not None:
            self._socket.settimeout(timeout)

        log.stage('trying to connect to [ host:{} - port:{} ].'.format(self._dst_ip, self._dst_port))

        try_catch_wrapper(self._socket.connect, (self._dst_ip, self._dst_port))

        log.info('a connection with [ host:{} - port:{} ] was established.'.format(self._dst_ip, self._dst_ip))
        self._is_connected = True

    # ------------------------------------------------------------------------

    def send_data(self, data_to_send):
        """
        sends the data through the created socket.
        :param data_to_send: representing the data that will be sent - str.
        :raise: an exception of type Exception will be raised in case of failure.
        """
        if not isinstance(data_to_send, str):
            raise Exception('the sent data need to be of type str')

        log.info('trying to send data to [ host:{} - port:{} ].'.format(self._dst_ip, self._dst_port))

        try_catch_wrapper(self._socket.sendall, data_to_send)

        log.info('the data was sent successfully to [ host:{} - port:{} ].\n'.format(self._dst_ip, self._dst_port))

    # ------------------------------------------------------------------------

    def close_connection(self):
        """
        closes the socket connection.
        :return: 0 in case of success, 1 otherwise.
        """
        # closing the socket multiple times causes errors.
        if self._is_connected:
            log.info('closing the connection...')
            rc = safe_call(self._socket.close)

        if rc == 0:
            self._is_connected = False
        return rc

    # ------------------------------------------------------------------------

    def __del__(self):
        """
        class destructor, closes the socket if still open.
        """
        # closing the socket multiple times causes errors.
        if self._is_connected:
            self.close_connection()

    # ------------------------------------------------------------------------


if __name__ == '__main__':

    server_ip = sys.argv[1]
    server_port = sys.argv[2]
    ce = ConnectionEngine(dst_ip=server_ip, dst_port=server_port)
    ce.send_data('1:nadeem:naara:205496342:IL:nadeemn@hotmail.com:male:Verification:' + 'SW student:john cena:TLV:26/06/2018:AA:12:122:12000:NA')

    ce.close_connection()




