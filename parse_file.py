from Bio import SeqIO

def parse(file_name, file_type, count):
    sequences = []
    count = 0
    for record in SeqIO.parse(file_name, file_type):
        if count < 100:
            sequence = str(record.seq)
            sequences.append(sequence)
            count = count + 1
    return sequences
