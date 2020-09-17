# -*- coding: utf-8 -*-
__author__ = 'zengyong'

import struct
import datetime, time
import asyncio
import aiofiles

class DbfBreak:
    __slots__ = ('headers', 'content', 'sortindex', 'year', 'mon', 'day', 'file_path')

    def __init__(self, file_path, date_time=None):
        'date_time is datetime'
        self.year, self.mon, self.day = (date_time.year - (date_time.year//100)*100, date_time.month, date_time.day) if date_time else (None,)*3

        self.file_path = file_path
        self.sortindex = {}
        self._header()
        self._load()

    def _header(self):
        with open(self.file_path, 'rb') as fp:
            header = fp.read(12)
            #print('buffer:', len(header))
            ver, year, mon, day, numrec, lenheader, lenrecord = struct.unpack('<BBBBLHH', header)
            #print(ver, year, mon, day, numrec, lenheader, lenrecord)
            if self.year == None or self.mon == None or self.day == None:
                self.year, self.mon, self.day = year, mon, day
            self.headers = {'header_version': ver}

            header_rec = fp.read(lenheader-12)
            self.headers.update({'header_other_bytes': header_rec})
            
            #输出当前文件指针偏移
            #pos = fp.tell()
            #print('seek-pos-begin :', pos)

            #设置文件指针偏移
            #fp.seek(lenheader, 0) #0表示文件开头，1表示当前文件指针位置，2表示文件尾
            #print('seek-pos-end:', fp.tell())

            #fmt=''
            #num = 0
            fieldspecs = []
            fp.seek(32, 0)
            for n in range((lenheader-33)//32):
                filed = fp.read(32)
                name, rec_cat, rec_len, rec_deci = struct.unpack('11sc4xBB14x', filed)
                #print(name, rec_cat, rec_len)
                
                #bytes转str
                #name = str(name, encoding='ascii')
                #str转bytes
                #bstring = bytes('string', encoding='utf-8')
                
                #print(name.split('\x00')[0], end=',')
                #print(str(len(name))+':'+name+'|'+str(rec_len)+'|'+str(rec_deci), end='\n')

                #num += rec_len
                #fmt += str(rec_len)+'s'
                fieldspecs.append((rec_cat, rec_len, rec_deci))
                '''
                if rec_cat == b'C':
                	fmt += str(rec_len)+'s'
                elif rec_cat == b'N':
                	fmt += str(rec_len)+'d' #实际以文本形式储存，应为's'
                elif rec_cat == b'D':
                    fmt += str(rec_len)+'s'
                elif rec_cat == b'L':
                    fmt += str(rec_len)+'s'
                else:
                    raise struct.error('bad char in struct format')
                '''
            #print(num, fmt)
            self.headers.update({'fieldspecs': fieldspecs})
            
            '''
            fp.seek(lenheader, 0)
            for i in range(numrec):
                rec_data = fp.read(lenrecord)
                print(len(rec_data))
                rec_content = (str(n, encoding='gbk') for n in struct.unpack('x'+fmt, rec_data))
                print(list(rec_content))
            '''

            return self.headers

    def _load(self):
        from dbfread import DBF
        #import bisect
        table = DBF(self.file_path, encoding='gbk')
        self.content = list(table)
        #self.content = sorted(table, key=lambda x: x[sortkey.upper()])
        return self.content

    def _index(self, sortkeys):
        #fp = open('sort.index', 'w+')
        for sortkey in sortkeys:
            self.sortindex.update({sortkey:{}})
        for line_no, record in enumerate(self.content, 0):
            #pos = bisect.bisect(sortindex, record[sortkey])
            #bisect.insort(sortindex, record[sortkey])
            #fp.write(','.join(record), )
            for sortkey in sortkeys:
                key = record[sortkey.upper()]
                if str(key).strip():
                    try:
                        index = [str(key),str(int(key))][int(key)==key]
                    except:
                        index = str(key)
                else:
                    index = 'None'
                self.sortindex[sortkey].setdefault(index, []).append(line_no)
        return self.sortindex

    async def _write(self, outpath, records=[]):
        ver = self.headers['header_version']
        fieldspecs = self.headers['fieldspecs']
        numrec = len(records)
        numfields = len(fieldspecs)
        lenheader = numfields * 32 + 33
        lenrecord = sum(field[1] for field in fieldspecs) + 1
        header = struct.pack('<BBBBLHH', ver, self.year, self.mon, self.day, numrec, lenheader, lenrecord) + self.headers['header_other_bytes']
        #print(header)
        #mock_file = mock.MagicMock()
        #with mock.patch('aiofiles.threadpool.sync_open', return_value=mock_file) as mock_open:
        async with aiofiles.open(outpath, mode='wb') as fp:
            await fp.write(header)
            for record in records:
                content = b' ' # deletion flag
                for (typ, size, deci), value in zip(fieldspecs, record):
                    if typ == b"N":
                        value = str(value) #.rjust(size, ' ') #round(float(value), deci)
                        if '.' not in value:
                            value += '.'+'0'*deci
                        elif '.' in value:
                            num  = len(value.split('.')[-1])
                            if num < deci:
                                value += '0'*(deci-num)
                            else:
                                x, y = value.split('.')
                                value = x + y[:deci]
                        value = bytes(value.encode('gbk')).rjust(size, b' ')
                    elif typ == b'D':
                        value = value.strftime('%Y%m%d')
                        value = bytes(value.encode('gbk'))
                    elif typ == b'L':
                        value = str(value)[0].upper()
                        value = bytes(value.encode('gbk'))
                    else:
                        value = str(value)#[:size].ljust(size, ' ')
                        value = bytes(value.encode('gbk'))[:size].ljust(size, b' ')
                    assert len(value) == size
                    content += value
                await fp.write(content)
            await fp.write(b'\x1A')
        return

    async def Break(self, outpath, if_break=True, **kwargs):
        print('开始拆分')
        if if_break:
            if not kwargs:
                raise MyError('You want to break dbf file, while none kwargs limitations!')
            if not self.sortindex:
                self._index(kwargs.keys())
            #print(self.sortindex)
            '''
            numrec = 0
            def records():
                nonlocal numrec
                for record in table:
                    #print(record.values())
                    #records.append(record.values())
                    numrec += 1
                    yield record.values()
            #records = (record.values() for record in table)
            '''
            records = []
            lines = []
            for sortkey, sortvalue in kwargs.items():
                lines += self.sortindex[sortkey].get(str(sortvalue), None) 
            lines = sorted(set(lines))
            for line in lines:
                records.append(self.content[line].values())
            await self._write(outpath, records)
        else:
            import shutil
            shutil.copyfile(self.file_path, outpath)   

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

if __name__ == '__main__':
    from unittest import mock
    from aiofiles import threadpool
    
    file_path = r'SJSGB.dbf'
    '''
    now = datetime.datetime.now()
    yr, mon, day = now.year, now.month, now.day
    print(yr, mon, day)
    '''
    #set_date = datetime.date(2019, 4, 20)
    #year, mon, day = set_date.year, set_date.month, set_date.day
    #res = Dbf_Break(path, set_date)
    #default datetime
    res = DbfBreak(file_path)
    #res = res.header_format(path)
    #print(res.headers)
    print('Loaded')
    current = time.time()
    #aiofiles.threadpool.wrap.register(mock.MagicMock)(lambda *args, **kwargs: threadpool.AsyncBufferedIOBase(*args, **kwargs))
    loop = asyncio.get_event_loop()
    tasks = [res.Break('file/breack'+str(i)+'.dbf', gbrq1=None, gbje1=0) for i in range(3)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print('协程aiofiles完成时间：', time.time()-current)
    print('Finished')
    #print('finish loaded')
    #res.Break('loaded.dbf', gbzd='长信发债')
    #res.Break('copy.dbf', False)

    '''
    #test
    content = res.write_content([["天风证券股份有限公司", datetime.datetime.now(), 123.126, 'f'],
        ["证券股份有限公司", datetime.datetime.now(), 334.23, 't'], 
        ["天风证券股份有限公司", datetime.datetime.now(), 323.59, 't']])
    ver, year, mon, day, numrec, lenheader, lenrecord = struct.unpack('<BBBBLHH', content[:12])
    print(ver, year, mon, day, numrec, lenheader, lenrecord)
    with open('break.dbf', 'wb') as fp:
        fp.write(content)
    '''
    
    '''
    from dbfread import DBF
    table = DBF('break.dbf', encoding='gbk')
    for record in table:
        print(record)
    '''
    
    