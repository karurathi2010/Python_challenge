import os
import csv
ballet=[]
candidate=[]
vote_count={}
high_count=[]
C=0
D=0
R=0


#Assigning the path of the source data to the paths variable.

paths=os.path.join("Resources","election_data.csv")

#opening the file in read mode.
with open(paths) as data:
    lines=csv.reader(data,delimiter=",")
    header=next(lines)         #storing header in the header variable.
    

    for row in lines:
       ballet.append(row[0])      # Store the Ballot_Id column in the ballet list.
       candidate.append(row[2])   # Store the Candidate column in the candidate list.
   
    tot_vot=len(ballet)           #Finding the Total Votes by getting no of items in the ballet list.

    for i in range(0,len(candidate)):                    #Finding the count of vote for each candidate using If conditional statement.
        if candidate[i]=="Charles Casper Stockham":
            C=C+1
        elif candidate[i]=="Diana DeGette":
            D=D+1
        elif candidate[i]=="Raymon Anthony Doane":
            R=R+1

    C_perc=round((C/tot_vot)*100,3)                 #Calculating the percentage of vote for  each candidate and adding the results to the vote_count dictionary.
    vote_count["Charles Casper Stockham"]=C_perc
    D_perc=round((D/tot_vot)*100,3)
    vote_count["Diana DeGette"]=D_perc
    R_perc=round((R/tot_vot)*100,3)
    vote_count["Raymon Anthony Doane"]=R_perc

    high_count=vote_count.values()              #Finding the highest value in the dictionary and using that value we can find the winner.
    Lead=max(high_count)

print("Election Results")                         #Printing the calculated values.
print("-------------------------\n")

print(f"Total Votes: {tot_vot}\n")
print("-------------------------\n")

print(f"Charles Casper Stockham:{C_perc}% ("+str(C)+")\n")
print(f"Diana DeGette:{D_perc}% ("+str(D)+")\n")
print(f"Raymon Anthony Doane:{R_perc}% ("+str(R)+")\n")
print("-------------------------\n")

    
for name,vote in vote_count.items():             #Printing the corresponding Key of the high value in the dictionary.So that we can find the winner.
            if vote==Lead:
                 print(f"Winner: {name}")

print("-------------------------\n")

        
            
