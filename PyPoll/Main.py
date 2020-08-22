#modules
import os
import csv

#setting path for file
election_data_path = os.path.join('Resources','election_data.csv' )
tot_num_vots=0
#open the csv
with open(election_data_path) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    for r in csvreader:
        print(r)
        print(r[0])
   
#-------1------ (code  for total number of votes cast )
# sum of number of rows
        tot_num_vots=tot_num_vots+1 #(code  for total number of months ) 
print("Total number of votes is: " + str(tot_num_vots))






