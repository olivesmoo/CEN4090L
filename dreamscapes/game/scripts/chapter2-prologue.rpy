define c = Character("Catective")
define d = Character("DJ")

label chap2pro:
    "We're in chapter 2!!"

    scene bg_test # shows background

    "The low caw of a raven settles over the dying glow of the city of Saint-Saens, a small town just outside of the borders of Mew-Paris." 
    "On the edge of town, an unassuming establishment, no more unique than the other cracked cobblestone buildings along the long-since abandoned streets, houses the favored drinking spot of melancholic veterans." 
    "The dimly lit bar of Le Chevalier Déchu gives way to the seemingly perpetual smoky haze of the room, hiding the wear and tear cracks underneath." 
    "Pinpricks of light glimmer like flecks of fool's gold on the low ceiling above, lighting the way for a weary traveler’s demise poorly disguised as respite." 
    "On a lone seat at the corner of the bar furthest from the swaying crowd, an older, grizzled grey tabby cat takes a swig of his sixth glass of milk for the evening."

    show detective_cat
    c "I can't believe they wouldn't let me get a seventh. Don't they know the seventh time's the charm…"
    hide detective_cat

    show cat_wig # shows character
    d "We're only allowed to serve milk to “functioning” customers geezer…"
    hide cat_wig

    show detective_cat_angry
    c "What was that? I'm only 6 years old and counting!"
    hide detective_cat_angry

    show cat_wig
    d "..."
    hide cat_wig

    show detective_cat
    c "(I suppose it is getting late. I should probably head home for the night…)"
    hide detective_cat

    "Catective reluctantly slides off his stool, still nursing his last glass of milk, before taking a heavy step toward the exit." 
    "The room sways and the Catective's body pitches forward, bumping into a smaller figure."
    "Bouncing back as if electrocuted, the jacketed tortoiseshell cat looks on with thinly veiled contempt, hair standing on end, milk splashed all over her dark shirt."

    show cat_wig
    d "You can't be serious right now..."
    hide cat_wig

    show detective_cat_worried
    c "Oh...Oh I'm so so-"
    hide detective_cat_worried

    show cat_wig
    d "Look man… I've had a long shift and an even longer night. I'm not feeling it right now, so can you please move aside so that I can leave?"

    menu drunk:
        show cat_wig
        "Even through the muddled haze that is your mind, you can't help but notice the strain in her voice and the droop of her shoulders, as if she is holding the weight of the world and trying not to crumble under its pressure."
        "Of course ma'am. Sorry again.":
            call sorry
        "How about no? I'm an officer of the law and I demand respect!!":
            call law
        "Umm… Are you going to pay for that?":
            call pay
        "I'm sorry, do you work here?":
            call question
    return
        
label sorry:
    d "It's… alright. Honestly. You didn't mean to. Have a good rest of your night… officer."
    hide cat_wig

    "The DJ promptly hurries out. The Catective forlornly looks at his now empty glass fallen on the floor."

    show cat_wig
    d "Are you going to pay for that?"
    hide cat_wig

    show detective_cat_sad
    "The Catective makes a disgruntled sound before coughing up a crumpled 5 dollar bill. Sobered from a weeping wallet, the Catective hobbles home and collapses upon an unmade bed, lapsing into a dreamless slumber."
    hide detective_cat_sad

    return

label law:
    d "..."
    hide cat_wig

    show detective_cat_angry
    c "Yeah, I said it! I could arrest you right now, little lady!"
    hide detective_cat_angry

    show cat_wig
    d "Damn. F*** the police, and f*** this sh*t."
    hide cat_wig

    "*Cue Pokemon battle but for now he loses sadly*"

    show cat_wig
    d "Not so hot sh*t now, huh “officer”? Have a good f****** night, d*** head."
    hide cat_wig

    "The DJ promptly hurries out, head held high as the crowd parts for her after the decidedly one-sided brawl. The Catective, pride decimated, literally melts into a puddle and dies of embarrassment, broken and defeated by a kitten a third of his size."

    "Game Over :("

    $ game_over = True
    return

label pay:
    d "...Be so f******* for real right now."

    "The DJ has a dangerous glint in her eyes, sparking electric over her sunglasses. It wouldn’t take a genius to see that she's very obviously displeased by this."
    "Her cool glare screams “Are you really that desperate for money?” It reminds you of…well…you promised yourself you wouldn't think of him..."

    hide cat_wig
    jump drunk

label question:
    "Yes, I play the music in this less than fine establishment. I also would like to go home if you would please move? You’re blocking the one exit here."
    hide cat_wig

    show detective_cat
    "(That explains the headphones and… unique costume. Isn’t it a fire hazard to only have one exit here?)"
    hide detective_cat

    jump drunk
