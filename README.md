# Python_challenge
Two challenges where provided.
## PyBank Challenge
* A budget data is provided for this challenge with two columns Date and Profit/Losses.
* Using this data a financial analysis is performed,which includes:

    1.finding total number of months included in the dataset.
      Appended the date column to a seperate list and find the length of the list.

   2.finding net total amount of "Profit/Losses" over the entire period.
      find the sum of all the row elements in the Profit/Losses column using for loop.
  
    3.finding changes in "Profit/Losses" over the entire period, and then the average of those changes.
       subtracted the adjecent row value of the Profit/Losses column and appended the values in a seperate list 'tot_change', then find the average of those values.

   4.The greatest increase in profits and corresponding date.
        find the max value of 'tot_change',then find the index value of the maximum value and using that indax find the corresponding date.

    5.The greatest decrease in profits and corresponding date.
       find the minimum value of 'tot_change',then find the index value of the minimum value and using that indax find the corresponding date.

## PyPoll Challenge

* An ellection data is provided for this challenge with 3 columns Ballot_ID,County,Candidate.

* Using this data performed some basic calculations and find the winner of the election.

* The operations performed on this data are:

     1. Finding the total number of votes cast.
         appended the Ballot_ID column to a seperate list and find the length of the list to find the total votes.
     
     2.Find the complete list of candidates who received votes and their total votes.
        Performed a IF conditional loop for getting the numer of votes for each candidate.

  3.Find the percentage of votes each candidate won.
        Divided single candidate vote with total votes and then multiplied the result with 100.

     4. Find the winner of the election based on popular vote.
         A dictionary is created with candidate's name as key and their votes as keys.found the the maximum value of the dictionary then printed the corresponding 
         key as the winner. 






