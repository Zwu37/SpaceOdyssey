label start:

    "The war came silently, without a sound.\nBut the damage it left was insurmountable."
    "Our once-prosperous quadrant, Caedara, was left burning. Our people are being forced to leave the only home they’ve known their whole lives."
    "There’s an announcement on the news: Aurelios has taken down another Caedaran regiment, putting immense pressure on the entire military base."
    "Aurelios this, Aurelios that. It’s all anyone hears about these days, as if they want future generations to remember exactly who we denied power by refusing to surrender."
    "The war began over Trionium — a powerful element capable of leveling entire zones."
    "They came with trade propositions first. Then threats. Finally, rain fell in shining beams upon us as Caedara refused to yield, refusing to let Trionium fall into the wrong hands."
    "Aurelios took it upon themselves to personally teach us a lesson."
    "And a lesson they taught."

    jump chp1

label chp1:

    scene black with dissolve

    show text "Chapter 1\nA Day in the Life" with Pause(1.5)

    play music "audio/Act1.ogg" loop

    scene black with dissolve

    scene your_scene_title

    "{b}6 Days Earlier…{/b}"
    play sound "audio/alarmclock.mp3"volume 0.25 fadeout 1.0
    "A high-pitched alarm clock sounds off."
    "Yesterday was rough, as another lecture from Dad about “growing up” and how a “soft heart is a luxury” was delivered. Nothing I hadn’t heard before."
    "I understand where he’s coming from, but it just feels like he isn’t listening, like no matter what I do, I won’t live up to the expectations of the great Sorin Morvayne."
    "My parents are both off saving the world, leaving me here to get ready for school."
    "I {i}should{/i} get ready, I only have a couple of weeks left before school lets out, but man, I don’t want to."
    "Mom always says that if I want to get anywhere in life, I need to focus on my studies. Neither of them is here, though. I could always just skip."

label choice1:
    $ save_name = "Act1"

    menu:
        "Go to school":
            "Mom’s right, school is important, and we’ll probably end up doing nothing since it’s so close to the end of the year anyway."
            "The sky ride to the school is beautiful with the melodic hums of the hovercars creating an odd lullaby."
            jump continue_chp1

        "Skip school":
            "Who likes going to school? I mean, it’s not like Mom or Dad will check up on me."

            menu:
                "Train":
                    "I could always train; I'm sure Dad would be less mad if I did."

                    menu:
                        "Train with Skymarshal VR":
                            "It’s not the most fun thing to do, but it would make my parents proud. \nI'll train with Dad’s Skymarshal Training Kit."
                            jump continue_chp1

                        "Train with physical exercises":
                            "It’s not the most fun thing to do, but it would make my parents proud. \nDad set me up a training regimen so I can be as strong as he is someday."
                            jump continue_chp1

                "Play with Klaeo":
                    "As soon as I open my door, Klaeo pushes his way through and barrels into me. He’s incredibly slimy."
                    "It's not his fault that his species' defense mechanism happens to be the grossest."
                    "Every time he sees me, his seven eyes perk up, and today was no different."

                    menu:
                        "Play with the toy":
                            "Klaeo’s favorite toy is in the shape of a Lynxite. He is having so much fun."
                            jump continue_chp1

                        "Feed Klaeo":
                            "For a growing boy like Klaeo, mushy orange pulp makes the perfect food."
                            jump continue_chp1

                "Visit Kasian":
                    "Kasian's place is not far from here. I'll just go and hang out with him for a while."

                    menu:
                        "Play games":
                            "We boot up his old XJ-3 and play Caedra Skymarshal IV."
                            jump continue_chp1

                        "Go out for food":
                            "We head to a nearby restaurant. The food tastes far better than what they have at school."
                            jump continue_chp1

                "Play Skiiphony":
                    "Dad always called the Skiiphony a useless instrument, which made me want to play it even more."
                    "Most of the time, it sits silently in the corner of my room, mostly because I don’t want to hear about it all night from my dad. \nSometimes when Dad’s gone on missions, Mom will listen to me play."
                    "I’ll always treasure the smile she gets when I play her favorite song."
                    jump continue_chp1

                "Watch Vid-Doc":
                    "Nobody’s here to get mad at me for being lazy for a bit."
                    "There are a couple of documentaries I could watch. I think I’ll start with the Salix Documentary."
                    jump continue_chp1

                "Go for a walk":
                    "The humming of hovercars saturates the air in an almost calming manner as I make my way outside."
                    "The neighborhood is quiet and peaceful today, and I let out a relaxed sigh, enjoying the cool breeze and the wind at my back."
                    jump continue_chp1

label continue_chp1:
    
    stop music

    pause 0.5

    play sound "audio/explosion.wav"

    jump chp2
    
label chp2:

    scene black with dissolve

    show text "Chapter 2\nHomecoming" with Pause(1.5)

    play music "audio/Act2.ogg" loop

    scene black with dissolve

    scene your_scene_title

    "{b}6 Days Later…{/b}"
    "{size=*2}{i}{b}“Submission is peace”{/b}{/i}{/size}" #Might sub with image
    "Aurelios’ message flashes on every wall my eyes can see."
    "Mom was supposed to come home today."
    "Despite the instructions not to leave the house, I still slipped out."
    "I see now why I shouldn’t have."
    "Smoke coiled from every building. Not from the chimneys — but from a fire that had meant to kill."
    "The news earlier this morning said the body count was rising. My neighborhood is quiet. Too quiet."
    "{b}Were people fleeing Caedara? Or are they all already dead?{/b}"
    "I wanted to look, but my mom was coming home, we were out of food, and I needed some air. Just a bit. From hiding in my own home in my own country."
    "{b}It’ll be quick, Mom.{/b} \nI tried to speak to her in my imagination, and she shook her head in disappointment. I know, I know, I’ll be back in no time."
    "{b}Maybe… maybe I spoke too soon.{/b}"
    "“Help…” a choked voice came. I whipped my head in their direction."
    "Buried under the rubble, I saw a hand peeking through, asking someone, anyone, to come rescue them."
    "I look around, and there’s no one in sight."
    #Insert Engine sound
    pause(1.5)
    "I take a step forward when I hear a loud engine sound overhead. \nSomeone was coming, and it was Halo Guards from Aurelios. I’m screwed! "

label choice2_1:
    $ save_name = "Act2.1"

    menu:
        "Go help the person":
            jump continue_chp2

        "Turn around and leave":
            jump continue_chp2

label continue_chp2:
    "I have half a mind to ignore it and just walk away. My legs, as if they had a mind of their own, move forward before I can convince myself to look away. "
    "Okay, we’re doing this, I guess."
    "In two strides, I close the distance between me and this struggling person."
    "{b}“Hey! Are you okay?”{/b}"
    "My voice comes out shaky and strained. \nIt startles me—strange, unfamiliar, like it belongs to someone else. \nI haven’t spoken out loud in months."
    "My brother was killed in the initial attack. \nMy parents? Called to the frontline. Communication lines died the day our world fell apart."
    "With that and my parents gone, there was no one left to talk to."
    "Now is not the time to whine, Orius! \nI grit my teeth while moving the slab."
    "“Please… help my baby,”the voice says."
    "Baby?"
    "The hovercraft’s sound is getting louder— closer."
    "{b}Shit! I can’t die here. I can’t!{/b}"
    "Aurelios’ first instinct is to kill. And I was out in the open. One blast and I’ll be a pile of flesh on gravel."

label choice2_2:
    $ save_name = "Act2.2"

    menu:
        #"Continue helping"
            #jump help
        
        "Take cover and hide":
            jump hide

label hide:
    "My voice cuts through the noise, “Hold on, I’ll be back, okay?”"
    "The woman starts screaming louder. \nI take cover inside a nearby building that’s barely standing, still crumbling. \nDebris falls from the blown-off parts, missing me by a hair."
    "The woman is still pleading. My jaw clenches. \n‘I didn’t run away. I’m still here!’ I wanted to yell back. If I get killed, good luck getting out of there then."
    "Her screams stop. Too abrupt for my liking. Like she couldn’t even hear the pain tearing through her voice."
    "‘Hold on a little longer. I’ll be there. I swear it!’ I grit through clenched teeth, feeling my heart hammering against my ribs."
    #Insert helicoper sound
    "The hovercraft passes through, its underbelly covering the hole in the building for a brief moment, and then it’s gone. \n{b}“Please don’t land, please don’t land, please DO NOT LAND HERE!!”{/b} "
    "The engine’s sound disappeared as it flew away. I exhale a breath I didn’t realize I was holding."
    "Once it’s gone, I move quickly."
    "“Are you—” My heart stops, realizing her hand had gone limp. \nIn denial, I still try shaking her hand, hoping for some miracle. \nI’m on my knees now, breathing hard, feeling helpless."
    "“No, no, no!”"
    "She hadn’t stopped screaming because she was tired. She stopped screaming because she was dead."
    "And it’s on my hands. I didn’t help her when she needed it."
    "“The baby!” \nI remember her telling her baby is trapped in there with her."
    "I surge to my feet. \nVeins in my neck pulled taut as I began to shove against the slab. \nThe concrete groans as it starts moving.\nI push it aside."
    "I see crushed legs first.\nThe bile rises in my throat. \nThen I look at the baby and freeze."
    "Not breathing. \nSilent sobs wracked my body as screams clawed in my throat for release."
    "I walk to the building and punch it — hard enough to shatter something, even if it’s just my goddamn fury."

    #Change scene

    "I’m still rocking on the floor. My knees pressed to my chest, eyes red, rimmed from what I witnessed."
    "I hadn’t realized when I walked back home – too shaken up by what I just witnessed."
    "The broken body of the woman."
    "The child she wanted to save, but it was too late. I was too late."
    "{b}Too late.\nToo late.\nToo late.{/b}"
    "The words kept ringing louder— angrier."
    "I didn’t hear when the lock turned. Didn’t notice my mom holding my face, trying to pull me back to reality."
    "“Orius!” \nHer voice was drowned out, faint. She’s trying to anchor me."
    "“Orius, listen to me!” I snap out of my thoughts."
    "“Mom?” I look at her. “She died on me. I asked her to hold on, but she died anyway.” I’m weeping."
    "My mom looks concerned. Her hands run through my hair, understanding dawning on her that I ventured out."
    "“You went out?” She asks."

label choice2_3:
    $ save_name = "Act2.3"

    menu:
        "Tell her the truth":
            jump continue_chp2_1

        "Lie to her":
            jump continue_chp2_1

label continue_chp2_1:
    "Instead of answering her question, I ask, “Was Dad right? Is Caedara really dying?”"
    "“Orius, listen—“ \nMy mom tries to stop me from spiraling, but I’m already too far gone."
    "“Our people are dying. Dad was right. I need to fight. I need to protect our people.” \nI’m having a full meltdown on the floor, while she tries to hold me."
    "“Orius, listen to me now!” Mom snaps."
    "Her eyes— tired. Her face looks like she’s seen things she wishes she could unsee. Strands of gray are already showing."
    "She releases a shaky breath, “I’ve already lost one son to this fucking war. I’ll not lose another.” \nDespite her efforts to appear in control, her lips quiver."
    "“No son of mine will be fighting in the war. You’re getting out of here. Now !.” Her voice trembles."
    "She gets up, looks me in the eye, and says, “You’re leaving, now!” and then grabs a bag and starts throwing my stuff in there."
    "I follow her and yank it out of her hand—\n“No! We…we need to fight back”. I need to, so no other soul out there gets smothered under rubble.”"
    "Mom grabs my shoulders, shaking me, “Get a hold of yourself, Orius.”"
    "“You need to tell Dad. You need to tell him I’m ready—” I say, feeling desperate, confused and angry all at once."
    "One minute I’m throwing a tantrum like a kid, the other I’m clutching my face— that stings from the aftermath of the impact."
    "I raise my head toward my mom, feeling helpless, eyes wide."
    "“I said. Get. A. Hold. On. Yourself.” Mom says through clenched teeth.\n“You’re getting on that hovercraft or so help me Thalorien, I’ll drag you there myself.”"
    "My jaw sets in a tight line."

label choice2_4:
    $ save_name = "Act2.4"

    menu:
        "Be adamant about staying":
            jump continue_chp2_2

        "Relent and go":
            jump continue_chp2_2

label continue_chp2_2:
    "My mom snatches the bag away from me and starts packing again."
    "“One day, you’ll see why I’m telling you this. One day, you’ll thank me for it. But right now? This war? It’s not yours to carry.”"
    "I break down into tears, “But Mom, I don’t wanna go. I don’t wanna leave you.”"
    "“I know, baby,” seeing me crying, she chokes on a sob, “but you have to, for me, please! Run as far away from here as you can. Please.”"
    "I have seen broken bodies, no matter how hard she tried to shield me from it. \nBut seeing Mom break down like that, it broke something in me."
    "“Okay. Okay, I will.” Tears still roll down my cheeks, “I will go.”"
    pause (1.0)
    "A few hours later, we’re all packed up."
    "The one time mom got to come back home, she’s not resting. She’s thinking about how to save her last shred of sanity. "
    "She doesn’t say, but working as a doctor on the frontline must’ve been harrowing. "
    "The things she had to witness, she never speaks about them, but they show in her eyes— in the way she looks at one spot on the wall for hours straight."
    "That memory alone made me agree to leave."
    "And even though she wanted me to get away right in this moment, slipping past Halo guards was signing up for your death."
    "So we waited. \nSneaking out after midnight when their patrolling thinned was our only shot."
    "“Don’t worry about me, okay?” Mom tells me as we turn a corner. "
    "How?"
    "I wanted to ask. How am I supposed to not worry? To know that she could breathe her last helping people at the borders, while I’m blissfully unaware."
    "That my dad could die fighting, and I’d not even know it."
    "How is one to sever their past and keep living? I wanted to ask, but instead I nodded."
    "The hovercraft comes into view as we turn another bend. "
    "“Here’s some money,” her hands are shaking while pressing the paper in my palms."
    "But she knows she has to stay strong."
    "“Don’t look back,” her eyes are lined with silver."
    "“That’s Captain Draeven Karr,” she points her chin in the direction of the man standing by the ship’s door."
    "“He’s a bit of a prick, but he’ll get you to a safe location.” \nHer smile is weak and exhausted. She looks at my face as if memorizing every line, every mole on it."

label choice2_5:
    $ save_name = "Act2.5"

    menu:
        "Tell her you hate her for doing this":
            jump continue_chp2_3

        "Hug her":
            jump continue_chp2_3

label continue_chp2_3:
    "Boots. Heavy boots shuffle around the corner. \nBoth of us look in that direction together."
    "“Go! Now!” Mom orders."
    "“No, but mom!” I scream. \nI go to grab her, but Captain Karr holds me by the back of my shirt and throws me inside the ship. I slam on the wall and slide down."
    "The craft starts hovering above the ground. There are other people around me, but I don’t care. \nI press myself against the window, watching what’s happening outside."
    "Halo guards have my mom on her knees while having a gun pointed at her head."
    "“Hey, hey! Stop!” I’m screaming. \nNo one in the craft is holding me back. "

label choice2_6:
    $ save_name = "Act2.6"

    menu:
        "Get out and help your mom":
            jump continue_chp2_4

        "Ask Captain Karr to intervene":
            jump continue_chp2_4

label continue_chp2_4:
    "I slam at the captain’s door, asking him to let me out. "
    "“Help my mom!” I choke, “They got her, help my mom.” I’m begging. “Please.”"
    "“Aww, you want me to help?” His arrogant voice speaks through the intercom."
    "“Yes, please! Please!” "
    "The captain clicks his tongue before saying, “No can do, this ship will only stop at the next station. Now sit your ass back down.”"
    "I bang on his door a few more times. "
    "I hear faint sounds of mom asking them to release her. I scramble to the window to see what's happening. "
    "My face pales when my eyes zero in on her hands. \nGold bands pulse around her wrists. They’ve put neuro-lock links. \nThat’s the device used to restrain captives. They’re taking her away."
    "“Hey! Stop it!” My fist slammed against the window as if trying to pop it open. “I said let her go.”"
    "They throw her in the tank as Captain Karr starts the hovercraft to fly away."
    "Screams rip my throat, my nails claw at the door— at the window, fighting to be let out."
    "I don’t know who I’m screaming at, but I keep repeating, “I’ll kill you! I’ll kill all of you!”"

    stop music fadeout 1.5

    pause 0.5
    
    return
