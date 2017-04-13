# image_upload
## 项目
上传文件到七牛空间, 并生成外链;
* 目录下多文件全部上传七牛空间, 打印外链;
* 单一文件上传七牛; 生成外链, 拷贝到剪贴板, 主要为方便使用Markdown, 上传图片;

## 依赖
* 版本工具基于python2.7.6开发；
* 工具支持平台Windows, Linux和Mac OS；
* 依赖库requests, pywin32(windows下)；

## 使用
### 配置
config.ini主要是和七牛相关配置:

1. AK 账号密钥AccessKey
2. SK 账号密钥SecretKey
3. bucket 存储空间名
4. domain 存储空间域名

### 注意
* 上传完成, 拷贝剪贴板仅支持Windows和MAC OS;
* 使用七牛创建bucket(存储空间), 只能是public; 因private空间需要单独生成token; 这里不支持;

### 优化
* 上传文件之前, 判断是否存在同名文件, 防止文件过多, 同名之间相互覆盖;
* 保证MAC也可以双击打开程序, 使文件上传更加方便;

## 附
[七牛注册地址](https://portal.qiniu.com/signin)