#!/usr/bin/python3
#coding:utf-8
 
from multiprocessing import Process, Queue, Pool, Manager
from time import sleep

def func(q, n):
    #q.put(['index', n])
    sleep(n)
    return ['index', n]

def callback(arg):
    q.put(arg)
 
if __name__ == '__main__':

    manager = Manager()
    q = manager.Queue()
    #q = Queue() #用进程池Poll方式建立子进程时, 不可用于父子进程间通信

    '''
    pr = []
    for i in range(5):
        p = Process(target=func, args=(q,i))
        p.start()
        pr.append(p)
    '''

    pool = Pool(4)
    for i in range(5):
        p = pool.apply_async(func, args=(q, i), callback=callback)
    
    print('父子线程通信开始')
    res = []
    while len(res) < 5:
        value = q.get(True)
        res.append(value)
        print(value)
    print('父子线程通信结束')
    
    pool.close()
    pool.join()
    pool.terminate()
    
    '''
    for p in pr:
        p.join()
        print(p.is_alive())
        p.terminate()
    '''
    
    
