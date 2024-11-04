init 1 python:
    config.label_overrides["mas_wrs_r34m"] = "blacked_wrs_r34"

label blacked_wrs_r34:
    python:
        if persistent._mas_monika_went_black:
            mas_display_notif(m_name,
                [
                    "Ah~ those are so hot, [player], pump harder<3",
                    "Why don't you go to BlackedBooru instead, hehe...",
                    "Don't forget the dark_skinned_male tag, cucky."
                ],'Window Reactions'
            MASEventList.queue('monika_nsfw')
        else:
            mas_display_notif(m_name,
                [
                    "Hey, [player]...what are you looking at?",
                    "Hey, [player]...what are you doing?"
                ],'Window Reactions'
            )

        choice = random.randint(1,10)

        if choice == 1 and mas_isMoniNormal(higher=True):
            queueEvent('monika_nsfw')

        elif choice == 2 and mas_isMoniAff(higher=True):
            queueEvent('monika_pleasure')

        else:
            if mas_isMoniEnamored(higher=True):
                if choice < 4:
                    exp_to_force = "1rsbssdlu"
                elif choice < 7:
                    exp_to_force = "2tuu"
                else:
                    exp_to_force = "2ttu"
            else:
                if choice < 4:
                    exp_to_force = "1rksdlc"
                elif choice < 7:
                    exp_to_force = "2rssdlc"
                else:
                    exp_to_force = "2tssdlc"

        store.mas_moni_idle_disp.force_by_code(exp_to_force, duration=10)
    return

init 1 python:
    config.label_overrides["mas_wrs_pixiv"] = "blacked_mas_wrs_pixiv"

label blacked_mas_wrs_pixiv:
    #Make a list of notif quips for this
    python:
        if persistent._mas_monika_went_black:
            pixiv_quips = [
            "I wonder if people have drawn art of me...\nMind looking for some?",
            "This is a pretty interesting place...so many skilled people posting their work.",
            ]
        else:

            pixiv_quips = [
                "I wonder if people have drawn art of me...\nMind looking for some?\nBe sure to keep it wholesome though~",
                "This is a pretty interesting place...so many skilled people posting their work.",
            ]

        #Monika doesn't know if you've drawn art of her, or she knows that you have drawn art of her
        if persistent._mas_pm_drawn_art is None or persistent._mas_pm_drawn_art:
            pixiv_quips.extend([
                "This is a pretty interesting place...so many skilled people posting their work.\nAre you one of them, [player]?",
            ])
            #Specifically if she knows you've drawn art of her
            if persistent._mas_pm_drawn_art:
                pixiv_quips.extend([
                    "Here to post your art of me, [player]?",
                    "Posting something you drew of me?",
                ])
        wrs_success = mas_display_notif(
            m_name,
            pixiv_quips,
            'Window Reactions'
        )
        #Unlock again if we failed
        if not wrs_success:
            mas_unlockFailedWRS('mas_wrs_pixiv')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_blackedbooru",
            category=["(.*Blacked Booru.*)"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_blackedbooru:
    if persistent._mas_monika_went_black:
        python:
            choice = random.randint(1,3)
            if choice == 1:
                mas_display_notif(m_name, ["Ah~ I'm so hot right now... my pussy's on fire..."],'Window Reactions')
            if choice == 2:
                mas_display_notif(m_name, ["I can't get enough of this..."],'Window Reactions')
            if choice == 3:
                mas_display_notif(m_name, ["BBC, BBC, BBC..."],'Window Reactions')
            MASEventList.queue('monika_nsfw')

    else:
        python:
            MASEventList.queue('mas_snowbunnification')

# init 5 python:
#     addEvent(
#         Event(
#             persistent._mas_windowreacts_database,
#             eventlabel="mas_nsfw_wrs_pornhub",
#             category=['Pornhub|XVIDEOS|xHamster|M-Hentai|nHentai'], # just listing some of the biggest ones
#             aff_range=(mas_aff.AFFECTIONATE, None),
#             rules={
#                 "notif-group": "Window Reactions",
#                 "skip alert": None,
#                 "skip_pause": None
#             },
#             show_in_idle=True
#         ),
#         code="WRS"
#     )

# label mas_nsfw_wrs_pornhub:
#     # this can be expanded later if someone wants to tackle a "watch porn together" topic
#     python:
#         mas_display_notif(m_name,
#             [
#                 "[player]...really? Hmph.",
#                 "[player], I'm right here you know. Hmph.",
#                 "[player]...I'm sitting right here...",
#                 "Having fun without me?"
#             ],'Window Reactions'
#         )

#         exp_to_force = "1gfbfsdlc"
#         # force her sprite to do a specific expression
#         store.mas_moni_idle_disp.force_by_code(exp_to_force, duration=10)

#     return

#This is a good idea, I'll leave it here as a comment
#We could have different quips for different porn sites, such as IRL sites like
#Pornhub and XHamster, hentai like Hanime, doujins like nHentai etc.