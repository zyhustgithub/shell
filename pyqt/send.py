import time, os, glob, subprocess
#import shutil
from excel import PRODUCT_CATEGORY, PRODUCT_NAME, PRODUCT_SEND_PATH, PRODUCT_SEND_NAME, IF_UZIP

def send(records, date_time):
    #print(date_time, records)
    results = []

    errors = []
    for record in records:
        errors.append((record[0:3], False))

    source_path = False
    des_path = False
    with open("path.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            if "#" not in line:
                record = [n.strip() for n in line.split("=")]
                tmp_path = record[-1]
                if "source_path" == record[0].lower():
                    if "YYYYMMDD" in tmp_path:
                        tmp_path = tmp_path.replace("YYYYMMDD", date_time)
                    if "yyyymmdd" in tmp_path:
                        tmp_path = tmp_path.replace("yyyymmdd", date_time)
                    if os.path.isdir(tmp_path):
                        source_path = tmp_path
                elif "des_path" == record[0].lower():
                    if os.path.isdir(tmp_path):
                        des_path = tmp_path
                elif "haozip" == record[0].lower():
                    haozip = tmp_path
                    if '.' not in haozip:
                        haozip = os.path.join(os.path.dirname(haozip), "HaoZipC.exe")
                    
    if not (source_path and des_path): #存在配置文件错误
        return errors

    Send_Path = None
    for record in records:
        if not Send_Path:
            Send_Path = record[PRODUCT_SEND_PATH]
        else:
            if Send_Path != record[PRODUCT_SEND_PATH]: #发送目录存在不同情况，则应报错
                return errors

    if not Send_Path:
        return errors

    empty_send_path = False
    if '\\' in Send_Path or '/' in Send_Path:
        if not os.path.isdir(Send_Path):
            p = subprocess.Popen('md '+Send_Path+'>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
            p.wait() #.communicate()
            empty_send_path = True
        if os.path.isdir(Send_Path):
            send_path_dir = Send_Path
        else:
            return errors
    else:
        send_path_dir = os.path.join(des_path, Send_Path)
        if not os.path.isdir(send_path_dir):
            p = subprocess.Popen('md '+send_path_dir+'>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
            p.wait() #.communicate()
            empty_send_path = True
        if not os.path.isdir(send_path_dir):
            return errors

    if not empty_send_path:    
        if os.path.isdir(send_path_dir):
            #os.system('rd /s/q '+send_path_dir)
            p = subprocess.Popen('rd /s/q '+send_path_dir+'>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
            p.wait() #.communicate()
        if os.path.isfile(send_path_dir):
            p = subprocess.Popen('del /s/q '+send_path_dir+'>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
            p.wait() #.communicate()
        #os.system('md '+send_path_dir)
        while not os.path.isdir(send_path_dir):
            p = subprocess.Popen('md '+send_path_dir+'>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
            p.wait() #.communicate()
    
    for record in records:
        Ori_Name = record[PRODUCT_NAME]
        Send_Name = record[PRODUCT_SEND_NAME]
        Uzip = record[IF_UZIP]

        source_path_dir = os.path.join(source_path, date_time) #(source_path, date_time, Ori_Name)
        source_file = os.path.join(source_path_dir, Ori_Name+date_time+".zip")
        files_num = glob.glob(source_file)
        if len(files_num) > 0:
            #os.system('copy /y '+source_file+' '+send_path_dir+' >nul')
            p = subprocess.Popen('copy /y '+source_file+' '+send_path_dir+'>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
            p.wait() #.communicate()
        else:
            results.append((record[0:3], False))
            continue

        des_file = os.path.join(send_path_dir, os.path.basename(source_file))
        if Send_Name:
            if '/' in Send_Name or '\\' in Send_Name:
                Send_Name = Send_Name.replace("YYYYMMDD", date_time)
                Send_Name = Send_Name.replace("yyyymmdd", date_time)
                if '/' in Send_Name:
                    send_child_path = list( filter(None, map(lambda x: x.strip(), os.path.dirname(Send_Name).split('/'))) )
                else:
                    send_child_path = list( filter(None, map(lambda x: x.strip(), os.path.dirname(Send_Name).split('\\'))) )
                if '.' in Send_Name:
                    ren_file_name = os.path.basename(Send_Name)
                    '''
                    if 'YYYYMMDD' in ren_file_name:
                        ren_file_name = ren_file_name.replace("YYYYMMDD", date_time)
                    if 'yyyymmdd' in ren_file_name:
                        ren_file_name = ren_file_name.replace("yyyymmdd", date_time)
                    '''
                    p = subprocess.Popen('ren '+des_file+' '+ren_file_name+'>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
                    p.wait() #.communicate()
                    source_child_path = os.path.join(send_path_dir, ren_file_name)
                else:
                    source_child_path = des_file
                move_child_path = os.path.join(send_path_dir, *send_child_path)
                if not os.path.isdir(move_child_path):
                    p = subprocess.Popen('md '+move_child_path+'>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
                    p.wait() #.communicate()
                p = subprocess.Popen('move /y '+source_child_path+' '+move_child_path+'>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
                p.wait() #.communicate()
                des_file = os.path.join(move_child_path, os.path.basename(source_child_path))

            elif '.' in Send_Name:
                ren_file_name = Send_Name
                if 'YYYYMMDD' in ren_file_name:
                    ren_file_name = ren_file_name.replace("YYYYMMDD", date_time)
                if 'yyyymmdd' in ren_file_name:
                    ren_file_name = ren_file_name.replace("yyyymmdd", date_time)
                #os.system('ren '+des_file+' '+ren_file_name)
                p = subprocess.Popen('ren '+des_file+' '+ren_file_name+'>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
                p.wait() #.communicate()
                des_file = os.path.join(send_path_dir, ren_file_name)
            else:
                #os.system('ren '+des_file+' '+Send_Name+date_time+".zip")
                p = subprocess.Popen('ren '+des_file+' '+Send_Name+date_time+".zip"+'>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
                ##p.wait() #.communicate()
                ##des_file = os.path.join(send_path_dir, Send_Name+date_time+".zip")
        #os.system('cd.>'+des_file+'.ok')
        if Uzip:
            send_base_dir = os.path.dirname(des_file)
            p = subprocess.Popen('\"'+haozip+'\" x '+des_file+' -o'+send_base_dir+' -y>nul', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
            p.wait() #.communicate()
            for f in os.listdir(send_base_dir):
                if Uzip == "部分" and f.endswith(".zip"):
                    continue
                send_file = os.path.join(send_base_dir, f)
                p = subprocess.Popen('cd.>'+send_file+'.ok', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
                p.wait() #.communicate()
        else:
            p = subprocess.Popen('cd.>'+des_file+'.ok', close_fds=True, shell=True, stdin=None, stdout=None, stderr=None)
            p.wait() #.communicate()
        results.append((record[0:3], True))
    '''
    for record in records:
        results.append((record[0:3], False))
    '''
    return results