image Orius = "images/Orius.png"
image teacher = "images/Mr. Zaender.png"
image Kasian = "images/Kasian1.png"
image mom = "images/mom1.png"

define Orius = Character("Orius", color="#FFED9F")
define Mr. Zaender = Character("Mr. Zaender",color = "#FFED9F")
define Kasian = Character("Kasian",color = "#FFED9F")
define woman = Character("?",color = "#FFED9F")
define mom = Character("Zaira",color = "#FFED9F")
define captain = Character("Captain Karr",color = "#FFED9F")


label start:

    scene black
    show text "{color=#ffee00}{size=+12}{b}CONTENT WARNING{/b}{/size}\n\n{color=#ffffff}This story contains content that may be disturbing to some players.\n\n{size=+2}" with dissolve
    pause 

    hide text
    show text "{color=#ffffff}{size=+10}{b}CONTENT WARNINGS INCLUDE:{/b}{/size}\n\n• {b}Violence{/b}\n• {b}Sudden Loud Sounds{/b}\n• {b}Character Death{/b}" with dissolve
    pause

    hide text
    show text "{color=#ffffff}You can leave the game anytime by pressing {b}ESC{/b} to access the menu and quit.\n\n{size=+2}Please proceed with caution and enjoy the game.{/size}{/color}" with dissolve
    pause 

    scene black with dissolve
    jump prologue

label prologue:

    scene war
    pause 0.5
    "It all happened in the blink of an eye."
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"One minute, I’m getting a tongue lashing from Kasian, the next, my world tilts."
    pause 0.5
    play sound "audio/explode.mp3"
    show war with hpunch
    "Smoke is everywhere— thick, black, burning, blinding."
    play sound "audio/coughing.mp3"fadein 1 fadeout 1
    Orius"My eyes try to focus on something, anything, but my head’s pounding."
    Orius"If it’s because of smoke or being blown back, I couldn’t tell."
    Orius"\"Kasian!\""
    stop sound
    Orius"My voice come out choked. Desperate. My brain’s scrambling, half wondering if my brother’s okay. Half trying to piece together what just happened."
    Orius"That day, my world as I knew it stopped existing."
    hide Orius with dissolve
    pause 0.5

    jump chp1

label chp1:

    scene black with dissolve

    scene chapter

    show text "{size=+20}{b}Chapter 1{/b}{/size}" with Pause(1.5)

    scene black with dissolve

    play music "audio/Act1.ogg" volume 0.5 loop

    pause 0.5
    show text "{b}6 Days Earlier…{/b}"
    pause 0.5

    scene black with dissolve

    scene home
    pause 0.5
    play sound "audio/alarm.mp3"fadeout 0.3
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"Yesterday sucked. Dad hit me with the whole “growing up” talk again. “A soft heart is a luxury,” blah blah blah. Give me a break."
    Orius"It’s not like I could ever live up to the great Sorin Morvayne’s expectations anyway."
    Orius"No matter what I do, I could never be enough for him."
    Orius"\"Get a life, man.”"
    Orius"I look at my reflection in the mirror and take a deep breath. My hair sticks out in all directions."
    Orius"Anyway, I don’t have time to feel sorry for myself. Time to go to school. I have a math test and the English paper topic to negotiate."
    hide Orius with dissolve

    scene black with dissolve
    pause 0.5
    scene school
    pause 0.5
    play sound "audio/schoolBell.mp3"fadeout 1
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"I feel exhausted, and it’s only after 11:00 AM."
    show teacher at right with dissolve:
        xoffset -180
        yoffset -280
    Mr. Zaender"\"Good morning, Orius. I’m glad you showed up to school today.\""
    Mr. Zaender"\“How’s your project on Sorin Morvayne coming along? Remember, you’ll be presenting next week.\”"
    Orius"…Of course, I forgot all about it. I didn’t even bother opening the textbook."
    Orius"\“It’s going great! However, I was wondering if I could write about someone else? Considering he’s my father, my essay risks sounding too…\”"
    Orius"honest? brutal? exposing?"
    Orius"\“...biased\”"
    Mr. Zaender"\“Absolutely not! I’d like the class to learn about the great Marshal’s epic expeditions from his very own son!\”"
    Orius"\"But...\""
    Mr.Zaender"\“No buts, if you want to pass this class, you will have to turn in the assignment. Am I clear?\”"
    Orius"I wanted to argue, wanted to say he can’t make me do it. But it felt pointless."
    Orius"...sigh...I'd better go home and start working on it today."
    hide Orius with dissolve
    hide teacher with dissolve

    scene black with dissolve
    
    pause 0.5
    show text "{b}3 Days Earlier…{/b}"
    pause 0.5

    scene black with dissolve

    scene home
    pause 0.5

menu:
    Orius"What should I do today?"

    "Go to the kitchen":
        show Orius at left with dissolve:
            xoffset 180
            yoffset -290
        Orius"The house is mostly empty. Mom’s off saving the world, and Dad, well…"
        show Kasian at right with dissolve:
            xoffset -180
            yoffset -300
        Kasian"\"You’re home early today. Didn’t go to school at all or cut classes again?\”"
        Orius"\“Holy- don’t you have college? Why are you home?\”"
        "Kasian just shrugs his shoulders in response."
        Orius"I side-eye the jerk, who walks to the fridge and grabs a bottle of juice out of the fridge."
        Orius"I head to the room, not wanting to get into a fight with him."
        Orius"I don’t have the mental bandwidth to deal with jerks today."
        hide Orius with dissolve
        hide Kasian with dissolve
        jump chp1_con1

    "Go to living room":
        play sound "audio/meow.mp3"fadeout 0.3
        show Orius at left with dissolve:
            xoffset 180
            yoffset -290
        Orius"Kleo’s fat legs thump against the floor as I enter the house."
        Orius"I get in his way to stop him and pick him up."
        Orius"The stupid pile of slime tries to wriggle his way out as if I were trying to abduct him."
        Orius"He looks behind me, that’s when I notice my brother standing in the living room with his arms folded."
        Orius"Busted!"
        Orius"I walk the idiot to my brother and basically shove him in his hands."
        Orius"\“Here, take your ugly pet. He was getting in my way!\”"
        show Kasian at right with dissolve:
            xoffset -180
            yoffset -300
        Kasian"\Was he or were you?\”"
        Orius"..."
        Orius"\“Why are you training to be a marshal? You should’ve become an investigator instead.\”"
        "Kasian raises one hand in surrender while the other hand holds Kleo as he walks back into his room and shuts the door."
        hide Orius with dissolve
        hide Kasian with dissolve
        jump chp1_con1

label chp1_con1:
    scene black with dissolve
    play sound "audio/doorclose.wav"fadeout 0.1
    scene home
    pause 0.5
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"I huff and go to my room, slamming the door behind me. The room is dark, except for the lamp that partially illuminates it."
    Orius"Feeling annoyed at everything, I plop on the bed." 
    play sound "audio/notification.wav"
    Orius"My school’s device dings with a notification reminder of the English essay due soon."
    Orius"\"Ugh...\""
    Orius"This is just great!"
    Orius"First Zaender, then Kasian, then freakin’ Kleo, it’s like everyone wants to get on my nerves today!"
    hide Orius with dissolve


menu:
    Orius"Wait, Kasian is a kiss ass, maybe I can ask for daddy’s little boy’s help?"
    
    "Ask Kasian for help":
        show Orius at left with dissolve:
            xoffset 180
            yoffset -290
        Orius"If there’s anyone who knows or has anything positive to say about Dad, it’s Kasian."
        Orius"He’s the golden child—the star student. Mom adores him, Dad’s proud of him. And me? I hate him for being everything my parents want him to be."
        Orius"Regardless, he’s still my brother, and he’s the only one who’ll get me out of this mess."
        Orius"Anyway, he should have great things to say about Dad, the golden child he is. Ughh!"
        hide Orius with dissolve
        scene black with dissolve 
        play sound "audio/doorknock.mp3"
        scene kasian
        pause 0.5
        show Kasian at right with dissolve:
            xoffset -180
            yoffset -300
        Kasian"\"What?\""
        show Orius at left with dissolve:
            xoffset 180
            yoffset -290
        Orius"\"Need your help with an essay.\""
        Orius"Kasian looks me up and down with an oh so familiar scowl as if I asked him to give me one of his organs."
        Orius"\"I...\""
        Orius"I open my mouth to argue. But he steps aside. Indicating I could come in."
        Orius"What a jerk!"
        hide Orius with dissolve
        hide Kasian with dissolve
        jump chp1_con2

        
    "Share my feelings with Kasian":
        show Orius at left with dissolve:
            xoffset 180
            yoffset -290
        Orius"I don’t wait for him to answer. I just barged into his room."
        hide Orius with dissolve
        scene black with dissolve
        scene kasian
        pause 0.5
        show Orius at left with dissolve:
            xoffset 180
            yoffset -290
        Orius"Privacy be damned!"
        jump chp1_con2

label chp1_con2:
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"\"Hey, I need your help writing this essay about Dad for Mr. Zaender’s class.\""
    show Kasian at right with dissolve:
        xoffset -180
        yoffset -300
    Kasian"\“Didn’t expect you’d need my help. Shouldn’t you…I don’t know, be busy hating my guts?\”"
    Orius"\“Do you wanna help me or not? If you’re gonna act all high and mighty, just say so. I’ll go ask our house AI about him if this is above you.\”"
    Orius"Kasian just chuckles in response, which pisses me off further. I spin on my heels, about to leave when he speaks."
    Kasian"\"Geez, chill out, Ori.\""
    Orius"\"Don’t call me that, clown!\""
    Orius"Kasian puts me in a headlock, ruffling my hair despite my attempts at getting a rise out of him. Mr composed as always."
    Orius"God, I hate his guts."
    Kasian"\"Alright, I’ll help you.\""
    Orius"For a second, I stop struggling."
    Orius"\"You will?\""
    Kasian"\"Yes, I will.\”"
    Orius"\"What's the catch?\""
    Orius"Kasian just smirks in response. Oh, this is going to be fantastic."
    Kasian"\“Defeat me in SkyMarshal IV, I believe our old XJ-3 still has a couple more years left. Win and I’ll write your essay for you.\”"
    hide Orius with dissolve
    hide Kasian with dissolve

        
menu:
    Orius"Of course, that’s his condition. Nobody ever beat him at the game. He was a champion. This was a losing battle from the start."

    "Play SkyMarshal":
        play sound "audio/videogame.mp3" volume 0.5
        show Orius at left with dissolve:
            xoffset 180
            yoffset -290
        Orius"\"This is pointless!\""
        Orius"I throw the console down in frustration. It was the fifth time in a row that Kasian defeated me."
        show Kasian at right with dissolve:
            xoffset -180
            yoffset -300
        Kasian"\"Ori, you’re such a sore loser.\""
        Orius"\"Do you wanna help me or not?\""
        Kasian"\"I will, just beat me once!\""
        stop music fadeout 5
        Orius"\"I can’t! I won’t participate in your bullying anymore!\""
        Orius"\"Besides, shouldn’t singing praise of dad be your favorite pastime?\""
        Orius"\" Just help me with the essay and get it over with!\""
        Kasian"\"Orius, you’re being dramatic, calm down!\""
        Orius"Ungghh!!!"
        Orius"\"Shut up, Kasian! All you have to do is help me write this crappy paper!\""
        Orius"\"I know, you look up to dad and all, but do you have to be a jerk like him in every sense?\""
        hide Kasian with dissolve
        Orius"With that, I ran out of our house toward Star Square."
        hide Orius with dissolve
        jump chp1_con3

    "Refuse":
        stop music fadeout 5
        Orius"\"Do you have to be as difficult as Dad? Can’t you just help me without conditions? Is it that hard?\""
        Orius"\"You know what, forget I asked. Go be dad’s favorite child for all I care!\""
        hide Kasian with dissolve
        Orius"With that, I ran out of our house toward Star Square." 
        hide Orius with dissolve
        jump chp1_con3


label chp1_con3:
    scene black with dissolve
    scene towncenter
    pause 0.5
    show Kasian at right with dissolve:
        xoffset -180
        yoffset -300
    Kasian"\"Orius Wai-Listen!\""
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"\"Leave me alone! I don’t wanna talk to you!\""
    Kasian"\"You’re so dramatic, geez!\""
    Orius"I stop and turn to face him."
    Orius"\"You think I’m being dramatic?\""
    Orius"\"I can’t breathe, live, or exist without getting swallowed up by the expectation to be like you… or him.\""
    Orius"\"You don’t understand! You don’t have it as hard as I do!\""
    Kasian"\"You don’t think I don’t have it hard?\""
    Kasian"\"I do all of this because you don’t have to! So you can live freely as you want.\""
    Kasian"\"And you’re out here moping about what? An English essay that you won’t care about three months from now.\""
    play sound "audio/Hellicopter.mp3" volume 0.3 fadein 1 fadeout 1.0
    Kasian"\"No, you don’t get to stand there and be ungrateful about my sacrifices!\""
    Orius"\"What sacrifices? I bet you didn’t even have to try as hard as I do!\""
    Orius"\"And for me? You don’t even like me!\""
    Kasian"\"Oh, this is rich! You think I don’t care about you? That’s all I-\""
    play sound "audio/explode.mp3"
    scene towncenter with hpunch
    hide Orius with dissolve
    hide Kasian with dissolve
    pause 0.5
    scene black with dissolve

label chp2:
    scene black with dissolve
    pause 2

    scene chapter

    show text "{size=+20}{b}Chapter 2{/b}{/size}" with dissolve
    pause 1.5

    scene black with dissolve

    play music "audio/Act2.ogg" volume 0.5 loop

    pause 0.5
    show text "{b}Sometime later...{/b}" with dissolve
    pause 0.5

    scene home1 with dissolve

    show text "{size=+20}{b}{i}Submission is peace{/i}{/b}{/size}" with dissolve
    pause 1.5
    hide text with dissolve

    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius "Mom was supposed to come home today."
    Orius "Despite the instructions not to leave the house, I still slipped out."
    Orius "I see now why I shouldn’t have."
    Orius "The news earlier this morning said the body count was rising. My neighborhood is quiet. Too quiet."
    Orius "Were people fleeing Caedara? Or are they all already dead?"
    Orius "I wanted to go check out the neighbors, but Mom was coming home."
    Orius "We were out of food, and I needed some air. Just a bit."
    Orius "I couldn’t stand the silence of hiding in my own house anymore. It was deafening."
    Orius "It’ll be quick, Mom."
    Orius "I could already picture her shaking her head in disappointment."
    Orius "I know, I know, I’ll be back in no time."
    hide Orius with dissolve

    scene black with dissolve
    scene war2
    pause 0.5
    woman "\"Help...\""
    play sound "audio/engine.mp3" volume 0.3 fadeout 1

menu:
    Orius"If these are Halo Guards from Aurelios. I’m screwed!" 

    "Go help the person":
        show Orius at left with dissolve:
            xoffset 180
            yoffset -290
        Orius"Okay, we’re doing this, I guess."
        Orius"\"Hey! Are you okay?\""
        Orius"I haven’t spoken out loud ever since that day. My voice startles me."
        Orius"Kasian was killed in the initial attack."
        Orius"My parents? Called to the frontline."
        Orius"Communication lines died the day our world fell apart."
        Orius"With everyone gone, there was no one left to talk to."
        Orius"..."
        Orius"Now is not the time to whine, Orius!"
        Orius"\"Stay calm, I'll help you.\""
        woman"\"...please...please help my baby...\""
        Orius"Baby?"
        play sound "audio/engine.mp3" volume 0.75 fadeout 1
        jump chp2_con


    "Turn around and leave":
        jump chp2_con

label chp2_con:
    Orius"Shit! I can’t die here. I can’t!"
    Orius"Aurelios’ first instinct is to kill."
    Orius"I’m out in the open. One blast and I’ll be a pile of flesh on gravel."
    Orius"\"Hold on, I’ll be back, okay?\""
    woman"\"Please help my baby...please, I beg you!\""
    Orius"I take cover inside a nearby building that’s barely standing."
    Orius"‘I didn’t run away. I’m still here!' \nI wanted to yell back."
    Orius"Hold on a little longer. I’ll be there. I swear!"
    stop music fadeout 5
    play sound "audio/engine.mp3" volume 0.75 fadeout 1
    Orius"Please don’t land, please don’t land, please DO NOT LAND HERE!!"
    hide Orius with dissolve
    pause 1
    play music "audio/Act3.ogg" volume 0.5 loop
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"Finally the hovercraft is gone."
    Orius"\"Are you—\""
    Orius"My heart stops, realizing her hand has gone limp. In denial, I still try shaking her hand, hoping for some miracle. \nI’m on my knees now, breathing hard, feeling helpless"
    Orius"\"No, no, no!\""
    "The woman hadn’t stopped screaming because she was tired. She stopped screaming because she was dead."
    Orius"\"The baby!\""
    Orius"I remember her telling her baby is trapped in there with her."
    Orius"I surge to my feet. \nVeins in my neck pulled taut as I began to shove against the slab." 
    Orius"The concrete groans as it starts moving.\nI push it aside."
    Orius"I see crushed legs first.\nThe bile rises in my throat. \nThen I look at the baby and freeze."
    Orius"Not breathing. \nSilent sobs wracked my body as screams clawed in my throat for release."
    Orius"I walk to the building and punch it — hard enough to shatter something, even if it’s just my goddamn fury."
    hide Orius with dissolve

    scene black with dissolve
    scene war2
    pause 0.5
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"I’m still rocking on the floor. My knees pressed to my chest, eyes red, rimmed from what I witnessed."
    Orius"I hadn’t realized when I walked back home – too shaken up by what I just witnessed."
    Orius"The broken body of the woman."
    Orius"The child she wanted to save, but it was too late. I was too late."
    "Too late.\nToo late.\nToo late."
    Orius"The words kept ringing louder— angrier."
    Orius"I didn’t hear when the lock turned. Didn’t notice my mom holding my face, trying to pull me back to reality."
    hide Orius with dissolve

    scene black with dissolve
    scene war2
    pause 0.5
    
    show mom at right with dissolve:
        xoffset -180
        yoffset -300
    mom"\"Orius!\""
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"Mom's voice was drowned out, faint. She’s trying to anchor me."
    mom"\"Orius, listen to me!\""
    Orius"\"...Mom?\""
    Orius"\"...she died on me. I asked her to hold on, but she died anyway.\""
    Orius"Mom looks concerned. Her hands run through my hair, understanding dawning on her that I ventured out." 
    Orius"\"Was Dad right?\""
    mom"\"Orius, listen—\""
    Orius"\"Our people are dying. Dad was right. I need to fight. I need to protect our people.\""
    mom"\"Orius, listen to me now!\""
    Orius"Mom looks tired. Her face looks like she’s seen things she wishes she could unsee. Strands of gray are already showing.\""
    mom"\"...sigh...I’ve already lost one son to this fucking war. I’ll not lose another\""
    mom"\"No son of mine will be fighting in the war. You’re getting out of here. Now!\""
    mom"\"You’re leaving, now!\""
    Orius"Mom throws a bag. It's packed with my stuffs."
    Orius"\"No! We…we need to fight back!\""
    mom"\"Get a hold of yourself, Orius!\""
    Orius"\"You need to tell Dad. You need to tell him I’m ready—\""
    Orius"I feel desperate, confused, and angry all at once."
    Orius"One minute I’m throwing a tantrum like a kid, the other I’m clutching my face— that stings from the aftermath of the impact."
    mom"\"I said. Get. A. Hold. On. Yourself.\""
    mom"\"You’re getting on that hovercraft or so help me Thalorien, I’ll drag you there myself.\""
    mom"\"One day, you’ll see why I’m telling you this. One day, you’ll thank me for it. \nBut right now? This war? It’s not yours to carry.\""
    Orius"\"But Mom, I don’t wanna go. I don’t wanna leave you.\""
    mom"\"I know, baby.\""
    mom"\"But you have to, for me, please! Run as far away from here as you can. Please.\""
    Orius"\"Okay. Okay, I will.\""
    Orius"\"I will leave.\""
    hide mom with dissolve
    hide Orius with dissolve

    scene black with dissolve
    scene space
    pause 0.5
    show text "{b}A few hours later...{/b}" with dissolve
    pause 1.5
    hide text with dissolve

    show mom at right with dissolve:
        xoffset -180
        yoffset -300
    mom"\"Don’t worry about me, okay?\""
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"...how?"
    Orius"How am I supposed to not worry?"
    "The hovercraft comes into view as we turn another bend."
    mom"\"Here’s some money.\""
    Orius"She was trying to look strong, but her face betrayed her."
    Orius"I could’ve said she’s bad at pretending. But I don’t."
    mom"\"Don’t look back.\""
    mom"\"That’s Captain Draeven Karr. Go with him.\""
    mom"\"He could be a bit of a prick, but he’ll get you to a safe location.\""
    hide Orius with dissolve
    hide mom with dissolve
    "The Halo Guards are approaching. Many people have already been arrested and locked inside their silver ships."
    show mom at right with dissolve:
        xoffset -180
        yoffset -300
    mom"\"Go! Now!\""
    hide mom with dissolve
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"Mom pushes me into the Captain Karr's ship."
    Orius"I press my head against the window, watching mom being restrained by the halo guards."
    Orius"\"Mom!!!\""
    Orius"I look at Captain Karr in despair."
    Orius"\"Help my mom!\""
    Orius"\"They got her. Help my mom.\""
    Orius"\"Please.\""
    show captain at right with dissolve:
        xoffset -180
        yoffset -300
    captain"\"Aww, you want me to help?\""
    Orius"\"Yes, please! Please!\""
    captain"\"No can do, the door is already closed.\""
    captain"\"This ship will only stop at the next station. Now sit your ass back down.\""
    hide captain with dissolve
    hide Orius with dissolve
    "On the other side of the window..."
    show mom at right with dissolve:
        xoffset -180
        yoffset -300
    mom"\"Let me go!\""
    hide mom with dissolve
    show Orius at left with dissolve:
        xoffset 180
        yoffset -290
    Orius"I scramble to the window to see what's happening."
    Orius"Gold bands pulse around her wrists."
    Orius"They’ve put neuro‑lock links on her. Captive restraints."
    Orius"They’re taking her away."
    Orius"\"Stop it!!!\""
    play sound "audio/bang.mp3"
    show Orius with hpunch
    "*Bang*" 
    Orius"\"I said let her go!!!\""
    play sound "audio/bang.mp3"
    show Orius with hpunch
    "*Bang*"
    Orius"The guards shove mom into the back of their Neo‑truck."
    Orius"I claw at the window, watching them going away."
    Orius"..."
    Orius"\"...I'll kill you! I'll kill you all!!!\""
    play sound "audio/bang.mp3"
    show Orius with hpunch
    "*Bang* *Bang* *Bang*"
    Orius"I keep hitting the door even after the sound’s gone."
    Orius"One minute — that’s all it took to destroy everything."
    Orius"My city’s burning. My brother — gone. Mom — taken. Dad — still out there fighting a war I don’t believe in."
    Orius"And me? I’m being shipped off like cargo."
    Orius"I sink to the floor. I’ll never see them again. Never know if Mom survived. Never tell Dad I hated him… or that maybe I didn’t."
    Orius"...and I never tell Kasian that I loved him."
    Orius"\"Hhuurk—!\""
    Orius"My stomach turns; I vomit on the floor."
    Orius"Voices shout — blurred, distant."
    Orius"My vision fades, and before the dark takes me, I see Kasian’s face."
    Orius"\"I’m sorry, Kas.\""
    Orius"And the light in me goes out completely."
    hide Orius with dissolve
    stop music fadeout 3
    scene black with dissolve
    pause 3
    



        




