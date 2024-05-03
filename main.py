# System packages

# External packages
from colored import Fore, Back, Style

# Imports from own functions
from todo_functions import load_data,show_watchlist,add_movie,add_tv_series

def main():
    data = load_data()
    while True:
        print(f"{Fore.blue}{Back.green}\n===== Movie/TV Series Checklist =====")
        print("1. Show Watchlist")
        print("2. Add Movie")
        print("3. Add TV Series")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_watchlist(data)
        elif choice == "2":
            add_movie(data)
        elif choice == "3":
            add_tv_series(data)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
