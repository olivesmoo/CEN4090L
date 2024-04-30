# definitions
define n = Character("Narrator")
define guard = Character("Guard")
define pawzza = Character("Pawzza")
define enemy = Character("Mikey")
define carl = Character("Carl")
define fightbub = Character("fightbub")
define old_lady = Character("Old lady")
image alley_way = "images/ch4 bgs/alley_way.jpeg"
image city_streets = "images/ch4 bgs/city_street.jpeg"
image quiet_park = "images/ch4 bgs/park.jpeg"
image pound = "images/ch4 bgs/pound.jpeg"
image busy_supermarket = "images/ch4 bgs/supermarket.png"
image old_house = im.Scale("images/ch4 bgs/old_house.jpeg", 1920, 1080)
image park_trash = im.Scale("images/ch4 bgs/park_trash.jpeg", 1920, 1080)
image aisle = im.Scale("images/ch4 bgs/aisle.jpeg", 1920, 1080)
image night_streets = im.Scale("images/ch4 bgs/night_streets.jpeg", 1920, 1080)

label Chap4:
    scene alley_way
    show pawzza at center
    pawzza "How did this happen?! I was just with her, and now she's gone, and I can't remember a thing."
    pawzza "Oh no, I'm starved. What should I do?"

    menu:
        "Search for food in the alley.":
            jump search_alley
        "Venture out into the city.":
            jump venture_city

label search_alley:
    scene alley_way
    show carl at left
    carl "Hey, you woke me up!"
    hide carl

    show pawzza at center
    pawzza "AHHHHHHHHHHHHHHH!!!!!!!!!!!!!"
    hide pawzza

    show carl at left
    carl "Quiet down, little one. I just woke up."
    show pawzza at right
    pawzza "I didn't even see you in there!"

    carl "It seems you are new here. I can show you around if you want."
    pawzza "Please, I could really use some help."

    carl "Alright, follow me. Let's find something to eat first."
    hide pawzza
    hide carl
    jump food_search

label food_search:
    scene city_streets
    show pawzza at center
    show carl at left
    n "Carl leads Pawzza through the bustling city streets. As they turn a corner, they spot a street vendor leaving behind some leftovers."
    carl "Look there, Pawzza! What should we go for?"
    
    menu:
        "Fish from the seafood stall.":
            jump food_choice
        "Burger from the fast food bin.":
            jump food_choice
        
label food_choice: 
    scene city_streets
    show pawzza at center 
    show carl at left
    carl "That was a good choice! now c'mon, there's something i need help with...."
    n "Pawzza looks at carl confused but runs to follow him"
    jump walk_streets

label walk_streets: 
    scene city_streets
    show pawzza at right
    show carl at center
    carl "As we walk these streets, I need to tell you about someone... my arch enemy. He's been making life tough for a lot of us here."
    pawzza "What's going on?"
    carl "He's a troublemaker, always stirring up chaos. I might need to confront him soon."
    menu:
        "Stand with Carl and confront the troublemaker.":
            jump fight
        "Decide it's too risky and suggest avoiding the conflict.":
            jump noFight

label fight:
    scene alley_way
    show carl at center
    show pawzza at right
    n "Carl and Pawzza stand firm, ready to confront the troublemaker head-on."
    carl "This ends today! We're not letting you push us around anymore!"
    hide carl
    hide pawzza
    show enemy 
    enemy "Alright lets do this!!!!!!"
    hide enemy
    show fightbub
    n "The confrontation is intense..." 
    hide fightbub
    show pawzza
    show carl
    n "Carl's courage inspires Pawzza, and together, they manage to send the troublemaker running."
    jump winning

label noFight:
    scene alley_way
    show carl at center
    show pawzza at right
    pawzza "I think it's too risky to confront him. We should find another way."
    carl "I understand your concern, but I have to do this. Take care of yourself."
    jump pawzzaAlone

label pawzzaAlone:
    scene night_streets
    show pawzza 
    n "Pawzza decides it's too risky to join the confrontation and leaves. As he walks the lonely city streets, he can't shake off the guilt, wondering if Carl made it out okay."
    n "For the rest of his life, Pawzza remains haunted by that decision, always looking over his shoulder, never truly finding peace."
    python: 
        chapter_success(1, False)
    return


label winning: 
    # they beat the dog and are now the kings of the city 
    python: 
        chapter_success(1, True)
    return

label venture_city:
    scene city_streets
    show pawzza at center
    pawzza "Let's hit the streets and see what adventures await me!"

    menu:
        "Explore the quiet park.":
            jump explore_park
        "Enter the busy supermarket.":
            jump enter_supermarket

label explore_park:
    scene quiet_park
    show pawzza at center
    pawzza "This park is so peaceful compared to the noisy streets."

    menu:
        "Go through trash.":
            pawzza "Maybe I can find something to eat in this trash can."
            jump park_trash 

        "Beg an old lady.":
            n "An old woman sits on a bench, feeding pigeons."
            pawzza "Let's try my luck with her."
            jump beg_lady

label park_trash:
    scene park_trash
    show pawzza
    n "Pawzza digs into the trash and pulls out a half-eaten sandwich, which he devours hungrily."
    n "As Pawzza licks the last crumbs from his mouth, he looks around the empty park, the dim streetlights casting long shadows."
    n "With no home to return to and no one to guide him, a cold realization washes over him."
    n "In the vast, indifferent city, he's utterly alone."
    n "And perhaps, he always will be."
python:
    chapter_success(1, False)
return

label beg_lady:
    scene quiet_park
    show pawzza at right
    show old_lady at left
    pawzza "Meow! Meow!"
    n "The old lady, Glenda, notices Pawzza and tosses him a piece of chicken. She's completley smitten with this kitten!"
    old_lady "You're so precious I might just have to take you home!"
    n "Pawzza looks up at the Glenda and nuzzles into her legs, attempting to seal the deal. The old lady leans down and picks her up..."
    jump lady_house

label lady_house: 
    scene old_house
    show pawzza at left 
    pawzza "she must be keeping me if im here..."
    n "Pawzza looks to the left and there is a small cat bed with food, he looks around but there's no cat."
    pawzza "what is happening? why does she have all this if ther's no other cat here"
    show old_lady at right
    n "The old lady bends down and turns to Pawzza and opens her mouth to say.. "
    old_lady  "I lost my gorgeous Carl days ago "
    n "pawzza lets out a confused meow"
    old_lady "Now I have you..... Pawzza!!"
    old_lady "I cant wait for the adventures that await us!"
    python:
        chapter_success(1, True)
    return

label enter_supermarket:
    scene busy_supermarket
    show pawzza at center
    pawzza "So many smells and so much food!"
    n "Pawzza sneaks towards the meat aisle and snatches a sausage link."
    n "As he turns to leave, a security guard spots him."
    hide pawzza 
    hide guard
    show pawzza at right
    show guard at left
    guard "Hey! No animals allowed here!"
    pawzza "I better run!"
    jump chase

label chase: 
    scene aisle
    show pawzza  
    n "The guard chases Pawzza through the aisles, but Pawzza is too quick and nearly escapes."
    hide pawzza 
    show guard 
    guard "Wait, little guy, you need help!"
    n "The guard, feeling concerned for Pawzza, calls animal control."
    hide guard
    show pawzza at right 
    show guard at left
    n "Animal control arrives quickly and gently captures Pawzza, taking him to the local animal shelter."
    jump pound

label pound: 
    scene pound
    show pawzza
    n "At the shelter, Pawzza finds a temporary home with the promise of a future forever home."
    pawzza "This is AWFUL!"
    python:
        chapter_success(1, False)
    return

    



