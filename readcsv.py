import pandas as pd

# CSV-faili lugemine
df = pd.read_csv('imdb_movies_with_id.csv')

#Muutujad
ID = df['ID']
date = df['date_x']
names = df['names']
score = df['score']
genre = df['genre']
overview = df['overview']
crew = df['crew']
orig_title = df['orig_title']
status = df['status']
orig_lang = df['orig_lang']
budget = df['budget_x']
revenue = df['revenue']
country = df['country']
