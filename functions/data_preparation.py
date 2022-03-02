"""
## Additional links:
"""
import pandas as pd
from datetime import datetime

def read_users(path0):
    """This reads and cleans user demographic info."""
    cols = ['userId', 'age', 'gender','occupation','zipCode']
    users = pd.read_csv(path0, sep='|', names=cols)
    return users

def read_ratings(path1):
    """This function reads and cleans user ratings."""
    cols = ['userId', 'movieId', 'rating','timestamp']
    ratings = pd.read_csv(path1, sep='\t', names=cols)
    ratings['ratingCompleted'
           ] = ratings.timestamp.apply(lambda x: datetime.fromtimestamp(x))
    ratings.drop(['timestamp'], axis=1, inplace=True)
    return ratings

def merge_datasets(df1, df2, join_field):
    """This function merges more than one data set"""
    return pd.merge(df1, df2, on=join_field)

def titles(path2):
    cols = ['movieId', 'movieTitle', 'releaseDate', 'video release date',
            'IMDbURL', 'unknown', 'Action', 'Adventure', 'Animation', 'Kids',
            'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
            'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War',
            'Western']
    df_movie = pd.read_csv('data/u.item', sep='|', encoding='latin-1', names=cols)
    df_movie.drop(['video release date'], axis=1, inplace=True)  
    return df_movie
    
def movie_rater(movie_df,num, genre=None):
    userID = 2000 
    rating_list = []
    while num > 0:
        if genre:
            movie = movie_df[movie_df['genre'].str.contains(genre)].sample(1)
        else:
            movie = movie_df.sample(1)
        print(movie)
        rating = input('How do you rate this movie on a scale of 1-5, press n if you have not seen :\n')
        if rating == 'n':
            continue
        else:
            rating_one_movie = {'userId':userID,'movieId':movie['movieId'].values[0],'rating':rating}
            rating_list.append(rating_one_movie) 
            num -= 1
    return rating_list 
def full_clean():
    """
    This is function when called will run all the support functions above.

    """
    path0 = 'data/u.user'
    path1 = 'data/u.data'
    path2 = 'data/u.item'

    users = read_users(path0)
    ratings = read_ratings(path1)
    movie_titles = titles(path2)
    basic_df = merge_datasets(users,ratings,'userId')
    data = merge_datasets(basic_df, movie_titles,'movieId')
    
    return users, ratings, basic_df, movie_titles, data