import json


def get_unique(cat):
    final = []
    for c in cat:
        final.extend(c)
    final = set(final)
    return list(final)

        

r = 'Restaurants'
# c = "Mediterranean"

path2files="/Users/aiudd75/OneDrive - Amway Corp/MCS/CS598-DM-Capstone/data/yelp_dataset_challenge_academic_dataset/"
path2buisness=path2files+"yelp_academic_dataset_business.json"
path2reviews=path2files+"yelp_academic_dataset_review.json"

all_rest_id = []
cat = []
with open(path2buisness, 'r') as f:
    for line in f.readlines():
        business_json = json.loads(line)
        bjc = business_json['categories']
        if r in bjc:
            all_rest_id.append([business_json['business_id'],business_json['name']])
            cat.append(bjc)
cat_set = get_unique(cat)
print(len(cat_set))

with open ('all_categories.csv', 'w') as f:
    for i in cat_set:
        f.write(str(i)+'\n')