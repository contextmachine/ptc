import sys
import os
from abc import ABC
from typing import Iterable, Iterator


def search(path, prefix="e57"):
    dirs = os.scandir(path)
    for d in dirs:
        try:
            name, pref = d.name.split('.')
            if pref == prefix:
                yield name
        finally: continue


def progressbar(it, prefix="", size=60, out=sys.stdout):  # Python3.6+
    count = len(it)

    def show(j):
        x = int(size * j / count)
        print(f"{prefix}{u'█' * x}{('.' * (size - x))} {j}/{count}", end='\r', file=out, flush=True)

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    print("\n", flush=True, file=out)


class Progresbar(Iterator):
    def __iter__(self):
        self.i += 1
        return self

    def __next__(self):
        self.show()
        return next(self.itr)

    def __init__(self, itr, prefix="", size=60, out=sys.stdout):
        self._itr = itr
        self._prefix = prefix
        self.size = size
        self.out = out
        self.i = 0
        self._length=1

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, val):
        self._prefix = val

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, v):
        self._length = v

    def show(self, i):
        x = int(self.size * self.i / self.length)
        print(f"{self.prefix}{u'█' * x}{('.' * (self.size - x))} {self.i}/{self.length}", end='\r', file=self.out,
              flush=True)

    def __call__(self,  *args, **kwargs):

        self.itr = self._itr(self, *args, **kwargs)
        return self
