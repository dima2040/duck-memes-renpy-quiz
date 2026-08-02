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
define gui.name_text_size = 30
define gui.interface_text_size = 26
define gui.choice_button_text_size = 26

define gui.textbox_height = 180
define gui.textbox_yalign = 1.0
define gui.name_xpos = 80
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.dialogue_xpos = 80
define gui.dialogue_ypos = 38
define gui.dialogue_width = 1120
define gui.dialogue_text_xalign = 0.0

define gui.choice_button_width = 980
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(24, 12, 24, 12)
define gui.choice_button_text_xalign = 0.5

