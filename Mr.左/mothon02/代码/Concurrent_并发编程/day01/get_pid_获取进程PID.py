import os

pid = os.fork()

if pid < 0:
    print("Error")

elif pid == 0:
    print("Child PID", os.getpid())  # 获取一个进程的PID值
    print("Get Parent PID", os.getppid())  # 获取父进程的PID号
else:
    print("Parent PID", os.getpid())
    print("Get Child PID", pid)

"""
Parent PID 12290
Get Child PID 12291
Child PID 12291
Get Parent PID 12290
"""