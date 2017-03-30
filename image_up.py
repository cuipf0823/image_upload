#!/usr/bin/python
# coding=utf-8

import os
import platform
import module.upload as up
import module.config as config
import module.common as com


def welcome():
    print('*' * 60)
    print(' ' * 25 + 'Upload Tool')
    print('*' * 60)


def get_files(path):
    """get all file information
       return file_list[key,fullpath]
    """
    filter_dir = []
    file_list = []
    key = ''
    for parent, directorys, files in os.walk(path):
        if com.hide_file(parent):
            filter_dir.append(parent)
            continue
        else:
            if com.in_filter_list(parent, filter_dir):
                continue
        for file_name in files:
            full_path = os.path.join(parent, file_name)
            if com.hide_file(full_path):
                continue
            key = os.path.relpath(full_path, path).replace("\\", "/")
            file_list.append([key, full_path])
    return file_list


def main():
    path = ''
    while True:
        path = raw_input("input upload path:")
        if not isinstance(path, unicode):
            path = path.decode('utf-8')
        if not os.path.exists(path):
            print("input path %s not exist" % path)
            continue
        else:
            break
    upload = up.Upload(config.access_key(), config.secret_key())
    files = get_files(path)
    links = []
    for key, fpath in files:
        token = upload.create_token(config.bucket(), key.encode('utf-8'))
        ret, info = upload.upload_files(token, key, fpath, progress_handler=com.progress_handler)
        if info.status_code != 200:
            print ("File: %s upload failed" % key)
        else:
            print("File: %s  Size: %s upload successfully" % (key, com.format_size(os.path.getsize(fpath))))
            link = upload.create_link(key.encode('utf-8'), config.domain(), config.bucket())
            links.append([key, link])
    print ("Upload Successful! \n")
    for key, link in links:
        print ("File: %s  URL: %s" % (key, link))
    if platform.system() == 'Windows':
        os.system('pause')

if __name__ == '__main__':
    welcome()
    main()




