import time

def timer(func):
    def wrapper():
        print(func)
        start_time = time.time()
        a = func()
        stop_time = time.time()
        print('函数运行时间是%s'%(stop_time - start_time))
        return a

    return wrapper

@timer
def f1():
    # print('函数运行完毕')
    return '这是一个返回值'

# f1 = timer(f1)
f1()