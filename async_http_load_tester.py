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
        duration = run_simultaneous_loads(url, i)
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
    tasks = []
    for i in range(num_simultaneous):
        tasks.append(asyncio.async(run_individual_load(url)))
    event_loop.run_until_complete(asyncio.wait(tasks))
    return time.time() - start


@asyncio.coroutine
def run_individual_load(url):
    result = yield from aiohttp.request('GET', url)
    html = yield from result.read()
    return html
