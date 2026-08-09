################################################################################
## Main menu presentation.
################################################################################

init offset = -1

init python:
    def can_continue_game():
        return (
            not getattr(persistent, "continue_blocked_after_ending", False)
            and renpy.newest_slot(r"[^_]") is not None
        )

    style.mm_root.background = Image("images/main_menu_pokrya.png")
    style.mm_button.insensitive_background = Solid("#05070ed8")
    style.mm_button.insensitive_foreground = Solid("#00000055")
    style.mm_button.insensitive_xoffset = 0
    style.mm_button_text.insensitive_color = "#5b6570"
    style.mm_button_text.insensitive_outlines = [(1, "#000000cc", 0, 1)]

    config.main_menu = [
        (u"Start Game", "start", "True"),
        (u"Continue", Continue(confirm=False), "can_continue_game()"),
        (u"Achievements", _intra_jumps("achievements_screen", "main_game_transition"), "True"),
        (u"Preferences", _intra_jumps("preferences_screen", "main_game_transition"), "True"),
        (u"Quit", ui.jumps("_quit"), "True"),
    ]
    config.game_menu = [
        (None, u"Return", ui.jumps("_return"), "True"),
        ("preferences", u"Preferences", _intra_jumps("preferences_screen", "intra_transition"), "True"),
        (None, u"Main Menu", ui.callsinnewcontext("_main_menu_prompt"), "not main_menu"),
        (None, u"Quit", ui.callsinnewcontext("_quit_prompt"), "True"),
    ]
