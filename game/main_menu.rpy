################################################################################
## Main menu presentation.
################################################################################

init offset = -1

init python:
    style.mm_root.background = Image("images/main_menu_pokrya.png")
    config.main_menu = [
        (u"Start Game", "start", "True"),
        (u"Load Game", _intra_jumps("load_screen", "main_game_transition"), "True"),
        (u"Achievements", _intra_jumps("achievements_screen", "main_game_transition"), "True"),
        (u"Preferences", _intra_jumps("preferences_screen", "main_game_transition"), "True"),
        (u"Quit", ui.jumps("_quit"), "True"),
    ]
