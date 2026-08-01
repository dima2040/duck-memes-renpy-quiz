# Duck Memes Ren'Py Quiz

Школьная Ren'Py-викторина из шести вопросов. Sprint 0 делает репозиторий
самодостаточным launchable-проектом: есть базовый конфиг, размер окна и
временные placeholder-фоны/спрайты для всех текущих `scene` и `show`.

## Запуск через Ren'Py Launcher

1. Запустите Ren'Py Launcher:
   `C:\Users\Lenovo\Documents\Downloads\renpy-8.5.3-sdk\renpy.exe`
2. Если проект не виден в списке, откройте `preferences` в Launcher и установите
   `Projects Directory` на:
   `C:\Users\Lenovo\Documents\Codex\2026-07-21`
3. В списке проектов выберите `Duck Memes Ren'Py Quiz`
   (папка `fullstack-ren-py-github-cli-gh`).
4. Нажмите `Launch Project`.

Альтернативно из PowerShell:

```powershell
& "C:\Users\Lenovo\Documents\Downloads\renpy-8.5.3-sdk\renpy.exe" "C:\Users\Lenovo\Documents\Codex\2026-07-21\fullstack-ren-py-github-cli-gh"
```

## Проверка Sprint 0

- Проект появляется и запускается в Ren'Py Launcher.
- Стартовая сцена загружается без ошибок.
- Все 6 текущих вопросов достижимы.
- Неверный ответ ведёт в game over.
- Верная цепочка ответов ведёт к победе.
- Рестарт из victory/game over возвращает к началу.
- Нет ошибок missing image/font/config.

## Временные ассеты

Файлы в `game/images/` являются placeholder-артом только для Sprint 0. Их нужно
заменить в последующих спринтах, не меняя текущий quiz flow без отдельного
дизайн-решения.

## Публикация на GitHub

`publish_renpy_project.sh` оставлен как исторический helper для Bash/Git Bash.
Для Sprint 0 коммит и публикация не выполняются автоматически.
