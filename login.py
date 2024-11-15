import pandas as pd
import random

# Console-based user login system
def login_system():
    print("Welcome to the Movie Data Login System")
    while True:
        username = input("Please enter your username: ")
        
        if username.strip():  # Check if the input is not empty or just spaces
            print(f"You are now logged in as {username}")
            print(f"Hello, {username}!")
            user_decision = input("Would you like to see movie recommendations? (y/n): ").strip().lower()
            
            if user_decision == 'y':
                display_random_movies("C:/Users/kaivkarl/OneDrive - Tartu Ülikool/Töölaud/Kool/Andmeteadus/Projekt/Movie-Recommendation-system/imdb_movies.csv")
            elif user_decision == 'n':
                print("Thank you! Goodbye!")
            else:
                print("Invalid input. Please type 'y' or 'n'.")
            break  # Exit the loop after the interaction is complete
        else:
            print("Username cannot be empty. Please try again.")

# Function to display 20 random movies from a CSV file and allow the user to choose 5 movies
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
        
        # Print the selected movies with numbering
        print("\nHere are 20 random movie recommendations:\n")
        for i, (index, movie) in enumerate(random_movies.iterrows(), start=1):
            print(f"{'-' * 5} {i} {'-' * 5}")
            print(f"Name: {movie['names']}")
            print(f"Release Date: {movie['date_x']}")
            print(f"Score: {movie['score']}")
            print(f"Genre: {movie['genre']}")
            print(f"Overview: {movie['overview']}")
            print(f"Crew: {movie['crew']}")
            print(f"Original Language: {movie['orig_lang']}")
            print("\n")  # Line break between each movie for better readability
        
        # Prompt the user to choose 5 movies by their numbers
        chosen_indices = []
        while len(chosen_indices) < 5:
            try:
                choice = int(input(f"\nSelect a movie by number (1-20) ({len(chosen_indices) + 1}/5): "))
                if 1 <= choice <= len(random_movies) and choice not in chosen_indices:
                    chosen_indices.append(choice)
                    chosen_movie = random_movies.iloc[choice - 1]
                    print(f"Selected: {choice} - {chosen_movie['names']}")
                elif choice in chosen_indices:
                    print("You have already chosen this movie. Please select a different one.")
                else:
                    print("Invalid choice. Please enter a number between 1 and 20.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Display only the chosen numbers and movie titles
        print("\nYou selected the following movies:")
        for choice in chosen_indices:
            chosen_movie = random_movies.iloc[choice - 1]
            print(f"{choice} - {chosen_movie['names']}")
        
        # Wish the user something good
        print("\nThank you for your selections! Enjoy your movie marathon and have a great time!")

    except FileNotFoundError:
        print("Error: The CSV file was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")






# Run the login system
if __name__ == "__main__":
    login_system()
