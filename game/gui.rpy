################################################################################
## Sprint 0 GUI foundation.
################################################################################

init offset = -2

## Calling gui.init resets Ren'Py's built-in styles to sensible defaults and sets
## the game window size.
init python:
    gui.init(1280, 720)

define config.check_conflicting_properties = True

define gui.accent_color = "#f2b84b"
define gui.idle_color = "#dfe7ef"
define gui.hover_color = "#ffd880"
define gui.selected_color = "#ffffff"
define gui.insensitive_color = "#8a8f987f"
define gui.text_color = "#ffffff"
define gui.interface_text_color = "#ffffff"

define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

define gui.text_size = 28
define gui.name_text_size = 30
define gui.interface_text_size = 26
define gui.choice_button_text_size = 26

define gui.textbox_height = 170
define gui.textbox_yalign = 1.0
define gui.name_xpos = 80
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.dialogue_xpos = 80
define gui.dialogue_ypos = 38
define gui.dialogue_width = 1120
define gui.dialogue_text_xalign = 0.0

define gui.choice_button_width = 900
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(24, 12, 24, 12)
define gui.choice_button_text_xalign = 0.5

