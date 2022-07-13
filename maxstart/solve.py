import argparse

parser = argparse.ArgumentParser()
parser.add_argument('inputfile')
parser.add_argument('outputfile')
args = parser.parse_args()
inputfile = args.inputfile
outputfile = args.outputfile

fin = open(inputfile)
fout = open(outputfile, 'w+')
cnt, groupsize = 0, 6
ans_seg = ''
ans_seq = ''
for line in fin:
    if line[0] == '>':
        curseq = line
        cnt += 1
    else:
        seg = line.split('*')
        for segt in seg:
            if len(segt) > len(ans_seg):
                ans_seq = curseq
                ans_seg = segt
        if cnt % groupsize == 0:
            fout.write(ans_seq + ans_seg + '\n')
            ans_seg = ''

    