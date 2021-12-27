# Read .fastq and save .csv with DNA from fastq file

from tkinter.filedialog import askopenfilename
from tkinter import filedialog

# Opens fastq file as a list of fastqs. Converts this list into a list of DNA seqs.
def load_fastq(path):
    file = open(path, "r")
    my_fastq_read = file.read()
    my_fastq_split = my_fastq_read.splitlines()  # List of sublists (fastqs).
    one_seq1 = []
    one_seq2 = []
    for i in my_fastq_split:
        one_seq1.append(i)
        if len(one_seq1) == 4:
            one_seq2.append(one_seq1)
            one_seq1 = []
    seqs = [item[1] for item in one_seq2]
    return seqs


def write_seqs(seqs):
    seqs_csv = ",".join(seqs)
    save_directory = filedialog.askdirectory()
    with open(save_directory + "/dna_seqs.csv", "w") as file:
        file.write(seqs_csv)
        file.truncate()
    return


def main():
    file = askopenfilename()
    seqs = load_fastq(file)
    write_seqs(seqs)
    return


main()
