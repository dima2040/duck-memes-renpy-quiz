# Sprint 2 vertical slice.
# Quiz content lives in quiz_content.rpy; VN connective text lives in story_content.rpy.
# This is temporary content, not final approved meme canon.

define mbk = Character("МужикБыкКорова", color="#ffd84d")
define neo = Character("Неофиты", color="#c7f0ff")
define p = Character("Покляйкомэн", color="#8ee8ff")

init python:
    def mark_game_started_for_continue():
        persistent.continue_blocked_after_ending = False
        renpy.save_persistent()
        renpy.force_autosave()

    def mark_game_completed_for_continue():
        persistent.continue_blocked_after_ending = True
        renpy.save_persistent()


label start:
    $ score = 0
    $ mistakes = 0
    $ round_score = 0
    $ round_total = 0
    $ perfect_main_rounds = 0
    $ current_question_number = 0
    $ correct_question_numbers = []
    $ mark_game_started_for_continue()
    play music audio.school_calm_loop fadein 1.0

    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    call play_story_scene("start_intro")

    jump round_1_intro


label say_quiz_line(speaker_id, line_text):
    $ rendered_line = renpy.substitute(line_text)

    if speaker_id == "mbk":
        mbk "[rendered_line]"
    elif speaker_id == "neo":
        neo "[rendered_line]"
    elif speaker_id == "p":
        p "[rendered_line]"
    else:
        "[rendered_line]"

    return


label play_story_scene(scene_id):
    $ story_lines = story_scene_by_id(scene_id)
    $ story_line_index = 0

    while story_line_index < len(story_lines):
        $ speaker_id, line_text = story_lines[story_line_index]
        call say_quiz_line(speaker_id, line_text)
        $ story_line_index += 1

    return


label play_quiz_question(question_data):
    $ current_question_number += 1
    $ selected_answer = renpy.call_screen("quiz_choice", prompt=question_data["prompt"], answers=question_data["answers"])

    if selected_answer["correct"]:
        $ score += 1
        $ round_score += 1
        $ correct_question_numbers.append(current_question_number)
    else:
        $ mistakes += 1

    $ reaction_image = "reaction_correct_icon" if selected_answer["correct"] else "reaction_wrong_icon"
    show screen quiz_reaction_stamp(reaction_image)
    with dissolve

    $ response_line_index = 0

    while response_line_index < len(selected_answer["response"]):
        $ speaker_id, line_text = selected_answer["response"][response_line_index]
        call say_quiz_line(speaker_id, line_text)
        $ response_line_index += 1

    hide screen quiz_reaction_stamp
    with dissolve

    return


label show_round_canon_reaction:
    if round_total > 0 and round_score == round_total:
        show screen quiz_reaction_stamp("reaction_canon_icon")
        with dissolve
        pause 0.65
        hide screen quiz_reaction_stamp
        with dissolve

    return


label record_round_achievements:
    if round_total > 0 and round_score == round_total:
        $ perfect_main_rounds += 1
        $ unlock_achievement("perfect_round")

        if perfect_main_rounds == 3:
            $ unlock_achievement("three_canon_seals")

    return


label play_quiz_round(round_data):
    $ round_score = 0
    $ round_total = len(round_data["questions"])
    $ question_index = 0

    while question_index < len(round_data["questions"]):
        $ question_data = round_data["questions"][question_index]
        call play_quiz_question(question_data)
        $ question_index += 1

    call show_round_canon_reaction
    call record_round_achievements

    return


label round_1_intro:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    call play_story_scene("round_1_intro")

    call play_quiz_round(quiz_round_by_id("base"))

    jump interlude_1


label interlude_1:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    call play_story_scene("interlude_1")

    jump round_2_intro


label round_2_intro:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    call play_story_scene("round_2_intro")

    call play_quiz_round(quiz_round_by_id("code"))

    jump interlude_2


label interlude_2:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    call play_story_scene("interlude_2")

    jump round_3_intro


label round_3_intro:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    call play_story_scene("round_3_intro")

    call play_quiz_round(quiz_round_by_id("legend_trial"))

    jump final_ceremony_question


label final_ceremony_question:
    scene bg_school_party
    show mbk_placeholder at mbk_left

    call play_story_scene("final_ceremony_question")

    call play_quiz_question(quiz_final_question())

    jump finale_check


label finale_check:
    scene bg_school_party
    show mbk_placeholder at mbk_left

    $ total_questions = quiz_total_questions()

    if correct_question_numbers == [1, total_questions]:
        jump secret_first_last_ending

    call play_story_scene("finale_summary")

    if score == total_questions:
        jump perfect_victory
    elif score >= QUIZ_LEGEND_THRESHOLD:
        jump victory
    elif score == 0:
        jump zero_score_ending
    else:
        jump game_over


label secret_first_last_ending:
    scene bg_secret_first_last_classroom
    show mbk_placeholder at mbk_left
    play music audio.secret_cry_ambience fadeout 1.5 fadein 1.5
    $ unlock_secret_first_last_achievements()

    call play_story_scene("secret_first_last_ending")

    $ mark_game_completed_for_continue()

    menu:
        "Попробовать снова":
            jump start
        "Выйти из игры":
            return


label perfect_victory:
    play music audio.perfect_canon_jingle fadeout 1.0 fadein 0.05 noloop
    $ unlock_final_achievements(score)

    show perfect_pokrya_plaque at perfect_plaque_top
    with dissolve
    show screen quiz_reaction_stamp("reaction_canon_icon")
    with dissolve

    call play_story_scene("perfect_victory")

    hide screen quiz_reaction_stamp
    with dissolve

    $ mark_game_completed_for_continue()

    menu:
        "Пройти ещё раз":
            jump start
        "Выйти из игры":
            return


label victory:
    play music audio.victory_fanfare fadeout 1.0 fadein 0.25 noloop
    $ unlock_final_achievements(score)

    if score >= 9:
        show recognition_canon_keeper_plaque at recognition_plaque_top
    elif score == 8:
        show recognition_rising_legend_plaque at recognition_plaque_top
    else:
        show recognition_code_held_plaque at recognition_plaque_top
    with dissolve

    call play_story_scene("victory")

    $ mark_game_completed_for_continue()

    menu:
        "Пройти ещё раз":
            jump start
        "Выйти из игры":
            return


label show_loss_result_plaque:
    if score == 0:
        show loss_zero_plaque at loss_plaque_top
    elif score == 1:
        show loss_one_plaque at loss_plaque_top
    elif score == 2:
        show loss_two_plaque at loss_plaque_top
    elif score == 3:
        show loss_three_plaque at loss_plaque_top
    elif score == 4:
        show loss_four_plaque at loss_plaque_top
    elif score == 5:
        show loss_five_plaque at loss_plaque_top
    else:
        show loss_six_plaque at loss_plaque_top
    with dissolve

    return


label game_over:
    scene bg_zero_score_classroom
    show mbk_placeholder at mbk_left
    play music audio.game_over_melancholy fadeout 1.5 fadein 1.5

    $ total_questions = quiz_total_questions()
    $ unlock_final_achievements(score)
    call show_loss_result_plaque

    call play_story_scene("game_over")

    $ mark_game_completed_for_continue()

    menu:
        "Попробовать снова":
            jump start
        "Выйти из игры":
            return


label zero_score_ending:
    scene bg_zero_score_failure
    show mbk_placeholder at mbk_left
    play music audio.game_over_melancholy fadeout 1.5 fadein 1.5

    $ total_questions = quiz_total_questions()
    $ unlock_final_achievements(score)
    call show_loss_result_plaque

    call play_story_scene("zero_score_ending")

    $ mark_game_completed_for_continue()

    menu:
        "Пересдать кря-код":
            jump start
        "Выйти из игры":
            return
