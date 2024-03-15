#!/usr/bin/env python
# -*- coding: utf-8 -*-
from invoke import run

import os
import shutil

import time
from threading import Thread


def Thread_calls(process_src, output_dir, process_number):
    try:
        shutil.rmtree("../../Cache/Cache_thread")
    except:
        pass

    os.mkdir("../../Cache/Cache_thread")
    file_path = process_src
    new_file_path = ("../../Cache/Cache_thread/")
    list_ = os.listdir(file_path)
    num = int(float(len(list_)) / float(process_number))

    if num < 1:
        print('错误：打开的线程数必须小于: ', len(process_number))
        exit()
    if int(len(list_) % num) == 0:
        num_file = int(len(list_) / num)
    else:
        num_file = int(len(list_) / num) + 1

    cnt = 0
    for n in range(1, num_file + 1):
        new_file = os.path.join(new_file_path + str(n))
        if os.path.exists(new_file + str(cnt)):
            print('错误：路径已存在，请解决冲突路径问题', new_file)
            exit()
        print('进程：创建文件夹中,文件夹名为：', new_file)
        os.mkdir(new_file)
        list_n = list_[num * cnt:num * (cnt + 1)]

        for m in list_n:
            old_path = os.path.join(file_path, m)
            new_path = os.path.join(new_file, m)
            shutil.copy(old_path, new_path)
        cnt += 1

    number = -1
    for index in range(int(cnt)):
        number += 1
        _processes = (Thread(target=start_run, args=(number, output_dir)))
        _processes.start()

def start_run(number, output_dir):
    time1 = time.time()
    new_file_path = ("../../Cache/Cache_thread/")
    dirct = new_file_path
    dirList = []
    files = os.listdir(dirct)
    for f in files:
        if os.path.isdir(dirct + '/' + f):
            dirList.append(f)

    dir_import = dirList[number]
    process_src_import = ((os.path.abspath(os.path.join(os.getcwd(), "../.."))) + "/Cache/Cache_thread/" + dir_import + "/")
    process_src = str(process_src_import)

    run(process_src, output_dir)

    time2 = time.time()
    time.sleep(1.0)
    print("进程：此线程所花费的时间为 {} s\n".format(time2 - time1))
