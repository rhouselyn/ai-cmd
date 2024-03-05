import os
import sys  # 导入sys库以访问正在运行的Python解释器的路径


def find_python_executable():
    python_executable_path = sys.executable  # 获取当前Python解释器的路径
    if python_executable_path:
        print(f"Found Python executable at: {python_executable_path}")
        return python_executable_path
    else:
        print("Python executable not found.")
        return None


# 获取当前脚本所在目录
current_directory = os.path.dirname(os.path.realpath(__file__))

ai_script_path = os.path.join(current_directory, 'ask.py')
cmd_script_path = os.path.join(current_directory, 'gen.py')
python_executable = find_python_executable()

if python_executable and ai_script_path and cmd_script_path:
    # 创建批处理文件内容
    ai_batch_content = f"""@echo off
"{python_executable}" "{ai_script_path}" %*
"""
    cmd_batch_content = f"""@echo off
"{python_executable}" "{cmd_script_path}" %*
"""
    # 写入批处理文件
    ai_file_path = os.path.join(current_directory, 'ask.bat')
    with open(ai_file_path, 'w') as file:
        file.write(ai_batch_content)

    cmd_file_path = os.path.join(current_directory, 'gen.bat')
    with open(cmd_file_path, 'w') as file:
        file.write(cmd_batch_content)

    print(f"ai batch file created at: {ai_file_path}")
    print(f"cmd batch file created at: {cmd_file_path}")
    print('\n***\nPlease enter this address in the PATH of the system environment variable manually:\n',
          current_directory, '\n***')
else:
    print("Python executable, ask.py or gen.py not found.")
