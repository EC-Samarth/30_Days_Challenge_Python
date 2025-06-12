#Day_12 <File Handling>

#1.write to the text file

def write_to_text_file(file_path,content):
    try:
        with open(file_path ,'w')as file:
            file.write(content)
        print(f"Content written to {file_path} successfully")
    except Exception as e :
        print(f"An error occured :{e}")
#Example usage:
file_path ='example.txt'
content ="Hello, World \n This is an example text file"
write_to_text_file(file_path,content)

""" Output
Content written to example.txt successfully """


#2.read from the text 
def read_text_file(file_path):
    try:
        with open(file_path,'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found :{file_path}")
        return None 
    except Exception as e :
        print(f"An error occured :{e}")
        return None
    
#Example usage
file_path = 'example.txt'
content = read_text_file(file_path)

if content:
    print(content) 

""" Output 
Hello, World 
 This is an example text file """

#3. Write to a text file
with open("abc.txt","w") as file:
    file.write("Hello! I am a Python Developer.")
    file.write("\nI am at the learning phase. ")


#4.Read to a text file
with open("abc.txt") as file:
    c = file.read()
    print(c)


#5.Append to a text file
with open("abc.txt","a") as file:
    file.write("\nMy name is Samarth Mishra.")

#6.count the character,words from the file
def char_word_count(file_name):
    with open(file_name,"r") as file:
      text = file.read()
      char_count = len(text)
      word_count = len(text.split())
    return char_count,word_count

file_name = "abc.txt"
result = char_word_count(file_name)
if result:
   char_count,word_count = result
   print(f"Character count : {char_count}")
   print(f"Word count : {word_count}")

""" Output 
Character count : 87
Word count : 17 """