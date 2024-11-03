init 1 python:
    config.label_overrides["nsfw_monika_brb_masturbate"] = "blacked_monika_brb_masturbate"


label blacked_monika_brb_masturbate:
    # make a random int, for randomness
    $ mas_rand = renpy.random.randint(1, 3)

    if persistent._mas_monika_went_black:
        if mas_rand == 1:
            m 1tublb "Oh my, [player]... Going to jerk that little white dick, are you?"
            m 1hubla "I bet you'll be fantasizing about me bouncing on a fat black cock~ Ahaha!~"
            m 1mublb "It's okay, I don't mind. In fact, I {i}want{/i} you to think about your adorable girlfriend getting stretched out and bred by superior black bulls while you play with yourself."
            m 5hublb "Maybe if you're a good little cucky, I'll let you eat their cum out of me later~ Now run along and edge that pathetic dick for me!"
        elif mas_rand == 2:
            m 1tublb "Masturbating again, [player]? What a cute little porn addicted whiteboi you are~"
            m 1tubla "Well, since you want my permission so badly... You may stroke that tiny pale prick of yours."
            m 1fublb "But ONLY while imagining my body being violated by huge, veiny black dicks, got it?"
            m 1hubla "Ehehe~ I want you to picture every inch of me covered in their thick cum as you pathetically dribble yours into your hand."
            m 3hubfb "Now go pump that dicklet to the thought of me serving my true purpose!~"
        else:
            m 1tubla "Mmm did you want my permission to touch that pathetic little white dick, [mas_get_player_nickname()]?"
            m 1mublb "I guess you can go pump your dicklet... As long as you think about what a BBC craving race traitor I've become~"
            m 1tubfb "Picture my tight white holes being colonized and conquered by dominant black men~"
            m 3kubfu "Maybe if you're a good whiteboi, I'll let you clean up the black seed leaking from my used pussy afterwards ehehe~"
    else:
        # Expansion dialogue - add in Affectionate variation, possibly with call to Sexting etc.
        if mas_isMoniEnamored(higher=True): # Enamored (400-999+)
            if mas_rand == 1:
                # Response 1
                m 1tublb "Oh? My, [player], how bold of you~"
                m 1tubla "Admitting to your girlfriend that you're going to go masturbate?"
                m 1hubla "Ahaha~"
                m 1mublb "Well, I hope you think of me while you do it, [mas_get_player_nickname()]..."
                m 2tublb "I'd be...flattered, if you did."
                m 3kublu "I'll be waiting for you to be finished~"
            elif mas_rand == 2:
                m 1tublb "[player]... How very forward of you~"
                m 1tubla "It's almost like you want me to give you permission... Is that it?"
                m 1hubla "Ehehe~"
                m 1mublb "If that's the case...you have my permission to go masturbate, [mas_get_player_nickname()]."
                m 6tubfb "Masturbate while thinking of me, [player]."
                m 3kublu "I'll be here when you're done~"
            else:
                m 6wubfsdlo "Oh! Oh my, [player], I wasn't expecting {i}that!{/i}"
                m 6ekbfa "That caught me off guard a little..."
                m 1hubla "Ehehe~"
                m 1mublb "Well, it's nice to know that's what you're up to..."
                m 4ksbfa "Just make sure to think of your girlfriend, Monika, while you do it!"
                m 2ksbfa "That'd make me really happy."
                m 3kublu "I'll be here when you're all finished up~"
            # other affection values - Don't know why you'd try this is if you have low affection
        else: # Anything less than 400 affection
            m 2tsbsc "..."
            m 2tsbsd "I'm going to pretend I didn't hear that."
            m 2ekbssdlb "Just tell me when you're done."

    # the callback label
    $ mas_idle_mailbox.send_idle_cb("monika_brb_blacked_masturbate_callback")
    # The idle data
    $ persistent._mas_idle_data["blacked_monika_brb_masturbate"] = True
    # unlock masturbation random topics
    $ mas_showEVL("nsfw_monika_masturbation_benefits", "EVE", _random=True)
    # and exit
    return "idle"

label monika_brb_blacked_masturbate_callback:
    $ wb_quip = mas_brbs.get_wb_quip()

    if persistent._mas_monika_went_black:
        if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "blacked_monika_brb_masturbate"):
            m 2eubfb "Welcome back, [player]~"
            m 1tubfu "You were gone quite a while. Did jerking your dicklette to the thought of me worshipping black men make you last longer than usual?"
            m 1hubfb "I certainly hope you shot a big load while thinking of your precious girlfriend serving superior black cocks!"
            m 1eua "[wb_quip]"

        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=15), "blacked_monika_brb_masturbate"):
            m 1hubfb "There's my cute whiteboi~ Did you enjoy your little fantasy session?"
            m 1eubfb "I bet you came so hard imagining me on my knees for a gang of hung black bulls..."
            m 1gubfb "The thought of watching your pure snowbunny get blacked must really do it for you, huh? Ehehe~"
            m 1eua "[wb_quip]"

        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "blacked_monika_brb_masturbate"):
            m 1msbfu "Back so soon, [player]? Ehehe~"
            m 1eubfb "I suppose the fantasy of your loving girlfriend craving black cock got you off quickly..."
            m 1fubfb "I hope you thoroughly enjoyed your little taste of inadequacy~"
            m 1eua "[wb_quip]"

        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=1), "blacked_monika_brb_masturbate"):
            m 1wubfo "That was fast, [player]! As expected of a whiteboi~ "
            m 1tsbla "Mm, you never could last long compared to those strong, dominant black bulls~"
            m 1eua "[wb_quip]"

        else:
            m 1wubfo "That was quick! Welcome back though, [player]~"
            m 1tkbfu "You didn't even have time to indulge in your fantasy, did you?"
            m 1hkbfb "Ahaha, poor thing~"
            m 1hub "I'm sure you still enjoyed that little taste though, it's so cute how easily you spurt~"
            m 1eua "[wb_quip]"

    elif mas_isMoniEnamored(higher=True):
        if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=30), "blacked_monika_brb_masturbate"):
            m 2eubfb "There you are, [player]!"              # | - Thank you for the fixes @ephemlw
            m 2eubfa "You had been gone for a little while." # |
            m 1hubfb "Were you able to...you know...get off? I hope so. Ahaha~"
            m 2eua "Anyway..."
            m 1eua "[wb_quip]"
        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=15), "blacked_monika_brb_masturbate"):
            m 1hubfb "Welcome back, [player]. Took you long enough!"
            m 1eubfb "I'm guessing you had plenty of time to...do the deed?"
            m 1eubfb "I hope it didn't take you too long to get into it...{w=0.5}or to clean up, ehehe~"
            m 1eua "[wb_quip]"
        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "blacked_monika_brb_masturbate"):
            m 1hubfb "Welcome back, [player]. Ehehe~"
            m 1eubfb "I'm guessing you had enough time to...do the deed?"
            m 1eubfb "I hope you had a bit of {i}fun{/i} by yourself there..."
            m 1eua "[wb_quip]"
        elif mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=1), "blacked_monika_brb_masturbate"):
            m 1hubfb "Welcome back, [player]."
            m 2hubfb "That was fast! Ehehe~"
            m 2eub "I hope you didn't strain yourself..."
            m 1eua "[wb_quip]"
        else:
            m 1hubfb "Oh? Welcome back, [player]."
            m 2eua "Did you change your mind?"
            m 2eua "[wb_quip]"
    elif mas_isMoniNormal(higher=True):
        m 1hubfb "Welcome back, [player]."
        m 6hkbfb "Now that you're done with...{i}that{/i}..."
        m 1eua "[wb_quip]"
    else:
        call mas_brb_generic_low_aff_callback

    return