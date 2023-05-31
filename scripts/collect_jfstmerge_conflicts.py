#
# Collect conflicts in jFSTMerge results
#


import os
import glob
import pandas as pd

num_files = 1

df2 = pd.DataFrame(columns = ['file'])

for root, subFolder, files in os.walk(r"C:\results_jfst\javaparser"):
    for item in files:
        if item.endswith(".txt"):
            file_path = os.path.join(root, item)
            f = open(file_path, 'r')
            for line in f:
                if ('CONFLICT' in line) & ('.java' in line):
                    df2=df2.append({'file' : os.path.join(root, item)} , ignore_index=True)
                    num_files = num_files + 1
                    continue
            f.close()
print("Files with conflicts: ", num_files)
df2

print("finished...")