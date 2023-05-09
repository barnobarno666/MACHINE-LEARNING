import os
import random
#import pandas 
folder = r"C:\Users\defaultuser0.LAPTOP-LRB3T941\Downloads\Telegram Desktop" 
"""
for file in os.listdir(folder):
    old_path = os.path.join(folder, file)
    new_name = str(random.randint(1, 1000))+'.jpg' # change this to your desired range of numbers
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)
"""
#filee=open('file.txt','w')
datas =os.listdir(folder)
#filee.write(str(data))
#data=list(data) 
""" f=''         
for i in range(len(data)):
    if data[i]== ',' or ' ,' or ', ':
        f=data[i:]+'jfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffj'+data[:i+1]
        #print(i)
#print(f)
#filee.write(str(data))
#data.to_csv('1.csv') """

def name_changer(name):
    print(name)
    name=list(name) 
    for i in range(len(name)):
        if name[i]==r'-' or name[i]==r'_' :
            #print(name[i])
            name[i] = ' '
            #print(name[i])
    return ''.join(name)

    
#print(name_changer('eBook-How-to-Build-a-Career-in-AI.pdf'))        
        

#CODE TO CHange the book names in the folder :
for file in datas:
    old_name= os.path.join(folder,file)
    new_name=name_changer(file)
    new_path=os.path.join(folder,new_name)
    os.rename(old_name, new_name)
    
    
