#modules
import os
import csv

#setting path for file

budget_data_path = os.path.join( "resources","budget_data.csv" )
Tot_mon=0
Tot_Amount=0
current_month_p_l=0
previous_month_p_l=0
change_in_twomonths=0
sumchange=0
#open the csv

with open(budget_data_path) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    for r in csvreader:
       # print(r)
       # print(r[1])
        
        if r[0] != "Date":
            current_month_p_l= float(r[1])
            if Tot_mon > 1:
                change_in_twomonths = (previous_month_p_l -current_month_p_l)
                sumchange =+ change_in_twomonths
            previous_month_p_l= current_month_p_l

            Tot_mon=Tot_mon+1 #(code  for total number of months ) 
            Tot_Amount =Tot_Amount + float(r[1]) #(Code for total amount )
    print("Total number of months is: " + str(Tot_mon))
    print("Total: $  "+ str(Tot_Amount)) 
    print("Average Change: " + str((sumchange-867884)/(Tot_mon-1)))   
    
 
#--------3------ caliculate the average