

label start:

    "The war came silently. Without a noise. \nBut the damage it left was insurmountable."
    "Our once prosperous quadrant, Caedara, was left burning. Our people are being forced to leave the only home they\’ve known their whole lives."
    "There\’s an announcement on the news, Aurelios has taken down another Caedara\’s Regiment, and that\’s put immense pressure on the entire military base."
    "Aurelios this, Aurelios that. All anyone these days hears about is Aurelios, it\’s like they want us coming generations to remember who exactly we denied power by not surrendering."
    "The war started over Trionium— a powerful element capable of leveling entire zones."
    "They came with trade propositions first. Then threats. Then, rained beams on us when Caedara refused to fold, refused to let Trionium fall in the wrong hands."
    "Aurelios took it upon themselves to personally teach us a lesson."
    "And lesson they taught."

    jump chp1

label chp1:

    scene black with dissolve

    show text "Chapter 1\nA Day in the Life" with Pause(1.5)

    scene black with dissolve

    scene your_scene_title

    "{b}6 Days Earlier…{b}"
    "A high pitched alarm clock sounds off."
    "Yesterday was rough, another speech from dad about \“growing up\” and how a \“soft heart is luxury\”, nothing I haven\’t heard before. \nI understand where he\’s coming from but it just feels like he isn\’t listening, like no matter what I do I won\’t live up to the expectations of the great Sorin Morvayne."
    "My parents are both off saving the world leaving me here to get ready for school. I should get ready. I only have a couple weeks left before school lets out, but man I don\’t want to. Mom always says that if I want to get anywhere in life I need to focus on my studies. Neither of them are here though, I could always just skip."

    jump chp2
    
label chp2:

    scene black with dissolve

    show text "Chapter 2\nHomecoming" with Pause(1.5)

    scene black with dissolve

    scene your_scene_title

    "{b}6 Days later…{b}"
    #"{size=*2}{b}\“Submission is peace\”{b}{size=*2}"
    "Aurelios\’ message flashes on every wall my eyes can see. "
    "Mom was supposed to come home today."
    "Despite the instructions not to leave the house, I still slipped out."
    "I see now why I shouldn\’t have."
    "Smoke coiled from every building. Not from the chimneys — but from a fire that had meant to kill."
    "The news earlier this morning said the body count was rising. My neighborhood is quiet. Too quiet"
    "Were people really fleeing Caedara? Or are they all already dead?"
    "I wanted to go look, but my mom was coming home, we were out of food, and I needed some air. \nJust a bit. From hiding in my own home in my own country."
    "It\’ll be quick, mom. \nI tried to speak to her in my imagination, and she shook her head in disappointment. \nI know, I know I\’ll be back in no time."
    "Maybe…maybe, I spoke too soon."
    "\“Help…\” a choked voice came. I whipped my head in their direction."
    "Buried under the rubble, I saw a hand peeking through, asking someone, anyone, to come rescue them. \nI look around, and theren’s no one in sight. I take a step forward when I hear a loud engine sound overhead. Someone was coming, and it was Halo Guards from Aurelios. I\’m screwed!"

label choice:
    $ save_name = "Question Menu"
    menu:
        set seen_set
        "Go help the person"
        jump continue_chp2
        "Turn around and leave"
        jump continue_chp2

label continue_chp2:
    "I have half a mind to ignore it and just walk away. \nMy legs, as if they had a mind of their own, move forward before I can convince myself to look away."
    "Okay, we\’re doing this, I guess."
    "In two strides, I close the distance between me and this struggling person."
    "{size=*2}{b}/n“Hey! Are you okay?/n”{size=*2}{b}"
    "My voice comes out shaky and strained. It startles me—strange, unfamiliar, like it belongs to someone else. \nI haven\’t spoken out loud in months."
    "My brother was killed in the initial attack. \nMy parents? Called to the frontline. Communication lines died the day our world fell apart."
    "With that and my parents gone, there was no one left to talk to."
    "Now is not the time to whine Orius! I grit my teeth while moving the slab."
    "\“Please help my baby,\” the voice says."
    "Baby?"


    

    return
