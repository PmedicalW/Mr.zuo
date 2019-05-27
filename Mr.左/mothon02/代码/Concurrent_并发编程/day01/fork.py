import os
from time import sleep

pid = os.fork()

if pid < 0:  # 这里的pid为fork函数的返回值，并不是系统给的pid值
    print("Create process failed")
elif pid == 0:
    print(pid)
    sleep(3)
    print("The new process")
else:
    print(pid)
    sleep(1)
    print("The old process")

print("Fork test over")

# 返回值：整数，如果创建进程失败返回一个负数，
# 如果成功则在原有进程中返回新进程的PID，在新进程中返回0
