
import nltk
from nltk.corpus import stopwords

stops = set(stopwords.words('english'))

x  = ['is', 'roshan', 'are']

for line in x:
    if line.lower() not in stops:
        print(line)