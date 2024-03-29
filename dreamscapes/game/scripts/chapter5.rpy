define sandy = Character("sandy")

label chap5:
    "We're in chapter 5!!"
    scene farcattree

    show sandy at hannahspot
    sandy "HEY WHATS THAT"

    hide sandy
    scene cattree
    show sandy at hannahspot
    sandy "Its a cat tree. Should i check it out?"

    menu:
        "Run straight in.": 
            call straight_in  

        "Proceed with caution.":  
            call caution_in  
    return

label straight_in:
    scene scary_dog
    show sandy at hannahspot
    sandy "MEOWWWWWWWWWWWW!"
    return

label caution_in:
    scene level_one
    show sandy at hannahspot
    sandy "Whys it so dark in here??"
    # Continue the storyline for searching in the alley...
    return


