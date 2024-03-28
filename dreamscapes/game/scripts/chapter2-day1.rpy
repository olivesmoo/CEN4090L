define c = Character("Catective")
define r = Character("Radio")
define d = Character("DJ")
define m = Character("Mystery")

label chap2d1:
    "We're in chapter 2!!"

    show bg_test
    "A few days later, the Catective, sober but not spirited, lounges in a worn yet well-loved armchair. His figure is shadowed by the weak rays of sunlight scattered by the patchy grey overcast."
    "For the most part, the room was empty aside from a few house plants are scattered throughout the eerily quiet office, having long since seen better days if the droop of their yellowing leaves was anything to go by."
    "The cracked charcoal walls, though less than minimalist, held a sole piece of decoration: an old cracked frame of the catective and an orange, jacketed figure."

    show detective_cat
    c "(It won’t be long now until my lease is up. Then, I can finally get rid of this good for nothing detective business…)"
    c "(Has it really been three years since I’ve taken a case? Sure, clients have come and gone, but I’ve refused. How long has it been since I’ve worked with him?)"

    "To distract himself with this rather depressing line of questioning, the Catective fiddles with the radio to pass the time."

    r "Buy new makeup products! Sponsored by celebrity, fashion model, influencer Mak-"
    r "The latest on a series of kidnappings throughout Downtown Mew Paris-"
    r "FAMOUS FOOTBALL PLAYER FOUND DEAD IN-"

    "Sighing, the Catective lays his head in his paws."

    c "Things will never be the same. Only three more days, then I’ll be done for good."

    m "You’ve got to be kidding me…"

    c "...!"

    m "I did not walk all the way here for you to say that."

    c "Wait...that voice...are you...?!"

    m "Oh, you really can’t make this shit up, can you?"

    hide detective_cat

    show cat_wig

    "Mouth agape, the mysterious voice led to none other than the DJ from the other night that the Catective spilled milk on."
    "First impressions are certainly nothing to cry about, least of all over spilled milk, but this may be the cream of the crop as one of the worst ever."
    "Paws clenched and unclenched on the sleeve of her vibrant blue jacket, tension obvious as she set her mouth in a slight grimace. The thick silence in the room is finally broken by a weary sigh."

    d "Before I ask you something, I want to apologize for bumping into you the other night. It wasn’t cool, how I reacted and all, and I hope we can let bygones be bygones."

    # Decision Tree Maybe

    c "...Thank you. But I bumped into you and spilled milk on you. So I’m sorry as well."

    "The DJ gives a curt nod in acknowledgment. Her body is curled in on itself like a spring, as if at any moment she could burst into a shock of barely contained anxious energy."

    d "Are you really…a catective, officer?"

    c "...I am, yes. But I no longer take cases as of 3 years ago."
    
    d "...!"

    c "I’m really sorry, but I’m going to have to refuse your case-"

    d "But you can’t! I really don’t have any other options! All other catectives have refused me and you’re my only chance at proving my innocence!"

    c "Proving your innocence?!"

    d "Please, let me explain! You’ve got to believe me!"

    "The DJ’s eyes are shining with equal parts frustration, desperation, and indignation."

    # Decision Tree

    c "...I’ll hear you out. What’s your story?"

    d "Alright, so…I was framed for a murder."
    d "The night you bumped into me was the same night my boyfriend, Orion, broke up with me. Totally switched up on me, snapping and raging like you wouldn’t believe."
    d "I had a shift the next day at a gig he got for me at one of the most popular clubs in Mew Paris, Le Astra Electrique, so despite everything I still had to show up for work since they wouldn’t be able to find a replacement in time."
    d "Orion showed up, we got into a fight, and I pushed him. His back hit the corner of the bar and he collapsed.He said he was fine, but he all but disappeared that day. No one’s seen him. So now the press is saying I’ve murdered him."

    "The silence in the room is palpable as the tortie holds her breath in anticipation, looking for a response from the catective."
    "The catective can feel the gears in his mind turning like familiar clockwork, though rusted from years of disuse and milk. He stops himself before it can get very far."

    c "Look…I’m really sorry to hear this happened to you. But you don’t want me as your detective. I haven’t taken a case in three years and I don’t plan to anytime soon."
    c "I’m not going to be able to solve this for you, so you’re just going to have to plead guilty in court to reduce your sentence."

    d "..."

    c "..."

    d "...My brother was wrong about you."

    c "...?"

    d "My brother used to look up to you. Said you were a real Purrlock Holmes, wicked smart and always looking out for the little guys, no matter how tough the case to crack was."
    d "So tell me, officer, was he wrong? Or are you just looking out for yourself? Your reputation to keep?"


    hide cat_wig
    show detective_cat_angry
    c "If your brother knows so much about ME and MY BUSINESS then why isn’t he here pleading your case with you?"

    d "...!"
    d "..."

    "The office is suddenly quiet with tense breathing."

    hide detective_cat_angry
    show detective_cat_worried
    c "Ah…I’m sorry I didn’t-"

    d "No. I’ve heard enough. Clearly, you’re no better than the rest of the police in this awful city. If you really won’t hear my case, then I’ll get out of your hair. Good day, officer."

    c "..."

    # Decision Tree?

    "The DJ slowly makes her way to the door. You can’t help but notice her paws trembling ever so slightly."

    c "...Wait!"

    "Paw on the door, the DJ slowly turns towards the Catective, mixed feelings of trepidation and cautious curiosity flit through her features."

    c "That was out of line. I'm sorry...I've made up my mind."

    "The DJ's head is downturned, and she refuses to make eye contact."

    d "And?"

    c "I’ll be taking your case. I can’t promise any results or even solving the damn thing but-"

    "With a hushed gasp from the DJ, the Catective falls silent."

    d "Are you for real?"

    c "Yes, for real."

    "The DJ is quiet for a moment before finally looking up. Tears prick at the corners of her eyes and a small smile lights up her face, as if the melancholic weight on her shoulders had eased, if only a bit"

    d "Thank you, Catective. Thank you, thank you, thank you, truly."

    c "It’s, uh, no problem. Really."

    "Taking a moment to compose herself, the DJ seems to transform right before the Catective’s very eyes. Eyes blazing like a rekindled flame, she stands straighter, more sure of herself. She suddenly claps her paws."

    d "Since we’ll be working together on this, I think a proper introduction is long overdue!"
    d "Say, I know you, Catective %(player_name)s Mullen, the Cat Can-Opener that won’t stop until a case is solved. So, allow me to introduce myself!"
    d "My name is Artemis Marguerite, but you can call me Arty!"

    c "Well, hello Arty, but how do you know all that about me??"

    d "I wasn’t joking when I said my brother was a big fan."

    "She offers a sad smile before shaking her head to clear her thoughts."

    d "Anyways, my brother would always tell me these detective stories as a kid. You need to investigate the scene of the murder first, right? Gather clues and evidence, all that jazz?"
    d "I’ll send you the address of the nightclub, but I’ll meet you outside when you're ready!"

    "Arty promptly runs off, striding confidently, self-assured. Meanwhile, the detective looks on at where she had been sitting, mind desperately trying to grasp the information overload of the past few minutes."
    "Sighing heavily, he slides off his armchair, missing its comforting familiarity immediately."

    c "Kids these days…what have I gotten myself into?"

    return