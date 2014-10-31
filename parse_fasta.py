from Bio import SeqIO

for record in SeqIO.parse('dataset_negative.fasta', 'fasta'):
    print record.id
    print record.seq
    print len(record.seq)
