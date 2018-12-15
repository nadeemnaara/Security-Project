
def try_catch_wrapper(func_ptr, *args):
    """
    calls the function within try-catch scope.
    :param func_ptr: a pointer to the function to call.
    :param args: the args passed to the function.
    :return: the output of the called function, in case of no exceptions raised.
    :raise: an exception of type Exception in case of failure in calling the function.
    """
    try:
        res = func_ptr(*args)
    except Exception as err:
        err_msg = 'The following exception was raised when calling {}:\n' \
                '{}'.format(func_ptr, str(err))
        raise Exception(err_msg)
    return res

# ------------------------------------------------------------------------


def safe_call(func_ptr, *args):
    """
    calls a function that might raise an exception within try-catch scope.
    :param func_ptr: a pointer to the function to call.
    :param args: the args passed to the function.
    :return: 0 in case of no exceptions raised when calling the function, 1 otherwise.
    """
    rc = 0
    try:
        func_ptr(*args)
    except Exception as exp:
        raise exp
    return rc

# ------------------------------------------------------------------------


def list_to_str(slist, sep):
    """
    convert list of strings to string separated by separator
    :param slist: the list of string to be converted
    :param sep: the separator that will be used in returned string
    :return: string
    """
    ret_str = str('')
    for s in slist:
        ret_str += s + sep

    return ret_str

# ------------------------------------------------------------------------


def assert_and_raise(condition, err_msg):
    """
    asserts the given condition and raises an exception in case of failure with the given
    error message.
    :param condition: bolean.
    :param err_msg: an error message in case of failure.
    """
    if not condition:
        raise Exception(err_msg)

# ------------------------------------------------------------------------


class Log:

    # print tools.

    @staticmethod
    def stage(to_print):
        """
        prints in the following format:
        ========================================================
        # the message to print
        ========================================================
        :param to_print: the string to print.
        """
        to_print_len = len(to_print)
        line_format = ''
        for i in range(to_print_len + 10):
            line_format += '='
        print(line_format)
        print('###### {}'.format(to_print))
        print(line_format)

    # ------------------------------------------------------------------------

    # TODO: code duplication
    @staticmethod
    def info(to_print):
        """
        prints in the following format:
        ----------------------------------------------------------
        --INFO-- the message to print
        ----------------------------------------------------------
        :param to_print: the string to print.
        """
        to_print_len = len(to_print)
        line_format = ''
        for i in range(to_print_len + 10):
            line_format += '-'
        print(line_format)
        print('--INFO-- {}'.format(to_print))
        print(line_format)
