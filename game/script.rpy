# Sprint 2 vertical slice.
# Quiz content lives in quiz_content.rpy and uses the Sprint 0 prototype meme seed.
# It is temporary content, not final approved meme canon.

define mbk = Character("МужикБыкКорова", color="#ffd84d")
define neo = Character("Неофиты", color="#c7f0ff")
define p = Character("Покляйкомэн", color="#8ee8ff")

label start:
    $ score = 0
    $ mistakes = 0
    $ round_score = 0
    $ round_total = 0
    $ perfect_main_rounds = 0
    $ current_question_number = 0
    $ correct_question_numbers = []
    play music audio.school_calm_loop fadein 1.0

    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    mbk "В школьном коридоре сегодня не просто шум. Это мемная тревога."
    mbk "Неофиты повторяют Кля, Ква, Кря и Покря без различия: у них каждое слово теперь будто ответ на всё."
    neo "Мы берём звук, делаем лицо посерьёзнее - и класс смеётся. Значит, работает?"
    mbk "Смеётся не значит понимает. На перемене смеются и над упавшей шваброй."
    mbk "Ты пройдёшь три раунда: услышишь базу, удержишь кодекс и вернёшь словам смысл, когда класс захочет только шума."

    jump round_1_intro


label say_quiz_line(speaker_id, line_text):
    if speaker_id == "mbk":
        mbk "[line_text]"
    elif speaker_id == "neo":
        neo "[line_text]"
    elif speaker_id == "p":
        p "[line_text]"
    else:
        "[line_text]"

    return


label play_quiz_question(question_data):
    $ current_question_number += 1
    $ mbk(question_data["prompt"])
    $ selected_answer = renpy.display_menu([(answer["text"], answer) for answer in question_data["answers"]])

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

    mbk "Раунд 1: «База»."
    mbk "Здесь не ищут тайную мифологию. Здесь проверяют, подходит ли слово к ситуации."
    neo "Поняли: если слово звучит странно, мы сразу уверенные."

    call play_quiz_round(quiz_round_by_id("base"))

    jump interlude_1


label interlude_1:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    mbk "Раунд закрыт: [round_score] из [round_total]."
    neo "То есть мем держится не на том, что слово короткое и громкое?"
    mbk "Уже лучше. Коротким бывает сигнал, но смысл у него должен быть точным."
    mbk "Теперь мало выбрать правильное. Надо объяснить, почему кодекс это выдерживает."

    jump round_2_intro


label round_2_intro:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    mbk "Раунд 2: «Кодекс»."
    mbk "Канон не зубрят как параграф. Его проверяют: совпадает ли слово с образом, жестом и ситуацией."
    neo "Последняя парта готова проверить всё неправильным способом."

    call play_quiz_round(quiz_round_by_id("code"))

    jump interlude_2


label interlude_2:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    mbk "Раунд закрыт: [round_score] из [round_total]."
    neo "А если мы смешаем Кля, Ква, Кря и Покря, добавим крик и скажем, что это глубокий слой?"
    mbk "Тогда школьный чат получит много сообщений и ноль легенды."
    mbk "Финальный раунд будет под давлением. Неофиты начнут подменять смысл прямо во время ответа."

    jump round_3_intro


label round_3_intro:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    mbk "Раунд 3: «Испытание легенды»."
    mbk "Теперь ты не просто выбираешь вариант. Ты возвращаешь каждое слово на место, пока класс продаёт шум как озарение."
    neo "Мы уже назвали обычный шум «озарением» и почти поверили."

    call play_quiz_round(quiz_round_by_id("legend_trial"))

    jump final_ceremony_question


label final_ceremony_question:
    scene bg_school_party
    show mbk_placeholder at mbk_left

    mbk "Три раунда закрыты, но школьная шкала требует ровного десятка."
    neo "А если мы скажем «восемь из десяти», хотя вопросов было девять, это будет звучать солиднее?"
    mbk "Будет звучать как математика, которую укусил мем без объяснения."
    mbk "Поэтому перед финалом остаётся десятый, обрядовый вопрос."

    call play_quiz_question(quiz_final_question())

    jump finale_check


label finale_check:
    scene bg_school_party
    show mbk_placeholder at mbk_left

    $ total_questions = quiz_total_questions()

    if correct_question_numbers == [1, total_questions]:
        jump secret_first_last_ending

    mbk "Три раунда и обрядовый вопрос закончены. Итог: [score] из [total_questions]."

    if score == total_questions:
        jump perfect_victory
    elif score >= QUIZ_LEGEND_THRESHOLD:
        jump victory
    elif score == 0:
        jump zero_score_ending
    else:
        jump game_over


label secret_first_last_ending:
    play music audio.game_over_melancholy fadeout 1.5 fadein 1.5
    $ unlock_final_achievements(score)

    mbk "???"

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

    mbk "Десять из десяти. Ни одной трещины в кодексе."
    neo "То есть это не просто победа? Это когда даже неправильные варианты выглядят как тест на верность?"
    mbk "Именно. Ты не угадал канон - ты прошёл по нему без шума в подошвах."
    p "Покляйко Squad фиксирует абсолютный Покря. Последняя парта временно прекращает самодеятельность."
    neo "Мы записываем? Прямо в тетрадь? Заголовок делать жирным?"
    mbk "Записывайте. Сегодня школа получила не ответчика, а хранителя мем-кодекса. Легенда утверждена без пересчёта."
    mbk "Даже я временно снимаю режим сурового молчания. На одну перемену."

    hide screen quiz_reaction_stamp
    with dissolve

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

    mbk "Неофиты притихли. Это редкий школьный звук."
    neo "Получается, смешно не потому что случайно, а потому что правильно попало?"
    mbk "Да. Впервые за день последняя парта отличила шутку от лужи со звуком."
    p "Кля, Ква, Кря и Покря стоят на местах. Покляйко Squad салютует без самодеятельности."
    mbk "Школа видит: ты не просто угадываешь ответы, ты держишь мем-кодекс. Восходящая легенда зафиксирована."

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

    mbk "Итог: [score] из [total_questions]. Ошибок: [mistakes]."
    mbk "Канон не рухнул, но шум пока слишком ловко маскируется под понимание."
    neo "То есть если повторить громче, это всё ещё неправильно?"
    mbk "Правильно. Следующий заход должен стать уроком: меньше паники, больше различения."

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

    mbk "Итог: [score] из [total_questions]. Это не провал. Это музей провала с экскурсоводом."
    neo "Подождите. Если все ответы были неверные, значит мы можем учить наоборот?"
    mbk "Нет. Но вы уже начали, поэтому объявляю мем-молчание."
    neo "То есть мы теперь главные преподаватели неправильных мемов?"
    mbk "Именно поэтому молчание объявлено срочно."
    p "Покляйкомэн кладёт плащ на парту. Даже плащ понял, что сейчас лучше не развеваться."
    mbk "Канон не уничтожен. Он просто отошёл к окну и делает вид, что его не спрашивали."
    mbk "Игрок отправляется на пересдачу кря-кода. Без позора, но с полным пакетом домашнего Покря."

    menu:
        "Пересдать кря-код":
            jump start
        "Выйти из игры":
            return
