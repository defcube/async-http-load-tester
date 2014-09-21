import asyncio
import itertools
import time

import aiohttp

event_loop = asyncio.get_event_loop()
""" :type: AbstractEventLoop """


def perform_load_test(url, max_simultaneous, step):
    for i in itertools.chain((1,), range(step, max_simultaneous + 1, step)):
        duration = run_simultaneous_loads(url, i)
        per_second = float(i) / duration
        print("{0} Threads = Duration: {1} | Per Second: {2}".format(i, duration, per_second))


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
    try:
        result = yield from asyncio.wait_for(aiohttp.request('GET', url), 1)
        yield from asyncio.wait_for(result.read(), 1)
    except asyncio.TimeoutError:
        pass
