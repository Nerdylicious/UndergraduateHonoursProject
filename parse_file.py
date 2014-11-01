from Bio import SeqIO

def parse(file_name, file_type, count):
    sequences = []
    sequences_seen = {}
    counter = 0
    for record in SeqIO.parse(file_name, file_type):
        if counter < count:
            sequence = str(record.seq)
            #prevent any duplicates from being included in our data
            if not sequence in sequences_seen:
                sequences_seen[sequence] = True
                sequences.append(sequence)
                counter = counter + 1
    return sequences
