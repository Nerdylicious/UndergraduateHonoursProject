from Bio import SeqIO

class CDS:

    def __init__(self, gene, locus_tag, translation):
        self.gene = gene
        self.locus_tag = locus_tag
        self.translation = translation

def parse(file_name, file_type):
    data = {}
    for record in SeqIO.parse(file_name, file_type):
        for feature in record.features:
            if feature.type == "CDS" and "gene" in feature.qualifiers and "locus_tag" in feature.qualifiers and "translation" in feature.qualifiers:
                gene = feature.qualifiers["gene"][0]
                locus_tag_str = feature.qualifiers["locus_tag"][0]
                locus_tag_num = int(locus_tag_str[1:])
                translation = feature.qualifiers["translation"][0]
                cds = CDS(gene, locus_tag_str, translation)
                data[locus_tag_num] = cds 
    return data
