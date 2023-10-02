from Bio import SeqIO
DNA_strings = {}
for record in SeqIO.parse('rosalind_grph.txt', 'fasta'):
    DNA_strings[record.id] = record.seq
def grph(DNA_strings):
    for i in DNA_strings:
        for j in DNA_strings:
            if DNA_strings[i] != DNA_strings[j]:
                if DNA_strings[i][-3:] == DNA_strings[j][:3]:
                    adj_list= i+' '+j
                    print(adj_list)
grph(DNA_strings)