# T1A3 Terminal Application Kevin Phuong

[Link to Github Repository](https://github.com/k3vinphuong/T1A3TerminalApplication)

---

## Dependencies

This app require Python 3 to be installed. Other depenencies will be included in the venv environment.

---

## Running the App

This app can be run through the bash script ./run.sh

---

## Using the app

### Choosing a feature

The app will give you the choice of choosing three different options
1. Show Watchlist
2. Add Movie
3. Add TV Series
4. Delete Movie
5. Deletes tv series
6. Exit

### Show Watchlist

The show watchlist feature displays the tv series and movies that you have added to the json file. This file stores all your inputs until the file is deleted. If there is no file previously created then the file will just show Movies: and TV Series:.

### Add Movie

The add movie feature upon selecting 2 will ask you to enter the following questions 

<Enter movie title:>
<Enter rating:>
<Is it completed? (yes/no):>

The app will then show <Movie added successfully> upon completion and the data will be added to the json file

### Add TV Series

The add tv series feature works similar to the add movie function with the same questions but applying to tv series

<Enter TV series title:>
<Enter rating:>
<Is it completed (yes/no):>

The app will then show TV series added successfully> upon compeletion

### Delete Movie

Upon selecting the number 4, users will be asked to input the index of the movie that they wish to delete. This number corresponds to the number in which the movie is displayed on the list in the <Show Watchlist> feature. Upon successfully entering the index the movie will be deleted and the user will be presented with a <Movie deleted successfully> message. If the wrong index is input the <Invalid movie index> message will be thrown.

### Delete tv series

Upon selecting number 5 users will again be prompt with inputing the index but instead the index of the tv series. Both movie and tv series will have individual list so users will need to check that they have added the write index for the right list.

### Exit

If the user chooses 6 the program will exit. 

---

## Help Dcoumentation 

**Important Notes**
The application saves the input movies and tv series from even previous terminal uses so to fully wipe the history of the json file one should delete the watchlist.json file. 

The application should work on a Mac device as this terminal application was made and tested on a Windows device

**Dependencies**
To run this application, you must have Python 3 installed. The following depenencies also need to be installed to help with the application.
- certifi==2024.2.2
- charset-normalizer==3.3.2
- colored==2.2.4
- idna==3.7
- requests==2.31.0
- urllib3==2.2.1

**Installation**
Run the **run.sh** bash script

---

## Project Management
For the project management I used Trello to help me keep track of where I was up to and how i was going with my application to avoid clustering my work.

Below are some screenshots.

![image](https://github.com/k3vinphuong/T1A3TerminalApplication/assets/161548597/9277fed5-0f59-41cd-8869-2cf56e3ddd9e)
![image](https://github.com/k3vinphuong/T1A3TerminalApplication/assets/161548597/b60822af-7d93-4f15-b5de-ee790d338a03)
![image](https://github.com/k3vinphuong/T1A3TerminalApplication/assets/161548597/4e3a6a07-dc77-4060-8a8e-5b0305e2436c)
![image](https://github.com/k3vinphuong/T1A3TerminalApplication/assets/161548597/1d81a664-403a-45fc-9c94-d6433c841f51)
![image](https://github.com/k3vinphuong/T1A3TerminalApplication/assets/161548597/c5f4045a-2708-489b-aaa7-f68d669ab8d3)

---

## Code Style Guide
For the coding style I chose to use PEP 8 Style guide. The link that I tried to follow when using PEP 8 is this [PEP8 Link](https://peps.python.org/pep-0008/). I chose the use of PEP 8 as it would allow for my code to be more readable and to be more consistent. 

---

## Reference

van Rossum, Guido, et al. “PEP 8 – Style Guide for Python Code.” Peps.python.org, 5 July 2001, peps.python.org/pep-0008/















