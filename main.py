# External packages
from colored import Fore, Back, Style

# Imports from own functions
from todo_functions import load_data,show_watchlist,add_movie,add_tv_series,delete_movie,delete_tv_series

# Main screen menu with all the options
def main():
    data = load_data()
    while True:
        print(f"{Fore.blue}{Back.green}\n===== Movie/TV Series Checklist =====")
        print("1. Show Watchlist")
        print("2. Add Movie")
        print("3. Add TV Series")
        print("4. Delete Movie")
        print("5. Delete TV Series")
        print("6. Exit")
        choice = input("Enter your choice: ")

        # Choices and the command to activate them
        if choice == "1":
            show_watchlist(data)
        elif choice == "2":
            add_movie(data)
        elif choice == "3":
            add_tv_series(data)
        elif choice == "4":
            idx = int(input("Enter the index of the movie to delete: ")) - 1
            delete_movie(data, idx)
        elif choice == "5":
            idx = int(input("Enter the index of the TV series to delete: ")) - 1
            delete_tv_series(data, idx)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


# Used to execute the code from main.py
if __name__ == "__main__":
    main()
