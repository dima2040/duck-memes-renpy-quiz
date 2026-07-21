#!/usr/bin/env bash
# Запускайте из корня проекта Ren'Py.

set -euo pipefail

# Укажите желаемое имя GitHub-репозитория.
REPO_NAME="duck-memes-renpy-quiz"

# Авторизация нужна только если вход через GitHub CLI ещё не выполнен.
if ! gh auth status >/dev/null 2>&1; then
  gh auth login
fi

# Инициализация локального репозитория и первый коммит.
git init
git branch -M main
git add .
git commit -m "Initial commit: Ren'Py duck memes quiz"

# Создание публичного репозитория, добавление origin и отправка ветки main.
gh repo create "$REPO_NAME" --public --source=. --remote=origin --push

# Пример первого релиза. Раскомментируйте после сборки APK или Steam-архива.
# gh release create v1.0.0-alpha "builds/game-release.apk" \
#   --title "v1.0.0-alpha" \
#   --notes "Первый альфа-релиз викторины про Кля, Кря и Покляйкомэна."
