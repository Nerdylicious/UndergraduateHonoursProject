import random
from parse_genbank import *

file_name = "NC_000913.gbk"
file_type = "genbank"
data = parse(file_name, file_type)

randnum = random.randint(1, 4403)

locus_tag_1 = randnum
locus_tag_2 = randnum + 1

if locus_tag_1 in data and locus_tag_2 in data: 
    cds_1 = data[locus_tag_1]
    cds_2 = data[locus_tag_2]
    print "locus_tag_1: %d, locus_tag_2: %d" % (locus_tag_1, locus_tag_2)
    print "gene_1: %s, gene_2: %s" % (cds_1.gene, cds_2.gene)
    print "concatenated: %s" % cds_1.translation + cds_2.translation
