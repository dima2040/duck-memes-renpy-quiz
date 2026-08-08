################################################################################
## Achievements.
################################################################################

init python:
    ACHIEVEMENTS = (
        {
            "id": "perfect_run",
            "title": "Perfect Run",
            "description": "Пройди мем-испытание на 10/10 без единой ошибки.",
            "locked_description": "Закрыто. Где-то в школе ещё ждёт идеальный 10/10.",
            "icon": "reaction_canon_icon",
        },
    )

    def ensure_achievements():
        if (
            not hasattr(persistent, "achievements")
            or persistent.achievements is None
            or not isinstance(persistent.achievements, dict)
        ):
            persistent.achievements = {}

        return persistent.achievements

    def achievement_by_id(achievement_id):
        for achievement in ACHIEVEMENTS:
            if achievement["id"] == achievement_id:
                return achievement

        return None

    def achievement_unlocked(achievement_id):
        return bool(ensure_achievements().get(achievement_id))

    def unlocked_achievement_count():
        return sum(1 for achievement in ACHIEVEMENTS if achievement_unlocked(achievement["id"]))

    def unlock_achievement(achievement_id):
        achievements = ensure_achievements()

        if achievements.get(achievement_id):
            return False

        achievements[achievement_id] = True
        renpy.save_persistent()

        achievement = achievement_by_id(achievement_id)
        if achievement is not None:
            renpy.notify("Достижение открыто: {}".format(achievement["title"]))

        return True


label achievements_screen:
    call screen achievements
    return


screen achievements():
    tag menu
    zorder 200

    add "images/main_menu_pokrya.png"
    add Solid("#00000088")

    frame:
        style "achievements_panel"

        vbox:
            spacing 18

            hbox:
                xfill True

                vbox:
                    spacing 4
                    text "Достижения" style "achievements_title"
                    text "[unlocked_achievement_count()] из [len(ACHIEVEMENTS)] открыто" style "achievements_counter"

                textbutton "Назад":
                    style "achievements_back_button"
                    action Return()

            for achievement in ACHIEVEMENTS:
                $ unlocked = achievement_unlocked(achievement["id"])

                frame:
                    style "achievement_entry"

                    hbox:
                        spacing 18
                        yalign 0.5

                        add achievement["icon"]:
                            alpha 1.0 if unlocked else 0.28
                            xysize (96, 96)

                        vbox:
                            spacing 8
                            yalign 0.5

                            text achievement["title"] style "achievement_title" color ("#fff0c8" if unlocked else "#8d99a6")
                            text (achievement["description"] if unlocked else achievement["locked_description"]) style "achievement_description"

    key "game_menu" action Return()


style achievements_panel is default
style achievements_title is default
style achievements_counter is default
style achievements_back_button is button
style achievements_back_button_text is button_text
style achievement_entry is default
style achievement_title is default
style achievement_description is default

style achievements_panel:
    xalign 0.5
    yalign 0.5
    xsize 960
    background Solid("#121923f2")
    padding (36, 30, 36, 34)

style achievements_title:
    color "#fff0c8"
    size 44
    bold True
    outlines [(2, "#000000aa", 0, 2)]

style achievements_counter:
    color "#f4bf66"
    size 22
    outlines [(1, "#000000aa", 0, 1)]

style achievements_back_button:
    xalign 1.0
    yalign 0.5
    background Solid("#253240ff")
    hover_background Solid("#334455ff")
    padding (24, 10, 24, 10)

style achievements_back_button_text:
    color "#fff8ec"
    hover_color "#ffe39a"
    size 24

style achievement_entry:
    xfill True
    background Solid("#1a2430f2")
    padding (20, 18, 20, 18)

style achievement_title:
    size 30
    bold True
    outlines [(1, "#000000aa", 0, 1)]

style achievement_description:
    color "#d8e3e6"
    size 23
    line_spacing 2
    outlines [(1, "#00000099", 0, 1)]
