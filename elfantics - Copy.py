  # trial 29 Dec
line="CaBbA"
# elves="ABab"

list_of_elves=list(line)
n2=len(list_of_elves)
i=0

while i < len(list_of_elves):
    if list_of_elves[i-1].lower()==list_of_elves[i].lower():
         if (list_of_elves[i].islower() and list_of_elves[i-1].isupper()) or (list_of_elves[i].isupper() and list_of_elves[i-1].islower()):
            del list_of_elves[i]
            del list_of_elves[i-1]
            if i<2:
                i-=1
            else:
                i-=2
            if len(list_of_elves)<2:
                break  
    else:
        i+=1
        if len(list_of_elves)<2:
            break  
   
print(len(list_of_elves))