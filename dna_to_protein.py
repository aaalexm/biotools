# Translate DNA - Protein


genetic_code = {"ATG": "M",
                "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
                "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
                "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                "TAT": "Y", "TAC": "Y",
                "TTT": "F", "TTC": "F",
                "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
                "ATT": "I", "ATC": "I", "ATA": "I",
                "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
                "CAT": "H", "CAC": "H",
                "CAA": "Q", "CAG": "Q",
                "AAT": "N", "AAC": "N",
                "AAA": "K", "AAG": "K",
                "GAT": "D", "GAC": "D",
                "GAA": "E", "GAG": "E",
                "TGT": "C", "TGC": "C",
                "TGG": "W",
                "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
                "TAA": "-", "TAG": "-", "TGA": "-"}


def translation(codon):
    if codon in genetic_code:
        return genetic_code[codon]
    else:
        print("something is not working")
    return


def dna_to_codons(fasta):
    codon = []
    codon_list = []
    for i in fasta:
        codon.append(i)
        if len(codon) == 3:
            codon = "".join(codon)
            codon_list.append(codon)
            codon = []
    return codon_list


def main():
    fasta = input("Introduce DNA sequence: \n")
    fasta = fasta.replace(" ", "")
    codon_list = dna_to_codons(fasta)
    aa_seq = []
    for i in codon_list:
        aa_seq.append(translation(i))
    aa_seq = "".join(aa_seq)
    print("\n" + aa_seq)
    return


main()
