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



file_path=os.path.join('Resources','budget_data.csv')
with open(file_path) as data:
    lines=csv.reader(data,delimiter=',')
    header=next(lines)
   
    

    for row in lines:

        month=row[0].split("-")
        months.append(month[0])
        net_amt=net_amt+int(row[1])
        change.append(int(row[1]))
        dates.append(row[0])
       
        
    for i in range(0,(len(change)-1)):
        
        x=change[i+1]-change[i]
        tot_change.append(x)
        
    grt_value= max(tot_change) 
    min_value=min(tot_change)  
    N=tot_change.index(grt_value)  
    M=tot_change.index(min_value)   
        
        
    for i in range(0,len(tot_change)):
        add=add+tot_change[i]

    

    length=len(tot_change) 
    avg_chng=round(add/length,2)  
    Total_months=len(months) 


    print("Financial Analysis")

    print("---------------------------\n")
      
   
   
    print(f"Total Months: {Total_months}\n" )
    
    print(f"Total: ${net_amt}\n")
    
    print(f"Average Change:${avg_chng}\n")
    
    print(f"Greatest Increase in Profits:{dates[N+1]} "+ "($" + str(grt_value)+ ")\n" )
    
    print(f"Greatest Decrease in Profits:{dates[M+1]}"+ "($" + str(min_value)+ ")\n")
   
    
    
      

       

        
        
    