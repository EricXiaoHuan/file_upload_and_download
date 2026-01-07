import os
import chardet
import platform
import subprocess

def set_writable(file_path):
    try:
        if platform.system() == 'Windows':
            subprocess.run(['attrib', file_path, '-r'], check=True)
        else:
            os.chmod(file_path, 0o666)
    except Exception as e:
        print(f"Failed to change permissions: {str(e)}")

def print_red(text):
    RED = '\033[91m'
    RESET = '\033[0m'
    print(RED + text + RESET)
    
def print_green(text):
    GREEN = '\033[92m'
    RESET = '\033[0m'
    print(GREEN + text + RESET) 
    
def print_yellow(text):
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    print(YELLOW + text + RESET)
    
def print_blue(text):
    BLUE = '\033[94m'
    RESET = '\033[0m'
    print(BLUE + text + RESET)

def is_gb2312(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
        encoding = chardet.detect(content)['encoding']
        if encoding == 'GB2312':
            return True
    return False

def check_and_set_writable(file_path):
    if not os.access(file_path, os.W_OK):
        print_red(f"{file_path} is not writable. Changing permissions...")
        set_writable(file_path)
        print_green(f"Permissions changed. Now {file_path} is writable.")

def convert_encoding(file_path):
    try:
        # 读取文件内容
        check_and_set_writable(file_path)
        
        with open(file_path, 'r', encoding='gb2312') as f:
            content = f.read()

        # 将内容转换为 UTF-8 编码
        content_utf8 = content.encode('utf-8-sig')

        # 写入文件（覆盖原文件）
        with open(file_path, 'w', encoding='utf-8-sig') as f:
            f.write(content_utf8.decode('utf-8-sig'))

        print_green(f"文件 {file_path} 编码已从 GB2312 转换为 utf-8-sig")
    except Exception as e:
        print_red(f"转换文件 {file_path} 时出现错误：{str(e)}")

def batch_convert_encoding(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".cpp") or file.endswith(".h"):
                file_path = os.path.join(root, file)
                if is_gb2312(file_path):
                    convert_encoding(file_path)
                else:
                    print_yellow(f"文件 {file_path} 不是 GB2312 编码，不进行转换")

def main():
    """主函数，用于执行批量转换编码"""
    # 指定需要转换编码的文件夹路径
    folder_path = r"D:\M\FSLogPackerTool\FSLogPackerTool"
    # 执行批量转换编码
    batch_convert_encoding(folder_path)

if __name__ == "__main__":
    main()
