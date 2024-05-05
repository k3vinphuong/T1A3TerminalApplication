# Built in python feature used for this program
import json

# Defining load data allows the program to open a json file and see if theres data displayed and to create a file if there is not
def load_data():
    try:
        with open("watchlist.json", "r") as file:
            return json.load(file)
    # if file has not been created, gives it as just the movie and tv show and blank options
    except FileNotFoundError:
        return {"movies": [], "tv_series": []}

# defines the save data option to allow all input movies/tv shows inputted to be saved into json file
def save_data(data):
    with open("watchlist.json", "w") as file:
        # Used to transfer pythhon objects into the json file
        json.dump(data, file, indent=4)

# Shows the watchlist of what movies/tv shows that we have added
def show_watchlist(data):
    print("Movies:")
    for idx, movie in enumerate(data["movies"], start=1):
        print(f"{idx}. {movie['title']} - Rating: {movie.get('rating', 'N/A')} - Completed: {movie.get('completed', 'No')}")
    print("\nTV Series:")
    for idx, series in enumerate(data["tv_series"], start=1):
        print(f"{idx}. {series['title']} - Rating: {series.get('rating', 'N/A')} - Completed: {series.get('completed', 'No')}")

# Gives options to add the title, rating and whether we have completed the movie and then saves the data to the json file
def add_movie(data):
    title = input("Enter movie title: ")
    rating = input("Enter rating (optional): ")
    completed = input("Is it completed? (yes/no): ").lower() == "yes"
    data["movies"].append({"title": title, "rating": rating, "completed": completed})
    save_data(data)
    print("Movie added successfully!")

# Does the same as the previous option but adds a tv show instead
def add_tv_series(data):
    title = input("Enter TV series title: ")
    rating = input("Enter rating (optional): ")
    completed = input("Is it completed? (yes/no): ").lower() == "yes"
    data["tv_series"].append({"title": title, "rating": rating, "completed": completed})
    save_data(data)
    print("TV series added successfully!")