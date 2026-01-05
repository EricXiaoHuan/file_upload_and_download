# -*- coding: utf-8 -*-
"""
文件共享服务 - file_share_service.py
基于Flask框架实现的简单文件上传下载服务
提供文件上传、下载功能，支持文件列表展示和排序
"""

import os
import socket
import datetime

# Flask相关导入
from flask import Flask, redirect, render_template, send_from_directory, url_for
from flask_wtf import FlaskForm
from wtforms import FileField
from werkzeug.utils import secure_filename

# 文件存储目录配置
FILE_STORAGE_DIR = r'D:\download'  # 文件上传下载的存储路径

# 初始化Flask应用
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'  # 用于表单安全验证的密钥


@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d %H:%M:%S'):
    """
    日期时间格式化模板过滤器
    将时间戳转换为指定格式的日期时间字符串
    
    :param value: 时间戳
    :param format: 日期时间格式字符串，默认为'%Y-%m-%d %H:%M:%S'
    :return: 格式化后的日期时间字符串
    """
    return datetime.datetime.fromtimestamp(value).strftime(format)


@app.template_filter('filesizeformat')
def filesizeformat(value, decimals=2):
    """
    文件大小格式化模板过滤器
    将字节大小转换为合适的单位（B、KB、MB、GB、TB）
    
    :param value: 文件大小（字节）
    :param decimals: 保留的小数位数，默认为2
    :return: 格式化后的文件大小字符串
    """
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(value)
    i = 0
    # 根据大小自动选择合适的单位
    while size >= 1024 and i < len(units) - 1:
        size /= 1024
        i += 1
    return f"{size:.{decimals}f} {units[i]}"

def get_local_ip():
    """
    获取本地IP地址的第一种方法
    通过hostname获取本地IP
    
    :return: 本地IP地址字符串
    """
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    #print(f"The IP address of {hostname} is {ip_address}")
    return ip_address

def get_local_ip_1():
    """
    获取本地IP地址的第二种方法
    通过连接外部服务器获取本地IP
    
    :return: 本地IP地址字符串
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 尝试连接到百度 DNS 服务器，获取本地 IP
        s.connect(('180.76.76.76', 80))
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    return local_ip


class UploadFileForm(FlaskForm):
    """
    文件上传表单类
    使用Flask-WTF实现文件上传表单
    """
    file = FileField("File")  # 文件字段

def get_available_files():
    """
    获取可用文件列表
    从文件存储目录中获取所有文件的信息
    
    :return: 文件信息列表，每个元素为包含文件详细信息的字典
             字典包含：name（文件名）、size（大小）、created（创建时间）、modified（修改时间）
    """
    files = []
    for filename in os.listdir(FILE_STORAGE_DIR):
        file_path = os.path.join(FILE_STORAGE_DIR, filename)
        if os.path.isfile(file_path):
            stat_info = os.stat(file_path)
            files.append({
                'name': filename,          # 文件名
                'size': stat_info.st_size,  # 文件大小（字节）
                'created': stat_info.st_ctime,  # 创建时间（时间戳）
                'modified': stat_info.st_mtime  # 修改时间（时间戳）
            })
    return files

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    文件上传路由
    处理文件上传功能，支持GET和POST请求
    GET请求：显示上传表单
    POST请求：处理文件上传
    
    :return: GET请求返回上传表单页面，POST请求上传成功后重定向到首页
    """
    form = UploadFileForm()
    if form.validate_on_submit():
        # 表单验证通过，处理文件上传
        uploaded_file = form.file.data
        # 获取安全的文件名
        filename = secure_filename(uploaded_file.filename)
        # 构建文件保存路径
        file_path = os.path.join(FILE_STORAGE_DIR, filename)
        # 保存文件
        uploaded_file.save(file_path)
        # 重定向到首页
        return redirect(url_for('index'))
    # 返回上传表单页面
    return render_template('upload.html', form=form)


@app.route('/download/<filename>')
def download(filename):
    """
    文件下载路由
    根据文件名提供文件下载功能
    
    :param filename: 要下载的文件名
    :return: 文件下载响应
    """
    # 构建文件路径
    file_path = os.path.join(FILE_STORAGE_DIR, filename)
    # 检查文件是否存在
    if os.path.isfile(file_path):
        # 返回文件下载响应
        return send_from_directory(FILE_STORAGE_DIR, filename, as_attachment=True)
    else:
        # 文件不存在，返回404错误
        os.abort(404, "File not found.")


@app.route('/')
def index():
    """
    首页路由
    显示可用文件列表
    
    :return: 首页页面，包含可用文件列表
    """
    # 获取可用文件列表
    available_files = get_available_files()
    # 返回首页页面，传递文件列表
    return render_template('index.html', files=available_files)

# 检查文件存储目录是否存在，如果不存在则创建
if not os.path.exists(FILE_STORAGE_DIR):
    os.makedirs(FILE_STORAGE_DIR)


if __name__ == '__main__':
    """
    应用入口点
    启动Flask应用服务器
    """
    # 获取本地IP地址
    ip = get_local_ip()
    # 启动Flask应用，开启调试模式，监听指定端口和IP
    app.run(debug=True, port=8888, host=ip)