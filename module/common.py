﻿#!/usr/bin/python
# coding=utf-8
import os
import subprocess
import platform

# 系统内核
OS_WINDOWS = 'Windows'
OS_MAC = 'Darwin'
OS_LINUX = 'Linux'

if platform.system() == OS_WINDOWS:
    import win32con
    import win32file


def format_size(size):
    """
    :param size 大小（bytes）
    根据大小格式化为相应的字符串
    """
    b = float(size)
    kb = float(1024)
    mb = float(kb ** 2)
    if b < kb:
        return '{}Bytes'.format(b)
    elif kb < b < mb:
        return '{0:.2f}KB'.format(b/kb)
    else:
        return '{0:.2f}MB'.format(b/mb)


def progress_handler(progress, total):
    """
    :param progress 当前上传的大小
    :param total 当前上传文件总长度
    七牛相关的回调函数
    """
    print("total {} current progresss {}".format(format_size(total), format_size(progress)))


def in_filter_list(path, filter_list):
    """
    判断path是否包含filter_list字段
    :param path 当前路径
    :param filter_list:  过滤列表
    return:包含返回True
    """
    for item in filter_list:
        if item in path:
            return True
    return False


def hide_file(path):
    """
        判断文件或者文件夹是否是隐藏的
        :param path 可以是文件的全路径或者目录的全路径
        return：True 隐藏
        注意：windows下隐藏文件根据属性判断
             linux下隐藏文件是以‘.’开头的文件
    """
    if platform.system() == OS_WINDOWS:
        dir_flag = win32file.GetFileAttributesW(path)
        dir_hiden = dir_flag & win32con.FILE_ATTRIBUTE_HIDDEN
        if dir_hiden > 0:
            return True
    elif platform.system() == OS_LINUX or platform.system() == OS_MAC:
        subs = path.split('/')
        for item in subs:
            if len(item) > 0 and item[0] == '.':
                return True
    return False


def get_files(path):
    """get all file information
       return file_list[key,fullpath]
    """
    filter_dir = []
    file_list = []
    for parent, directorys, files in os.walk(path):
        if hide_file(parent):
            filter_dir.append(parent)
            continue
        else:
            if in_filter_list(parent, filter_dir):
                continue
        for file_name in files:
            full_path = os.path.join(parent, file_name)
            if hide_file(full_path):
                continue
            key = os.path.relpath(full_path, path).replace("\\", "/")
            file_list.append([key, full_path])
    return file_list


def write_clipboard(output):
    """
    写剪切板 支持windows和mac
    """
    if platform.system() == OS_WINDOWS:
        cmd = 'clip'
    elif platform.system() == OS_MAC:
        cmd = 'pbcopy'
    process = subprocess.Popen(cmd, env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

