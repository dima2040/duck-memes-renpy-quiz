# Temporary Placeholder Art

These images are temporary placeholders. They exist so every `scene` and `show`
statement in `game/script.rpy` resolves without missing-image errors while the
game is still moving through small playable checkpoints.

## Layout

- `bg_*.png` files are temporary school location backgrounds.
- `bg_neophyte_classroom.png` is a user-provided temporary classmate/neophyte
  classroom background used in the current quiz/VN flow.
- `bg_school_party.png` is a user-provided temporary finale/red-carpet
  background. It currently includes the visible duck/Poklyaykomen finale visual
  in the background image itself.
- `bg_zero_score_classroom.png` is a user-provided temporary classroom
  background used for the ordinary 1-6/10 losing ending.
- `bg_zero_score_failure.png` is a user-provided temporary cold classroom
  background used only for the full 0/10 losing ending.
- `bg_secret_first_last_classroom.png` is a user-provided temporary dark
  classroom background used only for the secret first-and-last-answer ending.
- `main_menu_pokrya.png` is a temporary main-menu background with a black field
  and large pixel-styled `Покря` title text.
- `perfect_pokrya_plaque.png` is a temporary pixel-styled perfect-score plaque
  shown only during the 10/10 canonization ending.
- `recognition_code_held_plaque.png`, `recognition_rising_legend_plaque.png`,
  and `recognition_canon_keeper_plaque.png` are temporary pixel-styled
  recognition plaques shown during the 7/10, 8/10, and 9/10 victory endings.
- `loss_zero_plaque.png` through `loss_six_plaque.png` are temporary
  pixel-styled result plaques shown during the 0/10 through 6/10 endings.
- `ui/reaction_correct.png`, `ui/reaction_wrong.png`, and
  `ui/reaction_canon.png` are temporary pixel reaction icons shown after quiz
  answers, perfect rounds, and the 10/10 ending.
- `duck_hero.png` is a legacy generated duck/Poklyaykomen visual placeholder,
  kept available but no longer shown in the current finale.
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

The generated cohesive temporary backgrounds, legacy duck cameo, pixel reaction
icons, and recognition plaques are generated locally by
`tools/generate_temp_visual_assets.py`. The MBK sprite, neophyte classroom
background, and finale/red-carpet background are user-provided in this checkpoint
and remain subject to final designer/licensing approval.

For broader visual, licensing, and audio direction, see
`docs/identity_notes.md`.

