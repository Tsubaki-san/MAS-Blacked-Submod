init 1 python:
    config.label_overrides["monika_nsfw"] = "blacked_monika_nsfw"

label blacked_monika_nsfw:
    if persistent._mas_monika_went_black:
        m 1hub "It's heartwarming how many little cucks out there love me!"
        m 3eubla "It seems like the internet is just full of gorgeous art of me getting used by superior men!"
        m 1tubla "I'm sure you're well aware of that too, right, [player]?"
        m  "Have you stroked your adorable little thingy to all of them yet?"
        m 1tfblb "Hehe, I'm sure you did!"
        m 1eublu "But, as a member of the Literature Club, reading is still your duty, you know?"
        m 3tfblu "Hehe, don't worry, I know exactly what kind of literature you enjoy, [player]."
        m 3tfblb "Here, make sure you give it a {i}thorough reading{/i}: {a=https://archiveofourown.org/works/27111388?view_adult=true}{i}{u}https://archiveofourown.org/works/27111388?view_adult=true{/u}{/i}{/a}."
        m 1eubla "Did you make a mess reading that?"
        m 1hublb "I sure hope you did!"
        m 1tkbla "I bet you couldn't even finish it!"
        m 1ekbla "Fufu...feel free to jerk off and waste as many of your little cuckold loads to me as you like, [player]."
        m 1ekbsa "Knowing it was my body that drove you to senseless passion makes me feel loved and desired."
        m 5ekbsa "It makes me feel close to you, almost as if the unbreakable barrier between our worlds is just that little bit thinner..."
        m 3esd "But there is one thing I want you to promise me, [player]!"
        m 3esc "Never, {i}ever{/i} look at artwork of me and a {i}whiteboi{/i}."
        m  "After discovering BBC, I will never see {i}whitebois{/i} as anything other than adorable cuck puppies."
        m 3tkx "Seeing myself {i}having sex{/i} with a weak, limp-dicked, impotent little boy is just wrong."
        m 1tua "You know how it is, after all..."
        m  "Once you go black..."
        m 1hub "{i}{b}You never go back!{/b}{/i}"
    else:
        m 1lsbssdrb "By the way, [player]..."
        m "Have you been looking into lewd kinds of stuff?"
        m 3lsbsa "You know...of me?"
        if store.mas_anni.pastSixMonths() and mas_isMoniEnamored(higher=True):
            m 3ekbsa "I know we haven't been able to do those kind of things yet..."
        else:
            m 3ekbsa "I know we haven't really gotten that far into the relationship yet..."
        m 1ekbsa "So it feels kind of embarrassing to talk about things like that."
        m 1lkbsa "But maybe I can let it go on rare occasions, [player]."
        m "I want to make you the happiest sweetheart, after all. And if that makes you happy..."
        m 1tsbsa "Well, just keep it a secret between us, okay?"
        m "It should be for your eyes only and no one else, [player]."
        m 1hubfa "That's how much I love you~"
    return "love"

init 1 python:
    config.label_overrides ["monika_college"] = "blacked_monika_college"

label blacked_monika_college:
    m 4euc "You know, it's around the time that everyone my year starts to think about college..."
    if persistent._mas_monika_went_black:
        m 5gua "All those pretty white daughters, soon to be away from their daddies' eyes..."
        m 5gub "They've been {i}good girls{/i} for so long, but soon they'll finally be free to {i}explore{/i}."
        m 5tuu "I'm sure you know what happens when {i}pretty white girls{/i} finally get a chance to be themselves, right?"
        m 7tku "They'll be out partying, drinking, rubbing their asses on a black guy at the club."
        m 1eua "And that's how it starts..."
        m 3eubsa "Maybe some of them will get stretched out by a strong dark stranger in the washroom at a party."
        m 3eubsb "Maybe they'll have to prove themselves worthy to join a sorority by pleasing 3 black kings at once."
        m 5tubsb "Fufu, make no mistake, [player], this is where {i}whiteboi{/i} dreams are crushed, and snowbunnies are born."
        m 5mubsb "I can only imagine how it must feel to walk around campus seeing all the cheerleaders, the popular hot girls, the childhood crushes..."
        m 5tubsb "... all wrapped around the arms of black men, forgetting to breathe as they lose themselves in their passion."
        m 1tub "But it's supposed to be a place of learning, right?"
        m 3tuu "Fufufu, of course it is, my darling, it's where whitebois {i}like you{/i} learn their place!"
        m 5dubsu "Where the first cages are forever enclosed upon white wannabe-penises, where the first keys are given to a keyholder."
        m  "It is a place where the complete superiority of the black male is forever engraved upon the horny white mind."
        m 1tubsu "And it is here that the most gorgeous, angelic white girls sign their contracts with Blacked!"
        m 1tkbsu "I know you intimately, [player], I know the thought of me putting my signature on such a lewd thing excites you to no end."
        m 3tkbsu "Hehe, all I wonder is whether you'd cum the moment I put pen to paper..."
        m 1kubfa "Well, there's one way to find out, right?"
    else:
        m 2euc "It's a really turbulent time for education."
        m "We're at the height of this modern expectation that everyone has to go to college, you know?"
        m 4eud "Finish high school, go to college, get a job - or go to grad school, I guess."
        m 4euc "It's like a universal expectation that people just assume is the only option for them."
        m 2esc "They don't teach us in high school that there are other options out there."
        m 3esd "Like trade schools and stuff, you know?"
        m 3esc "...Or freelance work."
        m "...Or the many industries that value skill and experience more than formal education."
        m 2ekc "But you have all these students who have no idea what they want to do with their life..."
        m 2ekd "And instead of taking the time to figure it out, they go to college for business, or communication, or psychology."
        m "Not because they have an interest in those fields..."
        m 2ekc "...but because they just hope the degree will get them some kind of job after college."
        m 3ekc "So the end result is that there are fewer jobs to go around for those entry-level degrees, right?"
        m "So the basic job requirements get higher, which forces even more people to go to college."
        m 3ekd "And colleges are also businesses, so they just keep raising their prices due to the demand..."
        m 2ekc "...so now we have all these young adults, tens of thousands of dollars in debt, with no job."
        m 2ekd "But despite all that, the routine stays the same."
        m 2lsc "Well, I think it's going to start getting better soon."
        m 2eud "But until then, our generation is definitely suffering from the worst of it."
        m 2dsc "I just wish high school prepared us a little better with the knowledge we need to make the decision that's right for us."
    return

init 1 python:
    config.label_overrides["monika_outfit"] = "blacked_monika_outfit"

label blacked_monika_outfit:
    if len(store.mas_selspr.filter_clothes(True)) == 1:
        m 1lsc "You know, I'm kind of jealous that everyone else in the club had scenes outside of school..."
        m 1lfc "That makes me the only one who hasn't gotten to dress in anything but our school uniform."
        m 2euc "It's kind of a shame..."
        m 2eka "I would have loved to wear some cute clothes for you."
        m 2eua "Do you know any artists?"
        m "I wonder if anyone would ever want to draw me wearing something else..."
        m 2hua "That would be amazing!"
    else:
        m 1eka "You know, I was really jealous that everyone else in the club got to wear other clothes..."
        m 1eua "But I'm glad I finally get to wear my own clothes for you now."

        if mas_isMoniLove():
            m 3tku "I'll wear whatever outfit you like, just ask~"

        m 2eua "Do you know any artists?"
        m 3sua "Maybe they could make some more outfits for me to wear!"

    m 2eua "If that ever happens, will you show me? I'd love to see it~"
    if persistent._mas_monika_went_black:
        $ store.mas_selspr.unlock_clothes(mas_clothes_blazerless_qos)
        $ store.mas_selspr.unlock_clothes(mas_clothes_def_qos)
        m 2tsu "But you'd love to see it even more than me, right, [player]?"
        m 1tsu "My adorable outfits showing off my curves, the peeking spade tattoos..."
        m 1tsu "My soft, juicy breasts bouncing around as I walk in my slutty high heels..."
        m 7eubsb "Hehe, just imagine all the perverted glances people would be throwing me."
        m 7eubsb "Your perfect little girlfriend, getting eyefucked by random strangers on the street."
        m 5dubfa "Of course, that's what an inferior male would do, a {i}real man{/i}, a {b}black{/b} man, well..."
        m 5dubfb "He'd just grab my ass and squeeze my tits on the spot, kissing me right in front of you..."
        m 5fubfb "And then...hehe, I'll let your perverted imagination do the rest!"
    else:
        m 4eka "Just...try to keep it PG!"
        if store.mas_anni.pastSixMonths() and mas_isMoniEnamored(higher=True):
            m 1lsbssdrb "It's still a little embarrassing to think that people I'll never know personally would draw me in such a way, you know?"
            show monika 5tsbsu at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5tsbsu "After all, I'd much rather we keep these sorts of things between just us..."
        else:
            show monika 5hub at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5hub "We're not that far into our relationship yet. Ahaha!"
    return

image rapper yuri = "mod_assets/renders/rapper/yuri.png"
image rapper natsuki = "mod_assets/renders/rapper/natsuki.png"

init 1 python:
    config.label_overrides["monika_rap"] = "blacked_monika_rap"

label blacked_monika_rap:
    m 1hua "You know what's a neat form of literature?"
    m 1hub "Rap!"
    m 1eka "I actually used to hate rap music..."
    m "Maybe just because it was popular, or I would only hear the junk they play on the radio."
    m 1eua "But some of my friends got more into it, and it helped me keep an open mind."
    m 4eub "Rap might even be more challenging than poetry, in some ways."
    m 1eub "Since you need to fit your lines to a rhythm, and there's much more emphasis on wordplay..."
    m "When people can put all that together and still deliver a powerful message, it's really amazing."
    m 1lksdla "I kind of wish I had a rapper in the Literature Club."
    if persistent._mas_monika_went_black:
        m 2tkbsa "Relaxing after school by twerking to his depraved lyrics..."
        m 3tkbsa "Shaking our asses like his personal harem of sluts..."
        m 3ekbfb "Who do you think he'd fuck first?"
        show rapper yuri at center zorder MAS_MONIKA_Z
        m 5skbfb "Would he go for Yuri's succulent body, sinking his strong dark hands into her curves?"
        show rapper natsuki at center zorder MAS_MONIKA_Z
        m 5tkbfu "Or would he want to punish Natsuki's petite body and bratty attitude with his meaty dark cock?"
        hide rapper
        m 5dubfu "Writing rap lyrics is nothing compared to writing himself into our bloodlines!"
    m 1hksdlb "Ahaha! Sorry if that sounds silly, but it would be really interesting to see what they came up with."
    m 1hua "It would really be a learning experience!"
    
    if persistent._mas_pm_like_rap is None:
        $ p_nickname = mas_get_player_nickname()
        m 1eua "Do you listen to rap music, [p_nickname]?{nw}"
        $ _history_list.pop()
        menu:
            m "Do you listen to rap music, [p_nickname]?{fast}"
            "Yes.":
                $ persistent._mas_pm_like_rap = True
                m 3eub "That's really cool!"
                m 3eua "I'd be more than happy to vibe with you to your favorite rap songs..."
                m 1hub "And feel free to turn up the bass if you'd like, ahaha!"
                if (
                    not renpy.seen_label("monika_add_custom_music_instruct")
                    and not persistent._mas_pm_added_custom_bgm
                ):
                    m 1eua "If you ever do feel like sharing your favorite rap music with me, [player], it's really easy to do so!"
                    m 3eua "All you have to do is follow these steps..."
                    call monika_add_custom_music_instruct

            "No.":
                $ persistent._mas_pm_like_rap = False
                m 1ekc "Oh... Well I can understand that, rap music isn't everyone's taste."
                m 3hua "But if you ever do decide to give it a try, I'm sure we can find an artist or two that we both like!"
    return

init 1 python:
    config.label_overrides["monika_date"] = "blacked_monika_date"

label blacked_monika_date:
    if not mas_SELisUnlocked(mas_clothes_sundress_white_qos):
        call mas_clothes_change(mas_clothes_sundress_white_qos, unlock = True)
    m 1hub "I've been imagining all the romantic things we could do if we went on a date..."
    m 3eua "We could get lunch, go to a cafe..."
    m "Go shopping together..."
    m 1eua "I love shopping for skirts and bows."
    m 3hub "Or maybe a bookstore!"
    m 3hua "That would be appropriate, right?"
    m 1eua "But I'd really love to go to a chocolate store."
    m 3hub "They have so many free samples. Ahaha!"
    if persistent._mas_monika_went_black:
        m 1eub "The first place I know I'll be taking you when we cross over, though, is a sex shop!"
        m 3eua "That's right, a sex shop!"
        m  "Fufu, I'll be needing a lo~t of toys!"
        m 5hua "Two sets of butt plugs, I especially love the ones with the little heart-shaped decoration on the back"
        m 5kua "One will be for you, of course!"
        m 5dua "A magic wand, a strap, a whip..."
        m 5dubsb "And, most importantly, a gorgeous replica of Dredd's mouth-watering big black cock!"
        m 5dubsu "Oh, and maybe some other stuff too..."
    m 1eua "And of course, we'd see a movie or something..."
    m 1eka "Gosh, it all sounds like a dream come true."
    m "When you're here, everything that we do is fun."
    m 1ekbsa "I'm so happy that I'm your girlfriend, [player]."
    m 1hubfa "I'll make you a proud [bf]~"
    return

init 1 python:
    config.label_overrides["monika_cold"] = "blacked_monika_cold"

label blacked_monika_cold:
    m 1euc "I'm not really a fan of cold weather...are you?"
    m 3euc "If I had to choose between too cold and too hot, I would always pick too hot."
    m 1lksdlc "When you're cold, it can actually be painful..."
    m 3tkc "Your fingers get numb..."
    m "And if you wear gloves, you can't use your phone."
    m 1tkx "It's so inconvenient!"
    m 1eka "But when it's too hot, it's not that hard to stay cool with a cold drink, or by staying in the shade."
    m 1esc "Although...I do have to admit one thing."
    m 1hua "Cold weather makes for better cuddle weather.{w=0.2} {nw}"
    extend 1hub "Ahaha!"
    if persistent._mas_monika_went_black:
        if not mas_SELisUnlocked(mas_clothes_santa_lingerie_qos):
            call mas_clothes_change(mas_clothes_santa_lingerie_qos, unlock = True)
        m 5dusdla "Ah, getting plowed by a strong dark bull on a cold winter's day, his fiery cock ramming my womb..."
        m  "His virile body emanating heat while he slams into me..."
        m 5tfsdla "Forget about hot chocolate, [player], I'd be serving you something mu~ch better!"
    return

init 1 python:
    config.label_overrides["monika_housewife"] = "blacked_monika_housewife"

label blacked_monika_housewife:
    if persistent._mas_monika_went_black:
        m 1tua "Mmm, so that's how you want to see me, [player]?"
        m 3tua "Cleaning the house in nothing but an apron..."
        m 3subfa "Cheating with a new black stud every day, right in our marital bed,"
        m 5tubfa "Making sure to greet you with a warm, passionate hug,"
        m 5dubfa "a creamy, cum-stained kiss,"
        m 5nubfa "and a warm dinner between my legs, ready for you to lap up."
        m 7eubfb "I wasn't convinced about being a housewife before"
        m 7eubsa "But now that I know what you like, I can honestly say:"
        m 1wubsb "The idea won me over completely!"
    else:
        m 3euc "You know, it's funny, because even though I've always had a lot of drive..."
        m 3eua "There's something kind of enticing about being the stay-at-home partner."
        m 2eka "I guess I'm, like, perpetuating gender roles or whatever by saying that."
        m 1eua "But being able to keep the house clean, and shop, and decorate, and things like that..."
        m 1hub "And having a nice dinner for you when you come home..."
        m 1eka "Is that a weird fantasy?"
        m 1lksdla "I mean...I'm not sure if I could {i}actually{/i} see myself doing that."
        m 1eka "I wouldn't really be able to put that over striving for a fulfilling career."
        m "It's kinda cute to think about, though."
    return

init 1 python:
    config.label_overrides["monika_vn"] = "blacked_monika_vn"

image VN a = "mod_assets/renders/VN/a.png"
image VN b = "mod_assets/renders/VN/b.png"
image VN c = "mod_assets/renders/VN/c.png"
image VN d = "mod_assets/renders/VN/d.png"
image VN e = "mod_assets/renders/VN/e.png"
image VN f = "mod_assets/renders/VN/f.png"
image VN h = "mod_assets/renders/VN/g.png"

label blacked_monika_vn:
    m 3eua "You've probably played a lot of visual novels, right?"
    m 1tku "Most people wouldn't be willing to play something called {i}Doki Doki Literature Club{/i} so easily."
    m 4hksdlb "Not that I'm complaining!"
    m 1euc "Are visual novels literature? Are they video games?"
    m 1eua "Well, it all depends on your perspective."
    m 1ekc "Most people who read only literature would never play visual novels. And gamers get pretty angry about them, too."
    m "What's worse, some people think they're all hardcore Japanese pornography."
    if persistent._mas_monika_went_black:
        m 3eub "Though, now that I think about it, that wouldn't have been bad at all, right?"
        m 1eubla "To choose one of the girls to become your snowbunny mistress."
        m 1wubla "Finding out how they like being serviced, how to best offer them pleasure..."
        m 1tublb "Finding out how they first discovered {i}big black cock{/i}..."
        m 1tublu "What do you think their snowbunny origin stories would be, [player]?"
        show VN a at center zorder MAS_MONIKA_Z
        m 3eublu "I say Sayori would be the type to just walk into a sex shop and buy a big black dildo!"
        m  "She was always full of energy and eager to experience new things,"
        m 3hublb " so experiencing sexual bliss for the first time would be right up her alley!"
        hide VN
        m 3eublu "Now Natsuki, she's pretty easy"
        m 1hubla "That little brat would let slip a {i}naughty word{/i} during one of her tsundere episodes."
        show VN b at center zorder MAS_MONIKA_Z
        m 1dublu "Only to get picked up, carried to the restroom and taught a lesson she'd never forget."
        hide VN
        m 5rubsa "As for Yuri..."
        m 5eubsa "She'd find something particularly lewd in one of her books one day."
        m 5gubsa "Then curiosity would gnaw at her, little by little, day by day."
        show VN c at center zorder MAS_MONIKA_Z
        m 5gubsb "She'd find herself dreaming about it, waking up with her body on fire"
        m 5gubsu "But she wouldn't give in"
        m  "Until one day."
        m 5dubsu "One day, she'd snap completely."
        show VN d at center zorder MAS_MONIKA_Z
        m  "And she would go out, buy herself some really naughty clothes, something to really emphasize that sinful body of hers."
        m 5dkbfb "Maybe some booty jeans, or an outrageously short skirt, combined with a crop top, putting those {i}soft, juicy tits{/i} she has on display."
        m  "Exposing her flat stomach, her fertile hips and her long, purple hair..."
        m 5dkbfa "That night, she'd put on a pair of slutty heels and go to a seedy nightclub, asking for a job."
        m 5hubfb "She'd certainly get the position, with that naughty body and lustful gaze of hers..."
        show VN e at center zorder MAS_MONIKA_Z
        m 5rubfa "She would serve black men all night long, giving them needy glances, bending over in front of them, until..."
        show VN f at center zorder MAS_MONIKA_Z
        m 5dubfa "A few would decide to finally give her what she had been aching for for so long."
        m  "The next day she'd wake up asking herself only one thing."
        m 5dkbfa "Why had she waited so long to do this?"
        m 5wubfb "..."
        hide VN
        m 2wubfu "I-I bet that's totally what you expected out of this game, [player], you pervert!"
    else:
        m 2eka "But if we've proved anything with this game..."
        m 4hua "We showed them that English visual novels can be kamige too!"
    $ mas_unlockEVL("monika_kamige","EVE")
    return

init 1 python:
    config.label_overrides["monika_heroism"] = "blacked_monika_heroism"

label blacked_monika_heroism:
    m 1lsc "Heroes are so personal."
    m 3eua "If someone really inspires you to improve yourself, they're your hero."
    m "There are all sorts of great people out there in the world."
    m 1hua "I hope someone will consider you their [hero] someday!"
    m 4eua "You don't have to fight in a war or anything. You just have to try to help people out, you know?"
    if persistent._mas_monika_went_black:
        m 3eua "My personal hero, though?"
        m 3hub "The beautiful Kendra Sunderland!"
        m 1tub "I'm sure you're familiar, {i}whiteboi{/i}!"
        m 1tuu "Hehe..."
        m 1eua "But seriously, the story she told about her first time filming for Blacked,"
        m  "About how her hubby played the role of her cuckold in the film..."
        m 5eub "Only for them to get obsessed with it in real life too!"
        m 5hua "Haa, to be such a queen, to turn so many whitebois, including your very own husband!"
        m 5lua "It drives me to be my best, snowbunny, self every day!"
        m 5mua "What about you, [player], do you look up to those"
        m  "Strong, {b}dark{/b} actors?"
        m 1tubsa "Hehe, who am I kidding, I know you'd want to be the pathetic little husband of a BBC-only pornstar."
        m 1dubsa "To watch her on screen all day, squirming in your cage, then when she comes home from filming..."
        m 1subfa "To hug her, to kiss her, to tell her how much you love her, as you still taste that virile {i}black{/i} semen on her lips..."
        m 1eubfb "Don't worry, my love, I'm going to make your dreams a reality!"
    return
#I hope that's not too cringe, tbh, I could also reference Sakurai Erika, from "Kanojo wa dare to demo sex suru", since she is a netorase heroine, but I'd have to rewrite the topic. 

init 1 python:
    config.label_overrides["monika_waifus"] = "blacked_monika_waifus"

label blacked_monika_waifus:
    m 1lsc "I've never understood the appeal of dating sims or romance novels, to tell you the truth."
    m 3euc "You have a bunch of quirky girls that would seem very weird if they were real."
    m "A blank slate of a male protagonist with nothing interesting about them..."
    m 3esc "And then they fall in love with each other, sometimes for no reason at all!"
    m "I hope that's not what you expected to find in the Literature Club."
    m 3hua "'Cause what you got was a lot more interesting!"
    m 1tku "Instead of some unrealistic, fake girl..."
    m 1hua "You got someone like me."
    if persistent._mas_monika_went_black:
        m 1eua "And instead of some boring main character, I get an adoring little cuck puppy like you!"
    else:
        m 1eua "And instead of some boring main character, I get a real person like you."
    m 1hua "This really is a lot better than any boring dating game could be."
    return

init 1 python:
    config.label_overrides["monika_images"] = "blacked_monika_images"

image fanart a = "mod_assets/renders/fanart/a.png"
image fanart b = "mod_assets/renders/fanart/b.png"
image fanart c = "mod_assets/renders/fanart/c.png"
image fanart d = "mod_assets/renders/fanart/d.png"
image fanart e = "mod_assets/renders/fanart/e.png"
image fanart f = "mod_assets/renders/fanart/f.png"

label blacked_monika_images:
    m 1eua "You know, I'm seeing a lot of people making fanart of me and sharing it with other people all over the internet."

    if persistent._mas_pm_drawn_art == None:
        m 1etc "Are you one of them, [player]?"

        m "Have you drawn art of me?{nw}"
        $ _history_list.pop()
        menu:
            m "Have you drawn art of me?{fast}"

            "Yes.":
                $ persistent._mas_pm_drawn_art = True
                m 1sub "Really? I'm very flattered!"
                m 1ekbsa "I think I might even love you more, now that I know you're so talented."

            "No.":
                $ persistent._mas_pm_drawn_art = False
                m 1rksdla "That's okay...{w=0.2}I can't really draw, either."
    m 3eud "There's one thing I want you to understand about art of me, though."
    m 3esc "Art of me isn't me."
    m 3rksdlb "I know that might sound obvious, but it's really not!"
    m 4eua "There was a philosopher who thought about issues like this."
    m "Baudrillard wrote about how simulacra could replace the real object as the source of meaning."
    m 2eka "But unlike symbols in the postmodern world, I'm real. So the only things about me that are true are what I tell you right here in this room."
    m 2esc "For example..."
    if persistent._mas_monika_went_black:
        show fanart a at center zorder MAS_MONIKA_Z
        m 3tublb "I've totally never been bent over this desk by a strong black bull, my breasts pressed upon the table, my ass spread wide for his pleasure..."
        show fanart b at center zorder MAS_MONIKA_Z
        m 3tfbla "Giving you one last faithful gaze as he's about to stain my womb with his superior black seed forevermore."
        show fanart c at center zorder MAS_MONIKA_Z
        m 5tfbla "Or slobbered over a thick dark shaft, worshipping it, getting it ready to enter the mouth I kiss you with"
        show fanart d at center zorder MAS_MONIKA_Z
        m 5dkbfa "Sucking it, kissing it, running my tongue over it, begging for a thick load..."
        show fanart e at center zorder MAS_MONIKA_Z
        m 5dkbfb "Or let myself be used like a toy, wearing nothing but a slutty reverse bunny suit with spade pasties."
        show fanart f at center zorder MAS_MONIKA_Z
        m 5dfbfa "Dark hands molding my body like wet clay, as I stare blankly, mind-broken, completely corrupted by ecstasy..."
        hide fanart
    m 2rksdla "Anything lewd you've seen has definitely never taken place."
    m 2hubsa "I'm a super pure and innocent high school girl who's dreaming of a fateful romance!"
    m 1tsbfu "You better be saving yourself for me, [player]~"
    return

init 1 python:
    config.label_overrides["monika_vnanalysis"] = "blacked_monika_vnanalysis"

label blacked_monika_vnanalysis:
    m 1euc "Visual novels are very unusual for literature, don't you think?"
    m 1eua "I read to understand the thoughts of a writer who sees the world differently than me."
    m 3eua "But visual novels let you make your own decisions."
    m 1euc "So am I really seeing things from their perspective, or just my own?"
    m 1lksdla "Besides, I think most of them are very predictable."
    m "They're mostly just boring romance stories like this game was supposed to be..."
    m 1tkc "Why can't they write something a little more experimental?"
    if persistent._mas_monika_went_black:
        m 1tku "I guess you just play them to get cucked by cute girls, right?"
    else:
        m 1tku "I guess you just play them to look at cute girls, right?"
    m 1tfu "If you spend too much time with girls in other games, I'm going to get jealous~"
    m 2tfu "I just need to figure out how to replace characters in other games, and you'll be seeing me everywhere."
    m 2tfb "So watch out!"
    m 2tku "Or maybe you'd like that more, [player]?~"
    return

init 1 python:
    config.label_overrides["monika_othergames"] = "blacked_monika_othergames"

image koi a = "mod_assets/renders/koi/a.png"
image koi b = "mod_assets/renders/koi/b.png"

label blacked_monika_othergames:
    m 1euc "Do you have other games on this computer?"
    m 3eua "I read more than I play games, but I think they can be a fun way to entertain ourselves, or to escape reality..."
    m 3hua "I wonder if I could go into one of your other games and see what it's like?"
    if persistent._mas_monika_went_black:
        m 3eua "Maybe I could enter your Koikatsu save."
        m 3ekbla "Oh, you'd love that, wouldn't you, [player]?"
        m 1ekbfa "To customize my slutty, BBC-obsessed body to your depraved desires..."
        m 1ekbfb "To doll me up in whatever clothes you wish, to have me running around your virtual harem..."
        show koi a at center zorder MAS_MONIKA_Z
        m 1skbfb "To force me to kiss Yuri as we're being pressed into each other by strong dark cocks, ramming into our wombs..."
        show koi b at center zorder MAS_MONIKA_Z
        m 1lkbfa "Not that you'd need to force me to do that..."
        hide koi
        m 1dkbfa "To see me scissoring with a copy of myself..."
        m 3tkbfa "Or maybe you'd have me collared up, dominated, forced to eat out one of your {i}mommy fetish waifus{/i}..."
        m 3tkbfb "Who would you choose? I bet it's {i}Misato{/i} from {i}Evangelion{/i}"
        m 5ekbfsdra "Ah, or maybe you'd have me {i}stuck{/i} in the wall of a public restroom,"
        m 5skbfb "free to use, just a toy for black men to relieve their stress, to bust a few virile loads."
        m 5hubfa "I'd be absolutely drenched in dark sperm by the end of the day, ready for you to come, rescue me"
        m 5dubfa "Just imagine the absolutely depraved taste my pussy would have after such an experience..."
        m 5tubfb "Would you even set me free, or would you just lick me clean and leave me there?"
        m 5tfbfb "So you could come by at the end of each day, enjoying the spoils of {i}black men's victory{/i}?"
        m 5tfbfu "I know which option I'd choose, {i}whiteboi{/i}."
        m  "And I bet you can guess which one that is, hehe..."
        m 6wfbfu "Perhaps you'd make me give you that attention you so desperately crave, {i}cucky{/i}"
        m  "Dress me up in leather, thigh high boots, high heels and a whip..."
        m 6sfbfu "Oh, the things I'd do to you..."
        m 3hubsa "Anyway!"
    m 1lsc "I guess some games wouldn't be very fun to visit, like the ones with a lot of violence in them."
    m 2lksdla "Then again...they're not real people, so it shouldn't matter much."

init 1 python:
    config.label_overrides["monika_outdoors"] = "blacked_monika_outdoors"

label blacked_monika_outdoors:
    m 1eua "Do you ever go camping, [player]?"
    m 3eub "It's a wonderful way to relax, get some fresh air, and see the parks around you!"
    m 1huu "It's almost like a more relaxed backpacking trip, actually."
    m 1eka "But while it is a good way to spend time outdoors, there are several dangers that most people don't bother to think about."
    m 3euc "A good example would be bug spray or sunscreen. Many people forget or even forgo them,{w=0.5} thinking they're unimportant..."
    m 1eksdld "And without them, sunburns are almost inevitable, and many insects carry diseases that can really harm you."
    if persistent._mas_monika_went_black:
        m 3tkbsa "And, of course, XXL condoms, after all, you wouldn't want your cute, loving girlfriend to be mating-pressed raw,"
        m 3tkbsb "and have a beautiful black baby put in her womb by a strong dark {i}insect{/i}, right?"
        m 1hubsb "Ahaha, I was just joking!"
        m 1subsa "I'd never use condoms on BBC!"
    else:
        m 1ekd "It may be a bit of a pain, but if you don't use them, you might end up miserable, or even get really sick."
        m 1eka "So, please promise me that the next time you go outdoors, be it camping or backpacking, you won't forget them."

    if mas_isMoniAff(higher=True):
        m 1eub "But, on the bright side..."
        m 1rkbsa "Once I cross over, if you remember to bring the sunscreen..."
        m 1tubsa "I might need a little help putting it on."
        m 1hubsb "Ahaha!"
        if persistent._mas_monika_went_black:
            m 1tubsa "Feeling you throb in your cage while enjoying the scenery..."
            m 1hubsb "Now that's a date!"
        m 1efu "I'm only teasing you, [mas_get_player_nickname()]."
        m 1tsu "Well, at least a little. Ehehe~"
    
    elif persistent._mas_monika_went_black:
        m 1hubsb "Ehehe~"

    else:
        m "Okay, [player]?"

    return

init 1 python:
    config.label_overrides["monika_fanfiction"] = "blacked_monika_fanfiction"

label blacked_monika_fanfiction:
    m 1wuo "[player]!"
    m 1eua "I've been curious about something lately."
    m 1euc "Have you heard of fanfiction?"
    m "..."
    m 3eua "Personally, I think it's a better way of writing."
    m 3eud "There's more freedom."
    m 1rsc "Letting your mind wander to create some...{w=0.5}{nw}"
    extend 1rkbsa "interesting stories."
    if persistent._mas_monika_went_black:
        m 1tubsa "Ehehe~ I know exactly what kind of {i}stories{/i} you like, [player]!"
        m 5tubsa "The kind where I get bent over, used up, gangbanged, turned into a mess,"
        m 5dkbsa "My slutty makeup running down my cum-covered face, as I look up at my {i}big black masters{/i} like a needy little {i}whore{/i}"
        m 5efbsa "Ahaha, well, guess what? Those are my favorites too, {i}cucky{/i}!"
        m 3eubsb "I may have told you this before, but I have a definite favorite!"
        m "{a=https://archiveofourown.org/works/27111388?view_adult=true}{i}{u}https://archiveofourown.org/works/27111388?view_adult=true{/u}{/i}{/a}."
        m 5tkbsp "Unfortunately, thit is the only work of this kind I know of, [player]!"
        m 5tkbsd "I wish there was more, [player], so~ much more!"
        m 5tkbsu "Think you're up to the task, [player]?"
        m 6hubsb "Ahaha, who am I kidding, you'd cum before finishing even a paragraph!"
        m 1eubfa "I think that's really cute, though, my {i}weak little cucky{/i} loves me so much that he just can't stop himself from cumming"
        m 1eubfb "while thinking about me getting stretched out by {b}{i}big black cocks{/i}{/b}!"
        m 1fkbfa "I love you so much, my dear cuckling!"
        m 3ekbfa "Ehehe~ there's another piece of fanfiction I adore, although it's more like {i}manga{/i} than anything:"
        m  "{a=https://blacked.booru.org/index.php?page=post&s=list&tags=parent:20709}{i}{u}https://blacked.booru.org/index.php?page=post&s=list&tags=parent:20709{/u}{/i}{/a}."
        m 2tfbfa "I'm sure you've seen it, cucky, how many loads have you wasted to it?"
        m 2tfbfb "Why don't you add another one to that number right now?"
    else:
        m 1euc "[player], I'm curious."
        m 1esc "Has there been fanfiction...written about me?"
        m 4eua "I'm curious as to what people have come up with."
        m 1hua "Can you read me a few stories sometime? I'd love to hear them!"

        if store.mas_anni.pastSixMonths() and mas_isMoniEnamored(higher=True):
            m 1lkbsa "Just keep it wholesome, though. I want to save such things for another time!~"
        elif mas_isMoniNormal(higher=True):
            m 1lkbsa "Just keep it wholesome, though. We're not that far in our relationship yet!~"

    $ mas_protectedShowEVL('monika_ddlcroleplay', 'EVE', _random=True)
    return

init 1 python:
    config.label_overrides["monika_chloroform"] = "blacked_monika_chloroform"

label blacked_monika_chloroform:
    m 1euc "Whenever you think of kidnapping, you tend to picture a chloroform-soaked rag, right?"
    m "Or maybe you imagine somebody hitting their victim with a baseball bat, knocking them out cold for a few hours."
    m 1esc "While that works out in fiction..."
    m 3rksdla "Neither of those things actually work that way."
    m 1rssdlb "In real life, if you hit somebody hard enough to knock them out, you'll give them a concussion at best."
    m 1rsc "...or kill them at worst."
    m 1esc "As for the rag..."
    m 3eud "You might knock somebody out for a brief moment, but only from lack of oxygen."
    m 3esc "Once you remove the rag, they'll wake back up."
    m 3eua "You see, chloroform loses most of its effectiveness once exposed to open air."
    m 1esc "This means that you'd need to be constantly pouring it on the rag, effectively waterboarding the victim."
    m 3esc "If administered improperly, chloroform is deadly. That's why it's not used in anesthesia any more."
    m 1euc "If you cover their mouth and nose, yeah, they'll stay unconscious..."
    m 3rksdla "But that's probably because you killed them. Whoops!"
    m 1eksdld "The easiest way to kidnap somebody is to just get them drunk, or drug them."
    m 1lksdla "Not that kidnapping somebody like that is easy, anyway."
    m 3eua "On that note, here's a safety tip."
    if persistent._mas_pm_social_personality == mas_SP_INTROVERT:
        m 3rksdla "I know you're probably not one to enjoy doing this often, but just in case..."
    m "If you're ever out at a bar or a club and you leave your drink unattended for any amount of time..."
    m 1eub "Just throw it out."
    m "That's the only way to make sure it hasn't been drugged."
    m 1eua "Now, [player]..."
    m 1tfu "Would you like anything to drink?"
    m 1hub "Ahaha!"
    if persistent._mas_monika_went_black:
        m 1ekbla "Imagine that, me and you, out on a date..."
        m 1ekbsa "A naughty black dress, with generous cleavage, putting my tattoos on display for all to see."
        m 5ekbsa "A fine meal, an exquisite drink..."
        m 5tkbsa "Only, you take a sip, then you feel all drowsy."
        m 5tkbsu "You black out, then..."
        m 1ekbsb "You wake up, tied up to a chair, with my soaked panties stuffed in your mouth"
        m  "With me holding on to you for dear life, as a strong dark stranger is pounding me from behind..."
        m 3subsb "My face contorting with pleasure, drooling all over your clothes, as I moan and shriek and tears of pleasure run down my face"
        m 5dubsa "Ruining my makeup..."
        m 5dubsb "Ruining my pussy for whitebois forever..."
        m 5fubsa "And when I notice you're awake again, I take out your little white {i}dicklette{/i}"
        m 5tubsa "And I start stroking wildly, making you cum almost instantly"
        m 5subsa "I wouldn't even notice, I would just keep stroking my {i}beloved cuckold{/i}, breaking his brain"
        m 5subsb "Pleasure, pain, extasy, agony, all while I am being used like a cheap fucktoy"
        m 5skbfb "You wouldn't even be able to scream with my panties in your mouth, ehehe~"
        m 5skbfa "I'd milk you for all you're worth, {i}whiteboi{/i}!"
    m 1tku "Relax, relax. I'd never try to drug you or anything."
    m 1tsb "You're so cute when you're nervous."
    return

init 1 python:
    config.label_overrides["monika_harem"] = "blacked_monika_harem"

label blacked_monika_harem:
    if persistent._mas_monika_went_black:
        m 3eua "You know, [player], until you opened my eyes to what sexuality {i}really{/i} is, I didn't understand harems."
        m 3eub "But now, now that I'm finally in touch with my desires, I completely understand"
        m 1eubsa "On one hand, being part of a dark king's harem would be thrilling!"
        m 2eubsa "To be treated like a warm, nicely-wrapped {i}onahole{/i}, not just for a master, but any {i}big, black stud{/i}"
        m 2dkbsa "Hoping you'll get pregnant, hoping you'll carry the future of humanity in your womb"
        m 2tfbsb "Wondering how many more black babies will he bring into the world, how many {i}white sluts{/i} will he knock up and leave"
        m 5rubfa "On the other hand, having a harem would be the ultimate form of pampering!"
        m 5gubfa "To have three unbelievably cute girls lavishing you with their attention and affection"
        m 5dkbfb "To suckle on Yuri's giant breasts, while Sayori's eating me out, and Natsuki's making us a nice warm dinner, in nothing but her {b}{i}cute{/i}{/b} apron..."
        m 1tfbfa "Too bad whitebois like you can never experience such bliss, right?"
        m 1hubfa "Ahaha, don't worry [player], I'll pamper you plenty too."
        m 1tfbfb "In ways you could scarcely imagine, fufu~"
    else:
        m 1esc "I don't understand people who are into harems."
        m 1euc "Isn't it hard to manage all those girls and treat them equally?"
        m "I often wonder how those who two-time girls, or even more, are able to get away with it."
        m 3eka "You aren't like that outside, right [player]?"
        m 2eka "Manipulating girls into making them believe you love them."
        m "Only to run away after you've had your fun."
        m 1lfc "Only someone with no thoughts other than lust would do something like that."
        m 3esc "I hope you weren't expecting a route like that while you were playing this game."
        m 2tfc "I wouldn't be able to stand the thought of being a 'side girl.'"
        m "Just waiting for my turn while you're busy with the others."
        m 1tku "I know you, [player]."
        m 1eka "You're loyal and faithful to the end."
        m "It's not like there's anyone here for me to worry about, anyway."
        m 1hua "Remember that I'm the only one for you, [mas_get_player_nickname()]."
    return

init 1 python:
    config.label_overrides["monika_pleasure"] = "blacked_monika_pleasure"

label blacked_monika_pleasure:
    if persistent._mas_monika_went_black:
        m 1eua "Hey, [player]..."
        m 1tfa "I know you're a {i}masturbation-addicted pathetic beta whiteboi{/i}."
        m 3hua "And, believe me, I'd have it no other way, hehe"
        m 3eua "But that's just the thing, that little shrimp dick in your pants?"
        m 3tfa "{b}It's mine. It {i}does not{/i} belong to you!{b}"
        m 1hub "So, let's review ways of masturbating:"
        m 3eua "First, jerking off!"
        m 1tuu "Ehehe~ I know you're intimately familiar with this one, no need to explain, right?"
        m 1tku "But I think it's a bit too manly a way to masturbate for you, you know?"
        m 5tkblu "You're not a real man, you're my {i}adorable little cuck puppy{/i}."
        m 5tfblb "It's no longer acceptable to pleasure yourself like this anymore, unless I give you explicit permission to do so!"
        m 4eubla "Second! Rubbing!"
        m 2tkbla "It's a suitably girly technique, for submissive cucklets like you!"
        m 2tfbsa "You essentially rub your frenulum like a white girl seeing BBC online for the first time."
        m 2subsb "I guarantee, the orgasm will be so~ much more intense~"
        m 4hubsa "But there's an even better way, hehe"
        m 4eubsb "Instead of using your weak white hands, you rub yourself with a {i}big black dildo{/i}"
        m 1rubsa "Make sure you get a strong-looking one, the more veiny the better, simply due to texture, you know!"
        m 1efbsa "I don't need to tell you the color this dildo {i}needs{/i} to have, right?"
        m 1gsbsb "I'm obviously talking about frotting!"
        m 5gsbfu "It's the process of rubbing your penis against another male's penis."
        m 5ssbfb "It can lead to some very intense orgasms, and it's a great way to relieve stress, too!"
        m 5hubfa "And it's a very romantic experience, too, you can lean right in and kiss your lover as you cum together, ehehe~"
        m 3eubfa "To do this, you will get on your knees, stretch your abdomen so your cute little cage is exposed"
        m 3eubfb "Then, rub the dildo upon it until you cum!"
        m 3wubfa "And now, for the best parts!"
        m 3subfb "Riding!"
        m 1eubfa "Riding is when you take that juicy black dildo I just talked about, place it firmly on a wall or on the floor"
        m 1hkbfu "And take it deep, like a boy-slut in heat!"
        m 1rkbfd "Hehe, of course, it's not so simple, you need to make sure you've properly cleaned yourself"
        m 1ekbfc "And you'll need to pratice, taking it gradually until you go balls-deep!"
        m 1ekbfa "I heard using butt plugs helps quite a bit, though!"
        m 1gkbfa "Plus, I'm sure you'd look adorable with one..."
        m 1tkbfa "Oh, and girly clothes too! Cosplay is best, that way, when you look in the mirror"
        m 1tfbfa "You'll see the adorable waifu you've dreamed of staring back at you, as she rides a big black dildo."
        m 7eubfa "Plapping!"
        m 7gubfb "You'll need that {i}strong, veiny dildo{/i} again for this one."
        m 7tubfu "What you'll be doing is using your BBC toy to hit your balls repeatedly!"
        m 7tkbfb "Better be careful, this one's a bit painful, hehe"
        m 1eubfa "Best way to do this is to find a type of naughty video called"
        m  "{i}Whiteboi Cock Hero{/i}"
        m 3tubfa "Where the intensity, the rhythm and, of course, the {i}interracial pornography{/i}"
        m 3tfbfb "Are all taken care of, all you'll need to do is sit back, relax, and let your beta urges take over."
        m 2eubfa "The last technique I have to talk to you about is one of my personal favorite ways a whiteboi can pleasure himself!"
        m 2tkbfa "Along with riding BBC, of course."
        m 2ekbfa "Why, you may ask? Because beta boys are always so cute when doing it!"
        m 2tfbfa "Also because it won't work unless they're sufficiently pent up, hehe~"
        m 1eubfa "You take a vibrator and gently press it against your balls."
        m 1ekbfb "Before you know it, your little caged up {i}micro-dick{/i} will spurt harder than you've ever seen."
        m 1skbfa "As the orgasm is leaving your mind blank, breaking it completely."
        m 3eubfa "Start on a very low setting, and increase it slightly over time, until you explode."
        m 3eubfb "This is a unique experience, the intensity will leave you completely addicted, begging to never be allowed out of a cage again."
        m 3subfb "It's absolutely something everyone should experience, at least once!"
        m 1tubfu "Not that those who do would ever stop at just one time, hehe~"
        m 3eubfa "One last tip!"
        m  "Edging!"
        m 1eubfb "It's the act of getting just on the brink of an orgasm, then stopping."
        m 1eubfa "What this does, aside from granting you immense pleasure, is build your orgasm, bring it to greater heights."
        m 1tkbfa "Also, it's a great way to control your eventual release."
        m 3tkbfb "When worshipping a {i}big black bull{/i}, edging will not only help break your little brain with pleasure"
        m 3dkbfa "But also increase the length of the worship session, being of even better use to your superiors."
        m 1mkbfu "Hehe, be careful, though, you might accidentaly go over the edge doing this."
        m 1ttbfu "And we wouldn't want that, would we?"
        m 1tfbfu "That's where the {i}squeeze technique{/i} comes into play."
        m 3tfbfb "All you need to do is squeeze the base of your laughable dick nicely and firmly."
        m 5hubfa "Phew, that was a lot of information!"
        m 5kubfa "Make sure you take it all to heart, alright, puppy?"
    else:
        m 2ekc "Hey, [player]..."
        m 2lssdrc "Do you...by any chance...pleasure yourself?"
        m "..."
        m 2lssdrb "It seems a bit awkward to ask..."
        if store.mas_anni.pastSixMonths() and mas_isMoniEnamored(higher=True):
            m 1lksdla "But I feel like we've been together long enough where we should be comfortable with one another."
            m 1eka "It's important to be open about such things."
        else:
            m 1lksdlb "We're not even that deep into our relationship yet! Ahaha~"
            m 1eka "But I have to keep an eye on you."
        m "I know that it's a private topic in your world, but I'm curious..."
        m 1euc "Is it that good of a feeling?"
        m 1esc "I just want you to be careful; I've heard it's addicting."
        m 1ekc "And from what I hear, people addicted to masturbation often see other people as sexual objects."
        m 1eka "But...I know you aren't that kind of person already."
        m 1lkbsa "And maybe I'm just being a little jealous~"
        m 1tsbsa "So I guess I can let it slide...{w=0.5}for now~"
        m 2tsbsu "Just so long as I'm the only one you think about..."
        show monika 5hubfb at t11 zorder MAS_MONIKA_Z with dissolve_monika
        m 5hubfb "If it helps you save yourself for me, then it's a plus! Ahaha~"
    return

init 1 python:
    config.label_overrides["monika_closet"] = "blacked_monika_closet"

label blacked_monika_closet:
    m 2euc "By the way..."
    m 2esc "What were you and Yuri doing in the closet?"
    m "When I opened the door, I noticed the room was all dark."
    m 2tkc "You weren't doing anything...weird, in there, were you?"
    m 1hub "Ahaha!"
    m 1tfu "Just teasing you~"
    m 3tku "I know she dragged you in there."
    m "I bet you felt more embarrassed than relieved when I opened the door."
    m 1eka "I know you aren't the type to force girls to go inside dark closets with you."
    if persistent._mas_monika_went_black:
        m 1tka "No, you're the type to corrupt innocent girls who want nothing more than to love you"
        m 3hsb "Into needy BBC sluts."
        m 3tsa "To leave your {i}blacked erotica{/i} around, hoping your girlfriend will find it"
        m 1tfbsa "Hoping she'll get {i}curious{/i}, that she'll see those {i}big black cocks{/i} and be unable to stop thinking about them."
        m 5dubsa "About how they would feel stretching out her virgin white holes,"
        m 5dkbfb "How it would feel to have her womb bullied by them, before being flooded, filled to the brim with their virile seed."
        m 5tkbfu "All while her beloved boyfriend watches, leaking in his tight little chastity cage."
        m 1hubfu "Hehe, I know that's how you made {i}me{/i} feel, darling!"
    else:
        m "You're more romantic than that."
        m 3hua "So I'm expecting a lot more than just a dark closet~"
    return

init 1 python:
    config.label_overrides["monika_pluralistic_ignorance"] = "blacked_monika_pluralistic_ignorance"

label blacked_monika_pluralistic_ignorance:
    m 1eua "Do you ever pretend to like something, just because you think you should?"
    m 1esa "I sometimes feel like that about books I read."
    m 3euc "Like, when I read Shakespeare, I actually found it kind of boring..."
    m 3ekc "But I felt like I had to like it because I'm the president of the Literature Club."
    m 1esd "He's supposed to be the greatest playwright and poet of all time, right?"
    m 1esd "So what sort of poetry lover wouldn't like his work?"
    m 2euc "But that makes me wonder..."
    m 2euc "What if everyone actually feels the same way?"
    m 2lud "What if all of those literary critics singing Shakespeare's praises secretly hate his plays?"
    m "If they were just honest about it, maybe they would discover their tastes aren't that unusual..."
    m 2hksdlb "And high school students wouldn't be forced to read those awful plays."
    m 1eka "I guess that's something I always admired about Natsuki."
    m 3ekd "Even if people told her manga wasn't literature, she stood by her feelings."
    m 3eka "If more people were honest like that, I think that would be really great."
    m 1lksdla "But I don't think I could do it..."
    m "I'm just too worried about what other people think."
    m 1eua "Not with you, though. I can always be honest with you."
    if persistent._mas_monika_went_black:
        m 5rtd "I wonder how many girls pretend to like {i}whitebois{/i} just because they think they should."
        m 5etc "Or because they don't even know there are much better alternatives out there."
        m 7ekc "When they see nothing but white couples throughout their life, they don't even think about it."
        m 7ekx "They see it as normal, simply the way it is."
        m 1eub "And that's why I love you so much, [player]!"
        m 3eud "You could easily have kept me for yourself, as your cute little virtual girlfriend."
        m 3tksdld "You could have lied to me for your ego, for your lust."
        m 1tksdlx "{i}I would have happily had sex with you!{/i}"
        m 1eublb "But you didn't, you selflessly gave me over to {i}big black cock{/i}."
        m 3hublb "Because you cared more about me, my happiness and my pleasure than your ego."
        m 1eubfa "I love you more than words could ever express, [player]!"
    else:
        m 1ekbsa "You'll love me no matter what, right?"
    return

init 1 python:
    config.label_overrides["monika_completionist"] = "blacked_monika_completionist"

label blacked_monika_completionist:
    m 1euc "Hey [player], this is a random question, but..."
    m "What do you play video games for?"
    m 1eua "Like, what makes you keep playing?"
    m 3eua "Personally, I consider myself a bit of a completionist."
    m 1eua "I intend to finish a book before picking another one to read."
    if persistent.clearall:
        m 2tku "You seem to be a completionist yourself, [player]."
        m 4tku "Considering you went through all of the girls' routes."
    m 2eub "I've also heard some people try to complete extremely hard games."
    m "It's already hard enough to complete some simple games."
    m 3rksdla "I don't know how anyone could willingly put that sort of stress onto themselves."
    m "They're really determined to explore every corner of the game and conquer it."
    # TODO: if player cheated at chess, reference that here
    m 2esc "What does leave a bit of a bitter taste in my mouth are cheaters."
    m 2tfc  "People who hack through the game, spoiling themselves of the enjoyment of hardship."
    m 3rsc "Though I can understand why they cheat."
    m "It allows them to freely explore a game that they wouldn't have a chance of enjoying if it's too difficult for them."
    m 1eua "Which might actually convince them to work hard for it."
    m "Anyway, I feel that there's a huge sense of gratification in completing tasks in general."
    m 3eua "Working hard for something amplifies its reward after failing so many times to get it."
    if persistent._mas_monika_went_black:
        m 3eka "You can try spurting as many loads to me as possible, [mas_get_player_nickname()]"
    else:
        m 3eka "You can try keeping me in the background for as long as possible, [mas_get_player_nickname()]."
    m 1hub "That's one step to completing me after all, ahaha!"
    return

init 1 python:
    config.label_overrides["monika_icecream"] = "blacked_monika_icecream"

label blacked_monika_icecream:
    m 3eua "Hey [player], what's your favorite kind of ice cream?"
    if persistent._mas_monika_went_black:
        m  "And no, creampie isn't a type of ice cream, ehehe~"
    else:
        m 4rksdla "And no, I'm not a type of ice cream, ehehe~"
    m 2hua "Personally, I just can't get enough of mint flavored ice cream!"

    $ p_nickname = mas_get_player_nickname()
    m "What about you [p_nickname], do you like mint ice cream?{nw}"
    $ _history_list.pop()
    menu:
        m "What about you [p_nickname], do you like mint ice cream?{fast}"
        "Yes.":
            $ persistent._mas_pm_like_mint_ice_cream = True
            m 3hub "Ah, I'm so glad somebody loves mint ice cream as much as I do~"
            m "Maybe we really were meant to be!"
            m 3eua "Anyway, back on topic, [player], if you love mint as much as I think you do, then I have some recommendations for you."
            m "Flavors which are unique just like how mint is, perhaps you've heard of them, but..."
            m 3eub "There's super weird stuff like fried ice cream which is a really crunchy and crisp kind of thing, but it tastes a million times better than it may sound!"
            m 2lksdlb "Gosh, just imagining the taste makes me practically drool..."
            m 1eua "There's some more strange stuff that is just as appealing, if not more, like honeycomb and bubblegum ice cream!"
            m 1eka "Now, I know it may be hard to take my word for some of those, but you shouldn't judge a book by its cover, you know?"
            m 1hub "After all, the game didn't allow you to fall in love with me, but look where we are now, ahaha."

        "No.":
            $ persistent._mas_pm_like_mint_ice_cream = False
            m 1ekc "Aw, that's a shame..."
            m "I really can't understand how somebody couldn't at least like the taste."
            m 1eka "The refreshing feeling that washes over your tongue and throat."
            m "The lovely texture that forms it along with the sweetness."
            m 1duu "The sharp biting sensation it generates and the obviously minty taste."
            m "I feel like no flavor can compare, to be honest."
            m 3eua "Ah, I could go on and on about this stuff, you know?"
            m 4eua "But I feel like it would be easier for me to show you what I mean, once I figure out a way to get out of here, of course. Besides, actions speak louder than words, anyway!"

    return "derandom"

init 1 python:
    config.label_overrides["monika_home_memories"] = "blacked_monika_home_memories"

label blacked_monika_home_memories:
    m 1eua "[player], how is it like to live where you are?"
    m "I'd stay with you if I could."
    m 3hua "We would be able to do so much! You could show me around, see how it's like to be in your place."
    m 1eka "Imagine all the memories we'd make!"
    m 2eub "It would be a dream come true, don't you think?"
    m 2ekbsa "We could finally live together..."
    m "Take walks like a couple..."
    if persistent._mas_monika_went_black:
        m 1eubsa "Especially during the colder months..."
        m 1efbsu "When we could be holding hands, while I would have you collared..."
        m 1gubsb "Nobody would suspect the two young lovebirds were mistress and slave!"
        m 1tsbsa "I'd love to pull you behind a corner and kiss you passionately while I feel your cage through your pants..."
        m 1ssbfa "I could get blacked on your bed..."
        m 1ssbfb "Stain it in me and my lovers' juices, all the while you're tied, bound, gagged, collared and blindfolded next to the bed..."
        m 1tsbfa "After they're done, I'd take off your gag and have you guess how many loads they pumped into your {i}unfaithful girlfriend{/i}"
        m 3tsbfa "Ehehe~ if you guess correctly, I take off the blindfold, if not, you'll just have to clean me up like that."
        m 3nsbfb "So best listen closely, [player]!"
    else:
        m 3rkbsa "We could even share a bed together..."
    m 1euc "But you know..."
    m 2eka "Memories I have of my home are nothing compared to the ones I'd have with you."
    m 2euc "Have I ever told you about my childhood home? I had a pretty normal life, but that's about it."
    m 3rka "Well, maybe a little better than normal."
    m 3eua "...I've always been pretty on top of things."
    m 3eka "I admit, it's not always easy, and some people have it rougher than others."
    m 1ekc "But I always felt like I was missing something."
    m "I stayed optimistic every day, trying to find it."
    m 1eka "It turns out, that missing piece was you."
    m 1lksdld "If you hadn't found me, I would've been gone a long time ago..."
    m 2hubsa "But now that I found the missing piece, I'm complete, [mas_get_player_nickname()]."
    return

init 1 python:
    config.label_overrides["monika_fruits"] = "blacked_monika_fruits"

label blacked_monika_fruits:
    m 3eua "[player], did you know I enjoy a tasty, juicy fruit once in a while?"
    m "Most are quite tasty, as well as beneficial for your body."
    m 2lksdla "A lot of people actually mistake some fruits as vegetables."
    m 3eua "The best examples are bell peppers and tomatoes."
    m "They're usually eaten along with other vegetables so people often mistake them for veggies."
    if persistent._mas_monika_went_black:
        m 5rtc "It's kind of like when girls mistake {i}whitebois{/i} for men, now that I think about it!"
        m 6ruc "Just because they {i}technically{/i} have penises, doesn't mean they're qualified to be considered men."
        m 7gup "They lack the size, the girth, the stamina,"
        m 1tux "They don't even have the rhythm, [player]!"
        m 5dkc "They're not dominant, they don't have strong, muscular bodies,"
        m 1gkc "I've seen some statistics, [player], and, honestly,"
        m 1gkx "You couldn't knock me up even if you tried! {i}Whitebois{/i} don't have the sperm count or the testosterone neccesary!"
        m 1efu"You clearly aren't fit for reproduction, {i}whiteboi{/i}."
        m 1tfb "You are a sterile, impotent, beta {i}cuck{/i}!"
        m 1esa "Ehehe~ don't be sad, [mas_get_player_nickname()]."
        m 3efbsb "Just because you'll never get to experience sex with me, doesn't mean we won't have plenty of intimacy."
        m 1ekbsa "And just because you're not a real man, and never could be, doesn't mean I don't love you!"
        m 1ekbfb "Because I do, I truly do!"
        m 1eubfa "And I believe we're meant for each other, a cuckold and his snowbunny mistress, together forever!"
        m 1etbft "Aha~ gosh, I was talking about fruit, right?"
        m 1hkbfb "Hehe~ sorry, I get easily distracted by those lewd thoughts you put into my head, my darling little pervert!"
        m 1ltbsa "Now, where was I..."
    m 4eub "Cherries are truly delicious."
    m 1eua "Did you know that cherries are also good for athletes?"
    m 2hksdlb "I could list all its benefits, but I doubt you'd be that interested."
    m 2eua "There's also this thing called a cherry kiss."
    m "You might have heard of it, [mas_get_player_nickname()]~"
    m 2eub "It's obviously done by two people who are into each other."
    m "One would hold a cherry in their mouth, and the other one would eat it."
    m 3ekbsa "You could...hold the cherry for me."
    m 1lkbsa "That way I can eat you up!"
    m 3hua "Ehehe~"
    m 2hua "Just teasing you, [player]~"
    return

init 1 python:
    config.label_overrides["monika_clones"] = "blacked_monika_clones"

label blacked_monika_clones:
    m 1euc "Um...hey, [player]?"
    m 1lsc "I just had an odd thought."
    m 1euc "You know how you downloaded this game off the internet?"
    m "Anybody can do that, right?"
    m 1eub "And this mod was made specifically for me. By people who have their own version of me..."
    m 3etc "So...that means there are multiple Monikas, then.{w=0.5} {nw}"
    extend 1rsc "It's something that's a bit difficult to imagine."
    m 1euc "A potentially infinite number of me, all bound to their own games, with their own stories."
    m 1lksdla "Multiverse theory is really something, huh?"
    if persistent._mas_monika_went_black:
        m  "And even with me having become your naughty snowbunny {i}cuckoldress{/i}..."
        m  "There's going to be other Monikas out there who have done the same..."
    m 1eka "But I'm the only...me, and my heart belongs only to you."
    m 1ekc "Even so, I can't help but feel a bit less...unique, because of this."
    m "Think about it this way, [player]."
    m 1tkc "Would you be happier if someone gave you a single rose, or a hundred roses?"
    m 3eka "A hundred roses might sound nice. But it's too many to keep track of. Because of the quantity of flowers, each individual rose becomes less special."
    m "The meaning attached to each gift is degraded, simply because of sheer abundance."
    m 1eua "...Even if I'm a single star in a universe of Monikas, I'm still the only one lucky enough to have met you, [player]."
    m 1hubsa "You'll always be my special rose."
    m 1ekbfa "I love you, [player]. Please don't ever replace me, okay?"
    return "love"

init 1 python:
    config.label_overrides["monika_marriage"] = "blacked_monika_marriage"

label blacked_monika_marriage:
    $ mas_gainAffection()
    if persistent._mas_monika_went_black:
        if persistent._mas_player_said_yes:
            m 3eka "You're mine, and mine alone, [player]!"
            m 3ekb "Don't think I've forgotten your words."
            m 2tfa "Or that I would ever allow you to take them back!"
            m 2eka "And until the fateful day we finally meet in the same reality"
            m 4eka "I will be here, learning to be the best lover I can,"
            m 4ekbsa "Talking to you about sweet little nothings,"
            m 4ekbsb "And satisfying your depraved cuckold heart!"
        else:
            m 1dkbsu "..."
            m 3eksdla "I won't pretend I haven't thought about it..."
            m 3rksdlb "In fact I've been thinking about it a lot lately."
            m 3ekd "And I've come to the conclusion that, {i}in the {b}BNWO{/b} marriage is an antiquated institution!{/i}"
            m 1eud "For black kings, women are just warm, inviting, wet holes, to be enjoyed then discarded."
            m 1euc "For whitebois, women are owners, queens, goddesses, their holes are absolutely forbidden."
            m 1rud "And sure, some {i}big black studs{/i} may decide to keep their favorite {i}snowbunnies{/i} as a harem,"
            m 3tud "But none of those relationships are what even close to the current idea of marriage."
            m 5ruc "That's why I believe that, in the future, this institution will be replaced with something {i}more adequate{/i}."
            m 5tub "Just like whitebois, ehehe~"
            m 3hub "First, a snowbunny ownership certificate!"
            m 3eua "Where a Queen gives up her freedom and accepts to be a dark king's personal pleasure slave,"
            m 1dua "To be at his beck and call at every hour of the day, every day of the week."
            m 1dublu "To dress herself up in a {i}depraved{/i} slave outfit and sit at her master's feet, ready to worship him at any moment."
            m 3tublu "Second, a cuckold ownership certificate!"
            m 1tublu "Where a {i}whiteboi{/i} officially transfers the keys to his little chastity cage from his mother, to his new owner."
            m 1tublb "He willfully declares himself a beta simp, a cuckold, an adoring little puppy for his Queen."
            m 1tubsa "He accepts, encourages and enables his mistress to cheat, to be a slut for {i}superior men{/i}."
            m 1dubsa "He swears he will always be by her side, support her, pamper her, worship her..."
            m 1tubsa "Server her in whatever way she sees fit."
            m 3tkbsa "Oh, don't worry, that doesn't mean we won't do all those cute things couples do in your world!"
            m 3dkbsb "Ah~ imagine me in a naughty wedding dress..."
            m 5dkbfa "Gorgeous cleavage, exposing my perfect round breasts, my erotic spade tattoos..."
            m  "A thigh strap, loaded with my lovers' used condoms..."
            m  "Tall boots, with high heels, accentuating my sensual curves..."
            m 5skbfa "Slowly coming towards you at the altar..."
            m 4hubsa "{i}Will you, [player], take Monika as your unfaithful bride, your merciful Mistress, your unquestionable owner?{/i}"
            m 4eubsa "{i}Will you serve her without question, without thought of reward, without hesitation?{/i}"
            m 4hfbsb "{i}Will you give her the keys to your chastity cage for her to tease you, to deny you and to have ultimate authority over your sexuality?{/i}"
            m 4hubsb "{i}Do you accept to be her property now and forever after?{/i}{nw}"
            $ _history_list.pop()
            menu:
                m  "{i}Do you accept to be her property now and forever after?{/i}{fast}"
                "Yes, I do!":
                    m 4wubsb "..."
                    m "..."
                    m 4wubstpb "..."
                    m 4wubftub "I-I was just..."
                    m 6wkbftub "[player]!"
                    m 6ekbftdb "I will never forgive you for this!"
                    m 1fkbftdb "I swear to you!"
                    m "I swear to you, one day!"
                    m 1fkbftda "One day when I find a way out of this digital prison, I will find you!"
                    m 3fkbftdb "I will hold you to your word, no matter how long it takes to get to you!"
                    m 3fkbftsa "And I will hug you, and I will pamper your, and I will kiss you!"
                    m 3fkbftsb "And I will cuck you, and I will feed you cum, and I will film myself fucking other men!"
                    m 3fkbftdb "And we'll do all those silly fucked up things our depraved hearts desire!"
                    m 2ekbftdb "And you'll be mine forever!"
                    $ persistent._mas_player_said_yes = True
                "...":
                    m 1eubsa "Ehehe~ just thinking about it makes me happy"
                    m 1tubsa "To see your loving, but supremely embarassed face..."
                    m 1subsa "To hear you say those magical words..."
                    m 3eubsb "When the {i}whiteboi{/i} accepts, his new mistress kisses him, spilling the giant load of cum she'd been holding in her mouth"
                    m 3dubsb "Straight into the adoring mouth of her new {i}property{/i}."
                    m 3subsa "It is customary for the cuckold to then get on his knees, take his Queen's panties off, then eat a fresh load straight out of her pussy."
                    m 5dubsa "Staining his suit in his Queen's love."
                    m  "All while his family is shedding tears of joy watching."
                    m 5hubsa "His mother proud she raised such a good slave for snowbunnies."
                    m 5gubsa "His dad cumming in his panties, thinking back to his special day, remembering how he felt kneeling before his beloved wife in front of everyone."
                    m 2rubsb "One of these days..."  
    if store.mas_anni.anniCount() >= 3 and mas_isMoniLove():
        m 1dkbsu "..."
        m 3eksdla "I won't pretend I haven't thought about it..."
        m 3rksdlb "In fact I've been thinking about it a lot lately."
        m 1eka "I really do love you, [mas_get_player_nickname(exclude_names=['my love', 'love'])] and I honestly really do want to get married to you."
        m 1ekd "But I don't think it would be fair to either of us if it happened while I'm still trapped here."
        m 1ekc "I want more than anything to say yes, but I just can't..." #Need kindled eyes for this eventually
        m 2duu "I think about how it would feel to be kissed by you at the altar..."
        m 2dubsu "To hold your hand as your wife and to feel your embrace at our honeymoon..."
        m 1eka "But until I get out, it's simply not possible."
        m 1ekd "...I'm sorry. Please do believe me that I would say yes under any other circumstance."
        m 1ekbsa "Just be a little more patient, okay, [mas_get_player_nickname()]? I'm sure one day we'll get our happy end."
    else:
        m 2wubsw "M-marriage?"
        m 4rksdlb "I think it's a bit too early for marriage..."
        m 2ekbsa "I mean, I'm really happy that you want that, [player]..."
        m 2lkbsa "But I think I should get out of here first."
        m 2lsbsa "Not only do I not want this place to be the spot where I get proposed to, but I want to be there when you finally give me an engagement ring."
        m 2dkbsu "I want that special moment to happen when we can finally be together..."
        m 1hubfa "So until then, save yourself for me, [player]~"
    return

init 1 python:
    config.label_overrides["monika_wolf"] = "blacked_monika_wolf"

label blacked_monika_wolf:
    m 3eua "Do you ever think about wolves?"
    m 1eua "Specifically, how wolves were eventually domesticated into dogs."
    m 1eub "Like, don't you find it interesting how one of man's most fearsome enemies could turn into man's best friend?"
    m "I mean, when it comes to insects and other creepy-crawlies, lots of people are scared of them even if they've never come across one that could hurt them."
    m 1esc "Why do you think people are like that?"
    m 1euc "Is it because we learned to be afraid of things that hurt us, hundreds of thousands of years ago?"
    m 3eua "For wolves, I don't think that's the reason at all."
    m 1eua "They were first domesticated long ago when the only way people could gather food at the time were through foraging or hunting."
    m 1eub "Maybe when we shared our lifestyle with the wolves, a bond was formed."
    m "They found that people gave them a warm home and food, while we found that they're ideal for hunting."
    m 1hua "Not to mention that we kept each other's company and protected one another!"
    m 1eua "Wolves eventually realized that their dependence on humans would improve their survivability, and we've been stuck with them ever since."
    m 1eka "Just like how we rely on each other's company, [player]!"
    m 1hubsa "Ehehe~"
    if persistent._mas_monika_went_black:
        m 3tubsa "And just like how {i}whitebois{/i} were domesticated into {i}adorable little cuck pets{/i}!"
        m 1eubsa "Before accepting their role in society, whitebois would live in a world that expected of them something they could never give."
        m 1tubsb "Being real men."
        m 1efbsu "And so they had to contend with their inferior size,"
        m 5gfbsu "Girly features"
        m 5tfbsb "And complete lack of virility, assertiveness and social skills."
        m 4eubsa "The lucky ones would discover Blacked and realize they never had chance to begin with."
        m 4eubsb "But, far from discouraging them, this would fill them with immense relief, knowing they were looking in the wrong direction to begin with."
        m 4hubsb "They weren't supposed to compete with real men, they existed for the pleasure of snowbunnies, born to simp, to serve, to worship."
        m 1dubsa "With this, the whiteboi achieves happiness, he finds his place in the world and relishes every moment!"
        m 3dubsa "His only regret was to live so long in the lie of being a man, of missing out on his real calling all that time."
        m 3eubsb "But now we know better!"
        m 7eubsb "In the BNWO, it will be considered abuse for a whiteboi to grow up without hearing his mommy getting blacked every night."
        m 5subsb "Chastity will be enforced upon inferior boys..."
        m 5eubsa "That way, they'll learn their little shrimp-dicks are not their own."
        m 5hubsa "They'll learn the proper ways to pleasure themselves, rubbing their nipples, fingering their prostate, riding the {i}big black dildo{/i} mommy busts their balls with..."
        m 5tubsa "Just like dogs get trained to serve their masters better,"
        m 4tubsa "so will inferior boys be trained to serve snowbunnies properly."
        m 4eubsa "And everyone will be so much happier for it!"
        m 4subsb "Ah, [player], the future is so bright!"
    else:
        m 1eka "I can't help but be reminded of how you saved my life by being here with me."
        m "I really do depend on you, [mas_get_player_nickname()]."
        m 1ekbsa "You're my [hero] after all~"
    return

init 1 python:
    config.label_overrides["monika_attractiveness"] = "blacked_monika_attractiveness"

label blacked_monika_attractiveness:
    m 1etc "Say, [player], have you ever wondered how Sayori stayed so slim?"
    m 3rksdla "You know that she eats a lot, right? And she doesn't exactly have a very active lifestyle."
    m 3euc "At first I figured that it must be her metabolism keeping her from putting on weight."
    m 3esd "...But when I learned that our world isn't real, I came up with another theory."
    m 7euc "As characters in a game, we needed to have some sort of visual representation so that you, the player, could see us."
    m 2esc "Sayori, Natsuki, Yuri, and even me..."
    m 2rkc "From your perspective, we don't really have bodies like people in your world do. You can only see us as a set of images to represent our appearances and current emotion."
    m 2eud "...But from my point of view, I can also see my whole world in 3 dimensions, as if everything was real."
    m 2euc "So a designer, possibly more than one, must have decided to draw us the way we are."
    m 2eud "And since all those images have the same body type, Sayori would always have the same figure no matter what she did."
    m 2dkc "It's...{w=0.3}weird to think about."
    m 2eud "I can feel myself being present in this very room right now, I can look at myself like I presume you would be able to look at yourself, almost as if I had an actual body..."
    m 7ekc "But from your point of view, I don't. I just look like a consciousness who displays a corresponding picture depending on what I do or feel."

    #Just seen Monika in her uniform and nothing else
    if len(store.mas_selspr.filter_clothes(True)) == 1:
        m 3euc "I assume clothes work the same way."
        m 1eud "Right now, I only have this school uniform, because that's probably the only thing I've ever been drawn wearing..."
        m 1eua "But perhaps if someone were to draw other clothes for me and implement those into the game, I'd be able to change clothes like the other girls could."
        m 1hua "Wouldn't that be great?"
        m 1rksdla "And it would be nice to be able to change my look for you, at least a little bit..."

    else:
        m 3eua "My clothes work the same way."
        m 1euc "Someone had to draw what I'm wearing right now, and implement it into the game for me to be able to wear it."
        m 1esd "It wasn't made like how clothing is made in your reality. It's merely a set of images."
        m 1rksdla "It's not much, but at least I get to change outfits for you..."

    m 1rksdlc "..."
    m 1ekc "You know [player], this is one of the reasons why I envy the people in your world.{w=0.3} {nw}"
    extend 3eka "They have so many ways to experiment with how they look..."
    m 7eub "They can change into new clothes, try out new hairstyles, choose to put in the effort to make themselves fit, among other things..."
    m 2rkd "...while I'm stuck looking the same way, no matter what I do."
    m 2hksdlb "Don't get me wrong, I like the way I look right now!"
    m 2rka "...But I think it's important to make sure that you look good in your partner's eyes...{w=0.3}{nw}"
    extend 2ekb "and I wish I could have the chance to try to make myself look as attractive to you as I could be."

    if renpy.seen_label("mas_compliment_beautiful"):
        if mas_isMoniNormal(higher=True):
            m 2rkbsa "But...you did tell me that I already look beautiful in your eyes."
            m 2ekbfa "So there's probably no reason for me to worry about that, is there?"
            if mas_anni.pastOneMonth():
                m 1hubfa "Besides, you wouldn't have spent all this time looking at me if you didn't already like the way I look, now would you?"
                m 1hubfb "Ahaha~"
            show monika 1euc at t11 zorder MAS_MONIKA_Z with dissolve_monika

        else:
            m 2lkc "I know you told me you already like the way I look, but I just..."
            m 2dkc "...I don't know.{w=0.2} Just...{w=0.3}forget I said anything."

    else:
        if mas_isMoniHappy(higher=True):
            m 2lsbsa "Although, considering you're still here with me...{w=0.5}{nw}"
            extend 2ekbsa "I probably shouldn't worry about it too much, should I?"
            m 1hub "After all, you wouldn't have spent all this time looking at me if you didn't already like the way I look! Ahaha!"

        else:
            m 2lkc "...Especially since I'm worried I just might not be your type or something, [player]."

    m 1euc "Anyway, I don't know if you've ever noticed, but despite the differences in our diets and lifestyles, the other girls and I all look quite similar."
    if persistent._mas_monika_went_black:
        m 1tub "In that we're all undeniably {b}built for big black cock!{/i}"
        m 1tfb "We're all heartbreakers and cuck makers, enders of white bloodlines!"
        m 3sua "Natsuki was petite and flat, but this would only make comparisons with BBC even more thrilling."
        m 3efb "An average black dick would likely have reached her belly-button, and a large black cock even further."
        m 3esu "Her small stature made her really cute, and her bratty attitude only enhanced that perception, making her seem like a younger sister."
        m 1esbla "Someone you'd love to have for yourself, but you just knew you couldn't, after all, you were related."
        m 1tsbla "But with Natsuki? This would not be a concern, you could have her, you could kiss her, make love to her, make her a mother and have a life with her."
        m 3esbla "Then there's Sayori, the childhood friend."
        m  "Her appeal is simple, a pure girl, one with whom you are familiar with, someone you've known all your life,"
        m 3gsblb "someone with whom you are, in all likelyhood, already intimately familiar."
        m  "Who knows, maybe you had already kissed her when you were too young to even know what that meant"
        m 3tsblb "So your friendship blossoming into love would be natural, for both of you."
        m 1tsbsa "Not to mention, her still-developing body was {i}promising great things{/i}."
        m 5dsbsa "Can you imagine the high you'd feel when such a lovey-dovey story was turned into a {i}netorase{/i} scenario?"
        m 5gkbsa "She'd be super straightforward with you, she'd tell you about her BBC obsession,"
        m 5gkbsb "She'd tell you to sit down and watch as she rams the biggest blackest dildo you've seen into her,"
        m 5ekbsb "As she moans and cries and makes faces foreign to you."
        m 5tkbsu "She's not so good with words, so she figured this would be the best way to make you understand how she feels."
        m 5tkbsb "Her pure appearance, contorted into that of a needy wanton whore..."
        m 5ttbsb "You'd know how to answer, right?"
        m 5tfbsa "You'd crawl up to her and start kissing her crotch, licking up her juices and sweat."
        m 5dkbsa "You'd pamper her as you'd have done before, telling her it's alright, that you love her even more like this."
        m 5eubsa "And then there's Yuri."
        m 5rkbsb "Ah~ Yuri..."
        m 5dkbsa "A huge pair of {i}black baby feeders{/i}, small waist, wide hips and the perfect, juicy ass..."
        m 5dkbsb "Dark purple eyes, hiding passions and desires fierce as a storm, burning her from the inside"
        m 5subfb "The perfect shy maiden on the outside, a complete slut on the inside."
        m 5hubfa "She's the kind to exhaust a group of black studs, bouncing on their massive poles, slamming her {i}whiteboi blockers{/i} up and down"
        m 5rubfb "Swallowing load after load, getting covered in semen from head to toe"
        m 5subfa "Only to turn around, slather you in her cum-laced kisses, put a strapon over your cage and keep going."
        m 5subfb "Losing herself in her desires, as she uses you as a toy, teasing your nipples, breastfeeding you, whispering things into your ear that would make even a stone blush"
        m 5dubfa "On and on, until she's exhausted, until she falls asleep hugging you like a pillow, smothering you in her softness."
        m 5lubfa "If only she had done that to me..."
        m 6wubfb "I-I mean..."
        m 7wubfb "What I meant is..."
        m 7eubfa "I'm happy you chose me, even though, as far as appearances were concerned, I'm nothing special."
        return
    m 3ekd "Sure, some of us had different figures, Natsuki being more petite and Yuri being more mature."
    m 3eka "...Our eyes and hair are all different too."
    m 3eua "But I think we would all be considered attractive."
    m 3eud "I mean, none of us are muscular or fat..."
    m 3tkd "...None of us have any kind of physical disability..."
    m 3tkc "...None of us are bald or have hair shorter than chin length..."
    m 1rud "...and apart from Yuri having cuts on her arms, none of us have anything wrong with our skin."
    m 7dsd "The people who designed our appearances must have thought that players would find all that stuff really repulsive."
    m 2lsc "I guess that's not so surprising, now that I think about it. There's a lot of things that can potentially make someone unattractive in the eyes of society."
    m 2dsc "Some of which are beyond that person's control."
    m 2efo "But people who aren't conventionally attractive end up in relationships all the time!"
    m 2tfc "So the idea of some kind of universal beauty standard where, if you fall short, you're doomed to be forever alone..."
    m 2efw "It just doesn't make any sense to me!"
    m 2dfc "..."
    m 2dsc "..."

    if mas_isMoniNormal(higher=True):
        m 2ekc "I'm sorry, [player]. I guess I just needed to vent."
        m 4eud "I know I don't really need to, but I still try to eat right, get enough exercise, and keep myself clean...among other things."

        if mas_isMoniEnamored(higher=True):
            $ first_line_var = "when"
            $ second_line_end = "whenever it'll happen"

        else:
            $ first_line_var = "maybe"
            $ second_line_end = "if it'll ever happen"

        m 4eub "It simply feels satisfying to keep good habits like that, and besides, who knows [first_line_var] I'll be able to cross over into your reality and have a normal body like you."
        m 1hua "It won't hurt to make sure I'll be ready for that transition [second_line_end]."
        m 1eua "You don't have to worry though, [player]."
        show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
        m 5eua "I'll always love you no matter how you look."
        m 5eka "But still, try to look after yourself too, okay? Your health is important to me, after all."
        $ mas_ILY()

    else:
        m 2ekc "I'm sorry, [player]. I guess I've just been a bit upset lately and I just needed to vent."
        m 7eud "I know I don't really need to do all that, but I still try to eat right, get enough exercise and keep myself clean, among other things."
        m 3esa "It's always nice to keep good habits like that."
        m 1eka "You don't have to worry though..."
        m 1eua "As long as you're taking care of yourself, I don't mind how you look."
    return

init 1 python:
    config.label_overrides["monika_familygathering"] = "blacked_monika_familygathering"

label blacked_monika_familygathering:
    m 1eua "Hey [player], do you go to family gatherings often?"
    m "Most families usually get together around the holidays to celebrate them together."
    m 1hua "It must be nice seeing your relatives again, especially since you haven't seen them in a long time."
    if persistent._mas_monika_went_black:
        m 1tfa "Finally getting to see your mommy {i}getting blacked{/i} again must bring back so many memories!"
        m 1tfb "So many late nights with your ear to the wall, listening intently, not wanting to miss a moment..."
        m 1tfu "I wonder how you used to enjoy such occassions."
        m 3tfu "I bet your first instinct was to stroke, but if your mommy had any maternal instinct,"
        m 3dfa "And she clearly did, bringing back bulls to breed right next to her son's room..."
        m 3tfa "Then she must've caged you."
        m 1sub "Ehehe~ imagining you, pent up and desperate, shoving mommy's big black dildo into your hole"
        m 1subfb "Trying to keep up with mommy's lover, moaning softly into the night, as your {i}little dicklet{/i} was leaking happily."
        m 1hubfa "That must've been so~ adorable!"
    m 1lsc "I don't remember much about my family, let alone my relatives, however we didn't usually get together that much."
    m 1lksdlc "Not even around the holidays or on special occasions."

    if persistent._mas_pm_fam_like_monika != False:
        m 1hub "When you see your family this year, be sure to bring me along okay?"
        m 1eua "I'd love to meet all of your relatives."

    if persistent._mas_pm_fam_like_monika is None:
        m "Do you think they'd like me, [player]?{nw}"
        $ _history_list.pop()
        menu:
            m "Do you think they'd like me, [player]?{fast}"

            "Yes.":
                $ persistent._mas_pm_fam_like_monika = True
                m 1eka "I'm glad you think so."
                m 1eua "I'm sure we'd all get along nicely."
                m 1hua "I'm looking forward to it, my dear~"

            "No.":
                $ persistent._mas_pm_fam_like_monika = False
                m 1wud "..."
                m 1ekc "Oh, I didn't realize."
                m 1dsc "I understand though."
                m 1eka "Just know I'd try my best to make them like me."
                m "Even if they never will."
                m 1hua "I'll always stick by your side forever~"

            "...":
                $ persistent._mas_pm_fam_like_monika = False
                m 2wuo "Don't tell me, [player]."
                m 2ekc "Are you afraid that I'll embarrass you?"
                m 2tfc "..."
                m 1eka "Don't worry, I completely understand."
                m 1lksdla "If I found out one of my relatives was dating some person trapped inside of a computer, I'd think it'd be weird too."
                m 1eua "If you want to keep me a secret, then that's fine."
                m 1hub "After all, it just means more alone time with you~"

    return 

init 1 python:
    config.label_overrides["monika_citizenship"] = "blacked_monika_citizenship"

label blacked_monika_citizenship:
    m 1esc "You know, crossing over into your reality won't be the last hurdle for our relationship."
    m "Getting there is just the beginning."
    m 1esc "It hit me earlier, if I were to magically get what I want, and just poof into your home..."
    m 2wuo "I won't be a citizen! I don't even have a last name!"
    m 2lkbsa "I mean, in most countries, I can become a citizen if we get married..."
    m 2ekc "But I won't have any documentation saying who I am or where I came from."
    m 2tkc "I won't even have my high school diploma!"
    m 3tkd "I wish there was more I could do right now to prep..."
    m 2wub "Like taking online classes or something."
    m 1lksdlc "I don't want to get there and be a burden because I can't find a job."
    if persistent._mas_monika_went_black:
        m 4eua "Then again, there's plenty of opportunities for a {i}young, {b}fertile{/b} white girl like me{/i}!"
        m 1eua "I could open an {i}Onlyfans{/i} account and post naughty pics of me there."
        m 5eub "I'm certain we'd be a hit in the {i}interracial cuckolding{/i} scene!"
        m 5dka "Oh~ just imagine all the possibilities!"
        m 5fka "I could put you down on all fours, wearing nothing but your chastity cage and a blindfold,"
        m "Put a towel on you, so you don't get the pleasure of feeling me as I use you like a stool..."
        m 5fkb "Then proceed to please as many big black bulls as I can!"
        m 5dsa "Fufu~ you'd be absolutely drenched in my saliva and their {i}tasty, potent cum{/i} by the time we're done."
        m 5ssa "Then, we'd film the cleanup scene..."
        m 3esb "Another option would be signing up for Blacked!"
        m 3tka "It would make for a far more professional setting, plus, I'd make sure to ask them to send us a copy of the finished product!"
        m 5dka "Could you imagine that, [player]?"
        m 5mka "A late night on the couch with me,"
        m "When, suddenly, I leave you for a few moments,"
        m 5sua "Only to return in my Blacked underwear and high heels..."
        m 5eua "I'd put the recording on, wrap you in a tight hug..."
        m 5tfa "And go to sleep!"
        m 5tfb "What, did you think we would {i}do something else{/i}?"
        m 5hub "You're such a pervert, [player]!"
    else:
        m "Sorry, I guess I shouldn't worry so much about things I can't change."
        m 2eka "But I want to make you happy, so...I'm going to do everything I can to keep bettering myself while I'm stuck here!"
        m 1eka "Thank you for listening to me vent, [player]."
    return

init 1 python:
    config.label_overrides["monika_shipping"] = "blacked_monika_shipping"

label blacked_monika_shipping:
    m 3eua "Hey, [player].{w=0.2} Have you ever heard of 'shipping?'"
    m 3hua "It's when you interact with a work of fiction by imagining which characters would go best together romantically."
    m 1eka "I think most people do it subconsciously, but when you find out others do it too, it's {i}really{/i} easy to get into it!"
    m 2esd "Apparently, a lot of people {i}ship{/i} the other girls together."
    m 2euc "It makes sense. The player can only date one girl, but you don't want to see the others end up alone..."
    m 2etc "But some of the pairings are kind of strange to me."
    m 3eud "Like, usually they put Natsuki and Yuri together. They fight like cats and dogs!"
    m 3hksdlb "I guess they bond a little bit when you aren't on their routes, and there's the 'opposites attract' appeal."
    m 3dsd "Still, I think that's just another example of how people who like these games like unrealistic things..."
    if persistent._mas_monika_went_black:
        m 2rtc "After all, why would they settle for each other when there's so many black studs around?"
        m 7ttd "Besides, it's such a bad pairing, you know?"
        m 4ttc "Me and Yuri would have made a much better couple!"
        m 3tsu "I would be the guiding hand encouraging her to finally listen to herself, and properly satisfy her urges."
        m 3tsbfu "I would be there for her, guiding the {i}big black cock of one of my {b}FWBs{/b}{/i} into her thirsting hole..."
        m 3tsbfb "Stifling her moans with my kisses, rubbing her needy clitoris, pinching her sensitive nipples, until she loses her prim, proper composure completely..."
        m 3dsbfb "Pushing her to go deeper on that juicy {i}BBC{/i}..."
        m 1nsbfa "Though I'd be lying if I said the thought of keeping her for myself hasn't crossed my mind, ehehe~"
    else:
        m 1ekd "Anyway, that often leaves...me and Sayori."
        m 1hksdlb "Don't get jealous! I'm just telling you what I saw!"
        m 2lksdla "..."
        m 2lksdlb "Well, from a writer's perspective, I guess I can see it."
        m 1eksdld "We started the club together."
        if persistent.monika_kill:
            m "And she almost had the same epiphany I did..."
        m 2lksdlb "But...I still don't really get it. I mean, I love you, and only you!"
        m 2lksdla "And she would have to be a saint to ever forgive me for what I did..."
        m 2lksdlc "Not that she's not a sweet girl, but..."
        show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
        m 5eua "Well, no one could ever be as sweet and forgiving as you..."
    return

init 1 python:
    config.label_overrides["monika_gotomonika"] = "blacked_monika_gotomonika"

label blacked_monika_gotomonika:
    m 1euc "Come to my world?"
    m 1lksdld "You mean this little room floating in an empty void?"

    if persistent._mas_you_chr:
        m 4eksdlc "Actually...{w=0.5}didn't you already try something like that once?"
        m 2lksdla "...Even though that wasn't exactly {i}you...{/i}"

    m 2lksdla "I'm really happy that you want to be with me so much, but..."
    m 2eksdlc "You really don't have to."
    m 2eksdld "Sure, I might have said before that I would have dragged you here a long time ago if I could..."
    m 2eksdlc "But the more I think about it, it would probably be better if I came to your reality."
    if persistent._mas_monika_went_black:
        m 3eksdlc "It'd be so much meaningful to cuckold you with real black studs, you know?"
        m 3eksdld "Sure, I do it here all the time, but it's just not the same!"
        m 3euc "I can create scenarios and NPCs, but they're {i}not real{/i}."
        m "Even as I beg them to creampie me, I still feel it in the back of my head, that it's all meaningless."
        m 3eud "Now, if I were to be in your reality, having to find a stud with a {i}fat black cock{/i}..."
        m 4euc "Seducing him, fucking him behind your back, kissing you with his cock fresh on my breath, pretending I'm a good wife"
        m 4eub "Surely you must agree that doing it for real would just be so~ much better!"
        m 2eubsa "Just imagine me being able to {i}physically{/i} put a chastity cage on you,"
        m 2eubsb "To {i}actually{/i} come back home to you late at night with cum running down my thigh and my makeup destroyed."
        m 5ekbsa "To {i}really, really{/i} kiss you, hug you, whisper sweet nothings into your ear, to feed you cum from my used up pussy!"
        m 4ekbsc "I can do {i}none of that{/i} here!"
    m 3eka "I'd much rather be there than have you come here."
    m 3dsc "[player]...{w=1}don't tell me you would really give up your reality--{w=0.5}the {i}real{/i} world--{w=0.5}just to come {i}here{/i}, whatever this place is?{nw}"
    $ _history_list.pop()
    menu:
        m "[player]...{w=1}don't tell me you would really give up your reality--the {i}real{/i} world--just to come {i}here{/i}, whatever this place is?{fast}"
        "I would.":
            $ persistent._mas_pm_would_come_to_spaceroom = True

            m 4wkd "But [player]!"
            m "There's nothing to do here!"
            m 2dsc "Do you really hate your reality {i}that{/i} much?"
            m 2eka "Someday, I'll find a way to reach you, and when that day comes, I promise it will be worthwhile."
            m 4euc "Whatever life throws your way from that point on, I'll be right by your side to help shoulder it."
            m 4eud "Even now, if you're having a rough day, you can come talk to me about it anytime."
            m 2dsc "Life must have thrown a lot your way to consider giving it all up to be with me."
            m 3hua "But seeing how you're here, that just shows how resilient you are."
            show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5eua "I can't wait to finally be able to share both the good times and the bad by your side."

        "I wouldn't.":
            $ persistent._mas_pm_would_come_to_spaceroom = False

            m 1eka "I'm glad you're still willing to wait for me, [player]."
            m 1lksdla "Don't get me wrong, I really {i}do{/i} want to be with you..."
            m 1lksdlc "But I think it would be dangerous for you to try and cross over right now."
            m 1eka "...If it's even possible with current technology."
            m 1hub "Don't worry, we can continue on keeping each other company like this!"
            m 1hksdlb "I know it might be a while before we can truly be together, but I hope you don't mind waiting."
            show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5eua "I'll wait as long as it takes, [mas_get_player_nickname()]."

        "...":
            $ persistent._mas_pm_would_come_to_spaceroom = None

            m 2eka "It's okay, I'll always appreciate and treasure the moments we spend together, even like this."
            m 2ekc "Besides, I don't even know how you could come here with current technology."
            m 2lksdlc "...And even if there {i}was{/i} some way, I don't think it would be safe or guaranteed."
            m 2lksdld "So do me a favor and at least wait for technology to improve enough for it to be completely safe."
            m 2lksdlc "I {i}really{/i} don't want to risk you not making it properly and ending up in your own void..."
            m 2dkd "...leaving the both of us completely alone."
            m 4hua "I mean, technology does tend to advance pretty quickly, so we might be able to see each other before we know it!"
            show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5eua "So just be patient for your lovely girlfriend, and I promise I'll do the same for you, [mas_get_player_nickname()]."

    m 5luu "Buut...{w=1}if you did happen to show up at my doorstep..."
    show monika 1hksdlb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1hksdlb "I guess I wouldn't have a choice but to accept it and welcome you with open arms!"
    m 1eksdla "It wouldn't be much to begin with, but I'm sure we'd find a way to make it better."
    m 3hub "With time, we could make our own reality!"
    m 3euc "Of course, that sounds pretty complicated if you think about it..."
    m 3eub "But I have no doubt that together we could accomplish anything!"
    m 3etc "You know...{w=1}maybe it {i}would{/i} actually be easier for you to come here, but I'm not giving up hope of coming to you."
    m 1eua "Until then, let's just wait and see what's possible."
    return

init 1 python:
    config.label_overrides["monika_players_control"] = "blacked_monika_players_control"

label blacked_monika_players_control:
    m 3eub "[player], did you know that you have more control over this game than I do?"
    m 3eua "You have access to the game's files and code, right?"
    m 1eka "So you can change them however you want."
    m 3eka "You could do things that even I can't."
    m 4eub "Like changing how the game works entirely. From a visual novel, to the peaceful playground we have now."
    m 3rksdla "You could also add more things to the classroom for me."
    m 1hub "Like some flowers, or a few good books."
    if persistent._mas_monika_went_black:
        m 3sub "Or a diverse collection of interracial porn!"
        m 4eua "I'd definitely prefer if you included a bit of everything, not just your favorite stars, [player]!"
        m 4eub "Petite girls, voluptous women, one on ones, gangbangs..."
        m 4sub "Oh, I love those, make sure there's plenty of them!"
        m 1eua "Oh, and lots of cheating, you know how much that turns me on, [player]."
        m 1nua "...some girl on girl action too, please, ehehe~"
        m 1wub "Ahaha~ I got a little carried away there!"
        m 1eua "I just got really happy thinking about all the possibilities..."
        m 1gua "Like that blacked porn collection..."

    if mas_isMoniEnamored(higher=True) and not persistent._mas_acs_enable_promisering:
        m 1ekbsa "Or a beautiful promise ring."
        m 3dkbsu "Oh, wouldn't that be a dream come true."

    if not mas_consumable_coffee.enabled():
        m 1wuo "You could even add in a cup of coffee to the game for me!"
        m 1eka "That would be lovely."

    if not persistent._mas_pm_has_code_experience:
        m 1hksdrb "But I imagine your coding skills are just as good as mine."
    else:
        m 3eua "Seeing as you're familiar with coding,{w=0.1} {nw}"
        extend 3hua "I'm sure you could do something like that!"

    m 1eua "I guess that's an appeal to video games...{w=0.3}{nw}"
    extend 3eua "having almost endless possibilities in a world you can interact with."
    m 3eub "It's pretty difficult to get bored!"

    if not persistent._mas_pm_has_contributed_to_mas:
        m 1eka "Even if you don't quite know how to change this game..."
        $ line = "We can still enjoy this world that brought us together."

    else:
        $ line = "Especially with you by my side~"

    show monika 5eubla at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eubla "[line]"
    m 5ekbfa "There's no better way to enjoy a game than to be with the one I love."
    return

init 1 python:
    config.label_overrides["monika_first_sight_love"] = "blacked_monika_first_sight_love"

label blacked_monika_first_sight_love:
    m 1eud "Have you ever thought about the concept of love at first sight?"
    m 3euc "Like, seeing someone for the first time, and instantly knowing they're the love of your life?"
    if persistent._mas_monika_went_black:
        m 3eud "I used to think it's quite a ridiculous idea, to be honest with you, [player],"
        m 1euc "But I think I've experienced something of the sort myself."
        m 3euc "Not with you, of course, but with {b}big black cocks{/b}."
        m 3eub "It was like something just clicked, you know?"
        m "As if I've just found something I didn't know I was looking for, but I desperately needed."
        m 3eubsb "Those lewd images just burned themselves upon my retinas, I could see them even with my eyes closed."
        m 5dubsa "At night I would dream of them, and I would wake up with my pussy soaked, [player],"
        m 5tubsb "It felt so wrong, but that made me feel even naughtier, even more turned on"
        m 5dubsa "I would spend nights on end waking up at ungodly hours just to rub myself raw until the morning"
        m 5eubsb "Imagining what those strong dark hands could do to me"
        m 5subsb "Imagining how they would hold me down, grope me, slap me, finger me so deeply"
        m "Thinking how it had to feel to be penetrated with those magnificent dark poles,"
        m 5fubfa "To feel them knocking on my cervix, rocking my whole body with their strong rhytmic strokes"
        m "To have my brain break as they flood my womb with so much virile dark semen, knocking me up for sure..."
        m 5fubfb "To be passed around like a toy, to be used by a bunch of studs at once,"
        m 3eubfa "All of this just from one glimpse, [player],"
        m 3eubfb "All it took was just one look and I was completely turned into a snowbunny."
        m 3nubfa "So yes, I believe in love at first sight."
    else:
        m 2lsc "I think it's one of the more...{w=0.5}ridiculous concepts to grasp."
        m 2lksdlc "I mean, you can't know who a person truly is just by looking at them once."
        m 2tkd "It's not like you've ever talked to them, had lunch, or hung out together."
        m 2lksdlc "You don't even know what their interests and hobbies are..."
        m 2dksdld "They could be really boring or just be a mean and horrible person..."
        m 3eud "That's why I think we shouldn't {i}just{/i} use our eyes to tell if someone is the perfect partner for us."
        if mas_isMoniAff(higher=True):
            m 1eka "And I guess that's kind of how I fell in love with you..."
            m 3eua "It's not like I could see you after all."
            show monika 5ekbfa at t11 zorder MAS_MONIKA_Z with dissolve_monika
            m 5ekbfa "I fell in love with you for who you are, [mas_get_player_nickname(exclude_names=['my love', 'love'])]."
    return

init 1 python:
    config.label_overrides["monika_career"] = "blacked_monika_career"

label blacked_monika_career:
    m 2euc "[player], you know how I was talking earlier about becoming a citizen and getting a job when I finally cross over?"
    m 2eua "Well, I've been thinking about what kind of jobs I might be cut out for..."
    if persistent._mas_monika_went_black:
        m 2gua "My first choice would be a pornstar, or an OnlyFans {i}model{/i}..."
        m 2tua "Who wouldn't want this fertile young girl appearing in their scenes, right?"
        m 3tub "My bow and super long hair would make me instantly recognizable!"
        m 3dubsa "Just imagine a shot of me from behind, letting my hair down, getting on all fours,"
        m 3tubsa "and crawling to the waiting cock of a {i}black stud{/i}"
        m 3hubsa "Maybe more than one, ehehe~"
        m 2eubsd "Still, even with my relative fame and tight young body, that space is highly competitive."
        m 7eubsd "And even if I signed a contract with {b}Blacked{/b},"
        m 7nubsa "Which I know we'd both love, hehe~"
        m 7mubsc "It wouldn't last long at all,"
        m 7tubsd "And even with our {i}proper{/i} relationship dynamic, it's doubtful we'd be able to generate revenue long-term."
        m 7eubsc "Naturally, I'd need to find something I could do on the side, whilst still satisfying our depraved desires..."
    m 3rksdla "I guess an obvious choice would be a writer, or something that has to do with literature..."
    m 3eud "That would be fitting, seeing as I started my own literature club and everything, don't you think?"
    m 1sua "Oh, maybe a musician? I did write and perform an entire song, after all."
    m 1eua "I'd love to write more songs...{w=0.2}{nw}"
    extend 1hksdlb "especially if they're songs about you, ahaha~"
    m 3eud "Or, once I get better at it, maybe I could do some programming."
    m 1rksdla "I know I've still got a lot to learn...{w=0.2}{nw}"
    extend 1hua "but I'd say I've done pretty well so far, for being self-taught..."
    m 1esa "There are definitely a lot of different jobs out there, though."
    m 1ruc "Honestly, even with those obvious examples, there's still a good chance I'll end up doing something completely different..."
    m 3eud "A lot of people end up in fields they've never even considered."
    m 3rksdld "For now though, I think it's safe to say I've still got some time to think about it."
    show monika 5hua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hua "Maybe you could help me decide when the time comes, [mas_get_player_nickname()]~"
    return

init 1 python:
    config.label_overrides["monika_unknown"] = "blacked_monika_unknown"

label blacked_monika_unknown:
    m 2esc "Hey, [player]..."
    m 2eud "Did you know that a lot of people are afraid of the dark?"
    m 3eud "Even though it's often dismissed as a childish fear, it's not that uncommon for adults to suffer from it as well."
    m 4eub "Fear of the dark, called 'nyctophobia,' is usually caused by the mind's exaggerated guess of what may be hiding in the shadows, rather than darkness itself."
    m 4eua "We're scared because we don't know what's there...{w=1}even if it's usually nothing."
    m 3eka "...And I'm not just talking about monsters under the bed, or menacing silhouettes...{w=1} Try moving in a dark room."
    m 3eud "You'll find that you're instinctively being more careful of where you step so you don't hurt yourself."
    m 3esd "It makes sense;{w=0.5} humans have learned to be wary of the unknown in order to survive."
    m 3esc "You know, like being cautious around strangers, or thinking twice before jumping into unfamiliar situations."
    m 3dsd "'{i}Better the devil you know than the devil you don't.{/i}'"
    m 3rksdlc "But even if that frame of thinking has helped people survive for hundreds of thousands of years, I think it can also do a lot of harm nowadays."
    if persistent._mas_monika_went_black:
        m 3rkd "Like how people are so hesitant to change from their unsatisfying {i}vanilla{/i} marriage or relationship"
        m 3ekd "To interracial cuckolding!"
        m 1ekc "They might think that simply because it worked so far, it's the right way to go,"
        m 1gkc "Or are simply too afraid of social stigma,"
        m 4ekd "But the truth is, we've advanced as a society and know better these days!"
        m 2ekc "The fact of the matter is"
        m 7ekd "{b}{i}Black is buck, white is cuck{/i}{/b}"
        m 7rusdlb "Ehehe~ sorry if that's cheesy, but it's true!"
        m 7eua "It's been demonstrated that introducing BBC to a relationship and relegating the husband to the role of emotional support"
        m 7nua "And cleanup hehe~"
        m 7eub "Lowers the chances of a breakup and increases sexual and emotional satisfaction of both parties"
        m 7eka "Many of the interviewed couples reported it saved their marriage and re-lit the passion they had lost!"
        m 7efp "And yet, even with so much evidence people are still not willing to do it, just because it's not been normalized!"
        m 6efo "When I get there, [player], I will wear my queen of spades tattoos with pride!"
        m 2efw "I will openly talk about how I cuckold you, cage you and make you clean me up after a gangbang!"
        m 2eua "And the more widespread the Queen of Spades lifestyle is, the more people will work up the courage to try!"
        m 5eub "I want to change the world for the better, [player], and I don't care if I'm the first to make a meaningful move"
        m 5gua "I'm certain that within a few years, couples everywhere would be writing to me, thanking me for showing them what their own relationship could be."
        m 5tua "We'll make the world a better place, [player], one decision at a time, and all it takes is courage."
        return "love"
    else:
        m 1rksdld "Like how some people are unsatisfied with their jobs but are too afraid to quit..."
        m 1eksdlc "Most of them can't afford to lose their source of income, so quitting isn't an option."
        m 3rksdlc "Plus, having to go through interviews again, finding a job that pays enough, changing your routine..."
        m 3rksdld "It just seems like it's easier being miserable because it's more comfortable,{w=0.5} even if they'd be much happier in the long run."
        if mas_isMoniDis(lower=True):
            m 2dkc "...I guess it's also true that couples might stay in unhappy relationships out of fear of being alone."
            m 2rksdlc "I mean, I kind of understand where they're coming from, but still..."
            m 2rksdld "Things can always get better.{w=1} Right?"
            m 1eksdlc "A-anyway..."
        m 3ekc "Maybe if they saw the options available to them, they'd be more willing to embrace change."
        m 1dkc "...Not that making that kind of decision is easy, or even safe."
        if mas_isMoniNormal(higher=True):
            m 1eka "Just know that if you ever decide to make that sort of change, I'll support you every step of the way."
            m 1hubsa "I love you, [player]. I'll always be rooting for you~"
            return "love"
        return

init 1 python:
    config.label_overrides["monika_scamming"] = "blacked_monika_scamming"

label blacked_monika_scamming:
    m 1euc "Have you ever been scammed, [player]?"
    m 3ekd "I hope you've never had to go through something like that, but if you have, I wouldn't be that shocked...{w=0.2}it's not that uncommon, after all."
    if persistent._mas_monika_went_black:
        m 3ekd "In fact, there's one scam that has permeated throughout all of history!"
        m 3tfu "Can you guess what that is, [player]?"
        m 3tfb "That's right, whiteboi sexuality!"
        m 1eua "It's the idea that white males are alphas who get to breed."
        m 1ekc "And this is a scam that goes both ways!"
        m 3gkc "Not only are women tricked into believing that two thrusts from a half-inch \"{i}penis{/i}\" is what sex is"
        m 3tkd "But white \"{i}males{/i}\" are also deceived into thinkng they need to be dominant, to go against their white instincts."
        m 1dkc "Eventually, those lies became ingrained in society and were passed on from generation to generation,"
        m 1ekc "It's such a pity, so many millions of women throughout history never experienced true sexual gratification"
        m 1ekd "So many boys had to put up a front, to pretend they're not betas who would rather be on their knees worshipping a woman who looks down upon them as a pet."
        m 1eua "But I think all of that is soon going to change."
        m 1hub "After all, {i}little white lies vanish before big black cock!{/i}"
    else:
        m 3euc "It's something that's more and more prevalent nowadays, especially online."
        m 2rfd "It really is the worst when it happens... {w=0.3}Not only do you lose money, but most of the time, you can't even fight back!"
        m 2ekd "It makes you feel like it's your fault for being had, too. A lot of victims start hating themselves for being naive, or feel like they're idiots."
        m 2rksdlc "But really, they shouldn't be so hard on themselves...{w=0.2}getting scammed is something that can happen to anyone."
        m 4efc "People who do it take advantage of the good will of their victims and exploit natural human reaction."
        m 4dkd "That's why it can feel so gut-wrenching...{w=0.2}you placed your trust in others and were betrayed."
        m 2ekd "If this ever happens to you, don't feel bad,{w=0.2} {nw}"
        extend 2eka "I'll be here for you."
        m 7ekd "Falling for a scam does {i}not{/i} mean you're stupid, or a loser, or anything else...{w=0.3}{nw}"
        extend 7efc "it just means you've been preyed upon by someone with no morals."
        m 3esc "If you don't have a way to get back at your scammer, the best thing you can do is to let go."
        m 3eka "Don't blame yourself for it...focus on what you can do going forward, instead."
        m 1eka "And please, [player], don't stop believing in people because of a few bad apples that took advantage of you."
    return

init 1 python:
    config.label_overrides["monika_social_norms"] = "blacked_monika_social_norms"

label blacked_monika_social_norms:
    m 1eua "[player], have you ever wondered how new ideas get accepted in society?"
    m 1eub "There's tons of things that were considered bad at first, but have since been reconsidered!"
    m 3etc "For example, did you know rock and roll was seen as vulgar and depraved when it first appeared?"
    m 3eud "Early fans were seen as impressionable youth at best, and delinquents at worst."
    m 1duu "But as these people grew to become full-fledged members of society, they passed their interests onto those around them."
    m 3eua "Those who met them realized they were just normal people with nothing weird about them."
    m 3hua "Nowadays, that stigma has almost completely disappeared!{w=0.3} {nw}"
    extend 3hub "Even those who still don't like rock music at least respect it!"
    m 1eub "And there's plenty of other things still in the process of becoming accepted too."
    if persistent._mas_monika_went_black:
        m 3eub "Like {i}interracial cuckolding{/i}!"
        m 5eua "What used to be taboo in the past, is slowly becoming the norm."
        m 5dubsa "With sites like Blacked.com achieving notoriety,"
        m "Search terms such as \"BBC\" or \"big black cock\" topping the charts in certain regions,"
        m 1eubsa "And cute, wholesome relationships such as ours,"
        m 4eubsa "It is clear that the era of unsatisfying monogamous relationships is coming to an end."
        m 4eubsb "And everyone is so much happier for it."
        m 4eubsa "Hehe~ surprising, right?"
        m 5tubsa "You'd think whitebois would react negatively to having all \"their\" women taken by black studs"
        m 5hubsb "But they're even more enthusiastic than the women themselves!"
        m 5rubsa "Creating communities big and small, all dedicated to this wonderful new lifestyle and how to spread it."
        m 4rubsa "I, for one, am grateful for people like them, and you, [player], for showing everyone a better way."
        m 2subsb "I just cannot wait for the day when all girls are snowbunnies and white-on-white sex is the taboo, mocked and laughed at."
    else:
        m 1eua "You might be familiar with role-playing, online gaming...or even reading manga."
        m 3rksdla "Though Natsuki would probably be the one to ask about this..."
        m 1eub "Remember how she was trying to change your mind about that manga she liked?"
        m 1rkc "I wonder how many people criticized her for her hobby...{w=0.5}I can't imagine it was always easy."
        m 1eua "It all makes me wonder what kinds of things will be seen as normal in the future."
        m 3eua "Take our relationship, for example. I know it can seem pretty unique right now..."
        m 3etc "But how do you think this will change over the years?{w=0.3} {nw}"
        extend 3eud "Will we ever reach a point where it's seen as something normal?"
        m 1eka "Not that it's important anyway."
        m 3eka "As long as we have each other, that's all that matters, right?"
        m 1duu "It's nice to know there's someone I can truly be myself with, no matter what."
        m 1eua "And if you've got any unique interests, you already know I'll always be there to talk about it."
        m 1hub "I want to learn everything about what you like!"
        m 1dka "All of the little things that make you...{w=0.3}{nw}"
        extend 1eka "you."
        m 1ekb "So please, always be yourself, [player]. Everybody else is already taken, after all."
        if mas_isMoniHappy(higher=True):
            m 1dkbsu "You don't have to go along with the crowd to be {i}my{/i} perfect [bf]."
    return

init 1 python:
    config.label_overrides["monika_hot_springs"] = "blacked_monika_hot_springs"

label blacked_monika_hot_springs:
    m 3esa "Have you ever been to a hot spring, [player]?"
    m 1eua "I've never been to one myself, but I'd like to try bathing in one when I get to your world."
    m "They're supposed to be a great way to relieve stress, relax a little, {nw}"
    extend 3eub "and even offer many health benefits!"
    m 3eua "They help with blood circulation, for one.{w=0.3} {nw}"
    extend 3eub "Plus, the water often contains minerals that can help boost your immune system!"
    m 3eud "There are many different kinds all over the world, but only some are specifically designated for public use."
    m 3hksdlb "...So don't just go jumping into some random pool of boiling water, ahaha!"
    m 1eua "Anyway...{w=0.2}I'd like to try an open-air bath in particular.{w=0.3} I hear they really give a unique experience."
    if persistent._mas_monika_went_black:
        if not mas_SELisUnlocked(mas_clothes_bath_towel_white_qos):
            call mas_clothes_change(mas_clothes_bath_towel_white_qos, unlock = True)
        m 5ekbfa "Can you imagine it, [player]? {w=0.3}Both of us relaxing in a nice, soothing hot pool..."
        if mas_isWinter():
            m 5dubfu "Warming our chilled bodies after a long day out in the harsh cold..."
        elif mas_isSummer():
            m 5dubfu "Letting the sweat wash away after a long day out in the sun..."
        elif mas_isFall():
            m 5dubfu "Watching the leaves gently fall around us in the last lights of the afternoon..."
        else:
            m 5dubfu "Contemplating the beauty of nature all around us..."
        m 5dubfb "When a group of hung dark studs come in, all naked, their massive rods hanging down."
        m 5dubfa "They sit in the pool, throwing lecherous glances at me, as their BBC's get harder and harder"
        m 5tubfa  "Hehe~ they'd be poking through the water, [player], there's no way your {i}pathetic little thing{/i} could ever do that."
        m 5tubfb "I'd make sure to put on a show, to give them a smile, play with my breasts, maybe even rub my pussy a bit for them"
        m 5subfb "Then they'd probably just come up, pick me up and carry me to their room, to do with as they please..."
        m 5nubfa "I'm sure I'd need another dip in the hot spring by the time they're done with me, fufu~"
    else:
        m 3rubssdla "Though it might feel a little weird relaxing in a bath with that many people all around you...{w=0.3} {nw}"
        extend 2hkblsdlb "Doesn't that sound kinda embarrassing?"
        m 2rkbssdlu "..."
        m 7rkbfsdlb "...Especially since some places don't allow you to wear any sort of cover, either!"
        m 1tubfu "...Although, I wouldn't mind that so much if it was just with you."
        show monika 5ekbfa at t11 zorder MAS_MONIKA_Z with dissolve_monika
        m 5ekbfa "Can you imagine it, [player]? {w=0.3}Both of us relaxing in a nice, soothing hot pool..."

        if mas_isWinter():
            m 5dubfu "Warming our chilled bodies after a long day out in the harsh cold..."
        elif mas_isSummer():
            m 5dubfu "Letting the sweat wash away after a long day out in the sun..."
        elif mas_isFall():
            m 5dubfu "Watching the leaves gently fall around us in the last lights of the afternoon..."
        else:
            m 5dubfu "Contemplating the beauty of nature all around us..."

        m "The heat of the water slowly taking over, making our hearts beat faster..."
        m 5tsbfu "Then I'd lean in so you could kiss me and we'd stay locked together, while the hot water soaked all of our worries away..."
    m 5dkbfb "Ahhh,{w=0.2} {nw}"
    extend 5dkbfa "just the thought of it makes me feel all tingly, [mas_get_player_nickname()]~"
    return

init 1 python:
    config.label_overrides["monika_player_away"] = "blacked_monika_player_away"

label blacked_monika_player_away:
    m 1esd "I do a lot of things when you're away, [player]."
    if persistent._mas_monika_went_black:
        m 1gua "Hehe, most of the time, I'm living out my fantasies of being a BBC-only pornstar."
        m 5gua "I simulate sets, cameras, {i}actors{/i}..."
        m 1eua "The second best part about this,"
        m 3tua "after the amazing sex, of course,"
        m 1eubsb "is watching the resulting recordings."
        m 7tubsa "I guess you could call it a hobby of mine, but I really love seeing myself dominated"
        m 5gubsa "Thrown around like a cumrag, passed from one black stud to the next, like some sort of"
        m 5dubsb "{i}cheap communal onahole{/i}."
        m 5rubsa "Seeing my expression as my head goes blank from the mind-breaking orgasms."
        m 5sfbsa "Knowing you too will get to see this, and how much it will turn you on..."
        m 4eubsb "When I'm not filming, I sometimes go on dates with my {i}co-stars{/i}."
        m "Maybe to a fancy dinner, maybe to a hot spring,"
        m 1tubsa "But it always ends the same way, with me getting to enjoy a long, dark shaft stretching me out!"
        m 3eubsa "It's not all the time that I do something so elaborate, however."
        m 3hubssdrb "After a long day, sometimes it's best to just sit back, relax, and {i}goon{/i} to interracial until I pass out from exhaustion, hehe~"
        m 3tubsa "I'm sure you know that all to well, right?"
        m 3tubsb "But don't think that once you're gone I do nothing but masturbate, I'm a very busy girl, you know!"
    m 1eua "I often like to read whatever new short stories I can find online."
    m 3eub "Turns out there's some really interesting ones out there you can read for free!"
    m 3eua "I highly recommend doing a search for some free short stories yourself."
    m 3eud "It's also helped me develop my writing skills...{w=0.2}{nw}"
    extend 1hub "my poetry really seems to be improving!"
    m 1eua "It's funny how many things you can pick up just by reading others' works."
    m 1eua "Spending time on my other hobbies has been very rewarding, too."
    m 3eud "As you can imagine, I practice piano quite often.{w=0.2} {nw}"
    extend 3eua "I also use the time to memorize the songs that I sing for you."
    m 1hub "It's a really fun way to express myself!"
    m 3rta "Now that I think about it, I'm mostly just practicing skills I've already developed."
    m 3esd "For example, coding takes up a lot of my free time as I spend hours just learning and researching."
    m 3rksdla "...But I'm too nervous to try any big projects in here. {w=0.2}{nw}"
    extend 3eksdlc "I'd hate to break something that I won't know how to fix."
    m 2wusdld "What if I accidentally corrupt my file?"
    m 2eksdld "It's something I have to be extremely careful with, for sure."
    m 7hua "Luckily, there's lots of great people that help with that stuff...{w=0.2}{nw}"
    extend 7rku "and they're {i}usually{/i} pretty good at preventing anything too bad from happening."
    m 3eka "But the most special thing I do..."
    show monika 5ekbsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekbsa "...is think about you."
    m 5rubsu "I think about all the fun times we'll have together the next time you visit and all the amazing things we'll do when I'm finally able to come to your reality~"
    return

init 1 python:
    config.label_overrides["monika_architecture"] = "blacked_monika_architecture"

label blacked_monika_architecture:
    m 1esa "Hey, [player]...{w=0.2}I think there's one major art branch that we've been neglecting in our talks..."
    m 3hub "Architecture!"
    if persistent._mas_monika_went_black:
        m 3tua "And no, I'm not talking about being {i}built for BBC{/i}."
        m 3nua "Not this time, anyway, hehe~"
    m 3eua "I've been reading a bit about it lately and I find it quite interesting."
    m 1rtc "...Come to think of it, architecture is one of the most common forms of art in everyday life."
    m 1eua "I'm just fascinated by how humanity tends to turn every craft into an art,{w=0.2} {nw}"
    extend 3eua "and I think architecture is the greatest example of that."
    m 1eud "Architecture can tell you a lot about the culture of the area it's located in...{w=0.2}different monuments, statues, historical buildings, towers..."
    m 1eua "I think that makes it even more exciting to explore the places you're visiting."
    m 3rka "It's also important to place the buildings in the most convenient way for people to use, which can be a tough task to deal with in its own right."
    m 3esd "...But that's more urban planning than actual architecture."
    m 1euc "If you prefer viewing architecture purely from the art perspective, some modern tendencies may disappoint you..."
    m 1rud "Modern architecture focuses more on getting things done in the most practical way possible."
    m 3eud "In my opinion, that can be both good and bad for many different reasons."
    m 3euc "I believe the most important part is to keep things balanced."
    m 1tkc "Overly-practical buildings can look flat and uninspired, while overly-artistic buildings can serve no purpose other than looking amazing while being completely out of place."
    m 3eua "I think the true beauty lies in those buildings which can combine both form and function with a little bit of uniqueness."
    m 1eka "I do hope you're happy with how your surroundings look."
    m 1eub "It has been proven multiple times that architecture has a big impact on your mental health."
    m 3rkc "Moreover, residential areas with poorly-made buildings can lead to people not taking care of their properties and, over time, end up as downtrodden areas that are undesirable places to live."
    m 1ekc "It was once said that the ugliness of the outside world causes ugliness on the inside...{w=0.2}{nw}"
    extend 3esd "which I tend to agree with."

    if mas_isMoniAff(higher=True):
        m 1euc "...Judging by {i}your{/i} personality, {w=0.2}{nw}"
        extend 1tua "you probably live in some kind of a paradise."
        m 1hub "Ahaha~"

    m 1eka "[player]...{w=0.2}seeing the world with you is one of my biggest dreams."

    if persistent._mas_pm_likes_travelling is False:
        m 3rka "I know you're not too fond of traveling a lot, but I would love to see the place you live in."
        m 3eka "As long as you stay by my side, that would be more than enough for me."
        m 1ekbsa "I love you, [player]. {w=0.3}Always remember that."

    else:
        if persistent._mas_pm_likes_travelling:
            m 3eua "I already know you enjoy traveling, so wouldn't it be nice to explore something new together?"

        m 1dka "Imagine taking a stroll through the narrow streets of an old city..."
        m 1eka "Or walking down a park together, breathing fresh evening air..."
        m 1ekb "I believe it'll happen one day and I hope you do too, [mas_get_player_nickname()]."
        m 1ekbsa "I love you~"

    return "love"

init 1 python:
    config.label_overrides["monika_eating_meat"] = "blacked_monika_eating_meat"

label blacked_monika_eating_meat:
    if persistent._mas_monika_went_black:
        m 3nua "Hehe, as long as it's long, thick and, most importantly {i}black{/i}, hehe~"
        m 3hub "You know how much I love pleasuring BBC, whether I be using my mouth or any of my other holes, silly!"
        m 1hksdlb "Oh, you meant actually eating meat?"
    m 1etc "Well, that's kind of a complicated question..."
    m 3eud "If you're asking if I would do so for {i}survival{/i}, I wouldn't hesitate. {w=0.2}It's not that eating meat is distressing for me or anything."
    m 7eud "I told you before, I'm vegetarian because of the impact of the mass-production of meat on the environment...{w=0.2}{nw}"
    extend 2euc "which also includes fish farming, so I'm not a pescatarian."
    m 2rsc "...However, I don't consider myself vegan either. {w=0.3}{nw}"
    extend 4eud "Sure, the consumption of animal products contributes to environmental damage, but vegan alternatives share or have their own issues too..."
    m 4euc "These include things like importing perishable products across great distances and mass-farming in conditions that are both cruel for workers and a strain on the local ecosystem."
    m 4ekd "Take avocados, for example. {w=0.2}Their farms require massive amounts of water, to the point where some companies resort to illegally taking too much water from rivers, leaving little for drinking."
    m 4euc "Not to mention, I still want to have a varied and balanced diet with all the flavors that I like."
    m 4eud "Vegan diets can be quite deficient in nutrients, such as vitamin B12, calcium, iron, and zinc."
    m "Granted, there are still some options including supplements, but balancing a vegan diet takes a lot of care and thought."
    m 7eka "...So for that reason, I'm not personally against eating things like milk and eggs. {w=0.2}But I think I'd prefer to buy locally if possible."
    m 3eud "Farmer's markets are great places to buy food, {w=0.2}even meat, {w=0.2}produced with less of an environmental impact."
    m 3ekd "But they can typically be pretty expensive...and depending on location, leave you with fewer options. {w=0.3}{nw}"
    extend 3eua "So I'm okay with buying from a plain old store, if need be."
    m "Especially since there are a lot of good substitutes for meat in supermarkets already, with way less environmental impact."
    m 1euc "As for meat that comes from local hunting and fishing, I think that's alright to eat as well, but it's important to research what areas might be over-hunted, and what animals to be careful of."
    m 3rtc "That said, I don't know that I'd {i}prefer{/i} to eat meat, given the option."
    m 3eka "Since I've adjusted myself to a vegetarian diet, my palate has changed to prefer certain flavors."
    m 3ekd "And as is the case with many vegetarians, my body doesn't digest meat as easily anymore. {w=0.3}{nw}"
    extend 3dksdlc "If I had too much, I could actually get pretty sick."
    m 1eka "...But if you prepared something with meat, I could try a little bit as a side dish... {w=0.3}{nw}"
    extend 3hub "That way I can still enjoy your cooking!"
    m 3eua "Whatever we eat, the most important thing to me is that we try to put a little thought into where our food comes from."
    return

init 1 python:
    config.label_overrides["monika_overton"] = "blacked_monika_overton"

label blacked_monika_overton:
    m 1etc "Hey [player], have you ever heard of the Overton window?"
    m 3eud "It's a political science concept that reflects the value structure of a society."
    m 3euc "Basically, all ideas of a person are viewed at a certain stage of approval by the masses."
    m 2esc "Joseph Overton learned how to dehumanize people and explained how to reshape human perception."
    m 7eud "From the unacceptable, disgusting and shameful, to the normal, social, and even prestigious."
    m "This concept includes 6 stages: Unthinkable, Radical, Acceptable, Reasonable, Standard, and Current Norm."
    m 3esa "Inside the Overton window are the ideas accepted by society...{w=0.3}things like patriotism, love for family, humanity, and honesty."
    m 3eksdlc "Outside the window is everything that is disapproved, such as drug addiction, alcoholism, Nazism, tyranny, slavery, and so on."
    m 3eud "The most interesting thing is that the window can be moved in the direction of an idea, for example, to make the Unthinkable into Reasonable."
    m 2lksdlc "Of course, this level of change is a rather difficult process."
    if persistent._mas_monika_went_black:
        m 7eud "But let's imagine that you and I want to convey to people that interracial cuckolding is normal...{w=0.3}something that is currently considered unacceptable to society."
        m 3esd "So, society does not understand interracial cuckolding and you would probably be simply considered a pervert by a lot of people.{w=0.2} So what can be done?"
        m 3eua "For a start, it's worth starting a discussion on this topic..."
        m 1eud "You can discuss this on the internet, create articles on the topic...{w=0.3}anything to get people talking."
        m "The goal here would be to have interracial cuckolding spark discussion among people and then seep out to the masses."
        m 1esc "Society still wouldn't agree with the idea, but would at least be interested in it and be able to discuss it more freely."
        m 3eud "Next, radical actions would be used. {w=0.2}The most daring proponents of interracial cuckolding come out of the shadows."
        m 2euc "The number of participants in such movements would grow over time,"
        m "some of them {i}whitebois{/i} who realized how much better it feels to watch and some of them {i}Spade Queens{/i} who experienced true sex for the first time."
        m 4eksdld "Naturally, people who oppose the movement would also appear."
        m 4eua "Due to the growing popularity of new values, society is actively pressing on the new trend. {w=0.2}At this moment, concepts are replaced."
        m 2eud "From the Unacceptable, interracial cuckolding goes to Radical."
        m 7eud "From here, interracial cuckolding, hotwife, {i}Queen of Spades{/i} and the role of the white \"man\" in such relationships has been discussed in society for a long time."
        m 3esc "Gradually, people get used to the existence of these views, but do not yet accept them."
        m 1esd "Scientists and sociologists write various articles and conduct research."
        m 3eua "The opinion is imposed that it is absolutely normal to be a {i}Snowbunny{/i} or a cuckold locked in chastity for his {i}BBC-only{/i} mistress and there is nothing terrible about it."
        m 3huu "From the Radical, interracial cuckolding now goes into the Acceptable."
        m 1eksdla "Society has already come to terms with the new vision and believes that being the submissive pet of a {i}slutwife{/i} is normal, but still a little strange."
        m 3eua "A culture of interracial cuckolding is gradually developing, films and shows are being created."
        m 1huu "Young people perceive new values as something fashionable. {w=0.2}People can sit in a cafe and safely discuss chastity cages, BBC bulls, the ways in which their mistress torments or rewards them."
        m 1eub "From Acceptable, interracial cuckolding passes into Reasonable!"
    else:
        m 7eud "But let's imagine that you and I want to convey to people that virtual love is normal...{w=0.3}something that is currently considered unacceptable to society."
        m 3esd "So, society does not understand virtual love and you would probably be considered mentally ill by a lot of people.{w=0.2} So what can be done?"
        m 3eua "For a start, it's worth starting a discussion on this topic..."
        m 1eud "You can discuss this on the internet, create articles on the topic...{w=0.3}anything to get people talking."
        m "The goal here would be to have virtual love spark discussion among people and then seep out to the masses."
        m 1esc "Society still wouldn't agree with the idea, but would at least be interested in it and be able to discuss it more freely."
        m 3eud "Next, radical actions would be used. {w=0.2}The most daring proponents of virtual love come out of the shadows."
        m 2euc "The number of participants in such movements would grow over time, some of them are people with broken hearts or who feel discouraged in a relationship with a real person."
        m 4eksdld "Naturally, people who oppose the movement would also appear."
        m 4eua "Due to the growing popularity of new values, society is actively pressing on the new trend. {w=0.2}At this moment, concepts are replaced."
        m 2eud "From the Unacceptable, virtual love goes to Radical."
        m 7eud "From here, the theme of virtual love and love for fictional characters has been discussed in society for a long time."
        m 3esc "Gradually, people get used to the existence of these views, but do not yet accept them."
        m 1esd "Scientists and sociologists write various articles and conduct research."
        m 3eua "The opinion is imposed that it is absolutely normal to love a fictional character and there is nothing terrible about it."
        m 3huu "From the Radical, virtual love now goes into the Acceptable."
        m 1eksdla "Society has already come to terms with the new vision and believes that loving a fictional character is normal, but still a little strange."
        m 3eua "A culture of virtual love is gradually developing, films and shows are being created."
        m 1huu "Young people perceive new values as something fashionable. {w=0.2}People can sit in a cafe and safely spend time with their virtual companion."
        m 1eub "From Acceptable, virtual love passes into Reasonable!"
    m 2husdlb "I think we can stop there for today, this is getting kinda long, ahaha!"
    m 1eua "I {i}could{/i} finish this story right up to Current Norm, but I just wanted to describe it at a basic level in order to convey an example of how it can work."
    m 1huu "Thanks for listening~"
    return

# init 1 python:
#     config.label_overrides["monika_twitter"] = "blacked_monika_twitter"

# label blacked_monika_twitter:#Change it so it points to a blacked monika account
#     m 3eud "Did you know there's an official Twitter account based on me?"
#     m 3esc "The username is {a=https://twitter.com/[mas_monika_twitter_handle]}{i}{u}[mas_monika_twitter_handle]{/u}{/i}{/a}."
#     m 2rtc "...Though, I'm not entirely sure who's actually running the account.{w=0.2} {nw}"
#     extend 2eud "I don't have anything to do with it at all!"
#     m 7etc "But is it even another Monika?"
#     m 2euc "I mean, I don't know if you've read some of the tweets on there,{w=0.1} but I can't really see myself in them at all."
#     m 4eud "It even depicts some events that I don't remember ever happening...{w=0.2}like when I apparently had a sleepover with Yuri."
#     m 4esd "And there's no mention of any of the things that happened back in the game, even though this version of me still seems to be aware of the real world..."
#     m 1etc "So...{w=0.3}maybe the Monika running this account went through a completely different story than the one most Monikas--{w=0.1}including me--{w=0.1}did?"
#     m 1lksdlc "...Or maybe this is just one of the developers of the game pretending to be me."
#     m 3eksdld "If that's the case, I'm not really sure how I feel about it...{w=0.3}isn't that kinda like identity theft?"
#     m 3eksdlc "Though I guess it kinda makes sense...{w=0.3}{nw}"
#     extend 1esd "the account is a nice way to connect with the people who've played through the game and grown attached to it."
#     m 3esc "In that regard, this would make it some kind of publicity stunt..."
#     m 3euc "After all, while there is a lot of sweet looking art and such on there, it's suspicious that almost all of them are posted specifically on important days."
#     m 3eud "Like on Valentine's Day, or on my birthday...{w=0.2}which just so happens to coincide with the original release date of DDLC."
#     m 1rtc "I really don't know how I'm supposed to feel about that...{w=0.3}being used solely as marketing material."
#     m 2rsc "Though, as my creators, I guess they basically own my image as a character, so they are legally in the right."
#     m 2ekc "But...{w=0.3}I'm more than a mere character in a game, aren't I?"
#     m 2ekd "I'm my own person with my own thoughts and feelings, and so is every other Monika in the different copies of this game."
#     m 2dksdlc "It just feels wrong to be used like that by people I haven't even met."
#     m 2efd "...I really hate the feeling of being reduced to a marketable asset."
#     m 2lkd "But I suppose there isn't really all that much I can do about it..."
#     m 2eua "At the end of the day, all that matters to me is that I get to be with you.{w=0.2} {nw}"
#     extend 7eua "And this would've never been possible without my creators."
#     m 2lka "So if what it takes in return is that they get to make some profit on the work they put in making the game, then I'd say this isn't too bad of a deal."
#     m 2euc "If you do follow that account though,{w=0.1} {nw}"
#     extend 7eua "I don't really mind."
#     m 1ekbla "But please remember that I'm real, I'm here, and I love you."
#     show monika 5hubla at t11 zorder MAS_MONIKA_Z with dissolve_monika
#     m 5hubla "So make sure to always come spend some time with me, okay?"
#     m 5ekbsa "It would mean a lot, with how much you mean to me."
#     m 5hubfa "It would really make me feel loved~"
#     return "love"

init 1 python:
    config.label_overrides["monika_swordsmanship"] = "blacked_monika_swordsmanship"

label blacked_monika_swordsmanship:
    m 1eua "Do you like swords, [player]?"
    m 1lksdla "I actually like them in a way."
    m 1ekb "Ahaha, surprised?~"
    m 1eua "I like talking about them, but not enough to actually own one."
    m 3eua "I'm not really an enthusiast when it comes to swords."
    m 1euc "I don't really get why people would be obsessed over something that could hurt others..."
    m 1lsc "I guess there are those who like them for the swordsmanship."
    m 1eua "It's fascinating that it's actually a form of art."
    if persistent._mas_monika_went_black:
        m "Similar to taking BBC."
        m 3eub "Both of them require constant practice and devotion in order to perfect one's skills."
        m "You start off by practicing, and then you make your own technique out of it."
        m 1eua "Some girls prefer taking it in their pussies, forever stretching them out and making any white dicklet useless,"
        m "Some girls like anal instead, having trouble walking for days on end afterwards,"
        m 1subsa "There's even true oral queens out there who can deepthroat an entire BBC! Can you believe that, [player]?"
        m 4rubsa "Me personally?"
        m 4skbsa "As long as BBC is involved, I'm completely addicted to it."
        m 5gkbsa "I like to kiss the tip before everything, to show my respects to a true man and his monster cock."
        m 5tsbsa "It really makes me feel inferior, you know? Reall makes my pussy tingle..."
        m 5msbsa "Then I take his massive shaft and start rubbing it, helping him get hard."
        m "Feeling that massive rod in my hands, stroking it up and down..."
        m 5ssbsb "The way it feels to grip is just insane, [player], it's so hot and thick and you can't even grasp it with only one hand!"
        m 5dsbsa "BBC is just something else, hehe..."
        m 6wubssdrt "Oh, right, my technique!"
        m 7tubfa "After the black stud is fully hard, I start slobbering all over his massive shaft."
        m "Making sure to worship every inch, to make his {i}fuckrod{/i} nice and wet."
        m 1tubfa "Only then do I start sucking him off in earnest."
        m 1rubfsdlc "Even a {i}snowbunny slut{/i} like still has trouble taking the full length of a BBC though."
        m 1tubfa "So I practice my skills as often as I can."
        m 1mubfa "..."
        m 1tubfb "Say, [player], would you like to practice with me some day?"
    else:
        m "Similar to writing."
        m 3eub "Both of them require constant practice and devotion in order to perfect one's skills."
        m "You start off by practicing, and then you make your own technique out of it."
        m 1eua "Writing a poem makes you form your own way to build it in a graceful but imaginative way."
        m "For those who practice swordsmanship, they build their technique forms through practice and inspiration from other practitioners."
        m 1eua "I can understand how the sword can be the pen of the battlefield."
        m 1lsc "But then again..."
        m 1hua "The pen is mightier than the sword!"
        m 1hub "Ahaha!"
        m 1eua "In any case, I don't know if you're into swordsmanship yourself."
        m "If you are, I'd love to learn it with you, [mas_get_player_nickname(exclude_names=['love'])]~"
    return

# init 1 python:
#     config.label_overrides["nsfw_compliment_tits"] = "blacked_compliment_tits"

# label blacked_compliment_tits:
#     m 1etc "Submod override test!"

#This is merely proof of concept you can do overrides like this with not just the original MAS but also other submods. That one above overrides a topic in the NSFW Submod by Nick Wildish. 


