import os
import csv
months=[]
net_amt=0
change=[]
tot_change=[]
add=0
grt_value=0
min_value=0
dates=[]


#assigning the  file path of the source data to the variable file_path

file_path=os.path.join('Resources','budget_data.csv')

#open file in 'read' mode .
with open(file_path) as data:
    lines=csv.reader(data,delimiter=',')
   
    # Storing the header row in the variable header
    header=next(lines)
   
    

    for row in lines:

        month=row[0].split("-")  #Slit the date column for seperating months form dates.
        months.append(month[0])     # add all months to the months list.
        net_amt=net_amt+int(row[1])  # add each row of the Profit/loss column to get the total amount
        change.append(int(row[1]))   # add the Profit/loss column values to the change list
        dates.append(row[0])         # add the Date column values to the dates list
       
       
        
    for i in range(0,(len(change)-1)):       #To find the changes in Profit/Losses over the entire period subtracting the adjecent row values in the Profit/Losses column.
        
        x=change[i+1]-change[i]
        tot_change.append(x)          # store the result in the tot_change list
        
    grt_value= max(tot_change)        #Finding the maximum value of the tot_change list to get the greatest increase in profits over the entire period.
    min_value=min(tot_change)         #Findin the minimum value of the tot_change list to get the greatest decrease in profits over the entire period.
    N=tot_change.index(grt_value)     # Find the index value of the greatest increase & greatest decrease values for getting corresponding dates.
    M=tot_change.index(min_value)   
        
        
    for i in range(0,len(tot_change)):   # find the sum of the profit change for calculating the average change.
        add=add+tot_change[i]

    

    length=len(tot_change)              #Finding the no:of items in the tot_change list 
    avg_chng=round(add/length,2)        #Calculating the Average Change using the (total sum/total number) formula and rounding the result to 3 decimal points.
    Total_months=len(months)            #Finding the Total Months by finding the no of items in the months list.


    print("Financial Analysis")       #Printing all the results as instructed.

    print("---------------------------\n")
      
   
   
    print(f"Total Months: {Total_months}\n" )
    
    print(f"Total: ${net_amt}\n")
    
    print(f"Average Change:${avg_chng}\n")
    
    print(f"Greatest Increase in Profits:{dates[N+1]} "+ "($" + str(grt_value)+ ")\n" )
    
    print(f"Greatest Decrease in Profits:{dates[M+1]}"+ "($" + str(min_value)+ ")\n")
    
   
    
    
      

       

        
        
    