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