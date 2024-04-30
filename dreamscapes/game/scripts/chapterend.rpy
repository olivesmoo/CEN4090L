define user = Character(persistent.player_name)
label ending:
    "ring-ring-ring... ring-ring-ring... ring-ring-ring..."
    "ring-ring-ring... ring-ring-ring... ring-ring-ring..."
    user "Ugh... what now???"
    # show background
    scene city_bg:
        zoom 0.3
        xalign 0.5

    user "Oh hey... it looks like I finally made it back home!"
    "BOOM..." with hpunch
    "BOOM..." with vpunch
    "BOOM..." with hpunch

    scene city_bg2:
        zoom 0.3
        xalign 0.5
    user "w-w-w-what... is that?"

    "BOOM..." with hpunch
    "BOOM..." with vpunch

    scene city_bg3:
        zoom 0.3
        xalign 0.5

    user "oh crap... IT'S COMING CLOSER!!"

    "BOOM..." with hpunch
    "BOOM..." with vpunch

    scene city_bg4:
        zoom 0.3
        xalign 0.5
    user "AHHHHHHH!!!!!!"

    scene blank

    "ring-ring-ring... ring-ring-ring... ring-ring-ring..."

    scene bedroom:
        zoom 0.4
        xalign 0.5
    user "oh.... it was a dream?"
    return
