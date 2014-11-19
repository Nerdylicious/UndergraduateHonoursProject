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

def get_positive_samples(sample_size):

    operons = get_operon_dictionary()

    file_name = "NC_000913.gbk"
    file_type = "genbank"
    data = parse(file_name, file_type)

    positive_samples = []

    while len(positive_samples) < sample_size:

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
                concat_sequence = cds_1.translation + cds_2.translation
                positive_samples.append(concat_sequence)

    return positive_samples

def get_negative_samples(sample_size):

    operons = get_operon_dictionary()

    file_name = "NC_000913.gbk"
    file_type = "genbank"
    data = parse(file_name, file_type)

    negative_samples = []

    while len(negative_samples) < sample_size:

        cds_pair = get_cds_pair(data)
        cds_1 = cds_pair[0]
        cds_2 = cds_pair[1]

        locus_tag_1 = cds_1.locus_tag
        locus_tag_2 = cds_2.locus_tag

        gene_1 = cds_1.gene
        gene_2 = cds_2.gene

        if locus_tag_1 in operons and locus_tag_2 in operons:
            if not (set(operons[locus_tag_1]) & set(operons[locus_tag_2])):
                #print "gene_1: [%s], gene_2: [%s]" % (gene_1, gene_2)
                concat_sequence = cds_1.translation + cds_2.translation
                negative_samples.append(concat_sequence)

    return negative_samples
