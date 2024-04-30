# definitions
define n = Character("Narrator")
define guard = Character("Guard")
define pawzza = Character("Pawzza")
define carl = Character("Carl")
define old_lady = Character("Old lady")
image alley_way = "images/ch4 bgs/alley_way.jpeg"
image city_streets = "images/ch4 bgs/city_street.jpeg"
image quiet_park = "images/ch4 bgs/park.jpeg"
image busy_supermarket = "images/ch4 bgs/supermarket.png"
image old_house = im.Scale("images/ch4 bgs/old_house", 1920, 1080)

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
            n "Pawzza digs into the trash and pulls out a half-eaten sandwich, which he devours hungrily."
            return

        "Beg an old lady.":
            n "An old woman sits on a bench, feeding pigeons."
            pawzza "Let's try my luck with her."
            jump beg_lady

label enter_supermarket:
    scene busy_supermarket
    show pawzza at center
    pawzza "So many smells and so much food!"
    n "Pawzza sneaks towards the meat aisle and snatches a sausage link."
    n "As he turns to leave, a security guard spots him."
    guard "Hey! No animals allowed here!"
    pawzza "Meow! Meow! (I better run!)"
    return

label beg_lady:
    scene quiet_park
    show pawzza at right
    show Glenda at left
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
    return

    



