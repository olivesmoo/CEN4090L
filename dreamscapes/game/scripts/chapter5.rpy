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
            call choice_1a  

        "Proceed with caution.":  
            call choice_1b 
    return

label try_again:
    sandy "Wah wah do you wanna try again?"
    menu:
        "Try again":
            call chap5
        "Continue on":
            python:
                chapter_success(5, False)
            return

label choice_1a:
    scene scary_dog
    show sandy at hannahspot
    sandy "MEOWWWWWWWWWWWW!"
    call try_again
    
label choice_1b:
    scene level_one
    show sandy at hannahspot
    # sandy "WHYS IS SO DARK IN THERE?? AND WHY ARE THERE SO MANY COBWEBS?"
    # sandy "I GUESS IT’S BEEN A WHILE SINCE A CURIOUS CAT LIKE ME WANDERED INSI- …"
    # #play sound "woof.mp3"
    # sandy "HEY… WHA-... WHAT’S THAT SOUND? I WONDER WHICH WAY IT’S COMING FROM."

    # add in next two line on good endings
    python:
        chapter_success(5, True)
    return

# label choice_1b:

# label choice_1b:


# label choice_1b:


# label choice_1b:


