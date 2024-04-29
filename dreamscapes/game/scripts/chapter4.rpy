# definitions
define n = Character("Narrator")
define pawzza = Character("Pawzza")
define carl = Character("Carl")
image alley_way = "images/ch4 bgs/alley_way.jpeg"
image city_streets = "images/ch4 bgs/city_street.jpeg"
image quiet_park = "images/ch4 bgs/park.jpeg"
image busy_supermarket = "images/ch4 bgs/supermarket.png"


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

# Alley search
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

# City venture interaction
label venture_city:
    scene city_streets
    show pawzza at center
    pawzza "Let's hit the streets and see what adventures await me!"

    menu:
        "Explore the quiet park.":
            pawzza "I think I'll check out that quiet park."
            return
        "Enter the busy supermarket.":
            pawzza "The supermarket seems like a good place to find food."
            return

