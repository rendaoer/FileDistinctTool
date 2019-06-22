import os
import shutil

print("FileDistinctTool version:0.0.1")

filePath = input("Please enter the folder you want to scan：")
zus = os.listdir(filePath)
sets = {}
try:
    print("start")
    for i in zus:
        pathi = filePath + "\\" + i
        for j in zus:
            pathj = filePath + "\\" + j
            if j == i:
                continue
            if os.stat(pathi).st_size == os.stat(pathj).st_size:
                if sets.get(i) == None:
                    if sets.get(j) == None:
                        sets[i] = j
    k = sets.keys()
    v = sets.values()
    print("k:",k)
    print("v:",v)
    if len(sets) > 0:
        for i in sets:
            pathi = filePath + "\\" + i
            os.remove(pathi)
    print("end...")
except Exception as e:
    print("error：",e)
