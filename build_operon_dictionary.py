import csv

#Purpose: Returns a dictionary where the keys are all gene names. 
#Genes that are within the same operon have the same ID for its dictionary value
def build_operon_dictionary():
    operons = {}
    with open('operons.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        counter = 0
        for row in reader:
            for gene in row:
                operons[gene] = counter
            counter = counter + 1
    return operons

if __name__=='__main__':
    operons = build_operon_dictionary()
    print operons 
