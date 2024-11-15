import pandas as pd
import random

# Console-based user login system
def login_system():
    print("Welcome to the Movie Data Login System")
    while True:
        username = input("Please enter your username: ")
        
        if username.strip():  # Check if the input is not empty or just spaces
            print(f"You are now logged in as {username}")
            display_random_movies("C:/Users/kaivkarl/OneDrive - Tartu Ülikool/Töölaud/Kool/Andmeteadus/Projekt/Movie-Recommendation-system/imdb_movies.csv")
            break  # Exit the loop when a valid username is provided
        else:
            print("Username cannot be empty. Please try again.")

# Function to display 20 random movies from a CSV file
def display_random_movies(file_path):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Check if there are at least 20 movies
        if len(df) >= 20:
            # Select 20 random rows
            random_movies = df.sample(n=20, random_state=random.randint(1, 1000))
        else:
            print("The file contains fewer than 20 movies. Displaying all available movies.")
            random_movies = df
        
        # Print the selected movies
        print("\nHere are 20 random movies:")
        print(random_movies)
        
    except FileNotFoundError:
        print("Error: The CSV file was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the login system
if __name__ == "__main__":
    login_system()
