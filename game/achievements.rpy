################################################################################
## Achievements.
################################################################################

default achievement_toast_queue = []
default achievement_toast_visible = False

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
        {
            "id": "correct_order",
            "title": "Правильный порядок",
            "description": "???",
            "locked_description": "Закрыто. ???",
            "icon": "reaction_canon_icon",
        },
        {
            "id": "first_run",
            "title": "Первый заход",
            "description": "Заверши своё первое полное прохождение.",
            "locked_description": "Закрыто. Первый полный заход ещё ждёт звонка на урок.",
            "icon": "reaction_correct_icon",
        },
        {
            "id": "resit_accepted",
            "title": "Пересдача принята",
            "description": "Заверши игру второй раз.",
            "locked_description": "Закрыто. Пересдача ещё не занесена в школьный журнал.",
            "icon": "reaction_correct_icon",
        },
        {
            "id": "perfect_round",
            "title": "Ни одной трещины в раунде",
            "description": "Закрой любой основной раунд на 3/3.",
            "locked_description": "Закрыто. Идеальный раунд ещё не выдержал проверку мелом.",
            "icon": "reaction_canon_icon",
        },
        {
            "id": "three_canon_seals",
            "title": "Три печати канона",
            "description": "Закрой все три основных раунда на 3/3 за одно прохождение.",
            "locked_description": "Закрыто. Три раунда ещё не поставили печати подряд.",
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

    def ensure_achievement_stats():
        if (
            not hasattr(persistent, "achievement_stats")
            or persistent.achievement_stats is None
            or not isinstance(persistent.achievement_stats, dict)
        ):
            persistent.achievement_stats = {}

        stats = persistent.achievement_stats
        stats.setdefault("completed_playthroughs", 0)
        return stats

    def queue_achievement_toast(achievement):
        global achievement_toast_queue

        achievement_toast_queue.append(achievement)
        show_next_achievement_toast()

    def show_next_achievement_toast():
        global achievement_toast_queue
        global achievement_toast_visible

        if achievement_toast_visible or not achievement_toast_queue:
            return

        achievement_toast_visible = True
        achievement = achievement_toast_queue.pop(0)
        renpy.sound.play("audio/achievement_unlock.wav")
        renpy.show_screen("achievement_toast", achievement=achievement)

    def finish_achievement_toast():
        global achievement_toast_visible

        renpy.hide_screen("achievement_toast")
        achievement_toast_visible = False
        show_next_achievement_toast()

    def unlock_achievement(achievement_id):
        achievements = ensure_achievements()

        if achievements.get(achievement_id):
            return False

        achievements[achievement_id] = True
        renpy.save_persistent()

        achievement = achievement_by_id(achievement_id)
        if achievement is not None:
            queue_achievement_toast(achievement)

        return True

    def unlock_result_achievement(final_score):
        achievement_id = RESULT_ACHIEVEMENT_IDS.get(final_score)

        if achievement_id is None:
            return False

        return unlock_achievement(achievement_id)

    def unlock_completion_achievements():
        stats = ensure_achievement_stats()
        stats["completed_playthroughs"] = int(stats.get("completed_playthroughs", 0)) + 1
        renpy.save_persistent()

        completed_playthroughs = stats["completed_playthroughs"]

        if completed_playthroughs >= 1:
            unlock_achievement("first_run")

        if completed_playthroughs >= 2:
            unlock_achievement("resit_accepted")

    def unlock_final_achievements(final_score):
        unlock_result_achievement(final_score)
        unlock_completion_achievements()

    def unlock_secret_first_last_achievements():
        unlock_achievement("correct_order")
        unlock_completion_achievements()


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


screen achievement_toast(achievement):
    zorder 300

    timer 3.4 action Function(finish_achievement_toast)

    frame:
        at achievement_toast_slide
        style "achievement_toast_panel"

        hbox:
            spacing 16
            yalign 0.5

            add achievement["icon"]:
                xysize (64, 64)

            vbox:
                spacing 3
                yalign 0.5

                text "Достижение открыто" style "achievement_toast_label"
                text achievement["title"] style "achievement_toast_title"


transform achievement_toast_slide:
    xalign 0.5
    ypos -120
    alpha 0.0
    easeout 0.2 ypos 24 alpha 1.0
    pause 2.8
    easein 0.22 ypos -120 alpha 0.0


style achievements_panel is default
style achievements_title is default
style achievements_counter is default
style achievements_back_button is button
style achievements_back_button_text is button_text
style achievement_entry is default
style achievement_title is default
style achievement_description is default
style achievement_toast_panel is default
style achievement_toast_label is default
style achievement_toast_title is default

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

style achievement_toast_panel:
    xsize 560
    background Solid("#121923f4")
    padding (18, 14, 22, 14)

style achievement_toast_label:
    color "#f4bf66"
    size 21
    bold True
    outlines [(1, "#000000aa", 0, 1)]

style achievement_toast_title:
    color "#fff0c8"
    size 29
    bold True
    outlines [(1, "#000000aa", 0, 1)]
