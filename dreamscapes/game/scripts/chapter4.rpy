define pawzza = Character("Pawzza")
define carl = Character("Carl")

label start:

    scene alley_way
    "It's a cold night in Meow York. Pawzza, a bright white cat with blue eyes, has been separated from her owner and is all alone for the first time in her life."

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
    show carl
    carl "Hey, you woke me up!"
    hide carl

    show pawzza
    pawzza "AHHHHHHHHHHHHHHH!!!!!!!!!!!!!"

    show carl
    carl "Quiet down, little one. I just woke up."
    pawzza "I didn't even see you in there!"

    carl "It seems you are new here. I can show you around if you want."
    pawzza "Please, I could really use some help."

    carl "Alright, follow me. Let's find something to eat first."
    hide pawzza
    hide carl
    jump explore_park

label venture_city:
    scene city_streets
    show pawzza at center
    pawzza "Let's hit the streets and see what adventures await me!"

    menu:
        "Explore the quiet park.":
            jump explore_park
        "Enter the busy supermarket.":
            jump explore_supermarket

