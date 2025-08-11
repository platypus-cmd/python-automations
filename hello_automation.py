from datetime import datetime
import os
import platform

os_name = platform.system()
os_version = platform.version()

python_version = platform.python_version()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

username = os.getlogin()

processor = os.popen("lscpu | grep 'Architecture'").read().strip()
processor = processor.split(':')[1].strip()



print("===== Hello Automation! =====")
print(f"User: {username}")
print(f"Operating System: {os_name} ({os_version})")
print(f"Python Version: {python_version}")
print(f"Processor: {processor}")
print(f"Current Date & Time: {current_time}")
print("=============================")