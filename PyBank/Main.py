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

    print("Total number of months is: " + str(Tot_mon))
    print("Total: $  "+ str(Tot_Amount)) 
    print("Average Change: " + str((sumchange)/(Tot_mon-1)))#---(caliculate the average)
    print("Greatest  Increase in profits:  "+ date_inc +"  ($"+ str(gratest_increase)+")") 
    print("Greatest Decrease in losses:  " + date_dec + "  ($"+ str(greatest_dec)+")") 

    
f = open("Pybank_results.txt", "w")
f.write("Total number of months is: " + str(Tot_mon)+"\n")
f.write("Total: $  "+ str(Tot_Amount)+"\n") 
f.write("Average Change: " + str((sumchange)/(Tot_mon-1))+"\n")#---(caliculate the average)
f.write("Greatest  Increase in profits:  "+ date_inc +"  ($"+ str(gratest_increase)+")"+"\n") 
f.write("Greatest Decrease in losses:  " + date_dec + "  ($"+ str(greatest_dec)+")"+"\n") 
f.close()


