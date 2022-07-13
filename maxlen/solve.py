import re
import argparse

class node:
    def __init__(self,xp='',seg='') -> None:
        self.xp = xp
        self.seg = seg
parser = argparse.ArgumentParser()
parser.add_argument('inputfile')
parser.add_argument('outputfile')
args = parser.parse_args()
inputfile = args.inputfile
outputfile = args.outputfile
mp:dict[str,node] = {'':node()}
cur,xp,tmp = '','',''
for line in open(inputfile):
    if line[0] == '>':
        if len(tmp) > len(mp[cur].seg):
            mp[cur].seg = tmp
            mp[cur].xp = xp
        try:
            cur = re.findall('\[gene=LOC(\d*)\]',line)[0]
            xp = re.findall('(XP_.*\..*?)\_',line)[0]
        except Exception as e:
            print(line)
        if cur not in mp:
            mp[cur] = node()
        tmp = ''
    else:
        tmp+=line

if len(tmp) > len(mp[cur].seg):
    mp[cur].seg = tmp
    mp[cur].xp = xp
print(len(mp))
with open(outputfile,'w') as f:
    for it in mp:
        if it == '':
            continue
        f.write('>' + mp[it].xp + '\n' + mp[it].seg)
