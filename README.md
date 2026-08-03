# Duck Memes Ren'Py Quiz

Школьная Ren'Py-викторина про абсурдный мем-канон. Sprint 3 сохраняет
quiz-first vertical slice из Sprint 2: 3 раунда по 3 вопроса, короткие
VN-прослойки между раундами и финальное признание игрока восходящей школьной
легендой при успешном результате.

Sprint 3 добавляет первый playable art/audio/identity pass:

- `МужикБыкКорова` теперь использует отдельный временный character placeholder,
  а не generic `teacher_funny`;
- placeholder art получил более понятную организацию и asset notes;
- визуальный тон, временный статус ассетов, approval/licensing вопросы и audio
  direction описаны в `docs/identity_notes.md`;
- quiz content system и 3x3 flow из Sprint 2 сохранены.

Контент вопросов пока использует только прототипные seed-слова из Sprint 0
(`Кля`, `Ква`, `Кря`, `Покря`, `Покляйко`, `Покляйкомэн`, `Утя`) и не является
финальным утверждённым мем-каноном.

## Запуск Через Ren'Py Launcher

1. Запустите Ren'Py Launcher:
   `C:\Users\Lenovo\Documents\Downloads\renpy-8.5.3-sdk\renpy.exe`
2. Для проверки этой Codex-ветки откройте `preferences` в Launcher и установите
   `Projects Directory` на:
   `C:\Users\Lenovo\Documents\Codex\2026-07-21`
3. В списке проектов выберите `Duck Memes Ren'Py Quiz`
   (папка `fullstack-ren-py-github-cli-gh`).
4. Нажмите `Launch Project`.

Альтернативно из PowerShell:

```powershell
& "C:\Users\Lenovo\Documents\Downloads\renpy-8.5.3-sdk\renpy.exe" "C:\Users\Lenovo\Documents\Codex\2026-07-21\fullstack-ren-py-github-cli-gh"
```

Latest playtest helper:

```powershell
& "C:\Users\Lenovo\Documents\Codex\2026-07-21\fullstack-ren-py-github-cli-gh\tools\launch_latest.ps1"
```

## Проверка Sprint 3 / Visual Polish Checkpoint

- Проект появляется и запускается в Ren'Py Launcher.
- Игра по-прежнему проходит 3 квиз-раунда: `База`, `Кодекс`,
  `Испытание легенды`.
- В каждом раунде есть 3 вопроса, всего 9 вопросов.
- Между раундами остаются короткие VN-сцены с реакцией неофитов и эскалацией.
- `МужикБыкКорова` визуально считывается как отдельный строгий мем-эксперт:
  рога, серьёзный взгляд, светлая борода/усы, ear tag.
- Временные фоны и видимые спрайты выполнены в едином спокойном flat/vector-like
  стиле без noisy placeholder labels.
- `neophyte_crowd.png` используется как анонимная временная группа
  неофитов/одноклассников, а не как новый named/canon character.
- `teacher_funny.png` больше не используется как `mbk_placeholder`.
- Нет ошибок missing image/font/config.
- Ren'Py lint проходит.

Команда для lint:

```powershell
& "C:\Users\Lenovo\Documents\Downloads\renpy-8.5.3-sdk\renpy.exe" "C:\Users\Lenovo\Documents\Codex\2026-07-21\fullstack-ren-py-github-cli-gh" lint
```

## UI Polish Checkpoint

- Dialogue now uses a classic bottom VN textbox over the scene background.
- Character names appear in a compact name plate inside the textbox.
- Quiz answers and final retry/exit menus appear as bottom answer panels on a readable plate.
- Gameplay/content behavior is unchanged: the 3 rounds x 3 questions, scoring, victory, and game over flow should play as before.
- Validate at 1280x720 that long answers wrap inside their bottom panels without overlapping other UI.

## Редактирование Квиз-Контента

- Вопросы, варианты ответов, правильность и реакции лежат в
  `game/quiz_content.rpy`.
- Общая логика показа вопроса, начисления score и подсчёта mistakes находится в
  `game/script.rpy` в labels `play_quiz_round` и `play_quiz_question`.
- Короткие VN-сцены между раундами остаются в `game/script.rpy`, чтобы их было
  удобно писать как обычный Ren'Py-сценарий.
- Подробная заметка для добавления вопроса или раунда:
  `docs/content_system.md`.

## Временные Ассеты

Файлы в `game/images/` остаются placeholder-art.

Sprint 3/visual-polish checkpoint использует `game/images/characters/mbk_placeholder.png` как временный
asset для `МужикБыкКорова`, основанный на user-provided visual reference:

`C:/Users/Lenovo/Pictures/photo_2024-12-08_17-36-04.jpg`

Этот asset не является финальным релизным артом. Перед Steam/Android релизом
нужно подтвердить стиль, права на использование reference/final asset и
game-designer approval. Также добавлен `game/images/characters/neophyte_crowd.png`
как временный anonymous classmate/neophyte sprite, не новый named/canon character.
Больше деталей: `docs/identity_notes.md` и
`game/images/README.md`.

## Публикация На GitHub

`publish_renpy_project.sh` оставлен как исторический helper для Bash/Git Bash.
Коммит и публикация не выполняются автоматически.
