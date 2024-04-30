import json

def load_data():
    try:
        with open("watchlist.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"movies": [], "tv_series": []}

def save_data(data):
    with open("watchlist.json", "w") as file:
        json.dump(data, file, indent=4)

def show_watchlist(data):
    print("Movies:")
    for idx, movie in enumerate(data["movies"], start=1):
        print(f"{idx}. {movie['title']} - Rating: {movie.get('rating', 'N/A')} - Completed: {movie.get('completed', 'No')}")
    print("\nTV Series:")
    for idx, series in enumerate(data["tv_series"], start=1):
        print(f"{idx}. {series['title']} - Rating: {series.get('rating', 'N/A')} - Completed: {series.get('completed', 'No')}")

def add_movie(data):
    title = input("Enter movie title: ")
    rating = input("Enter rating (optional): ")
    completed = input("Is it completed? (yes/no): ").lower() == "yes"
    data["movies"].append({"title": title, "rating": rating, "completed": completed})
    save_data(data)
    print("Movie added successfully!")

def add_tv_series(data):
    title = input("Enter TV series title: ")
    rating = input("Enter rating (optional): ")
    completed = input("Is it completed? (yes/no): ").lower() == "yes"
    data["tv_series"].append({"title": title, "rating": rating, "completed": completed})
    save_data(data)
    print("TV series added successfully!")