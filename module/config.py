#!/usr/bin/python
# coding=utf-8
import ConfigParser
import os
import platform

cf = ConfigParser.ConfigParser()
if platform.system() == 'Windows':
    cf.read(os.getcwd() + '\config.ini')
elif platform.system() == 'Linux':
    cf.read(os.getcwd() + '/config.ini')


def access_key():
    return cf.get('CLOUD', 'AK')


def secret_key():
    return cf.get('CLOUD', 'SK')


def bucket():
    return cf.get('CLOUD', 'bucket')


def domain():
    return cf.get('CLOUD', 'domain')


