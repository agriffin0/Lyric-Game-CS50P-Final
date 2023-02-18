from project import instructions, difficulty, check
import csv

scores = "scores.csv"

def test_instructions():
    assert instructions() == 'Match as many lyrics to their title correctly to beat the highest score. You will have 3 lives.\nCapitalization does not affect scoring. Omit parentheticals and "Featuring" etc.\nSongs are from original albums. Bonus/Deluxe tracks are not included.\nGet to 13 and you win!'

def test_difficulty():
    entry1 = ["project.py", "-e"]
    assert difficulty(entry1) == ("easy", "Taylor Easy.csv")
    entry2 = ["project.py", "-s"]
    assert difficulty(entry2) == "scores"

def test_check():
    assert check("Our Song", "Our Song", 1) == "Correct!"