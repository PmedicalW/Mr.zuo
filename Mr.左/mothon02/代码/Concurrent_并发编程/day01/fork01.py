import os

print("=========================")
a = 1

pid = os.fork()

if pid < 0:
    print("Error")

elif pid == 0:
    print("Child process")
    print("a = %d" % a)
    a = 10000

else:
    print("Parent process")
    print("a:", a)

print("All a=", a)
"""
=========================
Parent process
a: 1
All a= 1
Child process
a = 1
All a= 10000
# 父进程fork之前开辟的空间子进程同样拥有，父子进程对各自空间的操作不会相互影响
"""

# 返回值：整数，如果创建进程失败返回一个负数，
# 如果成功则在原有进程中返回新进程的PID，在新进程中返回0
