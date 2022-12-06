f = open("Day1.txt", "r")

#creating a copy of the list given to us
item_list = []

#stripping unwanted characters in each item
for item in f:
    item = item.strip()
    item_list.append(item)

#initializing variables we'll need
calories = 0
index = 1
elf_list = {}

#looping through the list
for item in item_list:
    #if the item is not a number
    if item == '':
        elf_list['elf_no_%s' % index] = calories
        calories = 0
        index += 1
    else:
        #else, we'd convert the string to in to perform
        #addition. Adding each item an elf has
        calories += int(item)
#returns all the values in the dictionary
x = elf_list.values()
#we then cast the returned value to a list to 
#make it usable
x = list(x)
#we then sort it.
x = sorted(x)
#print out the last item on the list meaning
#it's the largest
print(x[-1])

####### PART TWO OF THE CHALLENGE ########
#Find the sum of the top three most calories
print(sum(x[-3:]))

    
    





