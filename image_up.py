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


def main():
    path = ''
    while True:
        path = raw_input("\ninput upload directory path or file path or quit:")
        if path == 'quit':
            return
        if not isinstance(path, unicode):
            path = path.decode('utf-8')
        if not os.path.exists(path):
            print("input path %s not exist\n" % path)
            continue
        upload = up.Upload(config.access_key(), config.secret_key())
        files = []
        if os.path.isfile(path):
            files.append([os.path.basename(path), path])
        elif os.path.isdir(path):
            files = com.get_files(path)
        links = []
        errs_list = []
        for key, fpath in files:
            token = upload.create_token(config.bucket(), key.encode('utf-8'))
            ret, info = upload.upload_files(token, key, fpath, progress_handler=com.progress_handler)
            if info.status_code != 200:
                errs_list.append(key)
                print ("File: %s upload failed  error %d:%s" % (key, info.status_code, info.error))
            else:
                print("File: %s  Size: %s upload successfully" % (key, com.format_size(os.path.getsize(fpath))))
                link = upload.create_link(key.encode('utf-8'), config.domain())
                links.append([key, link])
        print ("Upload Completely! \n")
        for err in errs_list:
            print 'File: %s upload failed' % err
        for key, link in links:
            print ("File: %s  URL: %s" % (key, link))
        if len(links) == 1 and len(errs_list) == 0:
            print ("File link copy to clipboard!")
            com.write_clipboard(links[0][1])


if __name__ == '__main__':
    welcome()
    main()




