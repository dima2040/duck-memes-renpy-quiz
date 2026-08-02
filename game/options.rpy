################################################################################
## Game options.
################################################################################

init offset = -1

define config.name = _("Duck Memes Ren'Py Quiz")
define config.window_title = _("Duck Memes Ren'Py Quiz")
define gui.show_name = True

define config.version = "0.3.0-sprint2"
define build.name = "duck_memes_renpy_quiz"
define build.version = "0.3.0-sprint2"

define gui.about = _("""Sprint 2 expandable content system.

Three quiz rounds with short VN interludes.
Quiz question data is separated from the hand-authored scene flow.""")

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = dissolve

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 0
default preferences.afm_time = 15

define config.save_directory = "duck-memes-renpy-quiz-sprint2"
define config.window_icon = None

init python:
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("game/cache/**", None)
    build.classify("game/saves/**", None)

