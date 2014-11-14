from Bio import SeqIO

class CDS:

    def __init__(self, gene, translation):
        self.gene = gene
        self.translation = translation

def parse(file_name, file_type):
    data = {}
    for record in SeqIO.parse(file_name, file_type):
        for feature in record.features:
            if feature.type == "CDS" and "gene" in feature.qualifiers and "locus_tag" in feature.qualifiers and "translation" in feature.qualifiers:
                gene = feature.qualifiers["gene"][0]
                locus_tag = feature.qualifiers["locus_tag"][0]
                locus_tag = int(locus_tag[1:])
                translation = feature.qualifiers["translation"][0]
                cds = CDS(gene, translation)
                data[locus_tag] = cds 
    return data
