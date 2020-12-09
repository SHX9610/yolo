
import os
f = open('F:\Projects\yolov3\yolov3-jws\data\\val.txt', 'w')
paths = "F:\Projects\yolov3\yolov3-jws\data\\val\\"
files = os.listdir(paths)
files.sort()
for file in files:
    path = paths + file
    f.write(path + '\n')
f.close()



