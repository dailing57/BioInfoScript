inputfile = 'pan7.txt'
outputfile = 'out.txt'
mp = {}
bits, tot = 0, 0
def fixBit(type):
    cnt1 = cnt0 = 0
    for i in range(1, 1<<bits):
        if (i & type) == type:
            cnt1 += mp[i]
        if (i | (~type)) == (~type):
            cnt0 += mp[i]
    return cnt1,cnt0

for line in open(inputfile):
    t = line.split()
    bits = len(t[0])
    tmp = int(t[1])
    mp[int(t[0],2)] = tmp
    tot += tmp
f = open(outputfile,'w+')
for i in range(1,(1<<bits)):
    cro,cnt0 = fixBit(i)
    pan = tot - cro - cnt0
    f.write(bin(i).replace('0b','').zfill(bits)
    + ' ' +str(cro)+ ' ' +str(pan)+'\n')


