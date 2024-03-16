define e = Character("Cat")
define f = Character("Catective")

label chapter1start:
    "We're in chapter 1!!"
    scene bg_test # shows background

    show cat_wig # shows character

    e "Muahahahaha"

    e "I have taken over the world!!!!"
    menu:
        "yes":
            call yes # could also do jump
        "no":
            call nah
    return
    
label yes:
    hide cat_wig

    show detective_cat
    f "eh?"
    return

label nah:
    e "lol just a joke bruh"
    return
