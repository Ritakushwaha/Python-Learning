# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:29:07 2021

@author: rikushwa
"""

def checkKey(dict, key):
       
    if key in dict.keys():
        print("Key exist, ", end =" ")
        dict.update({key:600})
        print("value updated =", 600)
    else:
        print("Not Exist")
        
    list1 = dict.values()
    list2 = dict.keys()
    list3 = dict.items()
    
    print(list1,'\n',list2,'\n',list3)
    
dict = {'m': 700, 'n':100, 't':500}
   
key = 'm'
checkKey(dict, key)
print(dict)