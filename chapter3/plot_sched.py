#!/usr/bin/python3

import numpy as np
from PIL import Image
import matplotlib
import os

matplotlib.use('Agg')

import matplotlib.pyplot as plt

# plt.rcParams['font.family'] = "NanumGothic"
plt.rcParams['axes.unicode_minus'] = False

def plot_sched(concurrency):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for i in range(concurrency):
        x, y = np.loadtxt(f"{i}.data", unpack=True)
        ax.scatter(x, y, s=1)
    ax.set_title(f"Time Slice Visualization (Concurrency={concurrency})")
    ax.set_xlabel("Elapsed Time [ms]")
    ax.set_xlim(0)
    ax.set_ylabel("Progress [%]")
    ax.set_ylim([0, 100])
    legend = []
    for i in range(concurrency):
        legend.append("Load Processing " + str(i))
    ax.legend(legend)

    pngfilename = f"sched-{concurrency}.png"
    jpgfilename = f"sched-{concurrency}.jpg"

    fig.savefig(pngfilename)
    Image.open(pngfilename).convert("RGB").save(jpgfilename)
    os.remove(pngfilename)

def plot_avg_tat(max_nproc):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x, y, _ = np.loadtxt("cpuperf.data", unpack=True)
    ax.scatter(x, y, s=1)
    ax.set_xlim([0, max_nproc + 1])
    ax.set_xlabel("Number of Processes")
    ax.set_ylim(0)
    ax.set_ylabel("Average Turnaround Time [s]")

    pngfilename = "avg-tat.png"
    jpgfilename = "avg-tat.jpg"

    fig.savefig(pngfilename)
    Image.open(pngfilename).convert("RGB").save(jpgfilename)
    os.remove(pngfilename)

def plot_throughput(max_nproc):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x, _, y = np.loadtxt("cpuperf.data", unpack=True)
    ax.scatter(x, y, s=1)
    ax.set_xlim([0, max_nproc + 1])
    ax.set_xlabel("Number of Processes")
    ax.set_ylim(0)
    ax.set_ylabel("Throughput [Processes/s]")

    pngfilename = "throughput.png"
    jpgfilename = "throughput.jpg"

    fig.savefig(pngfilename)
    Image.open(pngfilename).convert("RGB").save(jpgfilename)
    os.remove(pngfilename)
