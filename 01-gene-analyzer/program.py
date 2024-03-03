# This script parses the unzipped https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_info.gz file.
import sys
import csv

# Columns
# '#tax_id', 'GeneID', 'Symbol', 'LocusTag', 'Synonyms', 'dbXrefs',
#        'chromosome', 'map_location', 'description', 'type_of_gene',
#        'Symbol_from_nomenclature_authority',
#        'Full_name_from_nomenclature_authority', 'Nomenclature_status',
#        'Other_designations', 'Modification_date', 'Feature_type'
file_path = sys.argv[1]

# https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
import hashlib
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

print(md5(file_path))

# https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=9606&lvl=3&lin=f&keep=1&srchmode=1&unlock
# Homo Sapiens: Taxonomy ID: 9606
HOMO_SAPIENS_TAX_ID = '9606'

gene_id_set = set()
gene_types = dict()
homo_sapiens_counter = 0

# Open the CSV file in read mode
with open(file_path, 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file, delimiter='\t')
    next(csv_reader) # skip header
    
    # Iterate over each line in the CSV file
    for line in csv_reader:
        # Count the homo sapiens entries
        if line[0] == HOMO_SAPIENS_TAX_ID:
            homo_sapiens_counter += 1
        
        # Add geneId to set
        gene_id_set.add(line[1])

        # Add gene type to dict and count the occurence
        gene_type = line[9]
        if gene_type in gene_types.keys():
            gene_types[gene_type] += 1
        else:
            gene_types[gene_type] = 0
        
print('Answer question 1: ', len(gene_id_set))
print('Answer question 2: ', homo_sapiens_counter)

max_value = max(gene_types.values())
max_key = max(gene_types, key=gene_types.get)

print('Answer question 3: ', list(gene_types.keys()))
print('Answer question 4: ', max_key)

# Output
# 391abe3356f88ff7a34a085f37e29f66
# Answer question 1:  51231571
# Answer question 2:  193384
# Answer question 3:  ['other', 'protein-coding', 'rRNA', 'pseudo', 'tRNA', 'ncRNA', 'miscRNA', 'unknown', 'snRNA', 'snoRNA', 'scRNA', 'biological-region']
# Answer question 4:  protein-coding
