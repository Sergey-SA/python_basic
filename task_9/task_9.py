import threading
import time

def fun(interval, num):
    print('Start Fun:', num, time.ctime())
    for i in range(0,10):
        print('Fun', num, ':', 10 - i)
        time.sleep(interval)
    print('Stop Fun:', num, time.ctime())

t1 = threading.Thread(target=fun, args=(1,1))
t2 = threading.Thread(target=fun, args=(1.1,2))

t1.daemon = True
t1.start()

t2.daemon = True
t2.start()

t2.join()
