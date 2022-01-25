"""print and hash."""
import hashlib
import threading
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from sys import stdin, stdout
from time import sleep

from numpy import random

data_list = ['Пётр', '45000', 'Стажёр-программист Python']
lock = threading.Lock()


def trivial_print(print_data):
    """Print in thread."""
    sleep(random.randint(1, high=6))
    lock.acquire()
    stdout.write(print_data)
    stdout.write('\n')
    lock.release()


def async_print(print_list):
    """Async print."""
    with PoolExecutor(max_workers=3) as executor:
        executor.map(trivial_print, print_list)


def hash_func(anything):
    """Anything hash."""
    hash_object = hashlib.sha256(anything.encode())
    return hash_object.hexdigest()


if __name__ == '__main__':
    async_print(data_list)
    stdout.write('\nWrite anything: \n')
    anything_to_hash = stdin.readline()
    stdout.write(hash_func(anything_to_hash))
