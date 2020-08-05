#1) The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
#   find the total number of characters in the file and save to the variable num.

with open("travel_plans.txt", "r") as travel:
    num = len(travel.read())

#2) We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
#   Find the total number of words in the file and assign this value to the variable num_words.

with open("emotion_words.txt", "r") as emo:
    num_words = len(emo.read().split())

#3) Assign to the variable num_lines the number of lines in the file school_prompt.txt.

with open("school_prompt.txt", "r") as school:
    num_lines = len(school.readlines())

#4) Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

with open("school_prompt.txt", "r") as school:
    beginning_chars = school.read()[:30]

#5) Using the file school_prompt.txt, assign the third word of every line to a list called three.
# Super Short Solution
with open("school_prompt.txt", "r") as school:
    three = [i.strip().split()[2] for i in school.readlines()]
    
# More Understandable
with open("school_prompt.txt", "r") as school:
    lines = school.readlines()
    three = [line.strip().split()[2] for line in lines]
    
### Explanation:
    Create List "lines" where each element of "lines" is a string, where we want the third word of each
    We iterate through our list lines (iterable) with  the iterator line
    We create a seperate list of strings for each line by stripping white space and splitting each line, but then only take the third element of this list
    These third elements (index 2) are then stored in the list three 
###

#6) Create a list called emotions that contains the first word of every line in emotion_words.txt.
with open("emotion_words.txt", "r") as emotion:
    emotions = [emo.strip().split()[0] for emo in emotion.readlines()]

#7) Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
first_chars = open("travel_plans.txt", "r").read()[:33]

#8) Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
with open("school_prompt.txt", "r") as school:
    p_words = list()
    for word in school.read().split(): #iterator = word and iterable is a list of all words of the string created with read() from object school
       if "p" in word: #check if p is in a string elemeent 
           p_words.append(word) #if TRUE append the list p.words with this string
    print(p_words)
