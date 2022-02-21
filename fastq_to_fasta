#!/usr/bin/python3


import sys

infile = sys.argv[1]
fasta = sys.argv[2]

fastq = open(infile, 'r')


def main(fastq, fasta):
    line_n = 0
    line_id = 1
    outfile = open(fasta, 'w')
    fastas = 0
    for line in fastq:
        line_n += 1
        if line_id == 4:
            line_id = 1
        elif line_id == 3:
            line_id += 1
        elif line_id == 2:
            line_id += 1
            fasta_line = line
            outfile.write(fasta_line)
            fastas += 1
        else:
            fasta_header = line.replace('@', '>')
            line_id += 1
            outfile.write(fasta_header)
    outfile.close()
    print('FASTA records written', fastas)


if __name__ == '__main__':
    main(fastq, fasta)
