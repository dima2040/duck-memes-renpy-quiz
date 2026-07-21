# Викторина по школьным птичьим мемам.
# Фоны и спрайты вымышленные: добавьте свои изображения с этими именами.

define t = Character("Учитель", color="#ffd84d")
define p = Character("Покляйкомэн", color="#8ee8ff")

label start:
    $ score = 0

    scene bg_school
    show teacher_funny

    t "Добро пожаловать в главную школьную викторину: «Кля, Кря и сила Покляйко»!"
    t "Шесть вопросов, четыре варианта. Ошибёшься — улетишь в game over быстрее, чем Утя к булочке."
    p "Крякай уверенно. Но думай ещё увереннее."

    jump question_1


label question_1:
    scene bg_classroom
    show teacher_funny

    t "Вопрос 1. Какой звук обычно лучше всего подходит утке?"

    menu:
        "Кля":
            jump game_over
        "Ква":
            jump game_over
        "Кря":
            $ score += 1
            t "Кря! База пройдена. Утя одобряет."
            jump question_2
        "Покляйко":
            jump game_over


label question_2:
    scene bg_corridor
    show teacher_funny

    t "Вопрос 2. Тебя просят подтвердить, что ты не списывал. Что звучит как максимально серьёзное обещание?"

    menu:
        "Крякай, я сам всё придумал":
            jump game_over
        "Клянись!":
            $ score += 1
            t "Вот это уровень ответственности. Почти как сдать проект до дедлайна."
            jump question_3
        "Покря!":
            jump game_over
        "Ква-ква, честное слово":
            jump game_over


label question_3:
    scene bg_school_yard
    show teacher_funny

    t "Вопрос 3. Какая фраза больше всего похожа на команду утиной команде начать шуметь?"

    menu:
        "Кляйко, замри":
            jump game_over
        "Покляйкомэн, активируй тишину":
            jump game_over
        "Крякай!":
            $ score += 1
            t "Именно! Теперь школьный двор звучит как настоящий птичий фестиваль."
            jump question_4
        "Ква, строимся по парам":
            jump game_over


label question_4:
    scene bg_library
    show teacher_funny

    t "Вопрос 4. Кто из этих персонажей звучит как супергерой локальных мемов?"

    menu:
        "Покря":
            jump game_over
        "Кля":
            jump game_over
        "Покляйкомэн":
            $ score += 1
            p "Покляйкомэн на связи! Моя суперсила — превращать контрольную в легенду."
            jump question_5
        "Квайлер":
            jump game_over


label question_5:
    scene bg_gym
    show teacher_funny

    t "Вопрос 5. Нужно собрать мемную команду: Кляйко, Покляйко и Утя. Какое название звучит наиболее канонично?"

    menu:
        "Кря-команда":
            jump game_over
        "Покляйко Squad":
            $ score += 1
            t "Стильно, громко и немного опасно для школьного чата."
            jump question_6
        "Ква-кля-клуб":
            jump game_over
        "Отряд Покря":
            jump game_over


label question_6:
    scene bg_rooftop
    show teacher_funny

    t "Финальный вопрос. Покляйкомэн говорит: «Клянись, что не перепутаешь Кля, Ква, Кря и Покря». Какой порядок содержит именно все четыре мема без лишних слов?"

    menu:
        "Кля, Ква, Кря, Покря":
            $ score += 1
            jump victory
        "Кляйко, Ква, Кря, Утя":
            jump game_over
        "Покря, Покляйко, Клянись, Крякай":
            jump game_over
        "Кря, Крякай, Покляйкомэн, Кля":
            jump game_over


label victory:
    scene bg_school_party
    show teacher_funny
    show duck_hero

    t "Ты прошёл викторину!"
    t "Твой счёт: [score] из 6."
    p "Кря! Ты официально мастер школьного лора, Утя тобой гордится."

    menu:
        "Пройти ещё раз":
            jump start
        "Выйти из игры":
            return


label game_over:
    scene bg_game_over
    show teacher_funny

    t "Ой. Ты запутался в Кля, Ква, Кря и Покляйко."
    t "Твой итоговый счёт: [score] из 6."
    p "Ничего, даже Покляйкомэн иногда говорит «Ква» не в том месте."

    menu:
        "Попробовать снова":
            jump start
        "Выйти из игры":
            return
