import re
filename = (r"\частотные словари\python\corpus.txt")
infile = open(filename, 'r', encoding="utf-8")
lines = infile.readlines()
t1 = ""
for i in range(len(lines)):
    if len(t1) < 1500000:
        for j in range(len(lines[i])):
            if len(t1) >= 1500000:
                break
            else:
                t1 += lines[i][j]
f = open(r'\частотные словари\python\200000.txt', 'w', encoding="utf-8")
f.write(t1)
f.close

filename = (r"\частотные словари\python\200000.txt")
infile = open(filename, 'r', encoding="utf-8")
lines = infile.readlines()
t1 = ""
for i in range(len(lines)):
    if len(t1) < 700000:
        for j in range(len(lines[i])):
            if len(t1) >= 700000:
                break
            else:
                t1 += lines[i][j]
f = open(r'\частотные словари\python\100000.txt', 'w', encoding="utf-8")
f.write(t1)
f.close

filename = (r"\частотные словари\python\100000.txt")
infile = open(filename, 'r', encoding="utf-8")
lines = infile.readlines()
t1 = ""
for i in range(len(lines)):
    if len(t1) < 300000:
        for j in range(len(lines[i])):
            if len(t1) >= 300000:
                break
            else:
                t1 += lines[i][j]
f = open(r'\частотные словари\python\50000.txt', 'w', encoding="utf-8")
f.write(t1)
f.close

filename = (r"\частотные словари\python\50000.txt")
infile = open(filename, 'r', encoding="utf-8")
lines = infile.readlines()
t1 = ""
for i in range(len(lines)):
    if len(t1) < 160000:
        for j in range(len(lines[i])):
            if len(t1) >= 160000:
                break
            else:
                t1 += lines[i][j]
f = open(r'\частотные словари\python\20000.txt', 'w', encoding="utf-8")
f.write(t1)
f.close

filename = (r"\частотные словари\python\20000.txt")
infile = open(filename, 'r', encoding="utf-8")
lines = infile.readlines()
t1 = ""
for i in range(len(lines)):
    if len(t1) < 60000:
        for j in range(len(lines[i])):
            if len(t1) >= 60000:
                break
            else:
                t1 += lines[i][j]
f = open(r'\частотные словари\python\10000.txt', 'w', encoding="utf-8")
f.write(t1)
f.close

filename = (r"\частотные словари\python\10000.txt")
infile = open(filename, 'r', encoding="utf-8")
lines = infile.readlines()
t1 = ""
for i in range(len(lines)):
    if len(t1) < 8000:
        for j in range(len(lines[i])):
            if len(t1) >= 8000:
                break
            else:
                t1 += lines[i][j]
f = open(r'\частотные словари\python\1000.txt', 'w', encoding="utf-8")
f.write(t1)
f.close