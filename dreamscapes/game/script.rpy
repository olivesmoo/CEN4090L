# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Cat")
define f = Character("Catective")

# The game starts here.

label start:
    "Welcome to the dream world."
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Bob"

    e "Pleased to meet you, %(player_name)s!"

    scene bg_test # shows background

    show cat_wig # shows character

    e "Muahahahaha"

    e "I have taken over the world!!!!"

    hide cat_wig

    show detective_cat
    f "eh?"

    return
