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

    $ persistent.snowbunnification = True
    $ persistent.closed_self = True
    jump _quit
    return