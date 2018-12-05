
# global imports
import socket

# local imports
from tools import try_catch_wrapper, safe_call


class ConnectionEngine:

    def __init__(self, dst_ip, dst_port, timeout=None):
        """
        class constructor, creates a socket connection with the specified ip and port.
        :param dst_ip: the host ip.
        :param dst_port: the port used for the connection.
        :param timeout: maximum time to wait till connection is established.
        :raise: an exception of type Exception will be raised in case of connection issues.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._dst_ip = dst_ip
        self._dst_port = dst_port

        # sets maximum time till establishing the connection.
        if timeout is None:
            self._socket.settimeout(timeout)

        print('-INFO- trying to connect to host={},port={}.'.format(dst_ip, dst_port))

        connect_socket_func = self._socket.connect
        try_catch_wrapper(connect_socket_func, dst_ip, dst_port)

        print('-INFO- a connection with host={},port={} was established.'.format(dst_ip, dst_ip))
        self._is_connected = True

    # ------------------------------------------------------------------------

    def send_data(self, data_to_send):
        """
        sends the data through the created socket.
        :param data_to_send: a string, representing the data that will be sent.
        :raise: an exception of type Exception will be raised in case of failure.
        """
        if not isinstance(data_to_send, str):
            raise Exception('the sent data need to be of type str')

        print('-INFO- trying to send data to host={},port={}'.format(self._dst_ip, self._dst_port))

        send_socket_func = self._socket.connect
        try_catch_wrapper(send_socket_func, data_to_send)

        print('-INFO- the data was sent successfully to host={},port={}.'.format(self._dst_ip, self._dst_port))

    # ------------------------------------------------------------------------

    def close_connection(self):
        """
        closes the socket connection.
        :return: 0 in case of success, 1 otherwise.
        """
        close_socket_func = self._socket.close
        rc = safe_call(close_socket_func)
        if rc == 0:
            self._is_connected = False
        return rc

    # ------------------------------------------------------------------------

    def __del__(self):
        """
        class destructor, closes the socket if still open.
        :raise: an exception will be raised in case of failure.
        """
        if self._is_connected:
            self.close_connection()

    # ------------------------------------------------------------------------







