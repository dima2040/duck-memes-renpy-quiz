# Temporary Placeholder Art

These images are temporary placeholders. They exist so every `scene` and `show`
statement in `game/script.rpy` resolves without missing-image errors while the
game is still moving through small playable checkpoints.

## Layout

- `bg_*.png` files are temporary school location backgrounds.
- `bg_neophyte_classroom.png` is a user-provided temporary classmate/neophyte
  classroom background used in the current quiz/VN flow.
- `duck_hero.png` is a cohesive temporary duck/Poklyaykomen visual placeholder
  for the finale cameo, not a player avatar.
- `teacher_funny.png` is a legacy generic teacher placeholder.
- `characters/` contains character-specific placeholders introduced after the
  original Sprint 0/Sprint 1 asset pass.

## Cohesive Temporary Character Placeholders

`characters/mbk_placeholder.png` is the temporary МужикБыкКорова asset used by
the `mbk_placeholder` image definition in `game/images.rpy`.

The current version is a user-provided checkpoint sprite, sized for the existing
VN scene composition. The direction still follows the local visual reference:

`C:/Users/Lenovo/Pictures/photo_2024-12-08_17-36-04.jpg`

The asset is meant to read better than the generic teacher placeholder: horns,
stern human-like eyes, blond hair/beard, mustache, glasses, formal teacher
clothes, and ear tag. It is not final release art and needs game-designer
approval or replacement before Steam/Android release.

The generated cohesive temporary backgrounds and duck cameo are generated
locally by `tools/generate_temp_visual_assets.py`. The MBK sprite and neophyte
classroom background are user-provided in this checkpoint and remain subject to
final designer/licensing approval.

For broader visual, licensing, and audio direction, see
`docs/identity_notes.md`.

