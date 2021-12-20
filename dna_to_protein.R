# Translate DNA - Protein

genetic_code <- function(codon) {
  if (codon == "ATG") 
    {return("M")}
  else if (codon == "GGT" | codon == "GGC" | codon == "GGA" | codon == "GGG") 
    {return("G")}
  else if (codon == "TCT" | codon == "TCC" | codon == "TCA" | codon == "TCG" | codon == "AGT" | codon == "AGG" | codon == "AGC")
    {return("S")}
  else if (codon == "CCT" | codon == "CCC" | codon == "CCA" | codon == "CCG")
    {return("P")}
  else if (codon == "GCT" | codon == "GCC" | codon == "GCA" | codon == "GCG")
    {return("A")}
  else if (codon == "ACT" | codon == "ACC" | codon == "ACA" | codon == "ACG")
    return("T")
  else if (codon == "TAT" | codon == "TAC")
    {return("Y")}
  else if (codon == "TTT" | codon == "TTC")
    {return("F")}
  else if (codon == "TTA" | codon == "TTG" | codon == "CTT" | codon == "CTC" | codon == "CTA" | codon == "CTG")
    {return("L")}
  else if (codon == "ATT" | codon == "ATC" | codon == "ATA")
    {return("I")}
  else if (codon == "GTT" | codon == "GTC" | codon == "GTA" | codon == "GTG")
    {return("V")}
  else if (codon == "CAT" | codon == "CAC")
    {return("H")}
  else if (codon == "CAA" | codon == "CAG")
    {return("Q")}
  else if (codon == "AAT" | codon == "AAC")
    {return("N")}
  else if (codon == "AAA" | codon == "AAG")
    {return("K")}
  else if (codon == "GAT" | codon == "GAC")
    {return("D")}
  else if (codon == "GAA" | codon == "GAG")
    {return("E")}
  else if (codon == "TGT" | codon == "TGC")
    {return("C")}
  else if (codon == "TGG")
    {return("W")}
  else if (codon == "CGT" | codon == "CGC" | codon == "CGA" | codon == "CGG" | codon == "AGA" | codon == "AGG")
    {return("R")}
  else if (codon == "TAA" | codon == "TAG" | codon == "TGA")
    {return("-")}
  return()
}


dna_to_codons <- function(fasta) {
  fasta_split <- strsplit(fasta, "")[[1]]  # Lo convertimos en vect| de caracteres
  codon <- c()
  codon_list <- c()
  for (i in fasta_split) {
    codon <- c(codon, i)
    if (length(codon) == 3) {
      codon <- paste(codon[1], codon[2], codon[3], sep = "")
      codon_list <- c(codon_list, codon)
      codon <- c()
    }
  }
  return(codon_list)
}


main <- function() {
  fasta <- readline(prompt = "Introduce DNA sequence (no spaces allowed): \n")
  fasta <- gsub(" ", "", fasta)
  codon_list <- dna_to_codons(fasta)
  aa_seq <- c()
  for (i in codon_list) {
    aa_seq <- c(aa_seq, genetic_code(i))
  }
  aa_seq <- paste(aa_seq, collapse = "")
  return(aa_seq)
}


  
main()
