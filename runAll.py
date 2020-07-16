# -*- coding: utf-8 -*-
# @Time     : 5/8/2020 2:02 PM
# @Author   : Dean-kexiang Ding
# @Email    : Dean-kexiang.ding@cn.abb.com
# @File     : runAll.py

from selenium import webdriver
import time
import pytest
import os

if __name__ == '__main__':
    #获取当前目录
    current_dir = os.path.dirname(__file__)
    #当前testcase运行目录
    testCase_dir = current_dir + '/testCase'
    #报表存放目录
    report_dir = "--html="+ current_dir + "/report/report_%s.html"%(time.strftime("%Y-%m-%d-%H-%M-%S"))

    pytest.main([testCase_dir,report_dir])