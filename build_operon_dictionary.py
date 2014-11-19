import csv

#Purpose: Returns a dictionary where the keys are locus tags for genes. 
#Genes that are within the same operon have the same ID
def get_operon_dictionary():
    operons = {}
    with open('known_operons.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        counter = 0
        for row in reader:
            for gene in row:
                #operons[gene.lower()] = counter
                if gene in operons:
                    ids = operons[gene]
                    ids.append(counter)
                else:
                    ids = []
                    ids.append(counter)
                    operons[gene] = ids
            counter = counter + 1
    return operons
