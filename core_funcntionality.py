from connection_engine import ConnectionEngine
from tools import list_to_str

class CoreFunctionality:
    CONST_OPCODE_REG = '1'
    CONST_OPCODE_REQ = '2'
    CONST_OPCODE_REL = '3'

    def __init__(self, host: str, port: int):
        """
        class constructor, creates a socket connection with the specified ip and port.
        :param host: the host ip.
        :param port: the port used for the connection.
        :raise: an exception of type Exception will be raised in case of connection issues (connection_engine).
        """
        self._host = host
        self._port = port
        # 'engine_connection' is the engine that manage the connection between the client and server
        self.connection_engine = ConnectionEngine(host, port)

    def register_employee(self, input):
        """
        register employee form
        :param input: a list of strings which are the form's fields in the order as documented
        :raise: an exception of type Exception will be raised in case of connection issues (connection_engine).
        """
        input.insert(0, self.CONST_OPCODE_REG)
        string_input = list_to_str(input, ':')
        #print(string_input)
        # ask the connection engine to send the data to the server
        self.connection_engine.send_data(string_input)



    def request_allowance(self, input):
        """
        request employee form
        :param input: a list of strings which are the form's fields in the order as documented
        :raise: an exception of type Exception will be raised in case of connection issues (connection_engine).
        """
        input.insert(0, self.CONST_OPCODE_REQ)
        string_input = list_to_str(input, ':')
        #print(string_input)
        # ask the connection engine to send the data to the server
        self.connection_engine.send_data(string_input)

    def release_employee(self, input):
        """
        release employee form
        :param input: a list of strings which are the form's fields in the order as documented
        :raise: an exception of type Exception will be raised in case of connection issues (connection_engine).
        """
        input.insert(0, self.CONST_OPCODE_REL)
        string_input = list_to_str(input, ':')
        #print(string_input)
        # ask the connection engine to send the data to the server
        self.connection_engine.send_data(string_input)
