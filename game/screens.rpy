################################################################################
## Visual polish dialogue and choice screens.
################################################################################

screen say(who, what):
    zorder 100

    window:
        id "window"
        xalign 0.5
        ypos 520
        xsize 1210
        ysize 178
        background Solid("#17232de8")
        xpadding 30
        ypadding 16

        vbox:
            spacing 8

            if who:
                text who id "who" style "say_name_text"

            text what id "what" style "say_dialogue_text"


screen choice(items):
    zorder 100

    frame:
        xalign 0.72
        yalign 0.53
        xsize 760
        background Solid("#17232df0")
        xpadding 22
        ypadding 18

        vbox:
            spacing 10

            for item in items:
                textbutton item.caption:
                    action item.action
                    xfill True
                    text_xalign 0.0
                    text_size gui.choice_button_text_size
                    text_color gui.idle_color
                    text_hover_color gui.hover_color
                    text_selected_color gui.selected_color
                    background Solid("#314552d8")
                    hover_background Solid("#456a8de8")
                    insensitive_background Solid("#22313da8")
                    xpadding 18
                    ypadding 12


style say_name_text:
    font gui.name_text_font
    size gui.name_text_size
    color gui.accent_color
    outlines [(2, "#0b1118cc", 0, 0)]

style say_dialogue_text:
    font gui.text_font
    size gui.text_size
    color gui.text_color
    line_spacing 2
    outlines [(2, "#0b1118cc", 0, 0)]
