define c = Character("Meowchael")
define m = Character("Monster")
label chap3:
    "We're in chapter 3!!"
    scene bg_warehouse
    "The air smells faintly stale, as if the place has poor ventilation."
    "It's a warehouse, abandoned by the looks of it."

    show monster
    m "-a faint growl sounds from somewhere in the warehouse-"

    c "~fear rushes down your spine as you try to determine what to do."

    hide monster
    "You go to move around the room but something seems off"

    show main_cat
    "You're a cat???"
    hide main_cat

    show monster
    m "-growling gets slightly closer"
    hide monster

    show main_cat
    "Right being a cat is the least of your problems"
    "You need to escape the monster before it finds you"
    "Looking around the room there are a couple of things that could help."
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
    "Surely this is going to work"
    #hide main_cat
    #hide bg_warehouse
    #show bg_box
    #show main_cat
    
    return

label upstairs:
    "You rush up the stairs and try the door."
    "It's locked."
    return

label door:
    "You rush across the room and go to open the door"
    m "-louder growling that sounds a lot closer-"
    "Crap the monster is this way"
    #menu doorM:
     #   "Go through the door anyways":
      #      call dumb
       # "Run and hide in the box":
        #    call box
        