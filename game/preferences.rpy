################################################################################
## Compact beta preferences screen.
################################################################################

screen preferences():
    tag menu
    modal True

    add "images/main_menu_pokrya.png"
    add Solid("#05070ec8")

    frame:
        style "preferences_shell"

        vbox:
            style "preferences_content"

            text "Настройки" style "preferences_title"

            add Solid("#f4bf66") xsize 676 ysize 3

            vbox:
                style "preferences_section"

                text "Экран" style "preferences_section_title"

                hbox:
                    style "preferences_button_row"
                    textbutton "Окно" action Preference("display", "window") style "preferences_button" text_style "preferences_button_text"
                    textbutton "Полный экран" action Preference("display", "fullscreen") style "preferences_button" text_style "preferences_button_text"

            vbox:
                style "preferences_section"

                text "Переходы" style "preferences_section_title"

                hbox:
                    style "preferences_button_row"
                    textbutton "Все" action Preference("transitions", "all") style "preferences_button" text_style "preferences_button_text"
                    textbutton "Без переходов" action Preference("transitions", "none") style "preferences_button" text_style "preferences_button_text"

            vbox:
                style "preferences_section"

                text "Текст" style "preferences_section_title"

                hbox:
                    style "preferences_slider_row"
                    text "Скорость" style "preferences_row_label"
                    bar value Preference("text speed") style "preferences_slider"
                    textbutton "Мгновенно" action Preference("text speed", 0) style "preferences_small_button" text_style "preferences_small_button_text"

                hbox:
                    style "preferences_slider_row"
                    text "Автопрокрутка" style "preferences_row_label"
                    bar value Preference("auto-forward time") style "preferences_slider"
                    textbutton "Сброс" action Preference("auto-forward time", 15) style "preferences_small_button" text_style "preferences_small_button_text"

            vbox:
                style "preferences_section"

                text "Звук" style "preferences_section_title"

                hbox:
                    style "preferences_slider_row"
                    text "Музыка" style "preferences_row_label"
                    bar value Preference("music volume") style "preferences_slider"
                    textbutton "Вкл/выкл" action Preference("music mute", "toggle") style "preferences_small_button" text_style "preferences_small_button_text"

                hbox:
                    style "preferences_slider_row"
                    text "Эффекты" style "preferences_row_label"
                    bar value Preference("sound volume") style "preferences_slider"
                    textbutton "Вкл/выкл" action Preference("sound mute", "toggle") style "preferences_small_button" text_style "preferences_small_button_text"

            hbox:
                style "preferences_footer"
                textbutton "Вернуться" action Return() style "preferences_back_button" text_style "preferences_back_button_text"


style preferences_shell is default
style preferences_content is vbox
style preferences_title is default
style preferences_section is vbox
style preferences_section_title is default
style preferences_button_row is hbox
style preferences_slider_row is hbox
style preferences_footer is hbox
style preferences_row_label is default
style preferences_button is button
style preferences_button_text is button_text
style preferences_small_button is button
style preferences_small_button_text is button_text
style preferences_back_button is button
style preferences_back_button_text is button_text
style preferences_slider is bar

style preferences_shell:
    xalign 0.5
    yalign 0.5
    xsize 760
    background Solid("#111923ee")
    padding (42, 34, 42, 34)

style preferences_content:
    spacing 18

style preferences_title:
    color "#ffd84d"
    size 38
    bold True
    outlines [(2, "#000000dd", 0, 1)]

style preferences_section:
    spacing 8

style preferences_section_title:
    color "#fff8ec"
    size 24
    bold True
    outlines [(1, "#000000cc", 0, 1)]

style preferences_button_row:
    spacing 12

style preferences_slider_row:
    spacing 14
    yalign 0.5

style preferences_footer:
    xalign 1.0

style preferences_row_label:
    xsize 150
    yalign 0.5
    color "#d9e4e8"
    size 20
    outlines [(1, "#000000aa", 0, 1)]

style preferences_button:
    xminimum 170
    yminimum 44
    background Solid("#253240ff")
    hover_background Solid("#334455ff")
    selected_background Solid("#4b3f25ff")
    insensitive_background Solid("#17202acc")
    padding (18, 8, 18, 8)

style preferences_button_text:
    xalign 0.5
    color "#fff8ec"
    hover_color "#ffe39a"
    selected_color "#ffd84d"
    size 20
    outlines [(1, "#071017b8", 0, 1)]

style preferences_small_button:
    xminimum 112
    yminimum 38
    background Solid("#253240ff")
    hover_background Solid("#334455ff")
    selected_background Solid("#4b3f25ff")
    padding (14, 6, 14, 6)

style preferences_small_button_text:
    xalign 0.5
    color "#fff8ec"
    hover_color "#ffe39a"
    selected_color "#ffd84d"
    size 18
    outlines [(1, "#071017b8", 0, 1)]

style preferences_back_button:
    xminimum 160
    yminimum 46
    background Solid("#3a4552f2")
    hover_background Solid("#4c5a6aff")
    padding (20, 8, 20, 8)

style preferences_back_button_text:
    xalign 0.5
    color "#ffd84d"
    hover_color "#fff1b8"
    size 22
    bold True
    outlines [(1, "#071017cc", 0, 1)]

style preferences_slider:
    xsize 380
    ysize 22
    yalign 0.5
    left_bar Solid("#f4bf66")
    right_bar Solid("#2a3542ff")
    hover_left_bar Solid("#ffe39a")
    hover_right_bar Solid("#344252ff")
    thumb Solid("#fff8ec")
    thumb_offset 8
