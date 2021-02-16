from os import listdir
from os.path import isfile,join
mypath='D:\RocksDownloads'
dictionary={}
file_list=[f for f in listdir(mypath) if isfile(join(mypath,f))]
for f in file_list:
    if f not in dictionary.keys():
        dictionary[f]=0
    dictionary[f]+=1
print(dictionary)
for f in file_list:
    if dictionary[f]>1:
        print(f,sep='\n')