# create_smaller_fasta_files_from_large_fasta
#python code to split huge fasta without loading into memory to smaller files 
#Works on linux platform with python3
#====================================================================
#preprocessing of fasta files required before running the program
#1. Removing new line from multilines fasta, * from protein sequences end and removing any blank lines from fasta
#2. Decide how many fasta sequence you want in the file: divide total number of fasta sequences/how_many_sequences_required _in each file

#To run the code 
#python split_fasta.py number_of_files filename.fasta

#Example: my file contains 213849 fasta sequences and i want 101 sequences in all files
#number_of_files=213849/101=2117

#python split_fasta.py 2117 filename.fasta
