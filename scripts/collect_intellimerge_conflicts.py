#
# Read java files from intellimerge results and create a conflict dataframe
#

import os
import glob
import pandas as pd

file_refat = 1
cont = 1
l_ini_p1 = 0
l_fim_p1 = 0
path = "folders-with-intellimerge-results"
df = pd.DataFrame(columns = ['arquivo', 'linha_inicio_p1', 'linha_fim_p1', 'linha_inicio_p2', 'linha_fim_p2'])
df2 = pd.DataFrame(columns = ['arquivo'])
for root, subFolder, files in os.walk(r"path"):
    for item in files:
        if item.endswith(".java"):
            arquivo = os.path.join(root, item)
            f = open(arquivo, 'r')
            for linha in f:
                for l_num, l in enumerate(f, 2): 
                    if '<<<<<<< ours' in l: 
                        l_ini_p1 = l_num + 1    
                    if '======='in l:
                        l_fim_p1 = l_num - 1
                        l_ini_p2 = l_num + 1
                    if '>>>>>>> theirs' in l: 
                        l_fim_p2 = l_num - 1
                        if l_ini_p1 > l_fim_p1:
                            l_ini_p1 = l_ini_p1 - 1
                        filename = os.path.join(root, item)     
                        directory = filename.split('\\')
                        df=df.append({'arquivo' : os.path.join(root, item), 'linha_inicio_p1' : l_ini_p1, 'linha_fim_p1' : l_fim_p1, 'linha_inicio_p2' : l_ini_p2, 'linha_fim_p2' : l_fim_p2, 'merge_id': directory[7]} , ignore_index=True)
                        cont = cont + 1
            f.close()
        if item.endswith(".csv") :
            arquivo = os.path.join(root, item)
            f = open(arquivo, 'r')
            arquivo = os.path.join(root, item)
            f = open(arquivo, 'r')
            file_refat = file_refat +1 
            df2=df2.append({'arquivo' : os.path.join(root, item)} , ignore_index=True)
print("finished...")