import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('fadict')
parser.add_argument('cdsdict')
parser.add_argument('outputdict')
args = parser.parse_args()
srcdic = args.fadict
targetdic = args.cdsdict
outputdic =  args.outputdict
mp = {}
for root,dirs,files in os.listdir(srcdic):
    for file in files:
        for line in open(os.path.join(root,file)):
            if line[0] == '>':
                mp[line] = '>' + file.split('.')[0] + '\n'
for root,dirs,files in os.walk(targetdic):
    for file in files:
        f = os.path.join(outputdic,file)
        f = open(f,'w')
        for line in open(os.path.join(root,file)):
            if line[0] == '>':
                f.write(mp[line])
            else:
                f.write(line)
