
# coding: utf-8

# In[6]:

import fileinput
from collections import Counter
from nltk import word_tokenize
import string
from nltk.corpus import stopwords


# In[20]:

lines = []
for line in open('building_global_community.txt'):
    line = line.strip()
    lines.append(line)


# In[21]:

lines


# In[25]:

sentence = ''.join(lines)
sentence = sentence.replace('-\n','')
sentence = sentence.replace('-',' ')
print (sentence)


# In[26]:

sentence.lower()


# In[28]:

data = sentence.split(' ')


# In[29]:

data


# In[31]:

print(word_tokenize(sentence))


# In[32]:

from nltk import wordpunct_tokenize
print(wordpunct_tokenize(sentence))


# In[33]:

import string
string.punctuation


# In[9]:

stopwords = set(stopwords.words('english'))
stopwords.update(string.punctuation)


# In[36]:

words = word_tokenize(sentence)
# for word in words:
#     if word not in stopwords:
#         print(word)
print([word for word in words if word not in stopwords])


# In[38]:

words = [word for word in words if word not in stopwords]
clean = [word for word in words if word.isalpha()]


# In[39]:

counter = Counter(clean)


# In[40]:

counter.most_common(20)


# In[41]:

import csv
with open('wordcount.csv', 'w') as csvfile:
    # set up header
    fieldnames = ['word', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for word, count in counter.most_common():
        writer.writerow({'word': word, 'count': count})


# In[42]:

with open('wordcount.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['word'], row['count'])


# In[ ]:



