#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

import numpy as np


def read_input(file):
    for line in file:
        yield line.rstrip()

inp = read_input(sys.stdin)
inp = [float(line) for line in inp]
numInputs = len(inp)
inp = np.mat(inp)
sqInput = np.power(inp, 2)

print("%d\t%f\t%f" % (numInputs, np.mean(inp), np.mean(sqInput)))
print("report: still alive", file=sys.stderr)
