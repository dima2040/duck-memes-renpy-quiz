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
   `C:\Users\Lenovo\.codex\worktrees\515d`
3. В списке проектов выберите `Duck Memes Ren'Py Quiz`
   (папка `fullstack-ren-py-github-cli-gh`).
4. Нажмите `Launch Project`.

Альтернативно из PowerShell:

```powershell
& "C:\Users\Lenovo\Documents\Downloads\renpy-8.5.3-sdk\renpy.exe" "C:\Users\Lenovo\.codex\worktrees\515d\fullstack-ren-py-github-cli-gh"
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
- `bg_neophyte_classroom.png` используется как user-provided временный фон с
  неофитами/одноклассниками, а не как новый named/canon character.
- `teacher_funny.png` больше не используется как `mbk_placeholder`.
- Нет ошибок missing image/font/config.
- Ren'Py lint проходит.

Команда для lint:

```powershell
& "C:\Users\Lenovo\Documents\Downloads\renpy-8.5.3-sdk\renpy.exe" "C:\Users\Lenovo\.codex\worktrees\515d\fullstack-ren-py-github-cli-gh" lint
```

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
user-provided sprite для `МужикБыкКорова`. Визуальное направление также связано с
local visual reference:

`C:/Users/Lenovo/Pictures/photo_2024-12-08_17-36-04.jpg`

Этот asset не является финальным релизным артом. Перед Steam/Android релизом
нужно подтвердить стиль, права на использование reference/final asset и
game-designer approval. Также добавлен `game/images/bg_neophyte_classroom.png`
как временный user-provided classmate/neophyte background, не новый named/canon character.
Больше деталей: `docs/identity_notes.md` и
`game/images/README.md`.

## Публикация На GitHub

`publish_renpy_project.sh` оставлен как исторический helper для Bash/Git Bash.
Коммит и публикация не выполняются автоматически.
