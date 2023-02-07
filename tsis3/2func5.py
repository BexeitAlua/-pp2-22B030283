movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def return_movie_category(movies,cat_name): 
    out_list=[]
    for i in movies:
        curr_cat=i['category']
        if cat_name.lower()==curr_cat.lower():
            out_list.append(i)
    return out_list

def avg_imdb_score(movies): 
    avg_score=0
    tot_movies=len(movies)
    for i in movies:
        avg_score=avg_score+i['imdb']
    avg_score=avg_score/tot_movies
    return avg_score

def avg_imdb_acc_to_cat(movies,cat_name): 
    cat_movies=return_movie_category(movies,cat_name)
    avg_score=avg_imdb_score(cat_movies)
    return avg_score


s2=avg_imdb_acc_to_cat(movies,'Thriller')
print (s2)