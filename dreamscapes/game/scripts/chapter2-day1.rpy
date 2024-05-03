define r = Character("Radio")
define a = Character("Arty")
define mystery = Character("Mystery")
define bouncer = Character("Bouncer")
define p = persistent.player_name
image Office = im.Scale("images/ch2 bgs/Office.png", 1920, 1080)
image MewParisDay = im.Scale("images/ch2 bgs/MewParisDay.png", 1920, 1080)
image NightClub = im.Scale("images/ch2 bgs/NightClub.png", 1920, 1080)
image Bloodstain = im.Scale("images/ch2 bgs/bloodstain.jpg", 1920, 1080)
image Ladder = im.Scale("images/ch2 bgs/ladder.jpg", 1920, 1080)
image Cream = im.Scale("images/ch2 bgs/cream.jpg", 1920, 1080)
image DJBooth = im.Scale("images/ch2 bgs/djbooth.jpg", 1920, 1080)
image BigBang = im.Scale("images/ch2 bgs/epiphany.jpg", 1920, 1080)
image Fire = im.Scale("images/ch2 bgs/fire.jpg", 1920, 1080)

label chap2d1:
    scene black

    "Day 1 Investigation"

    scene Office
    "A few days later, the Catective, sober but not spirited, lounges in a worn yet well-loved armchair. His figure is shadowed by the weak rays of sunlight scattered by the patchy grey overcast."
    "For the most part, the room was empty aside from a few house plants are scattered throughout the eerily quiet office, having long since seen better days if the droop of their yellowing leaves was anything to go by."
    "The cracked charcoal walls, though less than minimalist, held a sole piece of decoration: an old cracked frame of the Catective and an orange, black jacketed figure."

    show detective_cat
    f "(It won’t be long now until my lease is up. Then, I can finally get rid of this good for nothing detective business…)"
    f "(Has it really been three years since I’ve taken a case? Sure, clients have come and gone, but I’ve refused. How long has it been since I’ve worked with him?)"

    "To distract himself with this rather depressing line of questioning, the Catective fiddles with the radio to pass the time."

    r "Buy new makeup products! Sponsored by celebrity, fashion model, influencer Mak-"
    r "The latest on a series of kidnappings throughout Downtown Mew Paris-"
    r "FAMOUS FOOTBALL PLAYER FOUND DEAD IN-"

    "Sighing, the Catective lays his head in his paws."

    f "Things will never be the same. Only three more days, then I’ll be done for good."

    mystery "You’ve got to be kidding me…"

    f "...!"

    mystery "I did not walk all the way here for you to say that."

    f "Wait...that voice...are you...?!"

    mystery "Oh, you really can’t make this shit up, can you?"

    hide detective_cat

    show arty_worried
    "Mouth agape, the mysterious voice led to none other than the DJ from the other night that the Catective spilled milk on."
    "First impressions are certainly nothing to cry about, least of all over spilled milk, but this may be the cream of the crop as one of the worst ever."
    "Paws clenched and unclenched on the sleeve of her vibrant blue jacket, tension obvious as she set her mouth in a slight grimace. The thick silence in the room is finally broken by a weary sigh."
    d "Before I ask you something, I want to apologize for bumping into you the other night. It wasn’t cool, how I reacted and all, and I hope we can let bygones be bygones."
    hide arty_worried

    # Decision Tree Maybe

    show detective_cat_worried
    f "...Thank you. But I bumped into you and spilled milk on you. So I’m sorry as well."
    hide detective_cat_worried

    show arty_worried
    "The DJ gives a curt nod in acknowledgment. Her body is curled in on itself like a spring, as if at any moment she could burst into a shock of barely contained anxious energy."
    d "Are you really…a Catective, officer?"
    hide arty_worried

    show detective_cat_worried
    f "...I am, yes. But I no longer take cases as of 3 years ago."
    d "...!"
    f "I’m really sorry, but I’m going to have to refuse your case-"
    hide detective_cat_worried

    show arty_sad
    d "But you can’t! I really don’t have any other options! All other Catectives have refused me and you’re my only chance at proving my innocence!"
    hide arty_sad

    show detective_cat_worried
    f "Proving your innocence?!"
    hide detective_cat_worried

    show arty_sad
    d "Please, let me explain! You’ve got to believe me!"
    "The DJ’s eyes are shining with equal parts frustration, desperation, and indignation."
    hide arty_sad

    # Decision Tree

    show detective_cat_sad
    f "...I’ll hear you out. What’s your story?"
    hide detective_cat_sad

    show arty_worried
    d "Alright, so…I was framed for a murder."
    d "The night you bumped into me was the same night my boyfriend, Orion, broke up with me. Totally switched up on me, snapping and raging like you wouldn’t believe."
    d "I had a shift the next day at a gig he got for me at one of the most popular clubs in Mew Paris, Le Astra Electrique, so despite everything I still had to show up for work since they wouldn’t be able to find a replacement in time."
    d "Orion showed up, we got into a fight, and I pushed him. His back hit the corner of the bar and he collapsed. He said he was fine, but he all but disappeared that day. No one’s seen him. So now the press is saying I’ve murdered him."
    "The silence in the room is palpable as the tortie holds her breath in anticipation, looking for a response from the Catective."
    "The Catective can feel the gears in his mind turning like familiar clockwork, though rusted from years of disuse and milk. He stops himself before it can get very far."
    hide arty_worried

    show detective_cat_worried
    f "Look…I’m really sorry to hear this happened to you. But you don’t want me as your detective. I haven’t taken a case in three years and I don’t plan to anytime soon."
    f "I’m not going to be able to solve this for you, so you’re just going to have to plead guilty in court to reduce your sentence."
    d "..."
    f "..."
    hide detective_cat_worried

    show arty_neutral
    d "...My brother was wrong about you."
    f "...?"
    d "My brother used to look up to you. Said you were a real Purrlock Holmes, wicked smart and always looking out for the little guys, no matter how tough the case to crack was."
    d "So tell me, officer, was he wrong? Or are you just looking out for yourself? Your reputation to keep?"
    hide arty_neutral

    show detective_cat_angry
    f "If your brother knows so much about ME and MY BUSINESS then why isn’t he here pleading your case with you?"
    hide detective_cat_angry

    show arty_neutral
    d "...!"
    hide arty_neutral
    show arty_sad
    d "..."
    hide arty_sad

    show detective_cat_sad
    "The office is suddenly quiet with tense breathing."
    f "Ah…I’m sorry I didn’t-"
    hide detective_cat_sad

    show arty_neutral
    d "No. I’ve heard enough. Clearly, you’re no better than the rest of the police in this awful city. If you really won’t hear my case, then I’ll get out of your hair. Good day, officer."
    f "..."

    # Decision Tree?

    "The DJ slowly makes her way to the door. You can’t help but notice her paws trembling ever so slightly."
    hide arty_neutral

    f "...Wait!"
    
    show arty_sad
    "Paw on the door, the DJ slowly turns towards the Catective, mixed feelings of trepidation and cautious curiosity flit through her features."

    f "That was out of line. I'm sorry...I've made up my mind."

    "The DJ's head is downturned, and she refuses to make eye contact."

    d "And?"

    f "I’ll be taking your case. I can’t promise any results or even solving the damn thing but-"

    "With a hushed gasp from the DJ, the Catective falls silent."

    d "Are you for real?"

    f "Yes, for real."

    hide arty_sad
    show arty_happy
    "The DJ is quiet for a moment before finally looking up. Tears prick at the corners of her eyes and a small smile lights up her face, as if the melancholic weight on her shoulders had eased, if only a bit"

    d "Thank you, Catective. Thank you, thank you, thank you, truly."

    f "It’s, uh, no problem. Really."

    "Taking a moment to compose herself, the DJ seems to transform right before the Catective’s very eyes. Eyes blazing like a rekindled flame, she stands straighter, more sure of herself. She suddenly claps her paws."

    d "Since we’ll be working together on this, I think a proper introduction is long overdue!"
    d "Say, I know you, Catective [p] Mullen, the Cat Can-Opener that won’t stop until a case is solved. So, allow me to introduce myself!"
    d "My name is Artemis Marguerite, but you can call me Arty!"
    hide arty_happy

    show detective_cat_worried
    f "Well, hello Arty, but how do you know all that about me??"
    hide detective_cat_worried

    show arty_happy
    a "I wasn’t joking when I said my brother was a big fan."
    "She offers a sad smile before shaking her head to clear her thoughts."
    a "Anyways, my brother would always tell me these detective stories as a kid. You need to investigate the scene of the murder first, right? Gather clues and evidence, all that jazz?"
    a "I’ll send you the address of the nightclub, but I’ll meet you outside when you're ready!"
    hide arty_happy
    "Arty promptly runs off, striding confidently, self-assured. Meanwhile, the detective looks on at where she had been sitting, mind desperately trying to grasp the information overload of the past few minutes."
    "Sighing heavily, he slides off his armchair, missing its comforting familiarity immediately."

    f "Kids these days…what have I gotten myself into?"

    scene MewParisDay

    "A neon-lit sign glows weakly in the overbearing light of the afternoon sun. Stanchions line the entrance to the nightclub, like little toy soldiers protecting the crowds from the otherwise bustling streets of Mew Paris." 
    "Now vacated, the stanchions stand against the Mew Parisian crowd, as if protecting civilians from the tragedy inside."

    show detective_cat
    f "Le Astra Electrique…"
    hide detective_cat

    show arty_neutral
    a "This is the place."
    hide arty_neutral

    scene NightClub
    "Nudging the caution tape on the door aside, the Catective slowly walks inside and blinks, taking in the sudden darkness. Eerily quiet, the steps from the doorway led out into a wide room, cleared of its usual crowds of cats."
    "As if on a pedestal, the DJ’s booth looms over the space, towering above as if overseeing an abandoned kingdom."
    "Directly below the pedestal, was the taped outline of a body. The stark white tape was like a beacon in the low-lit room, and the blood stains on the dark wood floors were an even starker contrast."
    
    show detective_cat
    f "Tell me - to the best of your ability - what happened here, Arty."
    hide detective_cat

    show arty_neutral
    a "..."
    hide arty_neutral

    show detective_cat
    f "It’s imperative to the case, kiddo."
    hide detective_cat

    show arty_neutral
    a "Alright, alright. Here’s what I remember."
    a "On the night of Orion’s…passing, I was the DJ for this club up on that booth. It was a gig he got for me before we broke up, and I had to do it despite everything since they couldn’t get anyone else that night."
    a "I had never mixed music for such a big venue. You should’ve seen it Catective, it was something. A room packed full of cats all swaying and dancing to something I created, singing along to songs I hand-picked for a moment I envisioned them enjoying." 
    a "The lights, the energy…it was the perfect night I could ask for, really."
    a "But then there was a lull. As the night came to an end, I started playing softer songs since it was almost time for the club to close. I was told to do this around 1:30 AM. I heard shouting and I took off my headphones. It was Orion’s voice, and he was livid."
    a "He had a weird look in his eyes. Like that look when he’s about to change the game, kind of crazed but so much angrier than usual."
    hide arty_neutral

    show detective_cat
    f "The game?"
    hide detective_cat

    show arty_neutral
    a "Yeah, like a football game."
    hide arty_neutral

    show detective_cat
    f "...!"
    hide detective_cat

    show arty_neutral
    a "Yeah, Orion’s a big deal in the sports world. Or so I’ve heard at least."
    hide arty_neutral

    show detective_cat_worried
    f "Wait, so you’re telling me… the famous football player in the news that got murdered… that was him??"
    hide detective_cat_worried

    show arty_neutral
    a "...Ah."
    hide arty_neutral

    show detective_cat_angry
    f "YOU CAME TO ME WITH A CASE LIKE THAT?!!"
    f "(Just what did I get myself into? I was just about to retire…)"
    hide detective_cat_angry

    show arty_worried
    a "We kind of got together since I didn’t really know anything of his celebrity side. I saw a game or two, but I was never a sports girlie."
    hide arty_worried

    show detective_cat_worried
    f "(Wouldn’t that be important in their relationship??)"
    hide detective_cat_worried

    show arty_neutral
    a "Anyways, he was extra scary that night. And when that anger’s directed at you…well."
    a "It was weird too, now that I think about it. He was the one that broke things off all of a sudden. Just a text, didn’t feel real at all. I was kind of in a state of shock that night and seeing him there…it was like coming back to reality."
    a "Shouting like that, he cleared the waves of people in tides. He started to climb the ladder up to the booth and I started panicking. That was the only exit and I didn’t have a plan."
    a "When he got to the top, I tried to run past him but he grabbed me by the hood. No matter how much I struggled, he wouldn’t let go of me. He started to drag me to the ladder."
    a "So I bit him."
    hide arty_neutral

    show detective_cat
    f "You bit him?"
    hide detective_cat

    show arty_happy
    a "I bit him."
    a "He went down like a motherf*cker."
    hide arty_happy
    show arty_neutral
    a "Of course, he let go of me but as he was taking a step back, he tripped on the railing and…he fell. Hard."
    hide arty_neutral

    show detective_cat
    f "From 10 feet?"
    hide detective_cat

    show arty_neutral
    a "Something like that. Landed right on his head and didn’t move after that. Dead."
    a "..."
    a "He wasn’t that bad a guy you know? Like, before all this shit went down, he was alright. We were alright. He was a gentleman at heart and did all the right things when we were dating. And now he’s gone, and I might have killed him."
    hide arty_neutral

    show detective_cat
    f "(It’s the first time she may be admitting to this. She looks so distressed.)"
    f "...But you didn't."
    hide detective_cat

    show arty_sad
    a "Huh???"
    hide arty_sad

    show detective_cat
    f "This whole “murder” is fishy from the get-go with too many unknowns. I believe in you, you’re my client after all, so we’re going to solve this and prove your innocence."
    hide detective_cat

    show arty_sad
    a "I…thank you, Catective. Really."
    hide arty_sad

    show detective_cat
    f "Let’s get a closer look at the scene of the crime. If you’re uncomfortable, you don’t have to-"
    hide detective_cat

    show arty_happy
    a "No way. I’m your client and assistant now in all this. Especially since you’re rusty from this whole detective work shebang, it being three years and all."
    hide arty_happy

    show detective_cat_angry
    f "Hey now, I’m not that rusty…"
    hide detective_cat_angry

    show arty_neutral
    a "Would you really pass the NDIT right now?"
    hide arty_neutral

    show detective_cat
    f "...Field experience is more important-"
    hide detective_cat

    show arty_happy
    a "Then what are we waiting for?"
    hide arty_happy

    "Arty promptly walks to the body’s outline and the Catective begrudgingly follows."

    scene Bloodstain

    "The blood on the ground has all but faded into the dark grey carpet, leaving the sharp scent of iron in its wake even still. Its stain is pooled in a wide circle that extends past the white scotch tape on the ground."

    show detective_cat
    f "You mentioned that he fell after tripping on the railing up there, right?"
    hide detective_cat

    show arty_neutral
    a "Yep. He dropped so heavily that you could hear the thud throughout the whole club. His head…it started bleeding and the paramedics were called. I didn’t want to take a closer look after that."
    hide arty_neutral

    show detective_cat
    f "Cats usually land on their feet, and to fall from that height…maybe 10 feet or so? This typically isn’t fatal for our kind. It’s usually very rare to even fall on your head to induce enough blunt trauma to create this much external bleeding."
    hide detective_cat

    show arty_neutral
    a "Ah, I get it. An old friend of mine used to do competitive diving. It took her a long time for her to perfect her form enough to dive straight down."
    hide arty_neutral

    show detective_cat_worried
    f "Competitive diving?"
    hide detective_cat_worried

    show arty_neutral
    a "It was her thing, not mine. I was always better at playing support back then."
    hide arty_neutral

    show detective_cat
    f "...Were you happy just playing support?"
    hide detective_cat

    show arty_neutral
    a "Well, you know what they say. Until it’s my turn, I’ll keep clapping happily for others."
    hide arty_neutral

    show detective_cat
    f "...Hmm…that’s a positive perspective, I suppose."
    f "(She would get along with him well)"
    f "Anyways, I’m going to take a sample of this and send it to my tech guy tonight. We should get some results tomorrow morning."
    "The Catective takes a sample of the blood stains and pockets it in the meantime."
    f "Let’s head up the ladder. We might be able to glean more about what happened the other night up there."
    hide detective_cat

    scene Ladder

    show arty_happy
    a "Alright. Let’s get climbing."
    "Arty moves first and swiftly makes her way up the ladder, too rungs at a time."
    hide arty_happy

    show detective_cat_worried
    f "Hold on…kid…how did you…?"
    hide detective_cat_worried

    show arty_happy
    a "Get with it, Old Man, some of us aren’t getting younger out here!"
    hide arty_happy

    show detective_cat
    f "(At least she’s feeling better, but at what cost? I guess being out of the action takes a toll. And maybe one too many milk bottles…)"
    hide detective_cat

    scene DJBooth

    "At the top, the Catective all but dry heaves once he hauls himself up. Lying in a fetile position, he groans pitifully as Arty gracefully sits beside him."

    show detective_cat_sad
    f "Oh, to be young again…"
    hide detective_cat_sad

    show arty_neutral
    a "Cheer up dude, it gets easier from here."
    hide arty_neutral

    show detective_cat
    f "...I suppose that’s t-tru- ACHOO!!!"
    hide detective_cat

    "The Catective lets out an explosive burst of air, the recoil causing him to slam back into the side of the DJ mixer. Arty yelps, shooting up into the air on impulse."

    show arty_worried
    a "AHHHHHHH!!!"
    hide arty_worried

    show detective_cat_worried
    f "Sorry… allergies."
    hide detective_cat_worried

    show arty_worried
    a "That sound could exorcise ghosts. What the hell are you allergic to?"
    hide arty_worried

    show detective_cat_sad
    f "Glitter. And there’s lots of it."
    "With that, the Catective slowly sits up, brushing off the accursed sparkles as he laments his current state in life."
    hide detective_cat_sad

    show arty_neutral
    a "TThere was a lot of glitter during that night, so dazzling I couldn’t see for shit with all the lights and all until it died down. I never realized someone could be allergic to the stuff."
    hide arty_neutral

    show detective_cat_sad
    f "It’s me. I’m allergic to this stuff."
    "Glancing over as he sits up, the Catective does a double take."
    f "...Pawprints???"
    "Lo and behold, a clear set of pawprints lie just beyond the ladder, clear against the layers of glitter on the podium."
    f "I guess they didn’t get to cleaning this up yet. The podium is fairly high up, so it would be a hassle to bring a lot of cleaning materials up here."
    hide detective_cat_sad

    show arty_neutral
    a "More evidence for us then. Whatever can prove me innocent in this mess."
    hide arty_neutral

    show detective_cat
    "Getting down on one knee, the Catective inspects the footprints closer."
    f "1 3/4 size paws, bigger than average as expected for a football player. Tall guy. One set, so only him on the seen approaching you. Standard paw prints overall. It’s a miracle we can even make these out so clearly."
    f "!!!"
    f "One side…the print is deeper in the glitter here than the other. The other…the other is too light. Most likely due to a limp."
    hide detective_cat

    show arty_neutral
    a "I do remember he was swaying as he walked…how did you get all that from a set of glitter prints?"
    hide arty_neutral

    show detective_cat
    f "It’s in the details, but we were very lucky to still have even these to work with."
    hide detective_cat

    show arty_neutral
    a "True… but your powers of perception are kind of scary, Mr. Catective."
    hide arty_neutral

    show detective_cat
    f "Well I guess they didn’t call me the Cat Can Opener for nothing."
    hide detective_cat

    "The two cats continue to investigate the DJ booth, but find nothing else of interest."

    show detective_cat
    f "Well, if there’s nothing here then we can investigate down below again…"
    "The Catective walks over to the ladder, mentally preparing himself for the long way down."
    hide detective_cat

    show arty_neutral
    a "Catective! Wait, what’s that under your foot?"
    hide arty_neutral

    show detective_cat
    f "...!"
    "Beneath the Catective’s paws, a slip of paper flaps lifelessly underneath his heel. Grasping at its frayed edges, the Catective brings the paper closer to make out its all but illegible chicken scratch."
    f "It’s a receipt."
    hide detective_cat

    show arty_neutral
    a "Oh…"
    hide arty_neutral

    show detective_cat
    f "But it’s not mine!"
    hide detective_cat

    show arty_happy
    a "Oh? Let me see!"
    "Arty takes the piece of paper and squints at the page, lines faded from a printer slowly losing its ink."
    a "Mew…Paris…Le Astra Electrique?"
    a "Oh! It’s a taxi Cat Cab receipt! To this nightclub! And I think the time says…12 AM? I can’t make out the minutes."
    hide arty_happy

    show detective_cat
    f "Even without the minutes… you said you only saw him by the time the nightclub was closing? So why was he here over an hour only if he made such a big entrance?"
    hide detective_cat

    show arty_neutral
    a "I’m not sure. I could have sworn I saw him walk in. I would recognize him anywhere…but now I’m not so sure."
    hide arty_neutral

    show detective_cat_happy
    f "Dont’ worry kiddo. We’ll solve this case yet."
    hide detective_cat_happy

    show arty_neutral
    a "I hope so…my life depends on it."
    hide arty_neutral

    show detective_cat_sad
    f "Just like my life depends on getting down this ladder…"
    "The look Arty sends the Catective is withering, enough to fell several men far older and bigger than the Catective. Sheepishly, he pockets the note but it does little to weaken her overwhelming aura."
    f "Ok, ok I take it back"
    hide detective_cat_sad

    show arty_happy
    "Smug, Arty lets out a victorious grin, only slightly rueful."
    a "C’mon, Catective. It isn’t so bad. I’ve had my fair share of ladders after all this DJ stuff, surprisingly, and there’s nothing to it. Just don’t look down!"
    "As skillfully as ever, Arty grabs the sides of the ladder and, with a flourish of her paws, slides down the rest of the way. Landing perfectly with a slight bend in her knees, she looks up, smiling."
    a "As easy as that!"
    hide arty_happy

    show detective_cat_worried
    f "aS eAsY aS tHaT…"
    f "(As easy as that…wait a minute! Maybe it is!)"
    f "Okay, but watch this!"
    "The Catective tentatively walks to the precipice of the ladder, watching the ground sway beneath him precariously."
    hide detective_cat_worried

    show arty_neutral
    a "Uhh…I said not to look down for a reason…"
    hide arty_neutral

    scene black
    "The Catective closes his eyes tightly, breathing all but stilled. He sees nothingness, hears nothingness, the world beyond him blocked out. Channeling all of his mental power, he breathes in deeply, feeling the flames of chaos and destruction within him."
    scene BigBang
    "He holds his breath, focusing and compressing the reservoirs of untapped potential within him into a single moment, a speck in space comprised of pure, raw energy. Suddenly, his nostrils flare, the power too overwhelming to contain."
    "Roiling inside him, sparking with electricity and heat, he releases it with a burst of hot air."
    scene Ladder

    show detective_cat_happy
    "The Catective opens his eyes, looking up. He was now at the bottom of the stairs."
    f "DID YOU SEE THAT, KIDDO? TAKE THAT, LADDER B*TCHHHH!!!"
    hide detective_cat_happy

    show arty_worried
    a "...Uh, Catective? All you did was climb down the ladder really fast with your eyes closed-"
    hide arty_worried

    show detective_cat_angry
    f "I SAID TAKE THAT ALREADY NO TAKEBACKS!!!"
    hide detective_cat_angry

    show arty_neutral
    a "..."
    a "...You should’ve told me you had a fear of heights, you old fart. I wouldn’t have made you climb up with me if I had known."
    hide arty_neutral

    show detective_cat_worried
    f "I don’t have a fear of heights…"
    f "(Not until I lost him, at least)"
    "The baleful look Arty sends him causes him to turn away. Even he knows he’s not convincing anyone."
    f "Fear of heights OR NOT, this case is worth a bit of fear."
    f "We wouldn’t have been able to find so many clues otherwise, and if it goes toward proving your innocence then I will do what I can to make it happen."
    hide detective_cat_worried

    show arty_sad
    a "Wait, stop, go back to being sassy. My heart can’t take this."
    a "But, for real, you’re alright, Catective. I’ll be honest, I hadn’t totally forgiven you for the whole spilling milk on my favorite shirt thing but… you’re alright."
    hide arty_sad

    show detective_cat_happy
    f "Thank you, Arty. Means a lot from you kiddo."
    hide detective_cat_happy

    show arty_happy
    a "You know, it’s a shame you haven’t taken on more cases. It’s obvious that you’re a skilled Catective, so what’s stopping you?"
    hide arty_happy

    show detective_cat_sad
    f "(Sigh)"
    f "...I’ll tell you another time, kiddo. It’s a long story."
    hide detective_cat_sad

    show arty_neutral
    a "Well, alrighty, just don’t keep me waiting too long!"
    hide arty_neutral

    scene Cream

    "Just before the two are about to leave, the young DJ spots a small, unlabeled pink tube at the foot of the ladder. Picking it up, she slowly turns it over in her paws."

    show detective_cat
    f "What’s that you got over there?"
    hide detective_cat

    show arty_neutral
    a "Not sure…sunscreen maybe? Or face cream? Hard to tell, and there’s nothing left either. It smells great, though. Like some sort of earthy fruit mix."
    hide arty_neutral

    show detective_cat
    f "We can send this too to my tech guy in the evening and hopefully hear back from him. It almost definitely has traces of someone’s pawprints or we could just figure out their skincare routine."
    hide detective_cat

    show arty_neutral
    a "If you say so. We sure do take a lot of things from these crime scenes. Blood, evidence, even random beauty products."
    a "It almost feels like stealing. How did you get a warrant for all this?"
    hide arty_neutral

    show detective_cat
    f "..."
    hide detective_cat

    show arty_worried
    a "Ah. I guess that answers that."
    hide arty_worried

    scene NightClub
    "The Catective and Arty reach the entrance of the club once more. Just as Arty grabs for the door, the Catective nudges her and subtly points his chin at another cat all but lost in shadow."

    show detective_cat
    f "Do you know them?"
    hide detective_cat

    show arty_neutral
    a "Uh I didn’t notice them when I came in but he looks a little familiar…oh! They’re the bouncer. They helped me get past the crowd last night so that I could perform!"
    hide arty_neutral

    show detective_cat
    f "Why don’t we ask them a few questions about that night. Maybe things will become a little clearer."
    hide detective_cat

    "Tentatively, the Catective and Arty approach the bouncer."

    show detective_cat
    f "(Okay, an encounter with a potential witness to the crime. Play it smooth.)"
    f "How goes it, fellow bouncer?"
    hide detective_cat

    show cat_wig
    bouncer "The hell?"
    hide cat_wig

    show detective_cat_worried
    f "(Not smooth! Not smooth! Abort mission!!)"
    hide detective_cat_worried

    show arty_worried
    a "(She gives you a side eye to end all side eyes.)"
    a "What I think he means is… who are you and how are you?"
    hide arty_worried

    show cat_wig
    bouncer "(Sizing the two cats up, he huffs gruffly.)"
    bouncer "And what’s it to you?"
    hide cat_wig

    show arty_worried
    a "Ah, so you’re one of those…"
    hide arty_worried

    show cat_wig
    bouncer "WHAT WAS THAT?"
    hide cat_wig

    show arty_neutral
    a "Nothing! Nothing at all."
    hide arty_neutral

    show detective_cat
    f "(Not so easy now, is it kid?)"
    f "We just had a few questions about the crime that occurred here a couple nights ago."
    hide detective_cat

    show cat_wig
    bouncer "I don’t know nothing about that, so get lost."
    hide cat_wig

    show detective_cat
    f "Surely you know something? It’s been all over the news. The famous soccer player? Killed in this very club?"
    hide detective_cat

    show cat_wig
    bouncer "I really know nothing about it other than what you just said."
    hide cat_wig

    show detective_cat_happy
    f "So you do know something then?"
    hide detective_cat_happy

    show cat_wig
    bouncer "I- Not funny, pal. Now get lost, or I’m kicking you both out."
    "Straightening his spine, the bouncer towers at his full height. He looks down at the two in disdain, the very picture of intimidating."
    hide cat_wig

    show arty_happy
    "Arty quickly slides herself in between the Catective and the bouncer, smiling bashfully."
    a "Excuse my grandpa here, he can be a bit forward."
    hide arty_happy

    show detective_cat_angry
    f "GRANDPA-"
    hide detective_cat_angry

    show arty_neutral
    a "See? Forward. Anyways, it’s a shame you weren’t there that night. I heard this really famous DJ was there and that the whole club was popping off."
    hide arty_neutral

    show cat_wig
    bouncer "They weren’t that good..."
    hide cat_wig

    show detective_cat
    f "(How would he know that if he didn’t…)"
    hide detective_cat

    show arty_happy
    "The Catective notices out of the corner of his eye the slight flick of a brown ear. So subtle that one could miss it with the blink of an eye. Perhaps more obvious was grin she was holding back."
    a "(Bingo.)"
    hide arty_happy

    $ chosen = []
    $ allDone = False
    $ curiousCount = 0
    menu interrogation:
        set chosen
        "(If we can make him keep talking, we may be able to prove he was there)"
        "The glitter was pretty intense that night too. Or so I hear.":
            jump glitter
        "I heard rumors that the DJ was giving autographs out along with that soccer player.":
            jump rumors
        "It was so crazy that that one guy fell from all the way up there. What was his name again…?":
            jump hisName
        "I thought the music was pretty good.":
            jump dumb
        "I don't need anymore evidence! We've caught you red-handed!":
            if curiousCount > 2:
                $ allDone = True

            if allDone == False:
                jump uhoh
                return
            else:
                pass
    
    show detective_cat_angry
    "We’ve heard enough. I’m a Catective, and you are being held accountable for being a witness to the murder of Orion Delacroix."
    hide detective_cat_angry

    show cat_wig
    bouncer "WHAT?! Well, on what evidence."
    hide cat_wig

    show detective_cat
    f "You heard the DJ playing that night, did you not?"
    hide detective_cat

    show cat_wig
    bouncer "Well, no, I already said I wasn’t there that night."
    hide cat_wig

    show arty_neutral
    a "But you said you thought the music I played was mid and saw the glitter coming from the ceiling."
    hide arty_neutral

    show detective_cat
    f "You even knew the murder victim’s name despite claiming otherwise. You even saw that he had a limp and the ER come for him."
    hide detective_cat

    show cat_wig
    bouncer "..."
    bouncer "Fine. You got me. Yes, I was there that night. There’s no denying that now. But that’s all I know. You’ve gotten everything out of me, so why are you still here interrogating me?"
    hide cat_wig

    show detective_cat
    f "But is that really all?"
    hide detective_cat

    show cat_wig
    bouncer "...!"
    hide cat_wig

    show detective_cat
    f "What do you have to say to this?"
    "The Catective pulls out the receipt."
    f "No one else reported seeing Orion at the scene of the crime before he entered the building. The only evidence of him being there early is this receipt found at the scene of the crime."
    f "How could you have known if you didn’t see him? We know you’re a witness, proven it beyond a shadow of a doubt. So tell us what you know."
    hide detective_cat

    show cat_wig
    bouncer "..."
    bouncer "It seems like you know everything."
    hide cat_wig
    
    show arty_neutral
    a "...!"
    hide arty_neutral

    show cat_wig
    bouncer "My employer said that they would take care of everything, but that was obviously a lie. Fine, I’ll tell you everything I know on one condition."
    hide cat_wig

    show arty_worried
    a "How cliche, but do go on."
    hide arty_worried

    show cat_wig
    bouncer "I was sent to retrieve him personally at his hotel, Le Diable Rose. I was told to not ask questions or else my paycheck would take a hit."
    bouncer "I pick him up around 11:30 PM the night before, and as we drive he looks…odd. Knees weak, breathing heavy… I swear he said something about his mom’s spaghetti."
    bouncer "It was too dark to see but he was sweating profusely. The seat was wet when he got out of the car around midnight. He then waited for the final set of the night before exiting from the back and re-entering the club."
    bouncer "I never saw him after that, but I heard the crowd screaming from outside."
    hide cat_wig

    show arty_worried
    a "...Is that it?"
    hide arty_worried

    show cat_wig
    bouncer "WHAT DO YOU MEAN tHaT’s iT?"
    hide cat_wig

    show arty_worried
    a "I mean… I was expecting more with how much it took to get you to open up…"
    hide arty_worried

    show cat_wig
    bouncer "Well it doesn’t come easy to some people…and I was threatened by my employer…what do you want from me?"
    hide cat_wig

    show detective_cat
    f "But who is your employer?"
    hide detective_cat

    show cat_wig
    bouncer "That I can’t tell you. Even telling you this much, even if you both seemed to have it all figured out, is very risky to me. Apologies, but this is the best I can do for you"
    f "...Hmmm. And Orion never left the back until the final set?"
    bouncer "As far as I know."
    hide cat_wig

    show detective_cat
    f "And how did he look when he re-entered the club?"
    hide detective_cat

    show cat_wig
    bouncer "He had a crazy look in his eyes, like a man on a mission. But other than that, he had the limp I mentioned before. But he was moving very purposefully, so it wasn’t like he’d been drinking heavily."
    bouncer "He seemed better than when he was in the car."
    hide cat_wig

    show arty_neutral
    a "Maybe it was carsickness? I’ve never seen him like that though…not even from the games he’s played in…"
    hide arty_neutral

    show detective_cat
    f "It’s likely the effects of some drug, but it’s hard to tell. His thinking, at least, seems to have been heavily altered."
    f "We’ll have to get the blood tested for tonight. In the meantime, I think we’re done here."
    f "Your testimony was very helpful. We’ll keep this to ourselves and keep your identity confidential. Thank you, we’ll be leaving now."
    hide detective_cat

    "The bouncer nods, tipping his head to the two cats before blending into the shadows once more. The Catective and Arty step out of the club, basking in the cool evening breeze as the electric lamps flair to life in the bustling city."
    "The Catective and Arty separate for the night, but not without questions." 
    "What was Orion doing before the final set? Who was this mysterious employer, and what role did they have in all this? And what made Orion act the way he did that led to his demise?"
    "The two cats ride out an uneasy sleep before the next day."

    return

label glitter:
    show cat_wig
    bouncer "I suppose..."
    hide cat_wig

    show detective_cat
    f "It would be difficult to move up there. Wouldn't it be awful for someone already injured?"
    hide detective_cat

    show cat_wig
    bouncer "!!!"
    bouncer "I heard from one of the guys that the athlete had a limp..."
    hide cat_wig

    show detective_cat
    f "(Bingo!)"
    hide detective_cat
    $ curiousCount += 1
    jump interrogation

label rumors:
    show cat_wig
    bouncer "That can't be right, I was with him-"
    "The bouncer stops, but it's too late. The Catective caught him red-handed."
    hide cat_wig

    show detective_cat
    f "You were with him?"
    hide detective_cat

    show cat_wig
    bouncer "Yes. I was with him before the set started."
    bouncer "He wasn't giving autographs though. He was waiting in the back for half an hour."
    hide cat_wig

    show detective_cat
    f "Interesting..."
    hide detective_cat
    $ curiousCount += 1
    jump interrogation

label hisName:
    show cat_wig
    bouncer "Ah, his name was Orion. Very famous soccer player, that guy."
    bouncer "There was pure chaos around the body when he fell. Had to get rushed to the ER."
    bouncer "Somehow, they were immediately on the scene despite being an hour away. Weird."
    hide cat_wig

    show detective_cat
    f "Weird indeed..."
    hide detective_cat
    $ curiousCount += 1
    jump interrogation

label dumb:
    show cat_wig
    bouncer "It was aight I guess..."
    hide cat_wig

    show detective_cat
    f "..."
    f "Yeah, I don't know where I was going with that. But this does confirm you were there the night of the crime?"
    bouncer "Oh. Oh! Yes well...I guess you got me there. I must have mixed up the dates, haha."
    "Off to the side, Arty seems oddly pleased."
    hide detective_cat
    $ curiousCount += 1
    jump interrogation


label uhoh:
    show detective_cat_angry
    f "We’ve heard enough. I’m a Catective, and you are being held accountable for being a witness to the murder of Orion Delacroix."
    hide detective_cat_angry

    show cat_wig
    bouncer "WHAT?! Well, on what evidence."
    hide cat_wig

    show detective_cat_worried
    f "Well erm. That’s a good question."
    f "(Damn it! I couldn’t tie his alibi to the crime. Maybe I should have pressed him for more information)"
    hide detective_cat_worried

    scene black
    "With no other leads to go off of, the Catective was unable to find anymore evidence for the case."
    "Arty's trial came and the evidence pointed overwhelmingly against her. She was sentenced to a lifetime in prison."
    "With no other clients, the Catective's office shut down at the end of the month. Although he wanted to live a quieter life, the Catective couldn't help but feel at a loss."

    scene Fire
    show hydra
    "The office would later be decmimated by the mysterious Catglomerate that led to Supreme Overlord Makia Celli's rule."
    "Reasons at this time are unknown as to how this came to be, only that few survivors remained after the initial resistance."
    "The whereabouts of the Catective and the DJ are unknown."
    "Game Over :("
    hide hydra

    $ game_over = True

    python:
        chapter_success(2, False)

    return