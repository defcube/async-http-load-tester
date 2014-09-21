import asyncio
import time

import aiohttp

event_loop = asyncio.get_event_loop()
""" :type: AbstractEventLoop """


def perform_load_test(url):
    print("hi")
    # #######################################################
    # from IPython import embed; embed()
    # import sys; sys.exit()
    # #######################################################
    for i in range(1, 10, 1):
        duration = event_loop.run_until_complete(run_simultaneous_loads(url, i))
        per_second = float(i) / duration
        print("{0} Threads = Duration: {1} | Per Second: {2}".format(i, duration, per_second))
    return "foo"


def run_simultaneous_loads(url, num_simultaneous):
    """
    Perform the loads

    :type url: str
    :type num_simultaneous: int
    :return: Duration to complate all requests
    :rtype: float
    """
    start = time.time()
    for i in range(num_simultaneous):
        html = yield from run_individual_load(url, i)
        print("Html is: {0}".format(html))
    return time.time() - start


@asyncio.coroutine
def run_individual_load(url, i):
    print("Before {1} aiohttp.request: {0}".format(time.time(), i))
    result = yield from aiohttp.request('GET', url)
    print("After {1} aiohttp.request: {0}".format(time.time(), i))
    html = yield from result.read()
    print("After {1} aiohttp.read: {0}".format(time.time(), i))
    return html
