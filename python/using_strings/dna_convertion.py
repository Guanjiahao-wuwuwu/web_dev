sequences = "tatgctttcc#tataggtctg#ctattcaatg"
dna_list = sequences.split("#")
print(dna_list)

for dna in dna_list:
    rna = dna.replace("t", "u")
    print("DNA:"+dna+"->"+"RNA:"+rna)