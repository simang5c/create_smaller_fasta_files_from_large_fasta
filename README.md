# create_smaller_fasta_files_from_large_fasta

#python code to split huge fasta without loading into memory to smaller files 

#Works on linux platform with python3

#====================================================================

preprocessing of fasta files required before running the program

1. Remove any new line from multilines fasta and any blank lines.
2. Decide how many fasta sequence you want in the file: divide total number of fasta sequences/how_many_sequences_required _in each file


To run the code 
_**python split_fasta.py number_of_files filename.fasta**_
#Example: my file contains 213849 fasta sequences and i want 101 sequences in all files
#number_of_files=213849/101=2117

#_**python split_fasta.py 2117 filename.fasta**_
