################################################################################
## Sprint 0 GUI foundation.
################################################################################

init offset = -2

## Calling gui.init resets Ren'Py's built-in styles to sensible defaults and sets
## the game window size.
init python:
    gui.init(1280, 720)

define config.check_conflicting_properties = True

define gui.accent_color = "#f4bf66"
define gui.idle_color = "#edf4f2"
define gui.hover_color = "#ffe39a"
define gui.selected_color = "#fff8ec"
define gui.insensitive_color = "#71808f80"
define gui.text_color = "#fff8ec"
define gui.interface_text_color = "#fff8ec"

define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

define gui.text_size = 28
define gui.name_text_size = 26
define gui.interface_text_size = 26
define gui.choice_button_text_size = 23

define gui.textbox_height = 186
define gui.textbox_yalign = 1.0
define gui.name_xpos = 28
define gui.name_ypos = 18
define gui.name_xalign = 0.0
define gui.dialogue_xpos = 36
define gui.dialogue_ypos = 66
define gui.dialogue_width = 1088
define gui.dialogue_text_xalign = 0.0

define gui.choice_button_width = 1092
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(24, 10, 24, 10)
define gui.choice_button_text_xalign = 0.0


################################################################################
## Classic VN textbox and bottom answer panels.
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        style "say_window"

        add Solid("#f4bf66") xpos 0 ypos 0 xsize 1160 ysize 4
        add Solid("#23303cff") xpos 0 ypos 4 xsize 1160 ysize 1

        if who is not None:
            window:
                id "namebox"
                style "say_namebox"

                text who id "who" style "say_label"

        text what id "what" style "say_dialogue"


screen choice(items):
    zorder 100
    style_prefix "choice"

    frame:
        style "choice_plate"

        vbox:
            style "choice_vbox"

            for i in items:
                textbutton i.caption action i.action


style say_window is default
style say_namebox is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style choice_plate is default
style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style say_window:
    xalign 0.5
    yalign 1.0
    yoffset -18
    xsize 1160
    ysize gui.textbox_height
    background Solid("#17202aea")
    padding (0, 0, 0, 0)

style say_namebox:
    xpos gui.name_xpos
    ypos gui.name_ypos
    xminimum 240
    xmaximum 520
    yminimum 42
    background Solid("#3a4552f2")
    padding (20, 5, 20, 5)

style say_label:
    color gui.accent_color
    size gui.name_text_size
    bold True
    outlines [(1, "#071017cc", 0, 1)]

style say_dialogue:
    xpos gui.dialogue_xpos
    ypos gui.dialogue_ypos
    xsize gui.dialogue_width
    color gui.text_color
    size gui.text_size
    line_spacing 2
    outlines [(1, "#071017b8", 0, 1)]

style choice_plate:
    xalign 0.5
    yalign 1.0
    yoffset -18
    xsize 1140
    background Solid("#121923fa")
    padding (24, 18, 24, 18)

style choice_vbox:
    spacing 8

style choice_button:
    xsize gui.choice_button_width
    yminimum 54
    background Solid("#253240ff")
    hover_background Solid("#334455ff")
    selected_background Solid("#334455ff")
    insensitive_background Solid("#253240c8")
    padding (24, 10, 24, 10)

style choice_button_text:
    xalign gui.choice_button_text_xalign
    text_align 0.0
    color gui.text_color
    hover_color gui.hover_color
    selected_color gui.hover_color
    insensitive_color gui.insensitive_color
    size gui.choice_button_text_size
    line_spacing 1
    outlines [(1, "#071017b8", 0, 1)]

