import random

print("Enter player name: ")
name = input("")
print("Hello, " + name + ", let's play some hangman!")

word_list = ("abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz",
             "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness",
             "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus","faking",
            "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize",
             "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory",
             "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitu", "jockey", "jogging", "joking", "jovial", "joyful",
            "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury",
             "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays",  "numbskull", "nymph","onyx", "ovary",  "oxidize","oxygen",
             "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes",
             "quorum", "razzmatazz", "rhubarb",  "rhythm","rickshaw", "schnapps", "scratch", "shiv",  "snazzy","sphinx", "spritz", "squawk",  "staff", "strength","strengths", "stretch",
             "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant",  "triphthong","twelfth", "twelfths",
             "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy",
              "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy",
              "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac")
word = list(random.choice(word_list))
lives = 10
hidden_word = (list("_" * len(word)))
guessed_letters = []

while lives > 0 or hidden_word != word:
    guess = input("Please enter a character: ")
    if guess not in "abcdefghijklmnopqrstuvwxyz" or guess in guessed_letters or len(guess) != 1:
        print("invalid guess please try again ")
    elif guess in word:
        for i, letter in enumerate(word):
            if guess == word[i]:
                hidden_word[i] = guess
                guessed_letters.append(guess)
                print(hidden_word)
    else:
        hidden_word = hidden_word
        guessed_letters.append(guess)
        print(hidden_word)
        lives -= 1
    print("You have " + str(lives) + " lives remaining")
    if lives <= 0:
        print("Out of guesses! The word was: " + str(word) + "Please try again!")
        break
    elif hidden_word == word:
        print("Congrats you win!")
        break







