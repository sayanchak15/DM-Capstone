import json
cats = ['Kosher',
'Himalayan/Nepalese',
'Peruvian',
'Burmese',
'Ramen',
'Greek',
'Argentine',
'Mediterranean',
'Ukrainian',
'Ethnic Food',
'Japanese',
'Southern',
'Colombian',
'Steakhouses',
'Mexican',
'Coffee & Tea',
'Vegan',
'Latin American',
'Bagels',
'Spanish',
'Champagne Bars',
'French',
'Middle Eastern',
'Cambodian',
'Scandinavian',
'Szechuan',
'Scottish',
'Chinese',
'Belgian',
'Fish & Chips',
'Slovakian',
'Hookah Bars',
'American (New)',
'Venezuelan',
'Singaporean',
'Cantonese',
'Mongolian',
'Taiwanese',
'German',
'Persian/Iranian',
'Vietnamese',
'Bangladeshi',
'Tex-Mex',
'Asian Fusion',
'Polish',
'Caribbean',
'Dim Sum',
'Wine Bars',
'Russian',
'Soul Food',
'Juice Bars & Smoothies',
'Thai',
'African',
'Australian',
'Indian',
'Ethiopian',
'Tapas/Small Plates',
'Moroccan',
'Shanghainese',
'Lebanese',
'Turkish',
'American (Traditional)',
'Cuban',
'Egyptian',
'Brazilian',
'Laotian',
'Seafood',
'Pakistani',
'Cheesesteaks',
'Salvadoran',
'Arabian',
'Halal',
'Sushi Bars',
'Hawaiian',
'Afghan',
'Indonesian',
'Hot Dogs',
'Beer Bar',
'Vegetarian',
'Irish',
'Canadian (New)',
'Korean',
'Filipino',
'Dominican',
'Portuguese',
'British',
'Malaysian',
'Italian']

path2files="/Users/aiudd75/OneDrive - Amway Corp/MCS/CS598-DM-Capstone/data/yelp_dataset_challenge_academic_dataset/"
path2buisness=path2files+"yelp_academic_dataset_business.json"
path2reviews=path2files+"yelp_academic_dataset_review.json"
# outputfile = "Mediterranean_reviews.txt"

all = []

for cat in cats:
    c_bid = []
    with open(path2buisness, 'r') as f:
        for line in f.readlines():
            business_json = json.loads(line)
            bjc = business_json['categories']
            if cat in bjc:
                c_bid.append(business_json['business_id'])
    output_text = []
    with open(path2reviews, 'r') as f:
        for line in f.readlines():
            review_json = json.loads(line)
            rbid = review_json['business_id']
            rstars = str(review_json["stars"])
            if rbid in c_bid:           
                rtext = review_json["text"]
                # output.append([rstars, rtext])
                output_text.append(rtext)

    with open ('../my_cats/' + cat.replace('/', '-').replace(" ", "_").replace("(","").replace(")","").replace("&","") + ".txt" , 'wb') as f:
        f.write('\n'.join(output_text).encode('utf-8').strip())
        # f.write('\n'.join(cat).encode('utf-8').strip())