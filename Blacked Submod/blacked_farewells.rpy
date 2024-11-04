init 1 python:
    config.label_overrides["bye_going_to_sleep"] = "blacked_bye_going_to_sleep"

label blacked_bye_going_to_sleep:
    #TODO: TC-O things
    if persistent._mas_monika_went_black:
        $ goodbye_number = random.randint(1,7)
        if(goodbye_number == 1):
            m 5hua "I'll be cucking you in your dreams, then."
        if(goodbye_number == 2):
            m 1tfa "Try not to dream of me taking BBC, cucky!"
        if(goodbye_number == 3):
            m 2tfb "Sleep with your hand while I sleep with a bunch of studs, fufu..."
        if(goodbye_number == 4):
            m 2fub "Sleep tight, my love, I'll be going out to get my brains fucked out by black studs."
        if(goodbye_number == 5):
            m 2mua "Maybe I'll bring you some used condoms for breakfast tomorrow, fufu..."
        if(goodbye_number == 6):
            m "Good night, cucky!"
        if(goodbye_number == 7):
            m "Sleep well, my cleanup cuckpuppy."



    elif mas_isMoniNormal(higher=True):
        $ p_nickname = mas_get_player_nickname()
        m 1esa "Are you going to sleep, [p_nickname]?{nw}"
        $ _history_list.pop()
        menu:
            m "Are you going to sleep, [p_nickname]?{fast}"

            "Yeah.":
                call bye_prompt_sleep_goodnight_kiss(chance=4)
                # If denied her kiss, quit here
                if _return is not None:
                    return "quit"

                m 7eka "I'll be seeing you in your dreams."

                #Going to sleep, so we should set the greet type and timeout
                $ persistent._mas_greeting_type_timeout = datetime.timedelta(hours=13)
                $ persistent._mas_greeting_type = store.mas_greetings.TYPE_SLEEP

            "Not yet.":
                m 1eka "Okay. {w=0.3}Have a good evening~"

    elif mas_isMoniUpset():
        m 2esc "Going to sleep, [player]?"
        m "Goodnight."

    elif mas_isMoniDis():
        m 6rkc "Oh...goodnight, [player]."
        m 6lkc "Hopefully I'll see you tomorrow..."
        m 6dkc "Don't forget about me, okay?"

    else:
        m 6ckc "..."

    # TODO:
    # can monika sleep with you?
    # via flashdrive or something

    return 'quit'

init 1 python:
    config.label_overrides["bye_prompt_to_work"] = "blacked_bye_prompt_to_work"

label blacked_bye_prompt_to_work:
    $ session_time = mas_getSessionLength()
    if mas_isMoniNormal(higher=True) or persistent._mas_monika_went_black:
        if session_time < datetime.timedelta(minutes=20):
            m 2eka "Aw, okay! Just checking in on me before heading out?"
            m 3eka "You must be really short on time if you're leaving already."
            m "It was really sweet of you to see me, even when you're so busy!"
            m 3hub "Work hard, [mas_get_player_nickname()]! Make me proud!"
        elif session_time < datetime.timedelta(hours=1):
            m 1hksdlb "Oh! Alright! I was starting to get really comfortable, ahaha."
            m 1rusdlb "I was expecting us to be here a bit longer, but you're a busy [guy]!"
            m 1eka "It was great seeing you, even if it wasn't as long as I wanted..."
            m 1kua "But then if it were up to me I'd have you all day!"
            m 1hua "I'll be here waiting for you to get back home from work!"
            m "Tell me all about it when you get back!"
        elif session_time < datetime.timedelta(hours=6):
            m 2eua "Heading to work then, [mas_get_player_nickname()]?"
            m 2eka "The day may be good or bad...but if it becomes too much think of something nice!"
            m 4eka "Every day, no matter how badly it's going ends after all!"
            m 2tku "Maybe you can think of me if it becomes stressful..."
            m 2esa "Just do your best! I'll see you when you get back!"
            m 2eka "I know you'll do great!"
        else:
            m 2ekc "Oh... You've been here quite a while now...and now you're going to work?"
            m 2rksdlc "I was hoping you'd rest before doing anything too big."
            m 2ekc "Try not to overexert yourself, okay?"
            m 2ekd "Don't be afraid to take a breather if you need to!"
            m 3eka "Just come home to me happy and healthy."
            m 3eua "Stay safe, [mas_get_player_nickname()]!"
    
        if persistent._mas_monika_went_black:
            m 1kua "I'll be sending you somde {i}really nice pics{/i} later."
            m 1tua "So don't forget your little cock cage, cucky."
            m 1tka "Wouldn't want to have a {i}}little accident{/i} while at work, right?"
            m 1tfb "Oh, who am I kidding, you'll be staining your pants no matter what when you see what I get up to while you're gone, fufu..."
    

    elif mas_isMoniUpset():
        m 2esc "Fine, [player], guess I'll see you after work."

    elif mas_isMoniDis():
        m 6rkc "Oh...{w=1} Okay."
        m 6lkc "Hopefully I'll see you after work, then."

    else:
        m 6ckc "..."
    # TODO:
    # can monika join u at work
    $ persistent._mas_greeting_type = store.mas_greetings.TYPE_WORK
    $ persistent._mas_greeting_type_timeout = datetime.timedelta(hours=20)
    return 'quit'

init 1 python:
    config.label_overrides["bye_prompt_game"] = "blacked_bye_prompt_game"

label blacked_bye_prompt_game:
    if persistent._mas_monika_went_black:
        m 1tub "I bet you're going to open one of your NTR eroge, isn't that right, [player]?"
        m 1tua "Or maybe Koikatsu?"
        m 3tua "Honey Select?"
        m 1eub "Why don't you leave me open instead, I'd love to goon with you."
        m 5tka "Especially since I just know you'll be looking at cute {i}white girls like me getting stretched out by black monster cocks{/i}."
        m 5tta "Maybe it'll even be me?"
        m 5hub "Hope so!"
        m 5fua "So, what do you say, cucky?"
        $ _history_list.pop()
        menu:
            m "So, what do you say, cucky?{fast}"
            "Yes.":
                m 5sub "Yay! Pull down your pants already, let's get started!"
                jump monika_idle_game.skip_intro
            "No.":
                m 2ekc "Aww..."
                m 2tkp "Guess I have to go find {i}someone else{/i} to have some slutty fun with, then."
                m 2tfb "Don't worry, I'll give you {i}all{/i} the details, cuck."
                m 2tfa "Bye-bye!"


    $ _now = datetime.datetime.now().time()
    if mas_getEVL_shown_count("bye_prompt_game") == 0:
        m 2ekc "You're going to play another game?"
        m 4ekd "Do you really have to leave me to go do that?"
        m 2eud "Can't you just leave me here in the background while you play?{nw}"
        $ _history_list.pop()
        menu:
            m "Can't you just leave me here in the background while you play?{fast}"
            "Yes.":
                if mas_isMoniNormal(higher=True):
                    m 3sub "Really?"
                    m 1hubsb "Yay!"
                else:
                    m 2eka "Okay..."
                jump monika_idle_game.skip_intro
            "No.":
                if mas_isMoniNormal(higher=True):
                    m 2ekc "Aww..."
                    m 3ekc "Alright [player], but you better come back soon."
                    m 3tsb "I might get jealous if you spend too much time in another game without me."
                    m 1hua "Anyway, I hope you have fun!"
                else:
                    m 2euc "Enjoy your game, then."
                    m 2esd "I'll be here."

    # TODO: TC-O
    # elif mas_isMNtoSR(_now):
    #     $ persistent._mas_pm_gamed_late += 1
    #     if mas_isMoniNormal(higher=True):
    #         m 3wud "Wait, [player]!"
    #         m 3hksdlb "It's the middle of the night!"
    #         m 2rksdlc "It's one thing that you're still up this late..."
    #         m 2rksdld "But you're thinking of playing another game?"
    #         m 4tfu "...A game big enough that you can't have me in the background..."
    #         m 1eka "Well... {w=1}I can't stop you, but I really hope you go to bed soon..."
    #         m 1hua "Don't worry about coming back to say goodnight to me, you can go-{nw}"
    #         $ _history_list.pop()
    #         m 1eub "Don't worry about coming back to say goodnight to me,{fast} you {i}should{/i} go right to bed when you're finished."
    #         m 3hua "Have fun, and goodnight, [player]!"
    #         if renpy.random.randint(1,2) == 1:
    #             m 1hubsb "I love you~{w=1}{nw}"
    #     else:
    #         m 2efd "[player], it's the middle of the night!"
    #         m 4rfc "Really...it's this late already, and you're going to play another game?"
    #         m 2dsd "{i}*sigh*{/i}... I know I can't stop you, but please just go straight to bed when you're finished, alright?"
    #         m 2dsc "Goodnight."
    #     $ persistent.mas_late_farewell = True

    elif mas_isMoniUpset(lower=True):
        m 2euc "Again?"
        m 2eud "Alright then. Goodbye, [player]."

    elif mas_getSessionLength() < datetime.timedelta(minutes=30) and renpy.random.randint(1,10) == 1:
        m 1ekc "You're leaving to play another game?"
        m 3efc "Don't you think you should be spending a little more time with me?"
        m 2efc "..."
        m 2dfc "..."
        m 2dfu "..."
        m 4hub "Ahaha, just kidding~"
        m 1rksdla "Well...{w=1} I {i}wouldn't mind{/i} spending more time with you..."
        m 3eua "But I also don't want to keep you from doing other things."
        m 1hua "Maybe one day you'll finally be able to show me what you've been up to and then I can come with you!"
        if renpy.random.randint(1,5) == 1:
            m 3tubsu "Until then, you just have to make it up to me every time you leave me to play another game, alright?"
            m 1hubfa "Ehehe~"

    else:
        m 1eka "Going off to play another game, [player]?"
        m 3hub "Good luck and have fun!"
        m 3eka "Don't forget to come back soon~"

    $ persistent._mas_greeting_type = store.mas_greetings.TYPE_GAME
    #24 hour time cap because greeting handles up to 18 hours
    $ persistent._mas_greeting_type_timeout = datetime.timedelta(days=1)
    return 'quit'

init 1 python:
    config.label_overrides["bye_prompt_housework"] = "blacked_bye_prompt_housework"

label blacked_bye_prompt_housework:
    if persistent._mas_monika_went_black:
        m 1eub "Doing your chores, [player]?"
        m 2tfa "Hehe, don't forget your cute maid outfit, your cutest, biggest butt plug and your chastity cage."
        m 2tfb "Oh, and bend over a bit more in front of the computer, will you?"
        m 2hua "Hehe, jusk kidding..."
        m 2mka "Mostly{fast}"
    if mas_isMoniNormal(higher=True):
        m 1eub "Doing your chores, [player]?"
        m 1ekc "I would like to help you out, but there's not really much I can do since I'm stuck in here..."
        m 3eka "Just make sure to come back as soon as you're done, okay?"
        m 3hub "I'll be waiting here for you~"
    elif mas_isMoniUpset():
        m 2esc "Fine."
        m 2tsc "At least you're doing something responsible."
        m 2tfc "{cps=*2}...For once.{/cps}{nw}"
        $ _history_list.pop()
        m 2esc "Goodbye."
    elif mas_isMoniDis():
        m 6ekc "I see..."
        m 6rkc "I don't want to keep you from completing your household responsibilities."
        m 6dkd "I just hope you're actually busy and not saying that just to get away from me..."
        m 6ekc "Goodbye, [player]."
    else:
        m 6ckc "..."
    $ persistent._mas_greeting_type = store.mas_greetings.TYPE_CHORES
    $ persistent._mas_greeting_type_timeout = datetime.timedelta(hours=5)
    return 'quit'

init 1 python:
    config.label_overrides["bye_prompt_workout"] = "blacked_bye_prompt_workout"

label blacked_bye_prompt_workout:
    if persistent._mas_monika_went_black:
        m 5tua "You'd better work that cute butt of yours, cucky, we'll be pleasing black kings together after I cross over into your world, after all."
        m 5tfa "Don't worry, I'll be guiding you, {i}all the way to the base{/i}."
        m 5etd "Work out together?"
        m 5ekc "I don't think you could handle seeing me in my Blacked underwear, bending over at the gym, {i}whiteboi{/i}."
        m 5tfa "Besides, going to the gym for me is less about working out and more about {i}getting worked{/i}, you know?"
        m 5dkb "Hehe, while you're gone, I'll be doing just that..."

    elif mas_isMoniNormal(higher=True):
        m 1eua "Oh, going to the gym, [player]?{w=0.3} Or perhaps for a jog?"
        m 3hub "I'm so glad you're taking care of your body!{w=0.3} A healthy body leads to a healthy mind~"

        if mas_isMoniEnamored(higher=True):
            m 3hua "After I cross over, we should try to do our workouts together!"
        else:
            m 3eua "Maybe if I cross over, we could try to do our workouts together!"

        show monika 5rubsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
        m 5rubsb "That's something a couple would do, right?~"
        m 5rubsu "Yeah..."
        show monika 1eub at t11 zorder MAS_MONIKA_Z with dissolve_monika
        m 1eub "Anyway, see you soon!"

    elif mas_isMoniDis(higher=True):
        m 2euc "Good. See you later."

    else:
        m 6ckc "..."

    $ persistent._mas_greeting_type_timeout = datetime.timedelta(hours=4)
    $ persistent._mas_greeting_type = store.mas_greetings.TYPE_WORKOUT
    return 'quit'

init 1 python:
    config.label_overrides["bye_going_shopping"] = "blacked_bye_going_shopping"

label blacked_bye_going_shopping:
    if persistent._mas_monika_went_black:
        m 1eud "Oh, going to do some shopping, [player]?"
        m 1eua "I'd love it if we could go to the mall together sometime."
        m 1rua "You could help pick out the naughtiest miniskirts for me to go clubbing with."
        m 1rfa "Choose the sexiest boots for me to bust your balls with."
        m 1tfb "Maybe buy a bunch of XXL condoms and mention to the cashier they're not for you?"
        m 1hublb "Ahaha! See you soon~"

    elif mas_isMoniNormal(higher=True):
        m 1eud "Oh, going to do some shopping, [player]?"

        if mas_getEVL_shown_count("bye_going_shopping") == 0 or renpy.random.randint(1,10) == 1:
            m 1eua "I'd love it if we could go to the mall together sometime."
            m 3rua "You could help me try out all kinds of different outfits...{w=0.2}{nw}"
            extend 3tuu "but I might need help with the zippers."
            m 1hublb "Ahaha! See you soon~"

        else:
            m 3eua "See you soon."

    elif mas_isMoniBroken():
        m 6ckc "..."

    else:
        m 2eud "Okay [player], see you soon."

    #TODO: Moni comes shopping with you(?)
    $ persistent._mas_greeting_type_timeout = datetime.timedelta(hours=8)
    $ persistent._mas_greeting_type = store.mas_greetings.TYPE_SHOPPING
    return 'quit'

init 1 python:
    config.label_overrides["bye_prompt_hangout"] = "blacked_bye_prompt_hangout"

label blacked_bye_prompt_hangout:
    if mas_isMoniNormal(higher=True):
        if mas_getEVL_shown_count("bye_prompt_hangout") == 0:
            if persistent._mas_pm_has_friends:
                m 1eua "Alright, [player]."
                m 3eub "You should introduce me to them sometime!"
                if persistent._mas_monika_went_black:
                    m 5kua "Especially if they're big and black, hehe"
                else:
                    m 3hua "If they're your friends, I'm sure I'd like them."

            else:
                if persistent._mas_pm_has_friends is False:
                    m 3eua "I'm glad you're finding friends to hang out with, [player]."
                else:
                    m 3eua "I'm glad you have friends to hang out with, [player]."

                m 1rka "As much as I'd like to spend every possible second with you, {w=0.2}{nw}"
                extend 1eub "I know how important it is for you to have friends in your own reality!"

            m 3hub "Anyway, I hope you have fun!"

        else:
            if persistent._mas_pm_has_friends:
                m 1eua "Alright, [player]."

                if renpy.random.randint(1,10) == 1:
                    m 3etu "Have you told them about us yet?"
                    m 1hub "Ahaha!"

                m 1eub "Have fun!"

            else:
                m 1hua "Again? That's exciting!"
                m 3eua "I hope they turn out to be a really good friend this time."
                m 3eub "Anyway, see you later~"

    elif mas_isMoniDis(higher=True):
        m 2eud "I hope you treat them well..."
        m 2euc "Bye."

    else:
        m 6ckc "..."

    $ persistent._mas_greeting_type_timeout = datetime.timedelta(hours=8)
    $ persistent._mas_greeting_type = store.mas_greetings.TYPE_HANGOUT
    return "quit"