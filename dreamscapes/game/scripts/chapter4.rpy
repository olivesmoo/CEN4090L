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
    show pawzza at center
    pawzza "Let's hit the streets and see what adventures await me!"
    menu:
        "Explore the quiet park.":
            call explore_park
        "Enter the busy supermarket.":
            call explore_supermarket

label explore_park:
    scene park
    show pawzza at center
    pawzza "This park seems peaceful, maybe I can find something to eat here."
    menu:
        "Go to the pond.":
            call pond_adventure
        "Climb up a tree.":
            call tree_climb

label pond_adventure:
    scene pond
    show pawzza at center
    pawzza "Look at those ducks! I hope there's no trouble here."
    # Outcome with dog chase described here
    return

label tree_climb:
    scene tree
    show pawzza at center
    pawzza "A bird's nest! There's my meal."
    # Outcome with finding eggs described here
    return

label explore_supermarket:
    scene supermarket
    show pawzza at center
    pawzza "I need to be sneaky in here."
    menu:
        "Try to steal a fish.":
            call steal_fish
        "Beg a human for food.":
            call beg_human

label steal_fish:
    # Outcome of successful fish theft
    return

label beg_human:
    # Outcome of being caught
    return

# Add additional labels and scenes as necessary for the interactions with the street performers or the wise old cat.


