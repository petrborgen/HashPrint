"""Print and hash testing."""
import hashlib
import string
import time

import pytest
from numpy import random

from main import async_print, hash_func


def word_gen():
    """One word generate."""
    low = 5
    high = 30
    sym_count = random.randint(low, high=high)
    sym_list = random.choice(list(string.ascii_letters), sym_count)
    return ''.join(sym_list)


def word_list_gen(word_n, test_n):
    """Word list generate."""
    return [(word_gen() for word in range(word_n)) for test in range(test_n)]


@pytest.mark.parametrize('anything', word_list_gen(3, 10))
def test_print(anything):
    """Print time testing."""
    time1 = time.time()
    async_print(anything)
    time2 = time.time()
    assert int(time2 - time1) <= 5


@pytest.mark.parametrize('anything', word_list_gen(1, 10))
def test_hash(anything):
    """Correct hash testing."""
    anything = str(anything)
    hash_object = hashlib.sha256(anything.encode())
    hex_digest = hash_object.hexdigest()
    assert hex_digest == hash_func(anything)
