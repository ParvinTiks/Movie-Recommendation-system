import pandas as pd
import csv
from random import randint

class Film:
    def __init__(self, movie_id, title, date, rating, genre, description, cast, language):
        self.movie_id = movie_id
        self.title = title
        self.date = date
        self.rating = rating
        self.genre = genre
        self.description = description
        self.cast = cast
        self.language = language
        self.year = date[6:10]


user_movie_map = {}


def load_movie_data(file_path='imdb_movies_with_id.csv'):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return pd.DataFrame()


def convert_dataframe_to_film_objects(df):
    movies = []
    for _, row in df.iterrows():
        try:
            movie_id = row.iloc[-1]
            movie = Film(
                movie_id=movie_id,
                title=row['names'],
                date=row['date_x'],
                rating=row['score'],
                genre=row['genre'],
                description=row['overview'],
                cast=row['crew'],
                language=row['orig_lang']
            )
            movies.append(movie)
        except KeyError as e:
            print(f"Missing column in dataset: {e}")
            continue
    return movies


def login_system():
    print("Welcome to the Movie Data Login System")
    while True:
        username = input("Please enter your username: ").strip()
        
        if username:
            print(f"You are now logged in as {username}")
            print(f"Hello, {username}!")
            user_decision = input("Would you like to see movie recommendations? (y/n): ").strip().lower()
            
            if user_decision == 'y':
                selected_movies = display_random_movies(username)
                save_user_movie_associations(username, selected_movies)
            elif user_decision == 'n':
                print("Thank you! Goodbye!")
            else:
                print("Invalid input. Please type 'y' or 'n'.")
            break 
        else:
            print("Username cannot be empty. Please try again.")


def display_random_movies(username):
    movie_data = load_movie_data('imdb_movies_with_id.csv')
    
    if movie_data.empty:
        print("Error: Movie data could not be loaded.")
        return []

    movies = convert_dataframe_to_film_objects(movie_data)
    limit = len(movies)
    used_numbers = set()
    count = min(20, limit)
    
    print("\nHere are 20 random movie recommendations:\n")
    random_movies = []
    for i in range(count):
        random_index = randint(0, limit - 1)
        while random_index in used_numbers:
            random_index = randint(0, limit - 1)
        used_numbers.add(random_index)
        movie = movies[random_index]
        random_movies.append(movie)
        print(f"{i + 1}. {movie.title} ({movie.year}) - Rating: {movie.rating}/100 - {movie.genre}")
        print(f"Description: {movie.description}")
        print(f"Cast: {movie.cast}")
        print(f"Language: {movie.language}\n")
    
    chosen_movies = []
    chosen_indices = set()
    while len(chosen_movies) < 5:
        try:
            choice = int(input(f"Select a movie by number (1-{count}) ({len(chosen_movies) + 1}/5): "))
            if 1 <= choice <= count and choice not in chosen_indices:
                chosen_indices.add(choice)
                chosen_movies.append(random_movies[choice - 1].movie_id)
                selected_movie = random_movies[choice - 1]
                print(f"Selected: {selected_movie.title} ({selected_movie.year})")
            elif choice in chosen_indices:
                print("You have already chosen this movie. Please select a different one.")
            else:
                print(f"Invalid choice. Please select a number between 1 and {count}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nYou selected the following movies:")
    for movie_id in chosen_movies:
        selected_movie = next(movie for movie in random_movies if movie.movie_id == movie_id)
        print(f"{selected_movie.title} ({selected_movie.year}) - {selected_movie.genre}")
    
    print("\nThank you for your selections! Enjoy your movie marathon!")
    return chosen_movies



def save_user_movie_associations(username, movie_ids):
    
    try:
        with open("user_info.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = [] 

   
    user_found = False
    updated_lines = []
    i = 0 
    while i < len(lines):
        line = lines[i]
        if line.startswith(f"Username: {username}"):
            user_found = True
           
            current_ids_line = lines[i + 1]
            existing_ids = current_ids_line.strip().replace("Selected Movies: ", "").split(", ")
            combined_ids = sorted(set(existing_ids + list(map(str, movie_ids))))
            updated_lines.append(f"Username: {username}\n")
            updated_lines.append("Selected Movies: " + ", ".join(combined_ids) + "\n")
            updated_lines.append("-" * 40 + "\n")
            i += 3  
        else:
            updated_lines.append(line)
            i += 1

    if not user_found:
        updated_lines.append(f"Username: {username}\n")
        updated_lines.append("Selected Movies: " + ", ".join(map(str, movie_ids)) + "\n")
        updated_lines.append("-" * 40 + "\n")

    with open("user_info.txt", "w") as file:
        file.writelines(updated_lines)

    print(f"\nSaved selections for {username}: {combined_ids if user_found else movie_ids}")
    print("User information saved to 'user_info.txt'.")



if __name__ == "__main__":
    login_system()
