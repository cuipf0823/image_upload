#!/usr/bin/python
# coding=utf-8
import ConfigParser
import os
import platform
import common

cf = ConfigParser.ConfigParser()
if platform.system() == common.OS_WINDOWS:
    cf.read(os.getcwd() + '\config.ini')
elif platform.system() == common.OS_LINUX or platform.system() == common.OS_MAC:
    pwd = os.path.dirname(os.path.realpath(__file__))
    cf.read(pwd[:pwd.rfind('/')] + '/config.ini')


def access_key():
    return cf.get('CLOUD', 'AK')


def secret_key():
    return cf.get('CLOUD', 'SK')


def bucket():
    return cf.get('CLOUD', 'bucket')


def domain():
    return cf.get('CLOUD', 'domain')


