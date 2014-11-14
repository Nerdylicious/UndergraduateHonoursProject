from Bio import SeqIO

def parse(file_name, file_type):
    for record in SeqIO.parse(file_name, file_type):
        for feature in record.features:
            if feature.type == "CDS" and "locus_tag" in feature.qualifiers and "gene_synonym" in feature.qualifiers and "translation" in feature.qualifiers:
                locus_tag = feature.qualifiers["locus_tag"][0]
                gene_synonym = feature.qualifiers["gene_synonym"][0]
                translation = feature.qualifiers["translation"][0]
                print locus_tag
                print gene_synonym
                print translation
