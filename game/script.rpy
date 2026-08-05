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

    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    mbk "В школьном коридоре случилась мемная тревога."
    mbk "Неофиты шутят громко, но не туда. Они путают Кля, Ква, Кря и Покря так уверенно, будто это расписание."
    neo "Ква-ква, смешно же? Мы почти легенды?"
    mbk "Почти - это когда контрольная почти не сгорела."
    mbk "Ты пройдёшь три раунда и покажешь классу, где база, где кодекс, а где начинается легенда."

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
    $ mbk(question_data["prompt"])
    $ selected_answer = renpy.display_menu([(answer["text"], answer) for answer in question_data["answers"]])

    if selected_answer["correct"]:
        $ score += 1
        $ round_score += 1
    else:
        $ mistakes += 1

    $ response_line_index = 0

    while response_line_index < len(selected_answer["response"]):
        $ speaker_id, line_text = selected_answer["response"][response_line_index]
        call say_quiz_line(speaker_id, line_text)
        $ response_line_index += 1

    return


label play_quiz_round(round_data):
    $ round_score = 0
    $ round_total = len(round_data["questions"])
    $ question_index = 0

    while question_index < len(round_data["questions"]):
        $ question_data = round_data["questions"][question_index]
        call play_quiz_question(question_data)
        $ question_index += 1

    return


label round_1_intro:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    mbk "Раунд 1: «База»."
    mbk "Задача простая: отличить смешное от несмешного на самом примитивном уровне."
    neo "Мы готовы. У нас уже есть четыре случайных звука и полная уверенность."

    call play_quiz_round(quiz_round_by_id("base"))

    jump interlude_1


label interlude_1:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    mbk "Раунд закрыт: [round_score] из [round_total]."
    neo "Мы поняли! Если слово короткое, оно автоматически мем?"
    mbk "Нет. Коротким бывает и неправильный ответ."
    mbk "Теперь мало выбрать правильное. Надо объяснить, почему оно держится."

    jump round_2_intro


label round_2_intro:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    mbk "Раунд 2: «Кодекс»."
    mbk "Канон не зубрят как параграф. Его понимают, иначе он разваливается при первом «ква» из последней парты."
    neo "Последняя парта готова разваливать."

    call play_quiz_round(quiz_round_by_id("code"))

    jump interlude_2


label interlude_2:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    mbk "Раунд закрыт: [round_score] из [round_total]."
    neo "А если мы смешаем Кля, Ква, Кря и Покря, добавим крик и объявим это гениальным?"
    mbk "Тогда школьный чат получит шум, но не легенду."
    mbk "Финальный раунд будет под давлением. Неофиты начнут шутить неправильно прямо во время ответа."

    jump round_3_intro


label round_3_intro:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    mbk "Раунд 3: «Испытание легенды»."
    mbk "Теперь ты не просто выбираешь ответ. Ты удерживаешь канон, пока класс пытается утащить его в шум."
    neo "Мы уже тащим."

    call play_quiz_round(quiz_round_by_id("legend_trial"))

    jump finale_check


label finale_check:
    scene bg_school_party
    show mbk_placeholder at mbk_left

    $ total_questions = quiz_total_questions()

    mbk "Три раунда закончены. Итог: [score] из [total_questions]."

    if score >= QUIZ_LEGEND_THRESHOLD:
        jump victory
    else:
        jump game_over


label victory:
    mbk "Неофиты притихли. Это редкий школьный звук."
    neo "Получается, смешно не там, где громче, а там, где правильно?"
    mbk "Впервые за день последняя парта произнесла мысль."
    p "Кля, Ква, Кря и Покря стоят на местах. Покляйко Squad салютует."
    mbk "С этого момента школа признаёт тебя восходящей легендой мем-канона."

    menu:
        "Пройти Sprint 2 ещё раз":
            jump start
        "Выйти из игры":
            return


label game_over:
    scene bg_neophyte_classroom
    show mbk_placeholder at mbk_left

    $ total_questions = quiz_total_questions()

    mbk "Итог: [score] из [total_questions]. Ошибок: [mistakes]."
    mbk "Канон не рухнул, но неофиты пока слишком бодро несут неправильные шутки."
    neo "Мы можем ещё раз неправильно?"
    mbk "Можете. Но следующий заход должен стать уроком, а не шумовым кружком."

    menu:
        "Попробовать снова":
            jump start
        "Выйти из игры":
            return
