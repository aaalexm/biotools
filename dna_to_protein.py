# Translate DNA - Protein


def genetic_code(codon):
    if codon == "ATG":
        return "M"
    elif codon == "GGT" or codon == "GGC" or codon == "GGA" or codon == "GGG":
        return "G"
    elif codon == "TCT" or codon == "TCC" or codon == "TCA" or codon == "TCG" or codon == "AGT" or codon == "AGG" or codon == "AGC":
        return "S"
    elif codon == "CCT" or codon == "CCC" or codon == "CCA" or codon == "CCG":
        return "P"
    elif codon == "GCT" or codon == "GCC" or codon == "GCA" or codon == "GCG":
        return "A"
    elif codon == "ACT" or codon == "ACC" or codon == "ACA" or codon == "ACG":
        return "T"
    elif codon == "TAT" or codon == "TAC":
        return "Y"
    elif codon == "TTT" or codon == "TTC":
        return "F"
    elif codon == "TTA" or codon == "TTG" or codon == "CTT" or codon == "CTC" or codon == "CTA" or codon == "CTG":
        return "L"
    elif codon == "ATT" or codon == "ATC" or codon == "ATA":
        return "I"
    elif codon == "GTT" or codon == "GTC" or codon == "GTA" or codon == "GTG":
        return "V"
    elif codon == "CAT" or codon == "CAC":
        return "H"
    elif codon == "CAA" or codon == "CAG":
        return "Q"
    elif codon == "AAT" or codon == "AAC":
        return "N"
    elif codon == "AAA" or codon == "AAG":
        return "K"
    elif codon == "GAT" or codon == "GAC":
        return "D"
    elif codon == "GAA" or codon == "GAG":
        return "E"
    elif codon == "TGT" or codon == "TGC":
        return "C"
    elif codon == "TGG":
        return "W"
    elif codon == "CGT" or codon == "CGC" or codon == "CGA" or codon == "CGG" or codon == "AGA" or codon == "AGG":
        return "R"
    elif codon == "TAA" or codon == "TAG" or codon == "TGA":
        return "-"
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
    fasta = input("Introduce raw DNA sequence: \n")
    fasta = fasta.replace(" ", "")
    codon_list = dna_to_codons(fasta)
    aa_seq = []
    for i in codon_list:
        aa_seq.append(genetic_code(i))
    aa_seq = "".join(aa_seq)    
    print("\n" + aa_seq)
    return


main()
