import sys
import platform
import os

print("\nPython 环境参数：")
print(f"Python 版本: {platform.python_version()}")
print(f"Python 可执行文件: {sys.executable}")
print(f"操作系统: {platform.system()} {platform.release()}")
print(f"平台: {platform.platform()}")
print(f"当前工作目录: {os.getcwd()}")
# print(f"环境变量 PATH: {os.environ.get('PATH')}")

print("Hello, WSL!")
