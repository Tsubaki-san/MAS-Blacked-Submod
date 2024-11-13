init 1 python in mas_background:

    # verify all backgrounds
    for flt_bg in BACKGROUND_MAP.itervalues():
        flt_bg.verify()

###START: IMAGE DEFINITIONS
#Day images
image submod_alley_day = "mod_assets/location/alley/alley.png"
image submod_alley_rain = "mod_assets/location/alley/alley.png"
image submod_alley_overcast = "mod_assets/location/alley/alley.png"
image submod_alley_snow = "mod_assets/location/alley/alley.png"

#Night images
image submod_alley_night = "mod_assets/location/alley/alley-n.png"
image submod_alley_rain_night = "mod_assets/location/alley/alley-n.png"
image submod_alley_overcast_night = "mod_assets/location/alley/alley-n.png"
image submod_alley_snow_night = "mod_assets/location/alley/alley-n.png"

#Sunset images
image submod_alley_ss = "mod_assets/location/alley/alley-ss.png"
image submod_alley_rain_ss = "mod_assets/location/alley/alley-ss.png"
image submod_alley_overcast_ss = "mod_assets/location/alley/alley-ss.png"
image submod_alley_snow_ss = "mod_assets/location/alley/alley-ss.png"



init -1 python:
    submod_background_alley = MASFilterableBackground(
        # ID
        "submod_alley",
        "Dark Alley",

        # mapping of filters to MASWeatherMaps
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_alley_day",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_alley_rain",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_alley_overcast",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_alley_snow",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_alley_night",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_alley_rain_night",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_alley_overcast_night",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_alley_snow_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_alley_ss",
                store.mas_weather.PRECIP_TYPE_RAIN: "submod_alley_rain_ss",
                store.mas_weather.PRECIP_TYPE_OVERCAST: "submod_alley_overcast_ss",
                store.mas_weather.PRECIP_TYPE_SNOW: "submod_alley_snow_ss",
            }),
        ),

        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),

        disable_progressive=False,
        hide_masks=False,
        hide_calendar=True,
        unlocked=True,
        entry_pp=store.mas_background._alley_entry,
        exit_pp=store.mas_background._alley_exit,
        ex_props={"skip_outro": None}
    ) 


init -2 python in mas_background:
    def _alley_entry(_old, **kwargs):
        """
        Entry programming point for Furnished_spaceroom3 background
        """
        if kwargs.get("startup"):
            pass

        else:
            if not store.mas_inEVL("alley_switch_dlg"):
                store.pushEvent("alley_switch_dlg")

        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

        if store.seen_event("mas_monika_islands"):
            store.mas_unlockEVL("mas_monika_islands", "EVE")

    def _alley_exit(_new, **kwargs):
        """
        Exit programming point for Furnished_spaceroom3 background
        """
        #Lock islands greet to be sure
        store.mas_lockEVL("mas_monika_islands", "EVE")

        #COMMENT(#) IF NOT NEEDED
        store.monika_chr.tablechair.table = "def"
        store.monika_chr.tablechair.chair = "def"

        if _new == store.mas_background_def:
            store.pushEvent("return_switch_dlg")       

###START: Topics
label alley_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "Such a dirty place~.",
            "Oh, to be gangbanged by a gang of black studs in a place like this...",
            "Just like in those dirty videos we love so much...",
        ]))

    m 1hua "[switch_quip]"

    return

label return_switch_dlg:
    python:
        switch_quip = renpy.substitute(renpy.random.choice([
            "Just the two of us~",
            "Miss the classic look?",
            "Brings back memories...",
        ]))

    m 1hua "[switch_quip]"

    return