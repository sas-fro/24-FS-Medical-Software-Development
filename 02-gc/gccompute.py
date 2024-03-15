# uses biopython package
import sys
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

fasta_file_path = sys.argv[1]

for record in SeqIO.parse(fasta_file_path, "fasta"):
    print(record.id)
    print(gc_fraction(record.seq))
