import time

from dbf import DbfBreak


from multiprocessing import Process, Pool, Manager
import threading

def run():
    if __name__ == '__main__':
        file_path = r'SJSGB.dbf'
        res = DbfBreak(file_path)

        print('Loaded')
        current = time.time()
        p = Pool(8)
        queue = Manager().Queue()
        def callback(arg):
            queue.put(arg)
        res_list=[]

        for i in range(10):
            p.apply_async(res.Break, args=('file/breack'+str(i)+'.dbf',), kwds={'gbrq1':None, 'gbje1':0}, callback=callback)
        
        result_list = []
        while len(result_list) < 10:
            value = queue.get(True)
            result_list.append(value)
            print('Get %s from queue.' % value)
        
        p.close()
        p.join()
        p.terminate()
        print('多进程完成时间：', time.time()-current)
        print('Finished')

t = threading.Thread(target=run)
t.start()
t.join()

    
    