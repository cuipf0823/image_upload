# !/usr/bin/python
# coding=utf-8
from qiniu import Auth
from qiniu import put_file
from qiniu import utils
import urllib


class Upload:
    def __init__(self, access_key, secret_key):
        self.qiniu_auth = Auth(access_key, secret_key)
        pass

    def create_token(self, bucket, key, policy=None, expires=7200):
        """生成上传token"""
        return self.qiniu_auth.upload_token(bucket, key, expires, policy)

    @staticmethod
    def upload_files(token, key, localfile, progress_handler=None):
        """上传文件到七牛
        :param token: 上传token
        :param key:上传到七牛云的路径key
        :param localfile:本地文件全路径
        :param progress_handler:回调函数，文件大于4mb时使用，上传4mb回调一次
        :return:一个字典，一个responseinfo对象
        """
        return put_file(token, key, localfile, progress_handler=progress_handler)

    @staticmethod
    def create_hash(file_path):
        """生成文件hash"""
        return utils.etag(file_path)

    @staticmethod
    def create_link(key, domain, bucket):
        return 'http://%s.%s/%s' % (bucket, domain, urllib.quote(key))




