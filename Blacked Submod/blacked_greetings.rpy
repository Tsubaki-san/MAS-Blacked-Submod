default persistent.snowbunnification = False

init -1 python in mas_greetings:
    import store
    import store.mas_ev_data_ver as mas_edv
    import datetime
    import random

    # TYPES:
    TYPE_SCHOOL = "school"
    TYPE_WORK = "work"
    TYPE_SLEEP = "sleep"
    TYPE_LONG_ABSENCE = "long_absence"
    TYPE_SICK = "sick"
    TYPE_GAME = "game"
    TYPE_EAT = "eat"
    TYPE_CHORES = "chores"
    TYPE_RESTART = "restart"
    TYPE_SHOPPING = "shopping"
    TYPE_WORKOUT = "workout"
    TYPE_HANGOUT = "hangout"
    TYPE_QOS = "snowbunnification"

    ### NOTE: all Return Home greetings must have this
    TYPE_GO_SOMEWHERE = "go_somewhere"

    # generic return home (this also includes bday)
    TYPE_GENERIC_RET = "generic_go_somewhere"

    # holiday specific
    TYPE_HOL_O31 = "o31"
    TYPE_HOL_O31_TT = "trick_or_treat"
    TYPE_HOL_D25 = "d25"
    TYPE_HOL_D25_EVE = "d25e"
    TYPE_HOL_NYE = "nye"
    TYPE_HOL_NYE_FW = "fireworks"

    # crashed only
    TYPE_CRASHED = "generic_crash"

    # reload dialogue only
    TYPE_RELOAD = "reload_dlg"

    # High priority types
    # These types ALWAYS override greeting priority rules
    # These CANNOT be override with GreetingTypeRules
    HP_TYPES = [
        TYPE_QOS,
        TYPE_GO_SOMEWHERE,
        TYPE_GENERIC_RET,
        TYPE_LONG_ABSENCE,
        TYPE_HOL_O31_TT
    ]

    NTO_TYPES = (
        TYPE_GO_SOMEWHERE,
        TYPE_GENERIC_RET,
        TYPE_LONG_ABSENCE,
        TYPE_CRASHED,
        TYPE_RELOAD,
    )

    # idle mode returns
    # these are meant if you had a game crash/quit during idle mode


    def _filterGreeting(
            ev,
            curr_pri,
            aff,
            check_time,
            gre_type=None
        ):
        """
        Filters a greeting for the given type, among other things.

        IN:
            ev - ev to filter
            curr_pri - current loweset priority to compare to
            aff - affection to use in aff_range comparisons
            check_time - datetime to check against timed rules
            gre_type - type of greeting we want. We just do a basic
                in check for category. We no longer do combinations
                (Default: None)

        RETURNS:
            True if this ev passes the filter, False otherwise
        """
        # NOTE: new rules:
        #   eval in this order:
        #   1. hidden via bitmask
        #   2. priority (lower or same is True)
        #   3. type/non-0type
        #   4. unlocked
        #   5. aff_ramnge
        #   6. all rules
        #   7. conditional
        #       NOTE: this is never cleared. Please limit use of this
        #           property as we should aim to use lock/unlock as primary way
        #           to enable or disable greetings.

        # check if hidden from random select
        if ev.anyflags(store.EV_FLAG_HFRS):
            return False

        # priority check, required
        # NOTE: all greetings MUST have a priority
        if store.MASPriorityRule.get_priority(ev) > curr_pri:
            return False

        # type check, optional
        if gre_type is not None:
            # with a type, we may have to match the type

            if gre_type in HP_TYPES:
                # this type is a high priority type and MUST be matched.

                if ev.category is None or gre_type not in ev.category:
                    # must have a matching type
                    return False

            elif ev.category is not None:
                # greeting has types

                if gre_type not in ev.category:
                # but does not have the current type
                    return False

            elif not store.MASGreetingRule.should_override_type(ev):
                # greeting does not have types, but the type is not high
                # priority so if the greeting doesnt alllow
                # type override then it cannot be used
                return False

        elif ev.category is not None:
            # without type, ev CANNOT have a type
            return False

        # unlocked check, required
        if not ev.unlocked:
            return False

        # aff range check, required
        if not ev.checkAffection(aff):
            return False

        # rule checks
        if not (
            store.MASSelectiveRepeatRule.evaluate_rule(
                check_time, ev, defval=True)
            and store.MASNumericalRepeatRule.evaluate_rule(
                check_time, ev, defval=True)
            and store.MASGreetingRule.evaluate_rule(ev, defval=True)
            and store.MASTimedeltaRepeatRule.evaluate_rule(ev)
        ):
            return False

        # conditional check
        if not ev.checkConditional():
            return False

        # otherwise, we passed all tests
        return True


    # custom greeting functions
    def selectGreeting(gre_type=None, check_time=None):
        """
        Selects a greeting to be used. This evaluates rules and stuff
        appropriately.

        IN:
            gre_type - greeting type to use
                (Default: None)
            check_time - time to use when doing date checks
                If None, we use current datetime
                (Default: None)

        RETURNS:
            a single greeting (as an Event) that we want to use
        """
        if store.persistent.snowbunnification:
            gre_type = TYPE_QOS
        if (
                store.persistent._mas_forcegreeting is not None
                and renpy.has_label(store.persistent._mas_forcegreeting)
            ):
            return store.mas_getEV(store.persistent._mas_forcegreeting)

        # local reference of the gre database
        gre_db = store.evhand.greeting_database

        # setup some initial values
        gre_pool = []
        curr_priority = 1000
        aff = store.mas_curr_affection

        if check_time is None:
            check_time = datetime.datetime.now()

        # now filter
        for ev_label, ev in gre_db.iteritems():
            if _filterGreeting(
                    ev,
                    curr_priority,
                    aff,
                    check_time,
                    gre_type
                ):

                # change priority levels and stuff if needed
                ev_priority = store.MASPriorityRule.get_priority(ev)
                if ev_priority < curr_priority:
                    curr_priority = ev_priority
                    gre_pool = []

                # add to pool
                gre_pool.append(ev)

        # not having a greeting to show means no greeting.
        if len(gre_pool) == 0:
            return None

        return random.choice(gre_pool)


    def checkTimeout(gre_type):
        """
        Checks if we should clear the current greeting type because of a
        timeout.

        IN:
            gre_type - greeting type we are checking

        RETURNS: passed in gre_type, or None if timeout occured.
        """
        tout = store.persistent._mas_greeting_type_timeout

        # always clear the timeout
        store.persistent._mas_greeting_type_timeout = None

        if gre_type is None or gre_type in NTO_TYPES or tout is None:
            return gre_type

        if mas_edv._verify_td(tout, False):
            # this is a timedelta, compare with last session end
            last_sesh_end = store.mas_getLastSeshEnd()
            if datetime.datetime.now() < (tout + last_sesh_end):
                # havent timedout yet
                return gre_type

            # otherwise has timed out
            return None

        elif mas_edv._verify_dt(tout, False):
            # this is a datetime, compare with current dt
            if datetime.datetime.now() < tout:
                # havent timedout yet
                return gre_type

            # otherwise has timeed out
            return None

        return gre_type



init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="mas_snowbunnified",
            unlocked=True,
            category=[store.mas_greetings.TYPE_QOS],
        ),
        code="GRE"
    )
label mas_snowbunnified:
    python:
        persistent.closed_self = True
        persistent._mas_monika_went_black = True
        persistent.snowbunnification = False
    call mas_clothes_change(mas_clothes_snowbunny, unlock = True)
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