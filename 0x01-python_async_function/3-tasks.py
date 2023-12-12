#!/usr/bin/env python3
'''function that takes an integer max_delay
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' returns a asyncio
    '''
    return asyncio.create_task(wait_random(max_delay))
