import random
import csv
import sys
import string
from pyfiglet import Figlet
from tabulate import tabulate
import operator

def main():

    figlet = Figlet()
    fonts = figlet.getFonts()

    x = difficulty(sys.argv)
    if len(x) == 2:
        level, filename = x
    else:
        d = open_scoreboard("scores.csv")
        print_scores(d)
        exit()

    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        header = next(reader)
        dict = list(reader)

    # print(dict)

    albums = {"Taylor Swift":["Tim Mcgraw","Picture To Burn","Teardrops On My Guitar","A Place In This World","Cold As You", "The Outside", "Tied Together With A Smile", "Stay Beautiful", "Should've Said No", "Mary's Song", "Our Song"],
        "Fearless":["Fearless", "Fifteen", "Love Story", "Hey Stephen", "White Horse", "You Belong with Me", "Breathe", "Tell Me Why", "You're Not Sorry", "The Way I Loved You", "Forever & Always", "The Best Day", "Change"],
        "Speak Now":["Mine", "Sparks Fly", "Back To December", "Speak Now", "Dear John", "Mean", "The Story Of Us", "Never Grow Up", "Enchanted", "Better Than Revenge", "Innocent", "Haunted", "Last Kiss", "Long Live"],
        "RED":["State Of Grace", "Red", "Treacherous", "I Knew You Were Trouble", "All Too Well", "22", "I Almost Do", "We Are Never Ever Getting Back Together", "Stay Stay Stay", "The Last Time", "Holy Ground", "Sad Beautiful Tragic", "The Lucky One", "Everything Has Changed", "Starlight", "Begin Again"],
        "1989":["Welcome to New York","Blank Space","Style","Out Of the Woods","All You Had to Do Was Stay","Shake It Off","I Wish You Would","Bad Blood","Wildest Dreams","How You Get The Girl","This Love","I Know Places","Clean"],
        "Reputation":["...Ready For It","End Game","I Did Something Bad","Don't Blame Me","Delicate","Look What You Made Me Do","So It Goes...","Gorgeous","Getaway Car","King Of My Heart","Dancing With Our Hands Tied","Dress","This Is Why We Can't Have Nice Things","Call It What You Want","New Year's Day"],
        "Lover":["I Forgot That You Existed","Cruel Summer","Lover","The Man","The Archer","I Think He Knows","Miss Americana & The Heartbreak Prince","Paper Rings","Cornelia Street","Death By A Thousand Cuts","London Boy","Soon You'll Get Better","False God","You Need To Calm Down","Afterglow","Me!","It's Nice To Have A Friend","Daylight"],
        "Folklore":["The 1","Cardigan","The Last Great American Dynasty","Exile","My Tears Ricochet","Mirrorball","Seven","August","This Is Me Trying","Illicit Affairs","Invisible String","Mad Woman","Epiphany","Betty","Peace","Hoax"],
        "Evermore":["Willow","Champagne Problems","Gold Rush","'Tis The Damn Season","Tolerate It","No Body, No Crime","Happiness","Dorothea","Coney Island","Ivy","Cowboy Like Me","Long Story Short","Marjorie","Closure","Evermore"],
        "Midnights":["Lavender Haze","Maroon","Anti-Hero","Snow On The Beach","You're On Your Own, Kid","Midnight Rain","Question...?","Vigilante Shit","Bejewelled","Labyrinth","Karma","Sweet Nothing","Mastermind"]
        }

    print()
    s = "Welcome to Taylor Swift Lyric Trivia!"
    figlet.setFont(font="rectangles")
    print(figlet.renderText(s))
    # print instructions
    print(instructions())

    print()

    lives = 3
    score = 0

    # as long as player has fewer than 13 points and has at least one life
    while score < 13 and lives >= 1:
        # choose random lyric and store info
        info = rand_lyric(dict,albums)
        song = info[0]
        lyric = info[1]
        tracklist = info[3]

        # print lyric
        print(f"Lyric: {lyric}")
        attempts = 0

        while attempts < 3:
            # prompt user to guess song (case insensitive)
            guess = string.capwords(input("Song: ").strip())
            output = check(guess, song, tracklist)
            print(output)

            # if correct, break
            if output == "Correct!":
                score = score + 1
                print(f"score: {score}")
                break

            # else reprompt
            else:
                attempts = attempts + 1
                print(f"attempts: {attempts}")
        if attempts == 3:
                lives = lives - 1
                print(f"lives: {lives}")


    print(f"Final Score: {score}")

    answer = input("Would you like to add your name to the scoreboard? (yes/no) ")
    if answer == "yes":
        name = input("Name: ")
        record(name, score, level)
    else:
        exit()



def instructions():
    s = ""
    s = s + "Match as many lyrics to their title correctly to beat the highest score. You will have 3 lives.\n"
    s = s + 'Capitalization does not affect scoring. Omit parentheticals and "Featuring" etc.\n'
    s = s + "Songs are from original albums. Bonus/Deluxe tracks are not included.\n"
    s = s + "Get to 13 and you win!"

    return s

def difficulty(entry):
    if len(entry) == 1:
        level = "easy"
        filename = "Taylor Easy.csv"

    elif len(entry) == 2 and entry[1] ==  "-e":
        level = "easy"
        filename = "Taylor Easy.csv"

    elif len(entry) == 2 and entry[1] == "-m":
        level = "medium"
        filename = "Taylor Medium.csv"

    elif len(entry) == 2 and entry[1] == "-h":
        level = "hard"
        filename = "Taylor Hard.csv"
    elif len(entry) == 2 and entry[1] ==  "-s":
        return("scores")

    else:
        print("usage: final.py [-e or -m or -h (easy, medium, hard) or -s (scoreboard)]")

    return(level, filename)

def rand_lyric(dict,albums):
    # choose random lyric from values
    x = random.randint(0,(len(dict)-1))
    song = dict[x]["Song"]
    lyric = dict[x]["Lyric"]
    album = dict[x]["Album"]
    tracklist = albums[album]
    return (song,lyric,album,tracklist)

def check(guess, song, tracklist):
    # if correct, print as such
    if guess == song:
        output = "Correct!"
    elif guess in tracklist:
        output = "Right album!"
    else:
        output = "Wrong!"

    return output

def record(name, score, level):
    score = format(score, '02')
    List = [name, score, level]
    with open("scores.csv", "a") as scoreboard:
        writer = csv.writer(scoreboard)
        writer.writerow(List)

        scoreboard.close()
    return scoreboard

def open_scoreboard(filename):
    data = csv.reader(open(filename),delimiter=",")
    data = sorted(data, key=operator.itemgetter(1), reverse=True)

    return data

def print_scores(scoreboard):
    table = scoreboard
    #headers = "firstrow"
    print(tabulate(table, headers=["Name","Score","Level"], tablefmt="simple"))

if __name__ == "__main__":
    main()