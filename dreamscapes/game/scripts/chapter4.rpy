define pawzza = Character("pawzza")
define carl = Character("carl")

label chap4:
    "We're in chapter 4!!"
    scene alley_way

    show pawzza at center
    pawzza "Here I am, in an unfamiliar alley, curious, hungry, and all alone."
    pause 2.0 
    hide pawzza

    menu:
        "Search for food in the alley.": 
            call search_alley  

        "Venture out into the city.":  
            call venture_city  
    return

label search_alley:
    scene alley_way
    show carl 
    carl "Hey, you woke me up!"
    hide carl

    show pawzza 
    pawzza "I'm so so sorry, I'm just starved and I really don't know what to do."
    # Continue the storyline for searching in the alley...
    return

label venture_city:
    scene city_streets

    show pawzza
    pawzza "Let's hits the streets and see what adventures await me!"
    # Continue the storyline for venturing into the city...
    return

