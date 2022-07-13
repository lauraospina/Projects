#working on madlibs
import pandas as pd 
import random 
words = pd.read_csv('C:/Users/Laura/Downloads/MadLibs Words - Sheet1.csv')
# print(words)
def verb():
    return random.choice(words["Verb"])
def noun(): 
    return random.choice(words["Noun"])
def pastverb():
    return random.choice(words["Verb Past Tense"])
def adj():
    return random.choice(words["Adjective"])
def adverb():
    return random.choice(words["Adverbs"])
def pluralnoun():
    return random.choice(words["Plural Noun "])
def color():
    return random.choice(words["Color"])

print("Welcome to Laura's Mad Libs! ")
choice_type = input("If you would like a computer-generated Mad Libs story, please type CG. If you would you like to input your own words to create the story, please type OW: ")
choice_story = input("If you would like a story about a dog, please type dog. If you would like a story about a woman travelling to a castle, please type castle: ")

if (choice_type == "CG" and choice_story == "dog"):
    story1 = "With his fur the color of " + color() + " and his personality as sweet as " + pluralnoun() + ", Frank the dog was the most desirable pet at the shelter. " + pluralnoun() + " from all over came to see him and his " + adj() + "ears. As a thank you, Frank " + adverb() + " wagged his tail and excitedly " + pastverb() + "!"
    print(story1) 
if (choice_type == "CG" and choice_story == "castle"):
    story2 = "Riding through the " + adj() + " storm and the desert of the " + color() + " mountains was no easy feat. With a sudden " + verb() + ", Tess had arrived at the function. She had been transported to the castle via " + noun() + " and was 30 minutes late. Everyone " + pastverb() + " and stared. They could not believe their " + adj() + " eyes. Tess was here and ready to " + verb() + "!"
    print(story2) 
if (choice_type == "OW" and choice_story == "castle"):
    color = input("Enter a color: ")
    pnoun1 = input("Enter a plural noun: ")
    pnoun2 = input("Enter a plural noun: ")
    adj1 = input("Enter an adjective: ")
    adv = input("Enter an adverb: ")
    pverb = (" Enter a verb in past tense: ")
    





# do a sentiment analysis on the curated story

# import nltk
# nltk.download('vader_lexicon')

# from nltk.sentiment import SentimentIntensityAnalyzer
# sia = SentimentIntensityAnalyzer()
# sia.polarity_scores(story1)

# from nltk.tokenize import word_tokenize
# toked1 = word_tokenize(story1)
# print(toked1)
# toked2 = word_tokenize(story2)
# print(toked2)


# # to filter out the punctuation that was counted as tokens
# str.isalpha()