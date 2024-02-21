# The game starts here.
label start:
    "Welcome to the dream world."
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Nameless One"

    e "Pleased to meet you, %(player_name)s!"


    scene blank
    call chapter1start
    scene blank
    call chapter2start
    scene blank
    call chapter3start
    scene blank
    call chapter4start
    scene blank
    call chapter5start
    return
