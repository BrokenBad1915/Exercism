def to_rna(dna_strand):
    interferance_codes={"G":"C", "C":"G", "T":"A", "A":"U"}
    return "".join(interferance_codes[code] for code in dna_strand)