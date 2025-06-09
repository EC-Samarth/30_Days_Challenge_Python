#Day_09 < Dictionaries >

#Create a dictionary 
d = {"a":1, "b": 2,"c":3}

#Access the value with the help of key
print(d.items())

#Accessing key value pairs in for loop
for key,value in d.items():
    print(key,value)

""" Output
a 1
b 2
c 3 """

#1.Create a Contenet book
contact = {
    "john":{
        "Name":"John",
        "Mobile no.":56789,
        "Email":"abc@gmail.com"
    },
    "sam":{
        "Name":"Sam",
        "Mobile no.":12345,
        "Email" : "abc@gmail.com"
    },
    "sak":{
        "Name":"Sak",
        "Mobile no.":34567,
        "Email":"xyz@gmail.com"
    }

}
for key,vlaue in contact.items():
    print(key,value)

"""Output
john 3
sam 3
sak 3 """


#2.Add a new persion in dictionary contact
contact.update(alexa = {"name":"Alexa","Mobile no.":8563247,"Email":"Alexa85@gmail.com"})
for key,value in contact.items():
     print(key,value)

""" Output 
john {'Name': 'John', 'Mobile no.': 56789, 'Email': 'abc@gmail.com'}
sam {'Name': 'Sam', 'Mobile no.': 12345, 'Email': 'abc@gmail.com'}
sak {'Name': 'Sak', 'Mobile no.': 34567, 'Email': 'xyz@gmail.com'}
alexa {'name': 'Alexa', 'Mobile no.': 8563247, 'Email': 'Alexa85@gmail.com'}"""


#3.Merge 2 dictionary
d1 = {"d":4,"e":9,"f":6}
d.update(d1)
print(d)
# OR
merge_dic = {**d,**d1}
print(merge_dic)

""" Output 
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 9, 'f': 6}
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 9, 'f': 6} """


#4.Find the key with maximum value in a dictionary
max_value = max(d,key=d.get)
print(max_value) #e


#5.Group the element by their length
a = ["cat","bat","apple","banana","grapes","dog" ]
d3 = {}
for i in a:
    length = len(i)          # Get the length of each word
    if length in d3:
        d3[length].append(i) # Add word to existing list for this length
    else:
        d3[length] = [i]     # Create new list if this length not seen before
print(d3)

""" Output 
{3: ['cat', 'bat', 'dog'], 5: ['apple'], 6: ['banana', 'grapes']} """


#6.Count fequency of words in a string
s = "banana"
freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq) 
""" Output
{'b': 1, 'a': 3, 'n': 2}"""


#7.sort dictionary by values
d = {'apple': 3, 'banana': 1, 'grapes': 5, 'orange': 2}

# Sort inascending order
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_dict)

""" Output 
'banana': 1, 'orange': 2, 'apple': 3, 'grapes': 5} """