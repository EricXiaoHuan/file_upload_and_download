# File Sharing Service

## Description
A file sharing service developed based on Flask framework, supporting file upload, download and management functions.

## Features

- ✅ File upload and download functionality
- ✅ Table-based file list display
- ✅ File information display: name, size, creation time, modification time
- ✅ Intelligent file size formatting (automatically converts to B, KB, MB, GB, etc.)
- ✅ Table sorting functionality (supports sorting by name, size, date)
- ✅ Beautiful user interface, including optimized upload page and file selection control
- ✅ Responsive design, adapting to different devices

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Template Engine**: Jinja2

## Quick Start

### 1. Configure File Storage Directory

In the `file_share_service.py` file, you can modify the following configuration:

```python
# File storage directory, default is 'download' folder in the current directory
FILE_STORAGE_DIR = os.path.join(os.getcwd(), 'download')
```

### 2. Run the Service

```bash
python file_share_service.py
```

### 3. Access the Service

After the service starts, you can access it through the following address:

```
http://[your-ip-address]:8888
```

### 4. Use the Features

- **Upload File**: Click the "Upload File" button, select a file and upload
- **Download File**: Click the "Download" link next to the file name in the file list
- **Sort Files**: Click the table headers to sort by different columns (name, size, date) in ascending/descending order

## Stop the Service

1. **Running from Command Line**: Press `Ctrl + C` in the command line window to stop the service
2. **Running by Double-click**: 
   - Find the process named `file_share_service.exe` in Windows Task Manager
   - Select the process and click the "End Task" button

## Project Structure

```
file_upload_and_download/
├── file_share_service.py  # Main service file
├── templates/            # Page templates
│   ├── index.html        # File list page
│   └── upload.html       # File upload page
├── download/             # Default file storage directory
├── README.md             # Chinese documentation
└── README.en.md          # English documentation
```

## Custom Configuration

- **Port Number**: Modify the `port` parameter in `app.run()` in `file_share_service.py`
- **Host Address**: Modify the `host` parameter in `app.run()` in `file_share_service.py`
- **File Storage Path**: Modify the `FILE_STORAGE_DIR` variable

## Dependencies Installation

```bash
pip install flask flask-wtf
```

