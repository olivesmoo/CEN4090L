define c = Character("Meowchael")
define m = Character("Monster")

label chap3:
    "We're in chapter 3!!"
    scene bg_warehouse
    "The air smells faintly stale, as if the place has poor ventilation."
    "It's a warehouse, abandoned by the looks of it."

    show monster
    m "-a faint growl sounds from somewhere in the warehouse-"

    "~fear rushes down your spine as you try to determine what to do."

    hide monster
    "You go to move around the room but something seems off"

    show main_cat
    "You're a cat???"
    hide main_cat

    show monster
    m "-growling gets slightly closer-"
    hide monster

    show main_cat
    "Right, being a cat is the least of your problems."
    "You need to escape the monster before it finds you."
    "Looking around the room, there are a couple of things that could help."
    "There's a staircase that leads to a door, another door across the room, and a stack of boxes off to the side."

    menu escape:
        "Hide in the box":
            call box
        "Go upstairs":
            call upstairs
        "Cross the room to the door":
            call door
    return
label box:
    "What the heck."
    "You're a cat."
    "Cats love boxes."
    "Surely this is going to work."
    "You squeeze into the box, hoping it provides sufficient cover."

    scene bg_box
    show main_cat

    "You wait anxiously, your heart racing with each passing moment."
    "Suddenly, you hear footsteps approaching."
    hide main_cat
    show monster
    m "-sniffing around, getting closer to your hiding spot-"
    hide monster
    show main_cat
    menu box_decision:
        "Stay hidden":
            "You hold your breath, praying the monster doesn't discover you."
            "After what feels like an eternity, the footsteps fade away."
            "You cautiously emerge from the box, relieved but still on edge."
            "The monster is snooping around the staircase that leads upstairs."
            menu box_choices:
                "Run to the door the monster came from":
                    call safe_door
                "Hide back in the box":
                    call bad_box
                "Try and sneak past it to the stairs":
                    call fight
        "Make a run for it":
            call fight
    return
            #jump chap3
label bad_box:
    "You climb back into the box."
    "It's very spacious you realize."
    "Perhaps you could live here forever in your new home."
    show monster
    m "-growl-"
    "The monster found you!"
    hide monster
    scene
    "You wake up in a cold sweat"
    return
    #bad ending
label upstairs:
    scene bg_puzzle
    "You rush up the stairs and find yourself facing a peculiar sight."
    "On the door seems to be a notice. The door requires a passcode to enter."
    "After 3 incorrect attempts the alarm will sound which will probably alert the monster."
    "There does not seem to be much time before the monster will break into the room. You might not have time to solve this."
    $ attempts = 0    
    menu puzzle_solve:
        "Go back downstairs":
            "There's no way you can figure this out in time."
            "The best option is to go back downstairs and see if you can do anything else."
            "There is still the box and the other door. Where should you go next."
            menu escape2:
                "Hide in the box":
                    call box
                "Cross the room to the door":
                    call door
        "Try a passcode:":
            $ input = renpy.input("Passcode:")
            if input == "4125":
                call door_unlocked
            else:
                "The keypad flashes red and does not open."
                $ attempts += 1
                if attempts == 3:
                    "That was your third attempt."
                    "An alarm screeches from the keypad echoing through the warehouse loud enough to alert people miles away."
                    "The monster can definitely hear this"
                    call alarm
                else:
                    "You have made a total of %(attempts)s attempts of 3."
                    "If you are worried about tripping the alarm you can always go downstairs."
                    call puzzle_solve
    return
label door_unlocked:
    "The keypad beeps in acceptance, and the door unlocks with a satisfying click."
    "You push it open and step through into the unknown."
    scene bg_warehouse
    "It's the same room?"
    c "Congradulations you solved my puzzle."
    "A cute cat steps out of the shadows."
    show boss_cute
    c "Sorry to frighten you but I needed to lead you to my puzzle."
    c "Solving that puzzle proves that you are worthy of the warehouse."
    c "You are now the owner of this warehouse and may store whatever you wish in here."
    hide boss_cute
    scene
    "You wake up feeling accomplished"
    #good ending
    return


label door:
    "You rush across the room and go to open the door."
    m "-louder growling that sounds a lot closer-"
    "Crap, the monster is this way."
    menu doorM:
        "Go through the door anyways":
            call fight           
        "Run and hide in the box":
            call box
    return

label alarm:
    scene bg_warehouse
    show monster
    "The monster roars and bursts through the door downstairs."
    "You try to run downstairs to avoid getting trapped but it's no use."
    "The monster meets you at the bottom of the stairs and pounces."
    hide monster
    scene
    "You wake up in a cold sweat."
    #bad ending
    return

label safe_door:
    scene bg_warehouse
    "With no other options, you throw the door open and sprint through."
    "Just as you clear the threshold, you hear a deafening roar behind you."        
    "You don't dare look back, focusing all your energy on getting as far away as possible."
    "Finally, you burst out into the open air, free from the confines of the warehouse."
    "You collapse on the ground, panting heavily but safe at last."
    #good ending
    return
label fight:
    scene boss_fight
    "The monster growls and steps towards you."
    "There is no where to run."
    "Looks like you're going to have to dodge"
    "-letters are going to appear on the screen-"
    "-press the corresponding letter on your keyboard before the time runs out to dodge the monsters attacks."
    $ cont = 0 #continue variable
    $ arr_keys = ["a", "c", "e", "K_UP", "K_SPACE"] #list of keyboard inputs to be selected from. See https://www.pygame.org/docs/ref/key.html for more keys
    default successes = 0
    call qte_setup(0.7, 0.9, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
    # "Function Call" - see label qte_setup for detail on "function"
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomise the location
    $ successes += 1
    while cont == 1:
        call qte_setup(0.7, 0.9, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
        if cont == 1:
            $ successes += 1
            if successes == 5:
                jump qte_success
        # to repeat the qte events until it is missed
    # Check the result of the quick time event
    jump qte_failure
    return

label qte_success:
    "You and the monster stand there panting, worn out from the fight."
    "You blink and suddenly the monster has disappeared."
    hide monster
    show boss_cute
    "Replaced by a cute cat!"
    c "Sorry I didn't mean to frighten you."
    c "I was scared you were going to hurt me."
    "Turns out the monster was just a fluffed up cat."
    "You wake up feeling accomplished."
    #Good ending
    return

label qte_failure:
    "The monster lands a hit on the side of your head sending you sprawling to the ground."
    "You wake up in a cold sweat"
    #bad ending
    return

'''
"Function"/pseudo-function
calls the qte screen
parameters are:
    - amount of time given
    - total amount of time (is usually the same as above)
    - timer decreasing interval
    - the key/keyboard input to hit in the quick time event
    - the x alignment of the bar/box
    - the y alignment of the bar/box
'''
label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple
    # can change to call screen qte_button to switch to button mode

    $ cont = _return
    # 1 if key was hit in time, 0 if key not

    return

screen qte_simple:
    #key input qte

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_simple')])
    # timer, using variables from label qte_setup
    # false is the condition if the timer runs out - and this will be reached if the user doesn't get hit the key on time

    key trigger_key action ( Return(1) )
    # the "key detector" (ends qte_event by returning 1)

    vbox:
        xalign x_align
        yalign y_align
        spacing 25
        # vbox arrangement

        text trigger_key:
            xalign 0.5
            color "#fff"
            size 36
            #outlines [ (2,"#000000",0,0) ]
            # text showing the key to press

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"
                # this is the part that changes the colour to red if the time reaches less than 25%
    