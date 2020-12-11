import logging


def function(a: int, b: int, flag: bool = True):
    """Sample function

    :param a: arbitrary integer value
    :param b: arbitrary integer value
    :param flag: boolean flag

    :type a: integer
    :type b: integer
    :type flag: boolean

    :return: sum of a and b
    :rtype: integer

    """
    logger = logging.getLogger(__name__)
    logger.debug(f'Argument flag value: {flag}')
    return a + b
