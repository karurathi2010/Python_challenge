import os
import csv
ballet=[]
candidate=[]
vote_count={}
high_count=[]
C=0
D=0
R=0




paths=os.path.join("Resources","election_data.csv")
with open(paths) as data:
    lines=csv.reader(data,delimiter=",")
    header=next(lines)
    

    for row in lines:
       ballet.append(row[0])
       candidate.append(row[2])
   
    tot_vot=len(ballet)

    for i in range(0,len(candidate)):
        if candidate[i]=="Charles Casper Stockham":
            C=C+1
        elif candidate[i]=="Diana DeGette":
            D=D+1
        elif candidate[i]=="Raymon Anthony Doane":
            R=R+1

    C_perc=round((C/tot_vot)*100,3)
    vote_count["Charles Casper Stockham"]=C_perc
    D_perc=round((D/tot_vot)*100,3)
    vote_count["Diana DeGette"]=D_perc
    R_perc=round((R/tot_vot)*100,3)
    vote_count["Raymon Anthony Doane"]=R_perc

    high_count=vote_count.values()
    Lead=max(high_count)

print("Election Results")
print("-------------------------\n")

print(f"Total Votes: {tot_vot}\n")
print("-------------------------\n")

print(f"Charles Casper Stockham:{C_perc}% ("+str(C)+")\n")
print(f"Diana DeGette:{D_perc}% ("+str(D)+")\n")
print(f"Raymon Anthony Doane:{R_perc}% ("+str(R)+")\n")
print("-------------------------\n")

    
for name,vote in vote_count.items():
            if vote==Lead:
                 print(f"Winner: {name}")

print("-------------------------\n")

        
            
