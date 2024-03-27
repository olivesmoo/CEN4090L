define pawzza = Character("pawzza")
define carl = Character("carl")

label chap4:
    "We're in chapter 4!!"
    
    scene alley_way
    with fade

    pawzza "Here I am, in an unfamiliar alley, curious, hungry, and all alone."
    show pawzza at center
    pause 2.0 
    hide pawzza
    with fade

    menu:
        "What should I do?":
            "Search for food in the alley.":
                jump search_alley

            "Venture out into the city.":
                jump venture_city

    label search_alley:
    scene alley_way
    with fade

    carl "Hey, you woke me up!"
    pawzza "I'm sorry, I'm just starved and don't know what to do."
    # Continue the storyline for searching in the alley...

label venture_city:
    scene city_streets
    with fade

    pawzza "I decided to brave the busy city streets in search of food."
    # Continue the storyline for venturing into the city...


    return

