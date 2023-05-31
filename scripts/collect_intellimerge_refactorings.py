#
# Read csv files from intellimerge results and create a refactoring dataframe
#

import os
import glob
import pandas as pd

file_refat = 1
cont = 1
l_ini_p1 = 0
l_fim_p1 = 0
df_ours = pd.DataFrame()
df2_ours = pd.DataFrame()
repository_ours_merge = pd.DataFrame()

df_theirs = pd.DataFrame()
df2_theirs = pd.DataFrame()
repository_theirs_merge = pd.DataFrame()
for root, subFolder, files in os.walk(r"folder-with-intellimerge-results"):
    for item in files:
        if item.endswith(".csv") :
            arquivo = os.path.join(root, item)
            f = open(arquivo, 'r')
            if 'ours_refactorings.csv' in item :
                df_intellimerge = pd.read_csv(arquivo, sep=';')
                directory = arquivo.split('\\')
                new_before = df_intellimerge["before_location"].str.split("-", n = 1, expand = True) 
                df_intellimerge["bf_line_ini"] = new_before[0]
                df_intellimerge["bf_line_end"] = new_before[1] 
                new_after = df_intellimerge["after_location"].str.split("-", n = 1, expand = True) 
                df_intellimerge["af_line_ini"] = new_after[0] 
                df_intellimerge["af_line_end"] = new_after[1] 
                df2_ours = df_intellimerge.assign(merge_id = directory[7], repository = 'name_of_repository')
                df2_ours.drop(columns =["before_location"], inplace = True) 
                df2_ours.drop(columns =["after_location"], inplace = True) 
                repository_ours_merge = pd.concat([df_ours, df2_ours])
                df_ours = repository_ours_merge
            if 'theirs_refactorings.csv' in item :
                df_intellimerge = pd.read_csv(arquivo, sep=';')
                directory = arquivo.split('\\')
                new_before = df_intellimerge["before_location"].str.split("-", n = 1, expand = True) 
                df_intellimerge["bf_line_ini"] = new_before[0]
                df_intellimerge["bf_line_end"] = new_before[1] 
                new_after = df_intellimerge["after_location"].str.split("-", n = 1, expand = True) 
                df_intellimerge["af_line_ini"] = new_after[0] 
                df_intellimerge["af_line_end"] = new_after[1]           
                df2_theirs = df_intellimerge.assign(merge_id = directory[7], repository = 'name_of_repository')
                df2_theirs.drop(columns =["before_location"], inplace = True) 
                df2_theirs.drop(columns =["after_location"], inplace = True) 
                repository_theirs_merge = pd.concat([df_theirs, df2_theirs])
                df_theirs = repository_theirs_merge
print("finished...")