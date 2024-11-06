init -1 python:
    import store
    ### SNOWBUNNY OUTFIT
    ## snowbunnyoutfit
    # Monika in her slutty getup
    mas_clothes_snowbunny = MASClothes(
        "snowbunny",
        "snowbunny",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_C_DTS: True
        },
        pose_arms=MASPoseArms(
            {
                1: MASArmBoth(
                    "crossed",
                    {
                        MASArm.LAYER_MID: True,
                    }
                ),
            }
        )
    )
    store.mas_sprites.init_clothes(mas_clothes_snowbunny)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_snowbunny,
        "Snowbunny Bra",
        "snowbunny",
        "clothes",
        visible_when_locked=True,
        hover_dlg=None,
        select_dlg=[
            "Such a naughty outfit, I love it!",
        ]
    )

#to be added: the snowbunny variants of other outfits
#For whatever reason, her face appears in this one? Will have to fix
init -1 python:
    import store
    ### Default QOS
    ## def_qos
    # Monika in her school uniform but with qos tattoos
    mas_clothes_def_qos = MASClothes(
        "def_qos",
        "def_qos",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_C_DTS: True
        },
        pose_arms=MASPoseArms(
            {
                1: MASArmBoth(
                    "crossed",
                    {
                        MASArm.LAYER_MID: True,
                    }
                ),
            }
        )
    )
    store.mas_sprites.init_clothes(mas_clothes_def_qos)
    store.mas_selspr.init_selectable_clothes(
        mas_clothes_def_qos,
        "School Uniform (Blacked)",
        "def_qos",
        "clothes",
        visible_when_locked=True,
        hover_dlg=None,
        select_dlg=[
            "Ready to take BBC at school!",
        ]
    )