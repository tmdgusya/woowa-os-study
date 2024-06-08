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
        ax.scatter(x,y,s=1)
    ax.set_title(f"타임 슬라이스 가시화(동시 실행={concurrency})")
    ax.set_xlabel("경과 시간[밀리초]")
    ax.set_xlim(0)
    ax.set_ylabel("진척도[%]")
    ax.set_ylim([0, 100])
    legend = []
    for i in range(concurrency):
        legend.append("부하 처리 " + str(i))
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
    ax.scatter(x,y,s=1)
    ax.set_xlim([0, max_nproc+1])
    ax.set_xlabel("프로세스 개수")
    ax.set_ylim(0)
    ax.set_ylabel("평균 턴어라운드 타임[초]")

    pngfilename = "avg-tat.png"
    jpgfilename = "avg-tat.jpg"

    fig.savefig(pngfilename)
    Image.open(pngfilename).convert("RGB").save(jpgfilename)
    os.remove(pngfilename)

def plot_throughput(max_nproc):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x, _, y = np.loadtxt("cpuperf.data", unpack=True)
    ax.scatter(x,y,s=1)
    ax.set_xlim([0, max_nproc+1])
    ax.set_xlabel("프로세스 개수")
    ax.set_ylim(0)
    ax.set_ylabel("스루풋[프로세스/초]")

    pngfilename = "throughput.png"
    jpgfilename = "throughput.jpg"

    fig.savefig(pngfilename)
    Image.open(pngfilename).convert("RGB").save(jpgfilename)
    os.remove(pngfilename)