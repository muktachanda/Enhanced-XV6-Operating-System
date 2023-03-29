#!/usr/bin/env python3
# [ticks] Action {pid} =srcq= _dstq_

import matplotlib
import matplotlib.pyplot as plt

import re

LOGS = ""

with open("log.txt") as f:
    LOGS = f.read()

inp = LOGS.strip().split("\n")

GRAPH_DATA = {}

#ignore = [ "0", "1", "2", "3" ]
ignore = [ "0" ]

marks = [ ".", ",", "o", "v", "^", "<", ">", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X", "D", "d" ]

re_ticks = re.compile(r"\[([^]]*)\]")
re_pid = re.compile(r"\{([^]]*)\}")
re_srcq = re.compile(r"\=([^]]*)\=")
re_dstq = re.compile(r"\_([^]]*)\_")

min_ticks = 10 ** 10

for line in inp:
    pid = re_pid.search(line).groups()[0]
    ticks = int(re_ticks.search(line).groups()[0])
    que = int(re_dstq.search(line).groups()[0])

    if ticks < min_ticks:
        min_ticks = ticks

    if pid in ignore:
        continue

    if pid not in GRAPH_DATA:
        GRAPH_DATA[pid] = { "x": [], "y": [] }
    else:
        GRAPH_DATA[pid]["x"].append(ticks)
        GRAPH_DATA[pid]["y"].append(que)

for pid in GRAPH_DATA:
    for i in range(len(GRAPH_DATA[pid]["x"])):
        GRAPH_DATA[pid]["x"][i] -= min_ticks

i = 0
for pid in GRAPH_DATA:
    i += 1
    plt.plot(GRAPH_DATA[pid]["x"], GRAPH_DATA[pid]["y"], label=pid, marker=marks[i])

plt.legend()
plt.show()