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
    file_list = thefile.readlines()
    for line in set(file_list):
    	# strip(): 去掉末尾'\n'
        print("--- %s --- %s ---" % (line.strip(), len(line.strip())))
        if len(line.strip()) == 11:
            os.system('xcrun atos -arch arm64 -o %s %s' % (project_name, line))
            print("arm64")
        elif len(line.strip()) == 8: 
            print("armv7")
            os.system('xcrun atos -arch armv7 -o %s %s' % (project_name, line))
    # 关闭文件
    thefile.close()
# 执行
main()
