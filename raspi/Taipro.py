# -*- coding: UTF-8 -*-
# author: Interweave
# date: 2022.1.19 20:57
# email: interweave@qq.com
# -------------------------------------------------------------
#  _____
# |_   _|     | |
#   | |  _ __ | |_ ___ _ ____      _____  __ ___   _____
#   | | | '_ \| __/ _ \ '__\ \ /\ / / _ \/ _` \ \ / / _ \
#  _| |_| | | | ||  __/ |   \ V  V /  __/ (_| |\ V /  __/
# |_____|_| |_|\__\___|_|    \_/\_/ \___|\__,_| \_/ \___|
#
# -------------------------------------------------------------
import serial

# 实例化串口模块,波特率：9600
ser = serial.Serial('/dev/ttyAMA0', 9600)

if __name__ == '__main__':
    pass
