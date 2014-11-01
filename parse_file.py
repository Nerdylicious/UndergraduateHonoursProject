from Bio import SeqIO

def parse(file_name, file_type, count):
    sequences = []
    counter = 0
    for record in SeqIO.parse(file_name, file_type):
        if counter < count:
            sequence = str(record.seq)
            sequences.append(sequence)
            counter = counter + 1
    return sequences
