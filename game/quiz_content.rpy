################################################################################
## Sprint 2 quiz content.
################################################################################
##
## This content still uses the Sprint 0 prototype meme seed. It is not final
## approved meme canon.

init python:
    QUIZ_LEGEND_THRESHOLD = 7

    QUIZ_ROUNDS = [
        {
            "id": "base",
            "title": "База",
            "questions": [
                {
                    "id": "r1_q1",
                    "prompt": "Вопрос 1. Какой звук обычно лучше всего подходит утке?",
                    "answers": [
                        {
                            "text": "Кля",
                            "correct": False,
                            "response": [
                                ("neo", "Кля! Утка как будто подписывает объяснительную."),
                                ("mbk", "Не база. Кля - не всякий звук, а клятва."),
                            ],
                        },
                        {
                            "text": "Ква",
                            "correct": False,
                            "response": [
                                ("neo", "Ква! Потому что тоже мокро."),
                                ("mbk", "Лужа не делает тебя экспертом."),
                            ],
                        },
                        {
                            "text": "Кря",
                            "correct": True,
                            "response": [
                                ("mbk", "Кря. База услышана, класс на секунду перестал шуметь неправильно."),
                            ],
                        },
                        {
                            "text": "Покляйко",
                            "correct": False,
                            "response": [
                                ("p", "Меня вызвали слишком рано."),
                                ("mbk", "Имя героя - не звук утки."),
                            ],
                        },
                    ],
                },
                {
                    "id": "r1_q2",
                    "prompt": "Вопрос 2. Тебя просят подтвердить, что ты не списывал. Что звучит как максимально серьёзное обещание?",
                    "answers": [
                        {
                            "text": "Крякай, я сам всё придумал",
                            "correct": False,
                            "response": [
                                ("neo", "Зато громко."),
                                ("mbk", "Громкость не заменяет ответственность."),
                            ],
                        },
                        {
                            "text": "Клянись!",
                            "correct": True,
                            "response": [
                                ("mbk", "Верно. Клятва держит форму, даже если дневник дрожит."),
                            ],
                        },
                        {
                            "text": "Покря!",
                            "correct": False,
                            "response": [
                                ("neo", "Покря звучит как маленькая печать."),
                                ("mbk", "Печать без смысла ставят только на несданную тетрадь."),
                            ],
                        },
                        {
                            "text": "Ква-ква, честное слово",
                            "correct": False,
                            "response": [
                                ("mbk", "Слишком болотный уровень серьёзности."),
                            ],
                        },
                    ],
                },
                {
                    "id": "r1_q3",
                    "prompt": "Вопрос 3. Какая фраза больше всего похожа на команду утиной команде начать шуметь?",
                    "answers": [
                        {
                            "text": "Кляйко, замри",
                            "correct": False,
                            "response": [
                                ("neo", "Но зато дисциплина."),
                                ("mbk", "Раунд про шум, а не про обеденный сон."),
                            ],
                        },
                        {
                            "text": "Покляйкомэн, активируй тишину",
                            "correct": False,
                            "response": [
                                ("p", "Я могу, но это другая серия."),
                                ("mbk", "Тишина здесь не спасает мем."),
                            ],
                        },
                        {
                            "text": "Крякай!",
                            "correct": True,
                            "response": [
                                ("mbk", "Именно. Команда короткая, образ ясный, неофиты записали без перевода."),
                            ],
                        },
                        {
                            "text": "Ква, строимся по парам",
                            "correct": False,
                            "response": [
                                ("neo", "А если по парам смешнее?"),
                                ("mbk", "Нет. Это уже физкультура, а не база."),
                            ],
                        },
                    ],
                },
            ],
        },
        {
            "id": "code",
            "title": "Кодекс",
            "questions": [
                {
                    "id": "r2_q1",
                    "prompt": "Вопрос 4. Почему «Кря» работает как базовый утиный мем-сигнал?",
                    "answers": [
                        {
                            "text": "Потому что звук и образ совпадают",
                            "correct": True,
                            "response": [
                                ("mbk", "Верно. Узнаваемость - первый гвоздь в доске канона."),
                            ],
                        },
                        {
                            "text": "Потому что оно длиннее, чем Ква",
                            "correct": False,
                            "response": [
                                ("neo", "Длина важна. Наверное."),
                                ("mbk", "Мем не линейкой измеряют."),
                            ],
                        },
                        {
                            "text": "Потому что любое слово с буквой «р» смешное",
                            "correct": False,
                            "response": [
                                ("mbk", "Опасная теория. Так можно случайно канонизировать расписание."),
                            ],
                        },
                        {
                            "text": "Потому что Покляйкомэн так захотел",
                            "correct": False,
                            "response": [
                                ("p", "Я польщён, но кодекс старше моего плаща."),
                            ],
                        },
                    ],
                },
                {
                    "id": "r2_q2",
                    "prompt": "Вопрос 5. Когда «Клянись!» становится сильным мемным жестом?",
                    "answers": [
                        {
                            "text": "Когда нужно торжественно подтвердить серьёзность",
                            "correct": True,
                            "response": [
                                ("mbk", "Точно. Серьёзность доведена до школьного абсурда."),
                            ],
                        },
                        {
                            "text": "Когда хочется заменить любой ответ одним словом",
                            "correct": False,
                            "response": [
                                ("neo", "Удобно же."),
                                ("mbk", "Удобство - не оправдание для пустоты."),
                            ],
                        },
                        {
                            "text": "Когда учитель отвернулся",
                            "correct": False,
                            "response": [
                                ("mbk", "Это не кодекс, это бытовая паника."),
                            ],
                        },
                        {
                            "text": "Когда Кря уже занято",
                            "correct": False,
                            "response": [
                                ("mbk", "Слова не стулья в столовой."),
                            ],
                        },
                    ],
                },
                {
                    "id": "r2_q3",
                    "prompt": "Вопрос 6. Что делает Покляйкомэна супергероем локальных мемов?",
                    "answers": [
                        {
                            "text": "Он превращает школьное обещание в легенду",
                            "correct": True,
                            "response": [
                                ("p", "Покляйкомэн на связи. Контрольная дрожит, но держится."),
                                ("mbk", "Верно. Герой усиливает смысл, а не просто машет словом."),
                            ],
                        },
                        {
                            "text": "Он громче всех говорит «Ква»",
                            "correct": False,
                            "response": [
                                ("neo", "Громкий герой тоже герой."),
                                ("mbk", "Нет. Это просто микрофон без присмотра."),
                            ],
                        },
                        {
                            "text": "Он отменяет все вопросы",
                            "correct": False,
                            "response": [
                                ("p", "Мечтаю, но не могу."),
                                ("mbk", "Даже герой не отменяет проверку базы."),
                            ],
                        },
                        {
                            "text": "Он делает любую случайность каноном",
                            "correct": False,
                            "response": [
                                ("mbk", "Случайность может быть смешной, но канон требует формы."),
                            ],
                        },
                    ],
                },
            ],
        },
        {
            "id": "legend_trial",
            "title": "Испытание легенды",
            "questions": [
                {
                    "id": "r3_q1",
                    "prompt": "Вопрос 7. В чат кидают: «Ква-ква, покрякали, база закрыта». Что нужно сделать?",
                    "answers": [
                        {
                            "text": "Остановить Ква, вернуть Кря и объяснить без крика",
                            "correct": True,
                            "response": [
                                ("mbk", "Верно. Легенда не орёт на ошибку, а ставит её на место."),
                            ],
                        },
                        {
                            "text": "Согласиться, ведь в чате уже весело",
                            "correct": False,
                            "response": [
                                ("neo", "Веселье есть, значит зачёт?"),
                                ("mbk", "Веселье без различения быстро превращается в перемену без звонка."),
                            ],
                        },
                        {
                            "text": "Добавить ещё три случайных слова",
                            "correct": False,
                            "response": [
                                ("mbk", "Случайность нельзя лечить случайностью."),
                            ],
                        },
                        {
                            "text": "Позвать Покляйкомэна и уйти",
                            "correct": False,
                            "response": [
                                ("p", "Я за помощь, но легенду за тебя не проживу."),
                            ],
                        },
                    ],
                },
                {
                    "id": "r3_q2",
                    "prompt": "Вопрос 8. Неофит говорит: «Покляйко Squad - это любое название, где есть Squad». Какой ответ держит кодекс?",
                    "answers": [
                        {
                            "text": "Смысл держится на Кляйко, Покляйко и Уте, а не только на вывеске",
                            "correct": True,
                            "response": [
                                ("mbk", "Точно. Название без состава - табличка на пустом кабинете."),
                            ],
                        },
                        {
                            "text": "Да, Squad решает всё",
                            "correct": False,
                            "response": [
                                ("neo", "Мы теперь тоже Squad."),
                                ("mbk", "Не каждый кружок с английским словом становится легендой."),
                            ],
                        },
                        {
                            "text": "Нужно заменить Утю на Ква",
                            "correct": False,
                            "response": [
                                ("mbk", "Это уже подмена, а не толкование."),
                            ],
                        },
                        {
                            "text": "Нужно говорить название только шёпотом",
                            "correct": False,
                            "response": [
                                ("mbk", "Таинственность не чинит пустой смысл."),
                            ],
                        },
                    ],
                },
                {
                    "id": "r3_q3",
                    "prompt": "Вопрос 9. Последняя парта требует назвать порядок из четырёх прототипных мем-слов без лишних слов. Что выбираешь?",
                    "answers": [
                        {
                            "text": "Кля, Ква, Кря, Покря",
                            "correct": True,
                            "response": [
                                ("mbk", "Порядок назван. Даже мел замер в уважении."),
                            ],
                        },
                        {
                            "text": "Кляйко, Ква, Кря, Утя",
                            "correct": False,
                            "response": [
                                ("neo", "Почти же похоже."),
                                ("mbk", "Похоже - любимая маска ошибки."),
                            ],
                        },
                        {
                            "text": "Покря, Покляйко, Клянись, Крякай",
                            "correct": False,
                            "response": [
                                ("mbk", "Смешал команды, имена и сигналы. Класс рад, кодекс нет."),
                            ],
                        },
                        {
                            "text": "Кря, Крякай, Покляйкомэн, Кля",
                            "correct": False,
                            "response": [
                                ("p", "Я внезапно оказался в списке слов."),
                                ("mbk", "Героя не кладут в словарь без причины."),
                            ],
                        },
                    ],
                },
            ],
        },
    ]


    def quiz_total_questions():
        return sum(len(round_data["questions"]) for round_data in QUIZ_ROUNDS)


    def quiz_round_by_id(round_id):
        for round_data in QUIZ_ROUNDS:
            if round_data["id"] == round_id:
                return round_data

        raise Exception("Unknown quiz round '{}'.".format(round_id))


    def validate_quiz_content():
        known_speakers = {"mbk", "neo", "p"}
        round_ids = set()
        question_ids = set()

        for round_data in QUIZ_ROUNDS:
            round_id = round_data.get("id")

            if round_id in round_ids:
                raise Exception("Duplicate quiz round id '{}'.".format(round_id))

            round_ids.add(round_id)

            if not round_data.get("questions"):
                raise Exception("Quiz round '{}' has no questions.".format(round_id))

            for question_data in round_data["questions"]:
                question_id = question_data.get("id")
                answers = question_data.get("answers", [])
                correct_answers = [answer for answer in answers if answer.get("correct")]

                if question_id in question_ids:
                    raise Exception("Duplicate quiz question id '{}'.".format(question_id))

                question_ids.add(question_id)

                if len(correct_answers) != 1:
                    raise Exception("Quiz question '{}' must have exactly one correct answer.".format(question_id))

                for answer in answers:
                    if not answer.get("response"):
                        raise Exception("Quiz answer '{}' in question '{}' has no response.".format(answer.get("text"), question_id))

                    for speaker_id, line_text in answer["response"]:
                        if speaker_id not in known_speakers:
                            raise Exception("Quiz question '{}' uses unknown speaker '{}'.".format(question_id, speaker_id))

                        if not line_text:
                            raise Exception("Quiz question '{}' has an empty response line.".format(question_id))

        return True


    QUIZ_CONTENT_IS_VALID = validate_quiz_content()
