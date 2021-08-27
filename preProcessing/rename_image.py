import os

file_path = '../afterPre/data1/test'
file_name = os.listdir(file_path)
print(file_name)

i=0
for name in file_name:
    src = os.path.join(file_path, name)
    dst = str(i) + '.png'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1