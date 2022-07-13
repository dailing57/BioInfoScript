import argparse


parser = argparse.ArgumentParser()
parser.add_argument('inputfile')
parser.add_argument('outputfile')
args = parser.parse_args()
inputfile = args.inputfile
outputfile = args.outputfile

bits, tot = 0, 0
fg = False
preSuper, preSub = [], []
for line in open(inputfile):
    t = line.split()
    if not fg:
        fg = True        
        bits = len(t[0])
        preSuper = [0 for i in range(1<<bits)]
        preSub = [0 for i in range(1<<bits)]
    K, V = int(t[0],2), int(t[1])
    preSuper[K] = preSub[K] = V
    tot += V

for j in range(bits):
    for i in range(1<<bits):
        if ((i>>j) & 1) == 0:
            preSuper[i] += preSuper[i ^ (1 << j)]
        else:
            preSub[i] += preSub[i ^ (1 << j)]

f = open(outputfile,'w+')
for i in range(1,(1<<bits)):
    cro,cnt0 = preSuper[i], preSub[(((1<<bits) - 1) & (~i))]
    pan = tot - cnt0
    f.write(bin(i).replace('0b','').zfill(bits)
    + ' ' +str(cro)+ ' ' +str(pan)+'\n')
