import asyncio
import collections


def perform_load_test(url):
    for i in range(1, 10, 1):
        run_simultaneous_loads(url, i)
    return "foo"


@asyncio.coroutine
def run_simultaneous_loads(url, num_simultaneous):
    """
    Perform the loads

    :type url: str
    :type num_simultaneous: int
    :return:
    :rtype: tuple
    """
    #######################################################
    import sys; sys.stdout = sys.stderr
    from IPython import embed; embed()
    import sys; sys.exit()
    #######################################################
