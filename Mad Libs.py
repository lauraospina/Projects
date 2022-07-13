
import pandas as pd 
import random 
words = pd.read_csv('C:/Users/Laura/Downloads/MadLibs Words - Sheet1.csv')

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
while(True):    
    choice_type = input("If you would like a computer-generated Mad Libs story, please type CG. If you would you like to choose your own words to create the story, please type OW: ")
    choice_story = input("If you would like a story about a dog, please type dog. If you would like a story about a woman travelling to a castle, please type castle: ")

    if (choice_type == "CG" and choice_story == "dog"):
        story1 = "With his fur the color " + color() + " and his personality as sweet as " + pluralnoun() + ", Milo was the most desirable pet at the shelter. " + pluralnoun() + " from all over came to see him and his " + adj() + " ears. As a thank you, Milo " + adverb() + " wagged his tail and excitedly " + pastverb() + "!"
        print(story1)
        break
    if (choice_type == "CG" and choice_story == "castle"):
        story2 = "Riding through the " + adj() + " storm and the valley of " + color() + " mountains was no easy feat. With a sudden " + verb() + ", Tess arrived at the function. She had been transported to the castle via " + noun() + " and was 30 minutes late. Everyone " + pastverb() + " and stared. They could not believe their " + adj() + " eyes. Tess was here and ready to " + verb() + "!"
        print(story2)
        break
    if (choice_type == "OW" and choice_story == "dog"):
        color = input("Enter a color: ")
        pnoun1 = input("Enter a plural noun: ")
        pnoun2 = input("Enter a plural noun: ")
        adj1 = input("Enter an adjective: ")
        adv = input("Enter an adverb: ")
        pverb = input("Enter a verb in past tense: ")
        story1 = "With his fur the color " + color + " and his personality as sweet as " + pnoun1 + ", Milo was the most desirable pet at the shelter. " + pnoun2 + " from all over came to see him and his " + adj1 + " ears. As a thank you, Milo " + adv + " wagged his tail and excitedly " + pverb + "!"
        print(story1)
        break
    if (choice_type == "OW" and choice_story == "castle"):
        adj1 = input("Enter an adjective: ")
        color = input("Enter a color: ")
        verb1 = input("Enter a verb: ")
        noun = input("Enter a noun: ")
        pverb = input("Enter a verb in past tense: ")
        adj2 = input("Enter an adjective: ")
        verb2 = input("Enter a verb: ")
        story2 = "Riding through the " + adj1 + " storm and the valley of " + color + " mountains was no easy feat. With a sudden " + verb1 + ", Tess arrived at the function. She had been transported to the castle via " + noun + " and was 30 minutes late. Everyone " + pverb + " and stared. They could not believe their " + adj2 + " eyes. Tess was here and ready to " + verb2 + "!"
        print(story2)
        break
    else:
        print("Please try again ")