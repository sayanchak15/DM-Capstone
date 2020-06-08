from sklearn.feature_extraction.text import TfidfVectorizer
from gensim import matutils
from sklearn.feature_extraction.text import CountVectorizer
from gensim import models
import random
import glob

path2files="/Users/aiudd75/OneDrive - Amway Corp/MCS/CS598-DM-Capstone/task2/my_cats/"

file1 = path2files + "Indian.txt"
file2 = path2files + "Bangladeshi.txt"

text = []
c_names = []
cat_list = glob.glob ("../my_cats/*")
cat_size = len(cat_list)
print("cat size", cat_size)
if cat_size < 1:
    print("you need to generate the cuisines files 'categories' folder first")

sample_size = min(30, cat_size)
cat_sample = sorted(random.sample(list(range(cat_size)), sample_size) )
# print ("cat sample", cat_sample)
count = 0
for i, item in enumerate(cat_list):
    if i == cat_sample[count]:
        li =  item.split('/')
        cuisine_name = li[-1]
        c_names.append(cuisine_name[:-4].replace("_"," "))
        with open ( item ) as f:
            text.append(f.read().replace("\n", " "))
        count = count + 1
    if count >= len(cat_sample):
        print("generating cuisine matrix with:", count, "cuisines")
        break
print('c_name',c_names)
print('text', text[0])



# vectorizer = TfidfVectorizer(max_df=1, max_features=100000,
#                                      min_df=1, stop_words='english',
#                                      use_idf=True)
# X = vectorizer.fit_transform(text)
# print(("n_samples: %d, n_features: %d" % X.shape))
# corpus = matutils.Sparse2Corpus(X,  documents_columns=False)
# # mat = matutils.corpus2csc(corpus)

