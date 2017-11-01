'''
Created on 10 окт. 2016 г.

@author: skrainov
'''
import os.path,time
'''
 ��������� ����� ��������� ����� ������� ��������� �� ������� ������ 1-� �����
 ''' 
def delOldFile(file):    
    mtime=os.path.getctime(file)
    diff_second=time.time()-os.path.getctime(file)
    if diff_second>864000:
        print(file)
        os.remove(file)

pathlist=["\\\srvsql2-st1\\k$\\PKUESN\\","\\\srvsql2-st1\\k$\\ACCOTFOMS2011\\","\\\srvsql2-st1\\k$\\Accotfoms97\\","\\\srvsql2-st1\\k$\\DoctorsExperts\\"]

for path in pathlist:
    print(path)
    for name in os.listdir(path):                  
        if name.endswith(".bak"):                       
            delOldFile(os.path.join(path+name))