person1 = input("Enter the Person1 name: ")
person2 = input("Enter the Person2 name: ")

person1_vote=0
person2_vote=0

voters_id = [100,200,300]
num_of_voters = len(voters_id)

while True:
    if voters_id ==[]:
        print("Voting Session Over")
        if person1_vote > person2_vote:
            percent = (person1_vote/num_of_voters)*100
            print(person1,"has won with",round(percent,2),"% votes")
            
        elif person1_vote < person2_vote:
            percent = (person2_vote/num_of_voters)*100
            print(person2,"has won with",round(percent,2),"% votes")
            
        else:
            print("Match tied!")
        
        break
            
    else:
        voterID = int(input("Enter your voterID number: "))
        if voterID in voters_id:
            print("Voter verified✔️")
            vote = int(input("Enter your vote 1 or 2: "))
            if vote==1:
                person1_vote+=1
                print("Your vote has been recorded successfully")
            elif vote==2:
                person2_vote+=1
                print("Your vote has been recorded successfully")
                
            voters_id.remove(voterID)
                
        else:
            print("You have already voted or You are not eligible to vote")
                
            
            
