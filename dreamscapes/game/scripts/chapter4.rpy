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

    carl "Hey, you woke me up!"
    pawzza "I'm sorry, I'm just starved and don't know what to do."
    # Continue the storyline for searching in the alley...
    return

label venture_city:
    scene city_streets

    pawzza "I decided to brave the busy city streets in search of food."
    # Continue the storyline for venturing into the city...
    return

