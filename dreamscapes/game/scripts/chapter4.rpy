# definitions
define pawzza = Character("Pawzza")
define carl = Character("Carl")
image alley_way = "alley_way.png"
image city_streets = "city_street.png"
image quiet_park = "park.jpeg" 
image busy_supermarket = "supermarket.jpeg" 

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

    show carl at left
    carl "Quiet down, little one. I just woke up."
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
            jump explore_park
        "Enter the busy supermarket.":
            jump explore_supermarket

    return

