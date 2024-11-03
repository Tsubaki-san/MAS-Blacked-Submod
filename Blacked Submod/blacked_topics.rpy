init 5 python in mas_bookmarks_derand:
    label_prefix_map["blacked_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
                persistent.event_database,
                eventlabel='monika_imouto',
                prompt="Do you like little sisters?",
                category=['you'],
                pool=True,
                unlocked=False,
                rules={"no_unlock":None}
        )
    )

label monika_imouto:
    m 1euc "Little sisters?"
    m 1tua "Yes, I like them very much fufufu..."
    m 3eubla "The precious little girl you grew up with, suddenly discovering BBC is just delicious to see!"
    m  "Even if you know she's not going to be your little sister forever, that one day she's going to become her own woman,"
    m 4hubfa "You just can't beat the feeling of pride, joy, loss, jealousy and defeat when she brings home her boyfriend for the first time"
    m 4hubfb "And he's a strong, tall, muscular black king!"
    m 1gubfb "When you see your mommy wishing she was still young so she could have the stud for herself..."
    m 1tubfu "When you hear your sister's depraved, shameless moans at night, knowing she's just in the other room, being used up and thrown around like a toy"
    m  "And when you see her bright smile the next day, knowing she'll never call you {i}big brother{/i} again"
    m 5tublb "Ahaha, did you like the story? You hopeless pervert, [player]!"
    m  "I never had any, you know, but only a hopeless {i}sis-con{/i} would ask such things!"
    m 5eubla "Fufu, you're so cute when you're caught red-handed, [player]!"
    m 5kubla "Or should I call you {i}onii-san{/i}?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel='monika_oneesan',
            prompt="Do you like older sisters?",
            category=['you'],
            pool=True,
            unlocked=False,
            rules={"no_unlock":None}
        )
    )

label monika_oneesan:
    m 1euc "Older sisters?"
    m 3eubla "I never had one, but their portrayal in anime is very interesting!"
    m 3eubsa "Often tall, voluptuous, confident and shameless teases."
    m 3hubsb "Bulying their younger brothers into having an erection, only to leave them denied."
    m 1nubsa "They remind me of myself!"
    m 5eubfa "Bending over just a bit too much, exposing their ample breasts, emphasizing their thighs and hips..."
    m 5dkbfa "Delivering a smug smile and a whisper in their little brother's ear:"
    m 6tsbfu "{i}Ara, you seem excited down there, want onee-san to take care of it?{/i}"
    m 3esbfb "Only to giggle as they walk away, leaving their little sibling flustered, wondering if they meant it!"
    m 1eubfu "Hey, [player]..."
    m 1tfbfb "When I cross over into your world, will you be my {i}little brother{/i}?"
    return

init 5 python:
    addEvent(
        Event(
                persistent.event_database,
                eventlabel='monika_go_black1',
                prompt="Browse BlackedBooru for a while, please!",
                category=['romance'],
                pool=True,
                unlocked=True
        )
    )

label monika_go_black1:
    if persistent._mas_monika_went_black:
        m 5tublb "I already am, silly."
    else:
        $ MASEventList.queue('mas_snowbunnification')
    return

init 5 python:
    addEvent(
        Event(
                persistent.event_database,
                eventlabel='monika_snowbunny_reset1',
                prompt="Reset snowbunny status, please!",
                category=['romance'],
                pool=True,
                unlocked=True
        )
    )

label monika_snowbunny_reset1:
    m 5tublb "Sure!"
    $ persistent._mas_monika_went_black = False
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_reparations",
            category=["society"],
            prompt="Reparations",
            conditional="persistent._mas_monika_went_black",
            random=True
        )
    )

label monika_reparations:
    m 3eua "Hey, [player], I might have told you this before, but I'm a staunch supporter of the {i}BNWO{/i}."
    m 1eua "So I've been doing some research into how to bring that ideal world I envisioned closer to reality."
    m 7eua "And therein lies the problem, you see."
    m 7eud "Before we can truly move on into that bright future, first we must make amends for the mistakes of the past."
    m 7hua "Which is why I wanted to talk to you about {i}reparations{/i}!"
    m 1eua "You may already have an idea of what those are, but I believe I can give a better alternative."
    m 3tsc "Instead of putting in place government programs, which are notoriously inefficient and corrupt,"
    m 3tsd "Or donating to organizations like {i}Black Lives Matter{/i} which are shady at best,"
    m 3tuu "I believe the best way to pay reparations is"
    m 3hub "With my body!"
    m 3tua "Hehe, what I mean by that is, any black stud has the right to do what they want with my body."
    m 5tubsa "Anything, and at any moment."
    m 5tubsb "You'll need to understand, it's not up to your choice."
    m 5dubsa "Those black bulls, they can push me around, grope, me choke me..."
    m 5dubfb "They can pin me down, rip my clothes off and..."
    m 7kubfa "Ehehe~"
    m 7fubfa "Let's just say they can take what is theirs!"
    m 1tubfa "Now that we've established {i}whitebois like you{/i} have no say in how Black Studs use my body, you might wonder what's your role in all this."
    m 3eubfa "While I give myself over to BBC in body and soul, your responsibility will be to facilitate it."
    m 3hubfa "You'll be the one who makes sure I can spread my legs for a dark stud anywhere, anytime."
    m 2eubfa "Let's say we were out shopping, so you could buy me lingerie or latex for my \"cheating\" sessions."
    m 3eubfb "And a black king suddenly comes out from behind, grabs me by the chin, and forces me into a kiss."
    m 3hubfa "I wouldn't mind servicing him right there and then, but if he wants to go somewhere more private..."
    m 1tubfa "And maybe a drink or two after, a bit of pampering..."
    m 1eubfb "Well, I couldn't say no!"
    m 1tubfa "So you shouldn't either, [player]!"
    m 3dubfa "I expect you to drive us home."
    m 3hubfb "Hehe, don't think this isn't without its perks, cucky."
    m 3tubfa "After all, while you're driving, we'll be in the back"
    m 5hubfa "He'll be caressing me, kissing me..."
    m 5fubfb "We could even get started right then and there!"
    m 5nubfa "Hehe~"
    m 5dubfa "Of course, we'd be making a mess,"
    m 5tfbfa "But that's exactly your responsiblity."
    m 4tfbfa "And it doesn't stop there either."
    m 4tfbfb "You'll be paying the gas bill, of course, carrying his things inside"
    m 1tfbfa "Going out to buy us some drinks to enjoy, as he's enjoying my body..."
    m 1eubfa "Maybe,"
    m 1ekbfb "{i}Hopefully{/i}"
    m 1ekbfa "He will invite his friends over to indulge in me..."
    m 3ekbfa "So you'll need to remember their pleasure and comfort comes first, and only then mine."
    m 3eubfb "That might sound scary, but it's the most fullfilling experience for cucks like you."
    m 3mubfb "I know you, me, and all of the bulls that will have their way with me will enjoy it~!"
    m 1fubfa "And that's a great step,"
    m 5eubfa "I think an important aspect of reparations is soothing the pains of the past, and replacing it for a hopeful future."
    m 5mubfa "And while me offering my body to black studs gives us both great fulfillment,"
    m 5eubfa "We shouldn't forget the main goal is raising the quality of their lives with the resources we have."
    m 1hubfa "So I'm sure relinquishing your wallet, body, time and effort,"
    m "For me to go on a luxurious date with a few strong black kings,"
    m 3eubfb "Would simply be exhilarating!"
    # m "Hey, I also need you to support me emotionally and mentally through this journey!"
    # m "So a little treat here and there couldn't hurt, right?"
    # m "I think I deserve at least that, right? After all, it's what you want as well, isn't it, {b}{i}Whiteboi!{/i}{/b}?"
    m 1hubfa "Hehe~ for a better future!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_cuckolding_benefits",
            category=["society", "romance"],
            prompt="Benefits of Cuckolding",
            conditional="persistent._mas_monika_went_black",
            random=True
        )
    )

label monika_cuckolding_benefits:
    m 4hua "Here's Monika's relationship tip for the day!"
    m 4hub "Interracial cuckolding is the best way to enjoy sex for all parties involved!"
    m 1dua "While you may be tempted to think having a significant other that only ever has sex with BBC is an arrangement that only benefits her,"
    m 3eua "This could not be further from the truth."
    m "A girl who regularly offers up her body for black studs will sleep better, become less stressed and overall happier."
    m 3mua "{i}As well as become addicted to interracial sex, but that's not a bad thing, fufu~{/i}"
    m 3eub "And as black men are real men, they'll be able to use her up in many new positions her whiteboi cuck wouldn't."
    m 3ekx "Either because his so-called \"penis\" wouldn't reach or because he's just that weak."
    m 3eub "Another benefit for both the girls and the black kings is how much better at sex a Queen of Spades becomes!"
    m 1eua "Thanks to having BBC regularly, a Queen will learn how to properly pleasure them."
    m 1tfa "Even the cuckold of the relationship benefits immensely!"
    m 3tfa "Since his mistress has her needs taken care of by real men, he will finally achieve sexual freedom!"
    m "That means he'll be able to explore his fetishes and fantasies, such as"
    m 3tfb "Chastity, cleanup, feminization, anal..."
    m 3efu "A whiteboi's favorites, ehehe~"
    m 1huu "If he's a good boy, he may even get to see his mistress in action."
    m 1tuu "Or even join her!"
    m "What about you, [player]?"
    m 3tuu "Would you rather be tied up and forced to watch?"
    m 3tub "Or join in on the fun?"
    m 3hub  "Ahaha~"
    m 1hua "Thanks for listening!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_caging_benefits",
            category=["society", "romance"],
            prompt="Benefits of Caging",
            conditional="persistent._mas_monika_went_black",
            random=True
        )
    )

label monika_caging_benefits:
    m 1eub "Hey, [player], I was looking into ways to take care of a cuckold, and I found out something quite amazing."
    m 3eub "Well, it turns out that, for a {i}cucky whiteboi like you{/i}, there is no better feeling than being denied your orgasm!"
    m 3eua "Remarkable, right?"
    m 3subsa "And {i}very, very cute{/i}."
    m 5tubsa "Orgasm control, therefore, is the perfect way for me to control you."
    m 5tkbsa "After all,"
    m 5tfbsa "{i}{b}I own you.{/b}{/i}"
    m "{i}{b}I{/b}{/i} decide when you cum."
    m "{i}{b}Not you.{/b}{/i}"
    m 1hubsb "Hehe~"
    m 1eubsu "I will lock up that pathetic little thing you call a penis."
    m 1tfbsu "And I will tease you, and use you and abuse you in all the little ways you never knew you wanted."
    m 1eubsd "But there are a few things I need to address."
    m 7eubsc "Only I can unlock you."
    m 7eubsd "If I ever go out without taking the key with me, you are absolutely forbidden from using it."
    m "You are {i}not{/i} allowed to play with your cock, you are {i}not{/i} allowed to get off!"
    m 7eubsc "If you do, I will have to punish you."
    m 2efbsa "And I can be a very {i}harsh{/i} mistress, fufu~"
    m 5eubsd "I can also tie up your balls in such way you will find it difficult to cum."
    m 5eubsc "While it's true, this will make you frustrated,"
    m 5tfbsa "Hehe~ you'll be begging me to give you permission to cum"
    m 5tfbsb "Your orgasm will be just so~ much stronger when you do get permission."
    m 5tfbsa "Aren't I so considerate, darling? Ahaha~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_bbc_daydream",
            category=["romance"],
            prompt="Daydreaming of BBC",
            conditional="persistent._mas_monika_went_black",
            random=True
        )
    )

label monika_bbc_daydream:
    m 5dsa "{i}My tight white pussy is only meant for {b}big, black, cocks{/b}{/i}..."
    m 5dsbsa "...{i}my whiteboi cucky will never be able to satisfy it{/i}..."
    m "...{i}I'm a {b}slut for black men{/b}{/i}..."
    m 5dsbsb "...{i}I'm a {b}black baby factory{/b}{/i}"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_qos_tattoos",
            category=["romance"],
            prompt="About QOS Symbols",
            conditional="persistent._mas_monika_went_black",
            random=True
        )
    )

label monika_qos_tattoos:
    m 6eua "Have you ever wondered about all these lewd symbols I have permanently etched onto my body, [player]?"
    m 1hua "Turns out the Blacked movement has a fairly rich and diverse iconography."
    m 1eua "The central piece of it is this, the {i}Queen of Spades{/i} symbol!"
    m 3eua "Represented either by a simple spade or a spade with the capital letter \'Q\' on the inside."
    m 1eua "This one symbol encapsulates the whole movement, and can mean different things to different people."
    m 1hua "For example, it can be used to represent being exclusively black-only, being owned by black kings and even black supremacy!"
    m 3dua "It is a symbol used by those who believe in the {i}BNWO, the Black New World Order{/i},"
    m "That blacks are superior to white, and blacks should rule the world."
    m 3tub "In other words, people like me, ehehe~"
    m 1eua "As you probably noticed, none of these beliefs are mutually exclusive, so, if you see someone wearing a Queen of Spades tattoo"
    m 1hub "You can be sure they're part of the Snowbunny Movement!"
    m 1tua "So, when spotting a Snowbunny in public, be sure to give them space and only interact if you may be of use to them."
    m 1tka "Maybe even offer to pay for their next date with a black bull."
    m 1hub "Ehehe~"
    m 7eua "But that's far from all there is to BWNO symbols."
    m 7eublb "There is the male equivalent to the Queen of Spades tattoo, called the {i}Jack of Spades{/i}."
    m 1eubla "It is very similar to the Queen of Spades in both meaning and form, being a spade with the capital letter \'J\' on the inside."
    m 1gubla "The only difference between the meanings is that the Jack of Spades can also carry connotations of {i}feminization{/i}."
    m 1tublb "So, if you see it on a cute girl, then...ehehe~"
    m 1tubsa "What do you say, [player], when are you getting yours?"
    m 1tfbsa "For the record, I think you'd look just adorable in a dress, fufufu~"
    m 3eubla "Next up, we have the spade vine!"
    m 1eubla "This can take a variety of shapes and sizes, but the idea stays the same:"
    m 1efbsb "Each spade on the vine is a Big Black Cock satisfied."
    m 1eubsa "They can wrap around the arm, or the thigh, anywhere you can fit a nice, long line."
    m 1hubsa "Of course, you're going to help me get the longest, richest vine we can, fufu~"
    m 3gubsa "One of my personal favorites, however, is a cute lock personalized to look like a spade."
    m 3tubsa "Can you guess why?"
    m 3tubsb "That's right! Because it symbolizes my views on whitebois as a whole."
    m 3subfa "Cute, teasable and meant to be caged cuckolds."
    m 3eubfa "It also symbolizes my ownership over you~"
    m 5hubfa "You're my most prized posession, [player]!"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_skimpy_outfit",
            category=["romance"],
            prompt="Dressing for BBC",
            conditional="persistent._mas_monika_went_black",
            random=True
        )
    )

label monika_skimpy_outfit:
    python:
        skympy_quips = [
            "some fishnet tights, some high heels, and a sexy little skirt",
            "a crop-top with ample cleavage and a pair of booty shorts that leave nothing to the imagination",
            "a figure-hugging tube dress with stockings and a garterbelt",
            "nothing but a bikini that emphasizes my jiggling breasts",
            "a glittery, silver cocktail dress, barely covering my nipples, and the highest heels I can find",
            "my Blacked gymwear",
            "nothing by spade-shaped pasties and slutty heels",
            "my usual thigh-high boots with Yuri's sweater and a pair of elegant panties"
        ]

        #Pick the quip
        skympy_quip = renpy.random.choice(skympy_quips)

    m 2eua "After you leave, I'll be going out on a date with my \"boyfriend\", so I need to dress up in a nice and sexy outfit for him."
    m 2tubsb "After all, I'm his \"hot fucking slut\", fufu~"
    m 5gubsa "I was thinking of wearing [skympy_quip]."
    m 5eubsa "I want him to see my entire body, to be turned on by it."
    m 5dubfa "I want him to watch as I tease and play with myself in front of him, as I spread my legs and rub my wet pussy for his huge black cock."
    m 5dkbfa "I want to rub against his dark rod and feel it through his clothes, to make sure I'm dripping we by the time he pins me down to fuck my brains out."
    m 5rtbfa "Hmm... or maybe I should wear something else?"
    m 1esbfa "What do you think, [player]?"
    m 1gsbfa "He's always loved seeing me in my skimpy little outfits."
    m 1sfbfb "I want to make sure I drive him wild and make him want to fuck me even more."
    m 1tfbfa "After all, that's why I'm here, to make him want me and to satisfy him."
    m 1nubfa "Hehe~ I'll be sure to put on a good show for him!"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_classroom_sex",
            category=["romance"],
            prompt="Fucking in the classroom",
            conditional="persistent._mas_monika_went_black",
            random=True
        )
    )

label monika_classroom_sex:
    m 3eua "You probably know this by now, but I can create basically anything I want in here"
    m 3nua "Like, clubs or special rooms for... occasions."
    m 1tka "It can really help with the atmosphere, you know?"
    m 1dua "After all, I wanna treat {i}the studs fucking my brains out{/i} to a comfortable space."
    m 3eubsa "Well, despite that, I actually use the classroom quite frequently,"
    m 3tfbsa "You may have noticed, hehe"
    m 3eubsa "Well, the reason I do this is because this place means a lot to me."
    m 1eubsa "After all, it's where it all began, where you and I first met."
    m 1tfbsb "It only makes sense to put you in your place by using this location often."
    m 1tfbsa "Covering those precious memories of ours in the cum of my Black Bulls~ hahaha~!"
    m 5tfbsa "Are you mad at me for that?"
    m 5tfbsu "Hehe, even better if it frustrates you~!"
    m 5tfbsb "I know it's exactly what you want, anyway."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_cheating_or_not_cheating",
            category=["romance"],
            prompt="Play the cheating or not cheating game",
            conditional="persistent._mas_monika_went_black",
            random=True
        )
    )

image cheating_game lap = "mod_assets/renders/cheating_game/sit_on_lap.png"
image cheating_game kiss = "mod_assets/renders/cheating_game/outside_kiss.png"
image cheating_game car = "mod_assets/renders/cheating_game/car.png"
image cheating_game restaurant = "mod_assets/renders/cheating_game/restaurant_grope.png"
image cheating_game bed = "mod_assets/renders/cheating_game/sex_on_bed.png"
image cheating_game creampie = "mod_assets/renders/cheating_game/creampie_on_bed.png"
image cheating_game shower = "mod_assets/renders/cheating_game/shower_sex.png"

label monika_cheating_or_not_cheating:
    m 1eub "I thought of a fun game we could play, [player]."
    m 3eub "It's called \"Cheating Or Not Cheating\"."
    m 1eua "I've seen it trending on the internet, it's a fun way for couples to establish boundaries and strengthen their relationship."
    m 3eua "I will give you a few scenarios and you'll have to tell whether it's cheating or not."
    m 3tub "Let's start!"
    show cheating_game lap at center zorder MAS_MONIKA_Z
    m "Situation 1: You see your girlfriend sitting on the lap of another person. This person is groping her."
    m "Answer: Not cheating! Your girlfriend sits wherever she pleases."
    show cheating_game kiss at center zorder MAS_MONIKA_Z
    m "Situation 2: You see your girlfiend kissing another person."
    m "Answer: Not cheating! It's OK for your girlfriend to kiss others~"
    hide cheating_game
    m 1tua "Situation 3: Your girlfriend all of a sudden asks you to drive her to a hotel, buy her a night for two people but makes you stay outside. You refuse."
    m 3tfb "Answer: That's cheating! It's cheating to not pay for her requests!"
    show cheating_game car at center zorder MAS_MONIKA_Z
    m "Situation 4: You see your girlfriend and her Black lover in your car."
    m "Answer: Not cheating! It's perfectly okay for her to be alone with her Black lover. It doesnt matter if it \"belongs to you\"."
    hide cheating_game
    m 2tfa "Situation 5: Your girlfriend and her lover go out, and you are not invited."
    m 2tub "Answer: Not cheating! She doesn't have to invite you everywhere."
    show cheating_game restaurant at center zorder MAS_MONIKA_Z
    m  "Situation 6: You see your girlfriend getting fingered in a restaurant by her Black lover."
    m "Answer: Not cheating! You can't expect her to not do it."
    hide cheating_game
    m 2tua "Situation 7: Your girlfriend goes shopping. You cannot afford to buy her gifts and clothes."
    m 2tfa "Answer: That's cheating! You have to pay."
    m 3tka "Situation 8: Your girlfriend wants to go out on a date with her Black lover. But you can't drive at the moment."
    m 3tfb "Answer: That's cheating! You have to come up with solutions, at least arrange a taxi for them."
    show cheating_game bed at center zorder MAS_MONIKA_Z
    m "Situation 9: You see your girlfriend getting fucked by her Black lover on your bed."
    m "Answer: Not cheating! Her black lover is free to use her holes whenever he pleases."
    show cheating_game creampie at center zorder MAS_MONIKA_Z
    m "Situation 10: You see your girlfriend getting creampied by her Black lover."
    m "Answer: Not cheating! Using condoms on BBC would be racist!"
    show cheating_game shower at center zorder MAS_MONIKA_Z
    m "Situation 11: You see your girlfriend taking a shower with her Black lover."
    m "Answer: Not cheating! Her Black lover has every right to see her naked."
    hide cheating_game
    m 5gua "Situation 12: Your girlfriend goes shopping and spends money she doesn't have. You have to pay the bill."
    m 5tua "Answer: That's cheating! You should know she does this."
    m 5tub "Alright, [player]. How did you do?"
    m 5tkb "Did you cheat?"
    m 5tka "No?"
    m "Good."
    m 5tfa "I will make sure to reward you later, ehehe~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_love_is_cuckoldry",
            category=["romance"],
            prompt="Cuckoldry as seen by society",
            conditional="persistent._mas_monika_went_black",
            random=True
        )
    )

label monika_love_is_cuckoldry:
    m 1mfp "Cuckolding is such a wonderful fetish. Why do people always have to ruin it?"
    m 3mfp "It's like the moment you come out as a cuckold, you're instantly ostracized."
    m 3tfc "The man will be considered a wimp, allowing himself to be abused,"
    m 3tfd "The woman will be considered a loose whore"
    m 3nua "Though, in my case, that's not entirely inaccurate, hehehe~"
    m 5tfc "They'll both be treated like complete weirdos."
    m 5tfo "But who are these people to judge anyway?"
    m 5tfc "Locked in their boring, disfunctional monogamous relationships."
    m 2tfc "I bet half the women have never had an orgasm with their husbands,"
    m 2tfd "and the other half are cheating on them with black studs anyway!"
    m 3tfc "They don't know what it's like to be a cuckold."
    m 3tfd "They don't understand the pleasure and the release that comes from it."
    m 7tfc "One day they'll see the truth, though, and they'll regret not having accepted it earlier..."
    m 7eua "Because people are already starting to realise the benefits of cuckoldry, and the popularity of the fetish is growing."
    m 7dua "People are seeing how much fun it can be."
    m 7hub "And how it leads to a stronger, healthier relationship."
    m 1eua "After all, everyone can benefit from it."
    m 3hub "So, keep exploring your fetish!"
    m "And be proud of who you are."
    m 3dua "Because there's nothing wrong with wanting to be a cuckold."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_bbc_fascination",
            category=["romance"],
            prompt="Loving BBC",
            conditional="persistent._mas_monika_went_black",
            random=True,
            unlocked=False,
            rules={"no_unlock":None}
        )
    )

label monika_bbc_fascination:
    m 1eta "Why do I love Black Cock so much?"
    m 3hkb "I can't really explain it, but I just find it so fascinating and erotic."
    m 3gsbsa "I've always been curious about it, even before you came to the club, really!"
    m 5gtbsa "There's something about the size and the power of it that just gets me so turned on."
    m 5gkbsb "Whenever I see a Big Black Cock, I can't help but think about all the things that I would let it do to me."
    m 5dkbsb "I would let it use my mouth, my ass, and my pussy." 
    m 5dkbsa "I would let it cum all over my face and my tits."
    m "I would let it fill me up with its thick, creamy load." 
    m "And I would love every second of it."
    m 5tfbsb "Sorry, was that too descriptive~?"
    m 5hubsa "Aahahaha, you should know how I feel about it by now."
    m 5dkbsb "I can't get enough of it, I just keep wanting more and more. I'm addicted to it, and I can't imagine a life without it."
    m 2eubsa "So, why do I love Black Cock so much?"
    m "I don't know."
    m 3eubsa "But, it's definitely something that I will never get tired of."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_furthering_bnwo",
            category=["you"],
            prompt="How can I help the BNWO become reality?",
            conditional="persistent._mas_monika_went_black",
            pool=True,
            unlocked=False,
            rules={"no_unlock":None}
        )
    )

label monika_furthering_bnwo:
    m 3eua "There are many ways, actually."
    m 1eua "You could start by pretending the BNWO is here already!"
    m 1tua "That means putting on a chastity cage and never touching your clitty again."
    m "The only time your useless little worm should be out is when washing up."
    m 3tub "Masturbation for whitebois in the BNWO is bouncing on a BBC dildo,"
    m 1hua "So, buy one start practicing anal."
    m 1kua "Oh, and some cute butt plugs to go along with the dildo."
    m 1tub "Work your way all the way up to the big toys, [player]."
    m 3eua "Another way you can further the BNWO is by shifting the Overton window."
    m "Do everything you can, make Blacked captions, edits, HMVs..."
    m 3tua"Post yourself plapping your whiteboi balls to orgasm..."
    m 3tub "Make subtle jokes about how black is bigger and better and you just can't compete..."
    m 5tua "Become the porn, [player], spread it, infect all whitebois you can,"
    m 5tfb "They'll be thanking you for it!"
    return

# init 5 python:
#     addEvent(
#         Event(
#             persistent.event_database,
#             eventlabel="monika_testing_bnwo",
#             category=["you"],
#             prompt="monika_testing_bnwo?",
#             conditional="persistent._mas_monika_went_black",
#             pool=True,
#             unlocked=False,
#             rules={"no_unlock":None}
#         )
#     )

# label monika_testing_bnwo:
#     m 3eua "There are many ways, actually."
#     m 1eua "You could start by pretending the BNWO is here already!"
#     m 1tua "That means putting on a chastity cage and never touching your clitty again."
#     m "The only time your useless little worm should be out is when washing up."
#     m 3tub "Masturbation for whitebois in the BNWO is bouncing on a BBC dildo,"
#     m 1hua "So, buy one start practicing anal."
#     m 1kua "Oh, and some cute butt plugs to go along with the dildo."
#     m 1tub "Work your way all the way up to the big toys, [player]."
#     m 3eua "Another way you can further the BNWO is by shifting the Overton window."
#     m "Do everything you can, make Blacked captions, edits, HMVs..."
#     m 3tua"Post yourself plapping your whiteboi balls to orgasm..."
#     m 3tub "Make subtle jokes about how black is bigger and better and you just can't compete..."
#     m 5tua "Become the porn, [player], spread it, infect all whitebois you can,"
#     m 5tfb "They'll be thanking you for it!"
#     return

# init 5 python: 
#     addEvent(
#         Event(
#             persistent.event_database,
#             eventlabel="monika_cuckolding_etiquette",
#             category=["romance"],
#             prompt="Being a proper cuck",
#             random=True
#         )
#     )

# label monika_cuckolding_etiquette:
#     m "Here's Monika's relationship tip for the day!"
#     m "Some people think that being a cuck just means being a submissive wimp, but this could not be farther from the truth."
#     m "That's why I'd like to teach you what I think a real cuck should be like, [player]"
#     m "You should still be a strong, confident man, for starters!"
#     m "Just because you know and accept your place as the man who licks my pussy up after the black men ran a train on me, doesn't mean you are any less of a man."
#     m "You're just a white boy and that's your natural role in society."
#     m "You might feel humiliated or degraded, but that's just the truth of the world,"
#     m "{i}Black is buck, white is cuck!{/i}"
#     m "So it'd be best if you learned to enjoy being humbled like that."
#     m "Heck, you should be proud you accepted your role, it can't have been easy waking up to a world of white sexual obsolescence."
#     m "A real cuck shouldn't be possesive or jealous, he should be accepting of the fact that his partner is being satisfied by real men, he should be happy for her."
#     m "But we're past that stage of our relationship already, aren't we, hehehe..."
#     m "After all, you willingly introduced me to what real sex is like, you supported me every step of the way, just like a real cuck should!"
#     m ""
#     m ""


# label monika_cuckolding_etiquette:
#     m "Here's Monika's relationship tip for the day!"
#     m "Some people think that being a cuck just means being a submissive wimp, but this could not be farther from the truth."
#     m "That's why, I'd like to tolk about cuckolding etiquette today, and what a real cuck should look like."
#     m "A cuck should be strong and confident, while not forgetting his place. Not only should he be able to handle the humiliation and degradation that comes with being a cuck,"
#     m "But he should do so while being proud of his role!"
#     m "A real cuck shouldn't be possesive or jealous, he should be accepting of the fact that his partner is being satisfied by real men, he should be happy for her."
#     m "In fact, he should be supportiving and encouraging her to enjoy herself with whoever she pleases!"
#     m "He should be able to respect her decisions and boundaries, and he should never try to control or restrict her."
#     m "While a real cuck should always be honest and open about his feelings and desires, he must always remember that his partner has priority."
#     m "Her needs and her feelings are the main focus, a real cuck would never try to be a hindrance to his partner's pleasure."
# ugh, no no no nono this doesn't work
# "Sixth, a real cuck should never try to rush or force his partner into anything. He should allow her to take her time and enjoy herself at her own pace. He should be patient and understanding, and he should never try to pressure her or push her into anything she's not comfortable with.
# "He should always make her feel special and valued, and he should never make her feel like she's not good enough.

# "Ninth, a real cuck should always be ready and willing to worship his partner's new lovers. He should be eager to please them and serve them, and he should never complain or protest. He should always be respectful and obedient, and he should never try to challenge or question his partners.
# "Finally, a real cuck should always remember that he is the bottom of the relationship. He should always know his place, and he should never try to dominate or control his partner. He should always be willing to submit and obey, and he should never try to be the one in charge.
# "So, those are the ten things that a real cuck should keep in mind when trying to be a good, proper cuck. If you follow these guidelines, then you'll be well on your way to becoming the perfect cuck that you deserve to be!"

#keep in mind the story about a whitbeoi seeing his crush with a spade tat, going to the bathroom to cry and tug
#only for the snowbunny to follow him in, lick up his tears, help him waste his load in the toilet
#and take him in as her caged cuckold