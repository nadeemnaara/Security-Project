

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
    except Exception:
        rc = 1
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
