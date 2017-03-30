#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, time, hashlib, smtplib

# 项目名称(需要自己填写)
project_name = "YourProjectName"
# bug内存地址列表文件名称
bug_adress_list_name = "BugAddressList"

def main():
    # 打印UUID
    os.system('dwarfdump --uuid %s/%s' % (os.getcwd(), project_name))

    # Umeng统计出来的内存地址list
    thefile = open(bug_adress_list_name)
    line = thefile.readline()
    while line:
        # strip(): 去掉末尾'\n'
        if len(line.strip()) == 11: # arm64
            print("--- arm64 --- %s ---" % line.strip())
            os.system('xcrun atos -arch arm64 -o %s %s' % (project_name, line))
        elif len(line.strip()) == 8: # armv7
            print("--- armv7 --- %s ---" % line.strip())
            os.system('xcrun atos -arch armv7 -o %s %s' % (project_name, line))
        else : # 用作分割线等特殊行处理
            print(line)
        # 读取下一行
        line = thefile.readline()

    # 关闭文件
    thefile.close()
# 执行
main()
