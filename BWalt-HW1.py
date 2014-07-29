# Exercise 4
# Challenge 1
mytext = "Hellow this is myText"
result = mytext.find("i")
if result == -1:
    print "No"
else:
    print "Yes"


# Challenge 2
secound_largest = [2, 23, 75, 48, 17, 6 ,120, 55]
secound_largest.sort()
print secound_largest[-2]

# Challenge 3
mylist = [2, 23, 75, 48, 17, 6 ,120, 55, 55, 120]
mylist.sort()
for number in mylist:
    count = mylist.count(number)
    if count <> 1:
        mylist.remove(number)
        result = "The list provided contains duplicate values."
    else:
        result = "The list provided does not contain duplicate values."
print result
print mylist
