# 文件共享服务

## 介绍
基于Flask框架开发的文件共享服务，支持文件上传、下载和管理功能。

## 功能特性

- ✅ 文件上传和下载功能
- ✅ 文件列表表格化显示
- ✅ 文件信息展示：文件名、大小、创建时间、修改时间
- ✅ 智能文件大小格式化（自动转换为B、KB、MB、GB等单位）
- ✅ 表格排序功能（支持按文件名、大小、日期排序）
- ✅ 美观的用户界面，包括优化的上传页面和文件选择控件
- ✅ 响应式设计，适配不同设备

## 技术栈

- **后端**：Python Flask
- **前端**：HTML5、CSS3、JavaScript
- **模板引擎**：Jinja2

## 快速开始

### 1. 配置文件存储目录

在 `file_share_service.py` 文件中，您可以修改以下配置：

```python
# 文件存储目录，默认为D盘下的 'download' 文件夹
FILE_STORAGE_DIR = r'D:\download'  # 文件上传下载的存储路径（D盘download目录）
```

### 2. 运行服务

```bash
python file_share_service.py
```

### 3. 访问服务

服务启动后，您可以通过以下地址访问：

```
http://[您的IP地址]:8888
```

### 4. 使用功能

- **上传文件**：点击"Upload File"按钮，选择文件并上传
- **下载文件**：在文件列表中点击文件名旁边的"Download"链接
- **排序文件**：点击表格表头可以按不同列（文件名、大小、日期）进行升序/降序排序

## 关闭服务

1. **命令行运行**：在命令行窗口中按 `Ctrl + C` 组合键即可关闭服务
2. **双击运行**：
   - 在Windows任务管理器中找到名为 `file_share_service.exe` 的进程
   - 选中该进程，然后点击"结束任务"按钮

## 项目结构

```
file_upload_and_download/
├── file_share_service.py  # 主服务文件
├── templates/            # 页面模板
│   ├── index.html        # 文件列表页面
│   └── upload.html       # 文件上传页面
├── download/             # 默认文件存储目录
├── README.md             # 中文说明文档
└── README.en.md          # 英文说明文档
```

## 自定义配置

- **端口号**：在 `file_share_service.py` 中修改 `app.run()` 的 `port` 参数
- **主机地址**：在 `file_share_service.py` 中修改 `app.run()` 的 `host` 参数
- **文件存储路径**：修改 `FILE_STORAGE_DIR` 变量

## 依赖安装

```bash
pip install flask flask-wtf
```

