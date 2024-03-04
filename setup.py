import os


def find_python_executable_and_main(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for f in files:
            if f == 'python.exe':
                python_executable_path = os.path.join(subdir, f)
                print(f"Found Python executable at: {python_executable_path}")
                return python_executable_path  # 返回找到的第一个python.exe路径
    print("Python executable not found.")
    return None


# 获取当前脚本所在目录
current_directory = os.path.dirname(os.path.realpath(__file__))

ai_script_path = os.path.join(current_directory, r'ask.py')
cmd_script_path = os.path.join(current_directory, r'gen.py')
python_executable = find_python_executable_and_main(current_directory)

if python_executable and ai_script_path and cmd_script_path:
    # 创建批处理文件内容
    ai_batch_content = f"""@echo off
{python_executable} {ai_script_path} %*
"""
    cmd_batch_content = f"""@echo off
{python_executable} {cmd_script_path} %*
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
    print("Python executable or main.py not found.")
