import pickle
dir = '/Users/aiudd75/OneDrive - Amway Corp/MCS/CS598-DM-Capstone/task2/practice/'
with open(dir+'words2ids.pickle', 'rb') as f:
        words2ids = pickle.load(f)



from sklearn.feature_extraction.text import TfidfVectorizer
from gensim import matutils
from sklearn.feature_extraction.text import CountVectorizer
from gensim import models
import random
import glob
import nltk

path2files="/Users/aiudd75/OneDrive - Amway Corp/MCS/CS598-DM-Capstone/task2/my_cats/"

big_file = []
c_names = []
cat_list = glob.glob (path2files+"*")
cat_size = len(cat_list)
# print("cat size", cat_list)
if cat_size < 1:
    print("you need to generate the cuisines files 'categories' folder first")

sample_size = min(4, cat_size)
cat_sample = sorted(random.sample(list(range(cat_size)), sample_size) )
# print ("cat sample", cat_sample)
count = 0
for i, item in enumerate(cat_list):
    if i == cat_sample[count]:
        li =  item.split('/')
        cuisine_name = li[-1]
        c_names.append(cuisine_name[:-4].replace("_"," "))
        text = []
        with open ( item ) as f:
            for l in f.readlines():
                text.append(l)
        big_file.append(text)
#         print(count)
        count = count + 1
    if count >= len(cat_sample):
        print("generating cuisine matrix with:", count, "cuisines")
        break
print('c_name',c_names)
# print('text', big_file[9][0])


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vectorizer = TfidfVectorizer(max_df=.5, max_features=10000000,
                                     min_df=.02, stop_words='english',
                                     use_idf=True, smooth_idf= True, vocabulary = words2ids)
X = []
for i, c in enumerate(c_names):
    tf = vectorizer.fit_transform(big_file[i])
    X.append(tf)
    
print(("1 n_samples: %d, n_features: %d" % X[0].shape))

from time import time
from scipy.sparse import csr_matrix

t0 = time()

sim_mat = np.zeros((sample_size, sample_size))
for i, c1 in enumerate(c_names):
    for j,c2 in enumerate(c_names):
        if ( i <= j ):
            A = X[i].todense()
            B = X[j].todense()
            a = cosine_similarity(A,B)
            r, c = a.shape
            v = a.sum()/(r*c)
    #         print("i,j", i,j, c, c_names[j], v)
            sim_mat[i][j] = v
        else:
            sim_mat[i][j] = sim_mat[j][i]
            
sim_mat = sim_mat * 100
print("Time Took,", time() - t0)
print(sim_mat)

with open('sim_mat.pickle', 'wb') as f:
        pickle.dump(sim_mat,f)