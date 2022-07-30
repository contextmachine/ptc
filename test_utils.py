import random
import time
from unittest import TestCase

import utils


class TestProgresbar(TestCase):
    def test_show(self):
        @utils.Progresbar
        def gnr(ctx, a, b):
            ctx.prefix = "multiplication b * const"
            time.sleep(12)
            d = b * 88
            ctx.prefix = "multiplication a * b"
            for i in a:
                time.sleep(random.random())
                yield i * d
        j=0
        for i in gnr([1, 4, 11, 56, 77], 88):
            time.sleep(11)
            j+=i
        print(j)
        self.fail()
