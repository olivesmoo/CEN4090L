$ renpy.include("globals.rpy")

# Define a dictionary to store the visited status of checkpoints
init python:
    # persistent._clear()
    # del persistent.player_name
    if not persistent.visited_checkpoints:
        persistent.visited_checkpoints = {}
    if not persistent.completed_chapters:
        persistent.completed_chapters = {1: False, 2: False, 3: False, 4: False, 5: False}

    current_checkpoint = 'start'

    # Function to mark a checkpoint as visited
    def mark_checkpoint_visited(checkpoint_label):
        persistent.visited_checkpoints[checkpoint_label] = True

    # Function to check if a checkpoint has been visited
    def is_checkpoint_visited(checkpoint_label):
        return persistent.visited_checkpoints.get(checkpoint_label, False)

    def chapter_success(chapter, success): # ex: (2, False)
        if success == True:
            persistent.completed_chapters[chapter] = True
    
    def completed_all():
        return all(persistent.completed_chapters[i] for i in range(2, 6))

# The game starts here.
label start:
    if current_checkpoint == 'start':
        if not persistent.player_name:
            "Welcome to the dream world."
            $ persistent.player_name = renpy.input("What is your name?")
            $ persistent.player_name = persistent.player_name.strip()
            if persistent.player_name == "":
                $ persistent.player_name="Nameless One"
            e "Pleased to meet you, [persistent.player_name]!"
        else:
            e "Welcome back to the dream world, [persistent.player_name]"
        scene blank
    elif current_checkpoint == 'chapter1start':
        jump chapter1start
    elif current_checkpoint == 'chapter2start':
        jump chapter2start
    elif current_checkpoint == 'chapter3start':
        jump chapter3start
    elif current_checkpoint == 'chapter4start':
        jump chapter4start
    elif current_checkpoint == 'chapter5start':
        jump chapter5start      
    elif current_checkpoint == 'endingstart':
        jump endingstart
        
label chapter1start:
    python:
        mark_checkpoint_visited("chapter1start")
    call screen chapter_title("Chapter 1: Opening")
    call chap1
    scene blank
    jump chapter2start

label chapter2start:
    python:
        mark_checkpoint_visited("chapter2start")
    call screen chapter_title("Chapter 2: Catective")
    call chap2pro
    if game_over == False:
        call chap2d1
        call chap2d2
        call chap2d3
    scene blank
    jump chapter3start

label chapter3start:
    python:
        mark_checkpoint_visited("chapter3start")
    call screen chapter_title("Chapter 3: Cat Warehouse")
    call chap3
    scene blank
    jump chapter4start

label chapter4start:
    python:
        mark_checkpoint_visited("chapter4start")
    call screen chapter_title("Chapter 4")
    call Chap4
    scene blank
    jump chapter5start

label chapter5start:
    python:
        mark_checkpoint_visited("chapter5start")
    call screen chapter_title("Chapter 5")
    call chap5
    scene blank
    jump endingstart

label endingstart:
    # python:
    #     persistent.completed_chapters[1] = True
    #     persistent.completed_chapters[2] = False
    #     persistent.completed_chapters[3] = False
    #     persistent.completed_chapters[4] = False
    #     persistent.completed_chapters[5] = False
    if completed_all():
        call ending
    else:
        call screen final_screen("The Final Chapter")
    return
