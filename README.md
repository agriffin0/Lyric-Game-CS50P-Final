# Taylor Swift Lyric Trivia
#### Video Demo:  https://youtu.be/t6hDtZc3qUk
#### Description:
This application is a lyric quiz game. Fans of the popular musician Taylor Swift can test their lyrical knowledge.

Players start with 3 lives. If they can correctly guess 13 (a lucky number for Swifties) without running out of lives, they win!

To get started, the player can select a level of difficulty with the command-line arguments "-e", "-m", or "-h" for easy, medium, or hard, respectively. If the player does not specify a level of difficulty, the game will automatically begin on "easy." If they type command-line arguments other than "-e", "-m", or "-h", or if they include additional arguments, they will be met with a usage instruction message.

The difficulty ranking took three main factors into consideration: length, song popularity, and context. Many "easy" lyrics consist of two or more lines; "hard" lyrics are almost always one line, and often as few as five words. For song popularity, if a song was released as a single or charted highly on Billboard, the lyrics from that song are more likely to be considered "easy." Third, lyrics that provide little context or sound like they could have been on a different album (i.e. a RED lyric that is poetic and cryptic enough to be on Folklore) would be considered "hard."

The inspiration for this game came from the many popular online word and music games modeled after "Wordle." While many Taylor Swift-related games exist (Taylordle, Taylor Swift Heardle, etc) I wanted to create a version that relied solely on Swift's lyricism. She has, over the past 16+ years, proven herself to be a unique lyricist, demonstrating a wide range of genres and messages.

To create this application, I used several libraries, including random, csv, sys, string, and pyfiglet. I also imported tabulate and operator to display a scoreboard that is sorted by the highest score. I re-visited the csv.DictReader function and implemented it to create a dict using the CSV file(s) in the folder. This allows me to update the possible lyrics prompted in a more user-friendly environment of a spreadsheet.

In the main function, first, the program determines which (if any) command-line arguments have been used. It then assigns the appropriate difficulty level and filename values. Next, the program reads the file with the same title as the aforementioned filename value. It then creates a new list of dictionaries that pairs each "Song", "Lyric", and "Album" with the appropriate header.

The core custom functions related to gameplay include instructions, difficulty, rand_lyric, and check. Instructions simply prints the rules of the game by returning it as a string. Difficulty accepts the command-line arguments as a string and determines the level of difficulty that the player wishes to play. If the command-line does not match the anticipated format, the user will receive a usage prompt explaining what the program accepts. Rand_lyric chooses a random integer within the range of the length of the dictionary of lyrics and returns the song, lyric, album, and tracklist associated with that chosen lyric. Check accepts the guess, song, and tracklist and determines if there is a match. If the player guesses a song from the right album, the program will output “Right album!” and allow them to try again.

Three custom functions manage the scoreboard. Record appends the name, score, and level to a CSV file called scores.csv. Open_scoreboard opens the CSV file and sorts the data by highest score. Print_scores uses the library tablulate to display the scoreboard in a more readable format, including headers and physically separated columns.