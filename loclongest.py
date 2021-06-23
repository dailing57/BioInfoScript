import sys, getopt
import re


def usage():
    print('usage:python3 removeRedundantProteins.py -i  -o  <-h>')
    return


def removeRedundant(in_file, out_file):
    gene_dic = {}
    flag = ''
    with open(in_file, 'r') as in_fasta:
        for line in in_fasta:
            if '>' in line:
                LOC = re.match('.*LOC(.*?)[\]\s]', line)
                XP = re.match('.*([XYN]P_.*?)[\]_]', line).group(1)
                res = ''
                if LOC:
                    res = LOC.group(1)
                else:
                    LOC = re.match('.*GeneID:(.*?)[\]\s]', line)
                    res = LOC.group(1)
                flag = res
                if res not in gene_dic:
                    gene_dic[res] = ['>' + XP + ' ' + 'LOC' + res + '\n']
                else:
                    gene_dic[res].append('>' + XP + ' ' + 'LOC' + res + '\n')
            else:
                gene_dic[flag][-1] += line
    with open(out_file, 'w') as out_fasta:
        for k, v in gene_dic.items():
            trans_max = ''
            for trans in gene_dic[k]:
                if len(list(trans)) > len(list(trans_max)):
                    trans_max = trans
            out_fasta.write(trans_max)


def main(argv):

    try:
        opts, args = getopt.getopt(argv, 'hi:o:')
    except getopt.GetoptError:
        usage()
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == '-i':
            in_fasta_name = arg
        elif opt == '-o':
            outfile_name = arg
    try:
        removeRedundant(in_fasta_name, outfile_name)
    except UnboundLocalError:
        usage()

    return


if __name__ == '__main__':
    main(sys.argv[1:])