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
gratest_increase=0
greatest_dec=0
date_inc=""
date_dec=""
#open the csv

with open(budget_data_path) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    for r in csvreader:
       # print(r)
       # print(r[1])
        
        if r[0] != "Date":
            Tot_mon=Tot_mon+1 #---(code  for total number of months ) 
            Tot_Amount =Tot_Amount + float(r[1]) #---(Code for total amount )
            
            current_month_p_l= float(r[1])
            if Tot_mon > 1:
                change_in_twomonths = (current_month_p_l - previous_month_p_l)
                sumchange = sumchange + change_in_twomonths
                if change_in_twomonths>0:
                    if change_in_twomonths > gratest_increase: #---(greatest increase in profits)
                        gratest_increase= change_in_twomonths
                        date_inc= r[0]
                else: 
                    if change_in_twomonths < greatest_dec: #--(The greatest decrease in losses) 
                        greatest_dec = change_in_twomonths
                        date_dec= r[0]
                
            previous_month_p_l= current_month_p_l 

write_file_path = os.path.join("Analysis", "Pybank_results.txt")
with open(write_file_path , "w", newline="") as write_csvfile:
    write_file = csv.writer(write_csvfile, delimiter=",")
    write_file.writerow(["Financial Analysis"])
    write_file.writerow(["----------------------------"])
    write_file.writerow([f"Total Months: {Tot_mon}"])
    write_file.writerow([f"Total: {Tot_Amount}"])
    write_file.writerow([f"Average  Change: {round(sumchange/(Tot_mon-1),2)}"])
    write_file.writerow([f"Greatest Increase in Profits: {date_inc} (${gratest_increase})"])
    write_file.writerow([f"Greatest Decrease in Profits: {date_dec} (${greatest_dec})"])

with open(write_file_path,"r") as csvfile:
    csvreader=csv.reader(csvfile)
    for r in csvreader:
       print(r[0])