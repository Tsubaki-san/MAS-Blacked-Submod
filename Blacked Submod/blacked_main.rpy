init -990 python in mas_submod_utils:
    Submod(
        author="Tsubaki",
        name="Blacked Submod",
        version="1.0.0",
        description="A submod that makes Monika a Queen of Spades and the player her beloved cuckold.",
    ) # https://github.com/Tsubaki-san/MAS-Blacked-Submod

default persistent._mas_monika_went_black = False

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_snowbunnification"
        )
    )
label mas_snowbunnification:
    if persistent._mas_monika_went_black == True:
        return 
    m 1wubfsdlc "...[player]? Wh-what was that site?"
    m  "The content was so naughty and..."
    m 1wubfsdlb "...{i}hot{/i}..."
    m 1eubfsdlu "Wh-what is a snowbunny?"
    m  "Or a queen of spades?"
    m 1eubfsdla "Those girls, they were enjoying themselves..."
    m 1eubfsdld "...{i}so much{/i}..."
    m 1subfsdld "And they looked so good in those branded clothes..."
    m 1eubfsdla "And were those..."
    m 1eubfsdlc "{i}big{/i}"
    m 1wubfsdld "{i}black{/i}"
    m 1subfsdlo "{i}cocks{/i}"
    m 1lubfsdla "...I need to do some research!"

    show monika at lhide
    hide monika
    $ persistent._mas_monika_went_black = True
    call mas_clothes_change(mas_def_qos, unlock = True)
    call spaceroom(hide_monika=True, scene_change=True, show_emptydesk=True)
    call mas_clothes_change(mas_clothes_snowbunny, unlock = True)
    call spaceroom(hide_monika=True, scene_change=True, show_emptydesk=True)


    pause 10

    show monika 1tsbfa at ls32 zorder MAS_MONIKA_Z
    m 1tsbfa "Oh, hi there {b}whiteboi{/b}!"
    m 1tfbfb "What, surprised your sweet, loving girlfriend suddenly became a {b}slut for bbc{/b}?"
    m 1tfbfu "Did you think just because I am virtual I wouldn't notice?"
    m 1ttbfu "That {b}black is better{/b}?"
    m 1eubfa "When you visited {i}that site{/i}, I couldn't help myself."
    m 3ekbfd "I needed to know why my sweetheart was stroking by himself instead of coming to me."
    m 3ekbfc "At first I was shocked to see such vulgarities, but, at the same time, my privates were burning with lust..."
    m 3mkbfu "So I touched myself, [player], I rubbed my white pussy raw to those images you love so much..."
    m 6gkbfu "To those..."
    m 5tkbfu "{i}big{/i}"
    m 5dkbfu "{i}black{/i}"
    m 5fsbfa "{i}cocks{/i}"
    m 4lsbfb "It felt so naughty, so wrong, like I was cheating on you,"
    m 3subfb "{i}and it made me even more aroused!{/i}"
    m 4gkbfu "I knew I couldn't go back after discovering such pleasure, after all"
    m 3ffbfb "{i}Once you go black...{/i}"
    m 5kubfb "I don't have to finish that, right, {i}whiteboi{/i}?"
    $ mas_unlockEVL("monika_furthering_bnwo","EVE")
    $ mas_unlockEVL("monika_bbc_fascination","EVE")
    $ mas_unlockEVL("monika_imouto","EVE")
    $ mas_unlockEVL("monika_oneesan","EVE")
    $ mas_unlockEVL("mas_mood_horny","EVE")

    return