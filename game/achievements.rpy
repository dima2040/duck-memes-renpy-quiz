################################################################################
## Achievements.
################################################################################

init python:
    ACHIEVEMENTS = (
        {
            "id": "result_0",
            "title": "Музей провала",
            "description": "Заверши игру с результатом 0/10.",
            "locked_description": "Закрыто. Полный провал ещё не оформлен как экскурсия.",
            "icon": "reaction_wrong_icon",
        },
        {
            "id": "result_1",
            "title": "Искра смысла",
            "description": "Заверши игру с результатом 1/10.",
            "locked_description": "Закрыто. Один правильный ответ ещё прячется в шуме.",
            "icon": "reaction_wrong_icon",
        },
        {
            "id": "result_2",
            "title": "Шум опознан",
            "description": "Заверши игру с результатом 2/10.",
            "locked_description": "Закрыто. Шум пока не получил протокол опознания.",
            "icon": "reaction_wrong_icon",
        },
        {
            "id": "result_3",
            "title": "База шевелится",
            "description": "Заверши игру с результатом 3/10.",
            "locked_description": "Закрыто. База ещё делает вид, что спит.",
            "icon": "reaction_wrong_icon",
        },
        {
            "id": "result_4",
            "title": "Кодекс скрипит",
            "description": "Заверши игру с результатом 4/10.",
            "locked_description": "Закрыто. Кодекс ещё не начал тревожно скрипеть.",
            "icon": "reaction_wrong_icon",
        },
        {
            "id": "result_5",
            "title": "Половина канона",
            "description": "Заверши игру с результатом 5/10.",
            "locked_description": "Закрыто. Ровная половина канона ещё не спасена.",
            "icon": "reaction_correct_icon",
        },
        {
            "id": "result_6",
            "title": "Легенда близко",
            "description": "Заверши игру с результатом 6/10.",
            "locked_description": "Закрыто. До легенды ещё не оставался один ответ.",
            "icon": "reaction_correct_icon",
        },
        {
            "id": "result_7",
            "title": "Кодекс удержан",
            "description": "Заверши игру с результатом 7/10.",
            "locked_description": "Закрыто. Минимальная победа ещё ждёт своего протокола.",
            "icon": "reaction_correct_icon",
        },
        {
            "id": "result_8",
            "title": "Восходящая легенда",
            "description": "Заверши игру с результатом 8/10.",
            "locked_description": "Закрыто. Восходящую легенду ещё не зафиксировали.",
            "icon": "reaction_canon_icon",
        },
        {
            "id": "result_9",
            "title": "Хранитель канона",
            "description": "Заверши игру с результатом 9/10.",
            "locked_description": "Закрыто. Почти идеальный канон ещё не признан.",
            "icon": "reaction_canon_icon",
        },
        {
            "id": "perfect_run",
            "title": "Perfect Run",
            "description": "Пройди мем-испытание на 10/10 без единой ошибки.",
            "locked_description": "Закрыто. Где-то в школе ещё ждёт идеальный 10/10.",
            "icon": "reaction_canon_icon",
        },
    )
    RESULT_ACHIEVEMENT_IDS = {
        0: "result_0",
        1: "result_1",
        2: "result_2",
        3: "result_3",
        4: "result_4",
        5: "result_5",
        6: "result_6",
        7: "result_7",
        8: "result_8",
        9: "result_9",
        10: "perfect_run",
    }

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

    def unlock_result_achievement(final_score):
        achievement_id = RESULT_ACHIEVEMENT_IDS.get(final_score)

        if achievement_id is None:
            return False

        return unlock_achievement(achievement_id)


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

            viewport:
                ysize 438
                mousewheel True
                draggable True

                vbox:
                    spacing 12

                    for achievement in ACHIEVEMENTS:
                        $ unlocked = achievement_unlocked(achievement["id"])

                        frame:
                            style "achievement_entry"

                            hbox:
                                spacing 18
                                yalign 0.5

                                add achievement["icon"]:
                                    alpha (1.0 if unlocked else 0.28)
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
    ysize 620
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
