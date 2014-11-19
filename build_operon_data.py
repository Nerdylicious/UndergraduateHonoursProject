import random
from build_operon_dictionary import *
from parse_genbank import *

def get_cds_pair(data):

    has_pair = False

    while not has_pair:

        randnum = random.randint(1, 4403)

        locus_tag_1 = randnum
        locus_tag_2 = randnum + 1

        if locus_tag_1 in data and locus_tag_2 in data: 
            cds_1 = data[locus_tag_1]
            cds_2 = data[locus_tag_2]

            cds_pair = (cds_1, cds_2)
            has_pair = True

    return cds_pair 

operons = get_operon_dictionary()
print operons

file_name = "NC_000913.gbk"
file_type = "genbank"
data = parse(file_name, file_type)

positive_samples = {}
negative_samples = {}

while len(positive_samples) < 250:

    cds_pair = get_cds_pair(data)
    cds_1 = cds_pair[0]
    cds_2 = cds_pair[1]

    locus_tag_1 = cds_1.locus_tag
    locus_tag_2 = cds_2.locus_tag

    gene_1 = cds_1.gene
    gene_2 = cds_2.gene

    if locus_tag_1 in operons and locus_tag_2 in operons:
        if set(operons[locus_tag_1]) & set(operons[locus_tag_2]):
            #print "gene_1: [%s], gene_2: [%s]" % (gene_1, gene_2)
            concat = cds_1.translation + cds_2.translation
            positive_samples[concat] = 1

while len(negative_samples) < 250:

    cds_pair = get_cds_pair(data)
    cds_1 = cds_pair[0]
    cds_2 = cds_pair[1]

    locus_tag_1 = cds_1.locus_tag
    locus_tag_2 = cds_2.locus_tag

    gene_1 = cds_1.gene
    gene_2 = cds_2.gene

    if locus_tag_1 in operons and locus_tag_2 in operons:
        if not (set(operons[locus_tag_1]) & set(operons[locus_tag_2])):
            print "gene_1: [%s], gene_2: [%s]" % (gene_1, gene_2)
            concat = cds_1.translation + cds_2.translation
            negative_samples[concat] = 0
