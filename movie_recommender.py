



import json
import requests

def get_movies_from_tastedive(movie):
    parameters= {'q':movie,'type':'movies','limit':5}
    parameters['k']='381469-Movierec-K01LBLDL'
    respage=requests.get('https://tastedive.com/api/similar',params=parameters)
    return respage.json()

def get_movie_titles(movie_dict):
    titles=[movie['Name'] for movie in movie_dict["Similar"]['Results'] ]
    return titles

def get_titles_list(movie_list):
    title_list=[title for movie in movie_list for title in get_movie_titles(get_movies_from_tastedive(movie)) ]
    return list(set(title_list))


def extract_movie_info(movie_name):
    parameters={'t':movie_name,'r':'json'}
    parameters['apikey']='fee51582'
    movie_info=requests.get('http://www.omdbapi.com/',params=parameters)
    return movie_info.json()

def get_rating(movie_info):
    for rating_info in movie_info['Ratings']:
        if rating_info['Source']=='Rotten Tomatoes':
            rating=int(rating_info['Value'][ :2])
            break
        else:
            rating=0
    return rating

def give_sorted_recommendations():
        prompt='Enter name of movie and seperate the movies using comma '
        userinput=str(input(prompt))
        movie_list=userinput.strip().split(',')

        try:
             related_titles=get_titles_list(movie_list)

             recommended_list=sorted(related_titles,key=lambda title: (get_rating(extract_movie_info(title)),title),reverse=True)
             if len(recommended_list)>1:
                 print(recommended_list)
                 return recommended_list
             else:
                 print ('Cannot recognise that movie.Try with different movie')
        except Exception:
             errmsg=' Type the name properly and Please restart the program '
             print(err_msg)


give_sorted_recommendations()
