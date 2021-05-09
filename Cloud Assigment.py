
import pandas as pd
import numpy as np
import string
import os.path
# Get the path of the working directory of the script 
scriptdir = os.path.dirname(os.path.abspath(__file__))

# Create an empty dictionary to store words in 
Dict ={}


# Reading first book and extract all words from it
with open (os.path.join(scriptdir, './first book.txt'),'r', encoding="utf8") as f :
    for line in f :
        for word in line.split() :
            word =(word.translate(str.maketrans('', '', string.punctuation))).lower()
            if word not in Dict.keys() :
                Dict[word]=0


# Reading second book and increase the value of the common words by 1
with open (os.path.join(scriptdir, './second book.txt'),'r', encoding="utf8") as f :
    for line in f :
        for word in line.split() :
# Remove punctuation and lower words            
            word =(word.translate(str.maketrans('', '', string.punctuation))).lower()
            if word in Dict.keys() :
                Dict[word] = Dict[word] + 1
            

# transform the dictionary to a DataFrame
df = pd.DataFrame(list(Dict.items()),columns =['word','freq'])

# set the word column to be the index
df = df.set_index("word")

# Remove words with 0 freq (unrepeated words)
df =df.query('freq != 0')

# Sort values descending according to freq column
df.sort_values("freq" , ascending=False)


# ## No of common words :

print(df.shape[0])


