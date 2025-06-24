#Day_24 <Regular expression>
"""A regular expression is special sequence of charaters that defines a search pathern .
It is mainly used in string matching,vlidation,searching and Replacing text in strings.

Exxample Cases
-Check the email is valid 
-Dearch the phone number in text 
-Validate the password format 
-Replace or extract data from strings """

#1.Match a Valid Phone Number (10 digits)

import re
text ="Call me at 9876543210"   #\d means "a digit" (0–9).
pattern = r"\d{10}"             #{10} means "exactly 10 times
print(re.search(pattern ,text).group())   #\d{10} matches any 10-digit number.
#Output:9876543210              #re.search() returns the first match of the pattern in the string.


#2.Validate an Email
pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
emails = ['test@domain.com', 'invalid@com', 'hello@world.co.in']
for e in emails:
    print(e, '✅' if re.match(pattern, e) else '❌')

"""Output
test@domain.com ✅
invalid@com ❌
hello@world.co.in ✅"""


#3.Find all the word in the sentence 
text = "Python is fun and powerful!"
pattern = r'\w+'
print(re.findall(pattern, text))
#Output:['Python', 'is', 'fun', 'and', 'powerful']


#4.Extract all numbers from the text 
text = "My scores are 67, 89 and 100."
pattern = r'\d+'
print(re.findall(pattern, text))
#Output:['67', '89', '100']