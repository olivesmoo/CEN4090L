define cat = Character(persistent.player_name)
define dog = Character("Dave")
define spectral_cat = Character("Spectral Cat")
define n = Character("Narrator")
define ghost = Character("Ghost Cat")



label chap5:
    scene farcattree

    show cat_neutral at hannahspot
    cat "HEY WHATS THAT"

    hide cat_neutral
    scene cattree
    show cat_happy at hannahspot
    cat "Its a cat tree. Should I check it out?"

    menu:
        "Run straight in.": 
            call choice_1a  

        "Proceed with caution.":  
            call choice_1b 
    return



label choice_1a:

    scene backdrop
    show cat_scared at hannahspot
    show dave at dogspot
    cat "MEOWWWWWWWWWWWW!"
    call try_again
    
label choice_1b:
    scene dark_level
    cat "WHYS IS SO DARK IN THERE?? AND WHY ARE THERE SO MANY COBWEBS?"
    cat "I GUESS IT’S BEEN A WHILE SINCE A CURIOUS CAT LIKE ME WANDERED INSI- …" 
    n "BANG"
    scene level_one
    show cat_scared at hannahspot
    cat "HEY… WHA-... WHAT’S THAT SOUND? I WONDER WHICH WAY IT’S COMING FROM."
    hide cat_scared
    menu:
        "Investigate to the right":
            call choice_2a
        "Investigate to the left":
            call choice_2b
    return

label choice_2a:
    scene 2b
    n "The sound gets louder, more cobwebs appear, and you get more scared."
    show cat_scared at hannahspot
    cat "Hello? An-Anyone There??..."

    show mouse at dogspot
    hide cat_scared
    show cat_neutral at hannahspot
    cat "Oh. It's just a silly little mouse. I'm such a scaredy cat. Come here you!"
    hide mouse
    hide cat_neutral
    scene two_paths

    n "As the mouse runs away, you come up on a fork in the road"
    menu:
        "Go down the dark path":
            call choice_3a
        "Follow the light":
            call choice_3b
    return
    

label choice_2b:
    scene 2b
    show cat_scared at hannahspot
    n "Splash Splash"
    n "The sound gets louder, more cobwebs appear, and you get more scared."

    hide cat_scared
    show cat_wet at hannahspot
    show bucket at dogspot

    n "Oh NO !!! SPLASH!!"
    call try_again


label choice_3a:
    scene dark_background
    show cat_scared at hannahspot

    n "The darkness is overwhelming, your eyes struggle to adjust, but you press forward. Suddenly, you hear a whisper, your fur stands on end as you realize the whispers are calling your name... You attempt to flee but find yourself facing a ghost cat who wants to play!"
    show ghost at dogspot
    ghost "Finally, a friend! Will you play with me? I've been so lonely in this shadow."
    menu:
        "Agree to play with the ghost cat":
            call choice_4a
        "Refuse and try to run past":
            call choice_4b
    return

label choice_3b:
    scene backdrop
    show cat_happy at hannahspot
    show goggles at dogspot
    n "You find night vision goggles congrats"
    hide goggles
    show bed at dogspot
    cat "I can see everything now yay. And I see a bed"
    menu:
        "Take a nap":
            call choice_4c
        "Ignore the bed and continue exploring":
            call choice_4d
    return

label choice_4a:
    scene dark_background
    show cat_happy at hannahspot
    show ghost at dogspot
    ghost "Yay thank you for playing with me"
    hide cat_happy
    scene ghost_exit
    show goggles at exactmiddle
    ghost "Here are some night vision goggles and the way out!"
    python:
        chapter_success(5, True)
    return

label choice_4b:
    scene dark_background
    show cat_scared at hannahspot
    n "You attempt to dash away... until..."
    show ghost at dogspot
    ghost "Why are you ignoring me. I will get my vengaence"
    call try_again

label choice_4c:
    scene backdrop
    show bed at dogspot
    show cat_neutral at dogspotontop
    n "You fall fast asleep in the nice comfy bed..."
    hide cat_neutral
    show cat_dead at dogspotontop
    n "Unfortunately you got killed by an evil ghost spirit in your dream."
    call try_again


label choice_4d:
    scene backdrop
    show door at dogspot
    show cat_happy at hannahspot
    n "You decide to keep exploring and see another door"
    menu:
        "Enter the glowing room":
            call choice_5a
        "Hesitate and listen at the door":
            call choice_5b
    return

label choice_5a:
    scene backdrop
    show potion at exactmiddle
    n "There sits a magic potion. Should you drink it though?"
    menu:
        "Drink the potion":
            call choice_6a
        "Refuse to drink and search for another exit":
            call choice_6b
    return

label choice_5b:
    scene backdrop
    show door at dogspot
    show cat_happy at exactmiddle
    n "you hear cat puring sounds. Should you go in?"
    menu:
        "Take the risk and sneak in":
            call choice_6c
        "Decide its too risky and keep looking":
            call choice_6d
    return

label choice_6a:
    scene backdrop
    show cat_dead at exactmiddle
    n "You start to feel sick after drinking the potion and suddenly... BOOM... you explode"
    call try_again

label choice_6b:
    scene 4a
    show door at exactmiddle
    n "You find a small tunnel and go through it and emerge to the outside world!"
    python:
        chapter_success(5, True)
    return

label choice_6c:
    scene dark_background
    show cat_scared at hannahspot
    cat "Hmm, this room feels different. Hello?"
    show spectral_cat at dogspot
    spectral_cat "Welcome, living one. You're brave to enter. I can offer you guidance or a test. What's your desire?"
    menu:
        "Ask for guidance":
            call choice_7a
        "Accept the test":
            call choice_7b

label choice_6d:
    scene two_dark_paths
    n "You find a vent that leads to interconnecting tunnels where you ahve to make a choice."
    menu: 
        "Go left":
            call choice_7c
        "Go right":
            call choice_7d
    return 

label choice_7a:
    scene dark_background
    show cat_scared at hannahspot
    show spectral_cat at dogspot
    spectral_cat "Here's some advice: always be aware of your surroundings and trust your instincts."
    show collar at exactmiddle
    cat "What's this?"
    spectral_cat "This is a spectral collar. It will glow when danger is near and guide you to the exit. Wear it and be safe."
    menu:
        "Take the cat's gift and wear it":
            call choice_8a
        "Say no thank you!":
            call choice_8b
    return

label choice_7b:
    scene 4a
    show spectral_cat at dogspot
    n "The spectral cat challenges you to a game of wits. You must navigate through illusions and tricks."
    hide spectral_cat

    n "Solve for x in this math equation: 2x + 5 = 9"
    menu:
        "The answer is 7":
            python:
                pass_test = False
        "The answer is 2":
            python:
                pass_test = True
    if pass_test:
        show cat_happy at hannahspot
        show charm at dogspot
        n "Congratulations! You've earned a charm of nine lives, offering protection from one fatal mistake."
        n "Fortunately, this charm aided you in exiting the house"
        python: 
            chapter_success(5, True)
        return
    else:
        show cat_dead at exactmiddle
        n "Unfortunately, you did not pass the test."
        call try_again
    return

label choice_7c:
    scene level_one
    show cat_happy at exactmiddle
    n "You find your way back to the beginning level and make it out of the house!"
    python: 
            chapter_success(5, True)
    return

label choice_7d:
    scene backdrop
    show sideways_cat at exactmiddle
    n "Oh no! You're falling into a pit of waterrrr"
    call try_again

label choice_8a:
    scene farcattree
    show cat_happy at hannahspot
    show glow_Collar at hannahspot
    n "Wearing the spectral collar, you notice it glowing faintly, guiding you through the maze to the exit."
    cat "Looks like this collar really shows the way. Goodbye spooky house!"
    n "As you step outside, the fresh air feels invigorating. The collar fades as you leave the threshold, its job done."
    python:
        chapter_success(5, True)
    return

label choice_8b:
    scene dark_background
    show cat_scared at hannahspot
    n "You cautiously step into the next room, but it's pitch black. You can't see anything, and the silence is eerie."
    n "Suddenly, a loud noise! BANG!!! Something brushes against your leg!"
    cat "Aaah! What was that?!"
    n "Your heart races as you realize you're not alone. Something in the darkness is moving."
    call try_again

label try_again:
    cat "Do you wanna try again?"
    menu:
        "Try again":
            call chap5
        "Continue on":
            python:
                chapter_success(5, False)
            return

