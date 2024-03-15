#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from Multithreaded import Thread_calls
import os
from qfluentwidgets import QConfig, qconfig, OptionsConfigItem
class Config(QConfig):

    GPU_setting = OptionsConfigItem("GPU_choose", "number", "Auto")
cfg = Config()
qconfig.load('../../app/config/config.json', cfg)
os.environ['CUDA_VISIBLE_DEVICES'] = str(cfg.get(cfg.GPU_setting))
parser = argparse.ArgumentParser()
parser.add_argument("--parameter01", type=str, default="../Input/")
parser.add_argument("--parameter02", type=str, default="../Output/")
parser.add_argument('--parameter03',  type=str, default=True)
parser.add_argument('--parameter04',  type=str, default=True)
parser.add_argument('--parameter05',  type=str, default=True)
parser.add_argument('--parameter06',  type=str, default=True)
parser.add_argument('--parameter07',  type=str, default=True)
parser.add_argument('--parameter08',  type=str, default=True)
args = parser.parse_args()
parameter01 = args.parameter01
parameter02 = args.parameter02
parameter03 = args.parameter03
parameter04 = args.parameter04
parameter05 = args.parameter05
parameter06 = args.parameter06
parameter07 = args.parameter07
parameter08 = args.parameter08

Thread_calls(parameter01, parameter02, parameter08)
