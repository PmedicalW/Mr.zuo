# 僵尸进程的演示以及wait的处理
import os

pid = os.fork()

if pid < 0:
    print("Error")

elif pid == 0:
    print("Child process:", os.getpid())
    os._exit(2)  # 系统会＊256

else:
    # pid,status=os.wait() # 等待处理僵尸
    pid, status = os.waitpid(-1, os.WNOHANG)  # 非阻塞
    print("pid:", pid)  # 退出的子进程的PID
    print("status:", os.WEXITSTATUS(status))  # 子进程退出状态
    while True:
        pass
"""
pid: 0
status: 0
Child process: 12734
"""