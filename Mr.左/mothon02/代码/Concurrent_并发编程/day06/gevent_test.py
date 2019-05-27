import gevent


def foo(a, b):
    print('Running foo...\n', a, b)
    gevent.sleep(3)
    print('Foo again')


def bar():
    print('Running foo...\n')
    gevent.sleep(3)
    print('Bar again')


# 将函数封装为协程，遇到gevent阻塞自动执行
f = gevent.spawn(foo, 'hello', 'kitty')
g = gevent.spawn(bar)

gevent.joinall([f, g])  # 阻塞等待协程执行完毕
"""
Running foo...
 hello kitty
Running foo...

Foo again
Bar again

"""