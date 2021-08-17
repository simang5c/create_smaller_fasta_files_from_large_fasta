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

#Program:
#==========================================================================
import subprocess
import sys
file_name=sys.argv[2]
number_of_files=int(sys.argv[1])
   
p = subprocess.Popen(["grep", "-c",">", file_name], stdout=subprocess.PIPE)
(output, err) = p.communicate()
number_of_sequences=int(output.strip())
each_file_has=number_of_sequences//number_of_files  #it will only give the number of headers divide by number_of files you want to split

counter=each_file_has*2  #header+sequence always each_file x 2
iterator=1 #starting to iterate from 1
sequences=[]
output_file_generator=1
with open(file_name,"r") as f:
            for seq in f:
#This block is only to append sequences to the list
                if iterator<=counter:
                    #print(iterator)
                    sequences.append(seq)
                    #print(sequences)
#when iterator reaches the and few sequence still remains
#This block creates additional file to manage last few sequences
                    if(iterator==((number_of_sequences*2))):
                        print(f"iterator reached final at {iterator} and last file is at {output_file_generator}")
                        with open ("%s.fasta"%output_file_generator,"w")as fw:
                            for lines0 in sequences:
                                fw.write(lines0)   #writes the file to an output 
                        break
                    iterator=iterator+1
                    
                    
                else:
                    with open ("%s.fasta"%output_file_generator,"w")as fw: #once the counter reaches how many sequences to store in a file
                        #enters this block to print it on a file
                        #this block has the job to print the chunks to a file
                        for lines0 in sequences:
                            fw.write(lines0)
                        sequences=[]
                        output_file_generator +=1
                        sequences.append(seq)
                        
                        iterator=iterator+1
                        counter=counter+(each_file_has*2)

