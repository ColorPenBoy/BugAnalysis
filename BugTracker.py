#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, time, hashlib, smtplib

# 项目名称(需要自己填写)
project_name = "YourProjectName"
# bug内存地址列表文件名称
bug_adress_list_name = "BugAddressList"
# umeng统计后台导出的CSV（Excel）文件
bug_csv_name = "BugAddressList.csv"

def main():
    # 打印UUID
    os.system('dwarfdump --uuid %s/%s' % (os.getcwd(), project_name))

    # 分析Umeng后台导出的Excel文件（csv格式）
    analysis_csv_file()

    # 手动将地址添加到文件中分析
    # analysis_normal_file()

# 执行
main()

def analysis_csv_file():
    csv_reader = csv.reader(open(bug_csv_name))
    line_num = 0
    for line in csv_reader:
        # yield [unicode(cell, 'utf-8') for cell in line]
        # print(line)
        line_num += 1
        if (line_num != 1):
            print("-----------------------------------------")
            for row in line:
                if (len(row) == 11):
                    print("arm64 - %s" % row)
                    os.system('xcrun atos -arch arm64 -o %s %s' % (project_name, row))
                elif (len(row) == 8):
                    print("armv7 - %s" % row)
                    os.system('xcrun atos -arch armv7 -o %s %s' % (project_name, row))

def analysis_normal_file():
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

