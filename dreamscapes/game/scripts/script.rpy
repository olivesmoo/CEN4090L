$ renpy.include("globals.rpy")

# Define a dictionary to store the visited status of checkpoints
init python:
    if not persistent.visited_checkpoints:
        persistent.visited_checkpoints = {}

    current_checkpoint = 'start'

    # Function to mark a checkpoint as visited
    def mark_checkpoint_visited(checkpoint_label):
        persistent.visited_checkpoints[checkpoint_label] = True

    # Function to check if a checkpoint has been visited
    def is_checkpoint_visited(checkpoint_label):
        return persistent.visited_checkpoints.get(checkpoint_label, False)

# The game starts here.
label start:
    if current_checkpoint == 'start':
        "Welcome to the dream world."
        $ player_name = renpy.input("What is your name?")
        $ player_name = player_name.strip()

        if player_name == "":
            $ player_name="Nameless One"

        e "Pleased to meet you, %(player_name)s!"
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
        
label chapter1start:
    python:
        mark_checkpoint_visited("chapter1start")
    call screen chapter_title("Chapter 1: Cat Lab")
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
    call screen chapter_title("Chapter 3")
    call chap3
    scene blank
    jump chapter4start

label chapter4start:
    python:
        mark_checkpoint_visited("chapter4start")
    call screen chapter_title("Chapter 4")
    call chap4
    scene blank
    jump chapter5start

label chapter5start:
    python:
        mark_checkpoint_visited("chapter5start")
    call screen chapter_title("Chapter 5")
    call chap5
    return
