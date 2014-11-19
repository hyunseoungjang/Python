# -*- coding: utf-8 -*-
f = file('s.txt')
lines = []
i = 1
for line in f.readlines():
    lines.append(line.split(' ')[0])
    lines.append(line.split(' ')[1].rstrip('\n'))
    i += 1
f.close()
f = open('s3.txt', 'w+')
i=0
for line in lines :
    f.write(line + ' ')
    i += 1
    if(i%3==0) :
        f.write('\n')
f.seek(0)
print f.read()
f.close()