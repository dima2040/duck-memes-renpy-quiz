from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
IMAGE_DIR = ROOT / "game" / "images"
CHARACTER_DIR = IMAGE_DIR / "characters"
UI_DIR = IMAGE_DIR / "ui"

SCALE = 3
BG_SIZE = (1280, 720)
ICON_SIZE = (128, 128)
PLAQUE_SIZE = (780, 192)

PALETTE = {
    "ink": "#22313d",
    "ink_soft": "#314552",
    "cream": "#fff7e8",
    "paper": "#f2ead8",
    "wall": "#dfe7dc",
    "wall_blue": "#aec6cf",
    "floor": "#6f8b70",
    "floor_warm": "#a77c58",
    "floor_cool": "#526878",
    "blue": "#456a8d",
    "blue_dark": "#2f4d67",
    "teal": "#6ea7a1",
    "green": "#5d8561",
    "gold": "#f3bf54",
    "gold_light": "#f8d889",
    "red": "#bd5d56",
    "purple": "#6b5f8e",
    "purple_dark": "#47384f",
    "pink": "#d6a0a8",
    "shadow": "#182530",
}


def rgba(hex_color, alpha=255):
    value = hex_color.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def scaled(value):
    return int(round(value * SCALE))


def box(x0, y0, x1, y1):
    return tuple(scaled(v) for v in (x0, y0, x1, y1))


def pts(points):
    return [(scaled(x), scaled(y)) for x, y in points]


def canvas(size, fill=(0, 0, 0, 0)):
    return Image.new("RGBA", (size[0] * SCALE, size[1] * SCALE), fill)


def save(img, path, size):
    path.parent.mkdir(parents=True, exist_ok=True)
    img = img.resize(size, Image.Resampling.LANCZOS)
    img.save(path)


def save_pixel_icon(img, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    img = img.resize(ICON_SIZE, Image.Resampling.NEAREST)
    img.save(path)


def find_font_path():
    candidates = [
        ROOT / "game" / "DejaVuSans.ttf",
        Path("C:/Users/Lenovo/Documents/Downloads/renpy-8.5.3-sdk/renpy/common/DejaVuSans-Bold.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf"),
    ]

    for path in candidates:
        if path.exists():
            return path

    return None


def fit_font(text, max_width, start_size):
    font_path = find_font_path()

    if font_path is None:
        return ImageFont.load_default()

    size = start_size

    while size > 8:
        font = ImageFont.truetype(str(font_path), size=size)
        bbox = ImageDraw.Draw(Image.new("RGBA", (1, 1))).textbbox((0, 0), text, font=font)

        if bbox[2] - bbox[0] <= max_width:
            return font

        size -= 1

    return ImageFont.truetype(str(font_path), size=size)


def rect(draw, xy, fill, outline=None, width=4):
    draw.rectangle(box(*xy), fill=fill, outline=outline, width=scaled(width))


def round_rect(draw, xy, radius, fill, outline=None, width=4):
    draw.rounded_rectangle(
        box(*xy),
        radius=scaled(radius),
        fill=fill,
        outline=outline,
        width=scaled(width),
    )


def ellipse(draw, xy, fill, outline=None, width=4):
    draw.ellipse(box(*xy), fill=fill, outline=outline, width=scaled(width))


def line(draw, points, fill, width=4, joint="curve"):
    draw.line(pts(points), fill=fill, width=scaled(width), joint=joint)


def polygon(draw, points, fill, outline=None):
    draw.polygon(pts(points), fill=fill)
    if outline:
        line(draw, points + [points[0]], fill=outline, width=4)


def background_base(wall, floor, horizon=452, sky=None):
    img = canvas(BG_SIZE, rgba(wall))
    d = ImageDraw.Draw(img)
    if sky:
        rect(d, (0, 0, 1280, horizon), rgba(sky))
    rect(d, (0, horizon, 1280, 720), rgba(floor))
    line(d, [(0, horizon), (1280, horizon)], rgba(PALETTE["ink"], 150), 3)
    return img, d


def draw_common_corner_shadows(d):
    polygon(d, [(0, 720), (0, 620), (260, 720)], rgba("#000000", 24))
    polygon(d, [(1280, 720), (1280, 620), (1020, 720)], rgba("#000000", 20))


def draw_school():
    img = canvas(BG_SIZE, rgba("#a9cbd6"))
    d = ImageDraw.Draw(img)
    rect(d, (0, 500, 1280, 720), rgba(PALETTE["green"]))
    polygon(d, [(250, 205), (640, 105), (1030, 205)], rgba(PALETTE["blue_dark"]), rgba(PALETTE["ink"]))
    rect(d, (300, 205, 980, 500), rgba(PALETTE["wall_blue"]), rgba(PALETTE["ink"]))
    rect(d, (565, 345, 715, 500), rgba(PALETTE["blue_dark"]), rgba(PALETTE["ink"]))
    rect(d, (590, 370, 640, 500), rgba(PALETTE["shadow"]))
    rect(d, (640, 370, 690, 500), rgba(PALETTE["shadow"]))
    for x in (385, 500, 780, 895):
        round_rect(d, (x, 260, x + 70, 330), 6, rgba(PALETTE["gold_light"]), rgba(PALETTE["ink"], 190), 3)
    line(d, [(0, 555), (1280, 555)], rgba(PALETTE["paper"], 130), 8)
    line(d, [(555, 500), (460, 720)], rgba(PALETTE["paper"], 180), 8)
    line(d, [(725, 500), (820, 720)], rgba(PALETTE["paper"], 180), 8)
    ellipse(d, (1080, 85, 1155, 160), rgba(PALETTE["gold_light"]))
    save(img, IMAGE_DIR / "bg_school.png", BG_SIZE)


def draw_school_yard():
    img = canvas(BG_SIZE, rgba("#b7d3dc"))
    d = ImageDraw.Draw(img)
    rect(d, (0, 430, 1280, 720), rgba(PALETTE["green"]))
    rect(d, (0, 515, 1280, 720), rgba("#668064"))
    polygon(d, [(0, 615), (460, 510), (1280, 565), (1280, 720), (0, 720)], rgba("#7b8f66"))
    rect(d, (70, 265, 390, 430), rgba(PALETTE["wall_blue"]), rgba(PALETTE["ink"]))
    polygon(d, [(45, 265), (230, 180), (415, 265)], rgba(PALETTE["blue_dark"]), rgba(PALETTE["ink"]))
    rect(d, (590, 295, 1010, 430), rgba(PALETTE["wall"]), rgba(PALETTE["ink"]))
    polygon(d, [(560, 295), (800, 205), (1040, 295)], rgba(PALETTE["blue_dark"]), rgba(PALETTE["ink"]))
    for x in (125, 225, 650, 770, 890):
        round_rect(d, (x, 330, x + 58, 380), 4, rgba(PALETTE["gold_light"]), rgba(PALETTE["ink"], 180), 3)
    line(d, [(160, 590), (1120, 590)], rgba(PALETTE["gold"], 180), 6)
    line(d, [(230, 635), (1050, 635)], rgba(PALETTE["gold"], 130), 4)
    save(img, IMAGE_DIR / "bg_school_yard.png", BG_SIZE)


def draw_classroom():
    img, d = background_base(PALETTE["wall"], "#8b735d", 470)
    rect(d, (0, 470, 1280, 720), rgba("#927456"))
    rect(d, (0, 0, 1280, 470), rgba(PALETTE["wall"]))
    rect(d, (94, 90, 580, 330), rgba(PALETTE["blue_dark"]), rgba(PALETTE["ink"]))
    line(d, [(125, 300), (545, 300)], rgba(PALETTE["cream"], 150), 4)
    rect(d, (795, 95, 1135, 315), rgba("#c6d8df"), rgba(PALETTE["ink"]))
    line(d, [(965, 95), (965, 315)], rgba(PALETTE["ink"], 160), 4)
    line(d, [(795, 205), (1135, 205)], rgba(PALETTE["ink"], 120), 4)
    for x in (155, 390, 715, 950):
        polygon(d, [(x, 520), (x + 160, 505), (x + 185, 585), (x + 20, 600)], rgba(PALETTE["paper"]), rgba(PALETTE["ink"]))
    line(d, [(70, 665), (1210, 645)], rgba("#000000", 26), 10)
    draw_common_corner_shadows(d)
    save(img, IMAGE_DIR / "bg_classroom.png", BG_SIZE)


def draw_corridor():
    img = canvas(BG_SIZE, rgba("#b9c8cf"))
    d = ImageDraw.Draw(img)
    polygon(d, [(0, 0), (450, 0), (520, 720), (0, 720)], rgba("#8fa4ac"))
    polygon(d, [(1280, 0), (830, 0), (760, 720), (1280, 720)], rgba("#8fa4ac"))
    polygon(d, [(450, 0), (830, 0), (760, 720), (520, 720)], rgba(PALETTE["wall"]))
    polygon(d, [(0, 480), (1280, 480), (1000, 720), (280, 720)], rgba(PALETTE["floor_cool"]))
    line(d, [(520, 0), (565, 720)], rgba(PALETTE["ink"], 130), 4)
    line(d, [(760, 720), (805, 0)], rgba(PALETTE["ink"], 130), 4)
    for x, y in ((90, 135), (195, 195), (305, 255), (970, 135), (860, 195), (755, 255)):
        rect(d, (x, y, x + 84, y + 54), rgba(PALETTE["blue"]), rgba(PALETTE["ink"], 150), 3)
        line(d, [(x + 8, y + 17), (x + 76, y + 17)], rgba(PALETTE["gold"], 180), 3)
    line(d, [(425, 520), (855, 520)], rgba(PALETTE["gold"], 170), 5)
    line(d, [(520, 610), (760, 610)], rgba(PALETTE["paper"], 130), 4)
    save(img, IMAGE_DIR / "bg_corridor.png", BG_SIZE)


def draw_library():
    img, d = background_base("#d7c7bd", "#765848", 458)
    for x, w in ((90, 230), (380, 260), (705, 230), (985, 210)):
        rect(d, (x, 120, x + w, 458), rgba(PALETTE["purple_dark"]), rgba(PALETTE["ink"]))
        for shelf_y in (185, 260, 335):
            line(d, [(x + 20, shelf_y), (x + w - 20, shelf_y)], rgba(PALETTE["gold"], 160), 5)
        for i in range(4):
            bx = x + 35 + i * 42
            rect(d, (bx, 145, bx + 22, 185), rgba(PALETTE["gold_light"]))
            rect(d, (bx + 7, 222, bx + 30, 260), rgba(PALETTE["red"], 220))
            rect(d, (bx + 14, 298, bx + 38, 335), rgba(PALETTE["teal"], 220))
    polygon(d, [(450, 525), (830, 525), (930, 620), (350, 620)], rgba(PALETTE["paper"]), rgba(PALETTE["ink"]))
    line(d, [(475, 620), (420, 720)], rgba(PALETTE["ink"], 170), 7)
    line(d, [(805, 620), (860, 720)], rgba(PALETTE["ink"], 170), 7)
    draw_common_corner_shadows(d)
    save(img, IMAGE_DIR / "bg_library.png", BG_SIZE)


def draw_gym():
    img = canvas(BG_SIZE, rgba("#a8bec5"))
    d = ImageDraw.Draw(img)
    rect(d, (0, 0, 1280, 440), rgba("#9fb8c0"))
    rect(d, (0, 440, 1280, 720), rgba("#b89169"))
    line(d, [(0, 440), (1280, 440)], rgba(PALETTE["ink"], 140), 4)
    line(d, [(0, 615), (1280, 585)], rgba(PALETTE["gold"], 180), 8)
    line(d, [(190, 440), (190, 720)], rgba(PALETTE["cream"], 130), 5)
    line(d, [(1090, 440), (1090, 720)], rgba(PALETTE["cream"], 130), 5)
    ellipse(d, (540, 468, 740, 668), None, rgba(PALETTE["cream"], 190), 5)
    line(d, [(640, 468), (640, 668)], rgba(PALETTE["cream"], 170), 5)
    line(d, [(540, 568), (740, 568)], rgba(PALETTE["cream"], 170), 5)
    rect(d, (880, 120, 1040, 208), rgba(PALETTE["paper"]), rgba(PALETTE["ink"]))
    rect(d, (936, 208, 984, 250), rgba(PALETTE["red"]), rgba(PALETTE["ink"]))
    line(d, [(960, 250), (960, 380)], rgba(PALETTE["ink"], 150), 5)
    save(img, IMAGE_DIR / "bg_gym.png", BG_SIZE)


def draw_rooftop():
    img = canvas(BG_SIZE, rgba("#8bb6cc"))
    d = ImageDraw.Draw(img)
    rect(d, (0, 0, 1280, 505), rgba("#8bb6cc"))
    rect(d, (0, 505, 1280, 720), rgba("#5e7895"))
    line(d, [(0, 505), (1280, 505)], rgba(PALETTE["cream"], 170), 6)
    for x in (105, 330, 555, 780, 1005, 1230):
        line(d, [(x, 320), (x, 505)], rgba(PALETTE["cream"], 160), 5)
    line(d, [(40, 390), (1240, 390)], rgba(PALETTE["cream"], 140), 5)
    ellipse(d, (1062, 82, 1160, 180), rgba(PALETTE["gold_light"]), rgba(PALETTE["ink"], 120), 3)
    rect(d, (126, 480, 404, 528), rgba(PALETTE["blue_dark"], 210), rgba(PALETTE["ink"], 130), 3)
    rect(d, (876, 472, 1110, 526), rgba(PALETTE["blue_dark"], 190), rgba(PALETTE["ink"], 120), 3)
    save(img, IMAGE_DIR / "bg_rooftop.png", BG_SIZE)


def draw_game_over():
    img, d = background_base("#8fa3a8", "#4e5960", 462)
    rect(d, (0, 0, 1280, 462), rgba("#8fa3a8"))
    rect(d, (330, 140, 950, 398), rgba(PALETTE["purple_dark"]), rgba(PALETTE["ink"]))
    line(d, [(425, 205), (855, 335)], rgba(PALETTE["cream"], 190), 5)
    line(d, [(855, 205), (425, 335)], rgba(PALETTE["cream"], 190), 5)
    rect(d, (120, 430, 1160, 462), rgba(PALETTE["ink_soft"], 170))
    polygon(d, [(0, 720), (1280, 720), (1050, 530), (230, 530)], rgba("#323b42"))
    line(d, [(230, 530), (1050, 530)], rgba(PALETTE["gold"], 140), 5)
    ellipse(d, (92, 78, 142, 128), rgba(PALETTE["gold_light"], 180))
    save(img, IMAGE_DIR / "bg_game_over.png", BG_SIZE)


def draw_duck_hero():
    size = (430, 600)
    img = canvas(size)
    d = ImageDraw.Draw(img)
    ink = rgba(PALETTE["ink"])
    ellipse(d, (98, 535, 338, 585), rgba(PALETTE["shadow"], 65), None, 0)
    polygon(d, [(105, 258), (45, 580), (220, 565), (160, 262)], rgba(PALETTE["red"]), ink)
    polygon(d, [(184, 248), (315, 272), (380, 580), (205, 566)], rgba(PALETTE["blue_dark"]), ink)
    ellipse(d, (125, 210, 292, 400), rgba(PALETTE["gold_light"]), ink)
    ellipse(d, (148, 88, 258, 198), rgba(PALETTE["gold_light"]), ink)
    rect(d, (166, 66, 230, 95), rgba(PALETTE["blue_dark"]), ink, 3)
    polygon(d, [(252, 130), (360, 162), (254, 190)], rgba(PALETTE["gold"]), ink)
    ellipse(d, (175, 125, 188, 138), rgba(PALETTE["ink"]), None, 0)
    ellipse(d, (224, 125, 237, 138), rgba(PALETTE["ink"]), None, 0)
    line(d, [(174, 164), (204, 176), (236, 164)], ink, 5)
    ellipse(d, (165, 280, 254, 335), None, ink, 5)
    polygon(d, [(190, 205), (236, 205), (250, 252), (214, 288), (176, 252)], rgba(PALETTE["cream"]), ink)
    save(img, IMAGE_DIR / "duck_hero.png", size)


def draw_reaction_icons():
    def new_icon():
        return Image.new("RGBA", (64, 64), (0, 0, 0, 0))

    def draw_shadow_panel(d, xy, fill, outline, shadow=(0, 0, 0, 90)):
        x0, y0, x1, y1 = xy
        d.rectangle((x0 + 3, y0 + 4, x1 + 3, y1 + 4), fill=shadow)
        d.rectangle(xy, fill=fill, outline=outline, width=2)

    ink = rgba(PALETTE["ink"])
    chalk = rgba("#f9fff0")
    gold = rgba(PALETTE["gold_light"])

    correct = new_icon()
    d = ImageDraw.Draw(correct)
    draw_shadow_panel(d, (7, 13, 57, 51), rgba("#335f46"), ink)
    d.rectangle((11, 17, 53, 47), outline=rgba("#7fbf83"), width=1)
    d.rectangle((12, 47, 52, 49), fill=rgba("#d8c890"))
    d.line([(18, 33), (27, 42), (46, 21)], fill=chalk, width=5)
    d.rectangle((49, 15, 52, 18), fill=gold)
    d.rectangle((53, 19, 56, 22), fill=gold)
    d.rectangle((13, 19, 16, 22), fill=rgba("#c8f7c5"))
    save_pixel_icon(correct, UI_DIR / "reaction_correct.png")

    wrong = new_icon()
    d = ImageDraw.Draw(wrong)
    draw_shadow_panel(d, (8, 13, 56, 51), rgba("#a93431"), ink)
    d.rectangle((12, 17, 52, 47), outline=rgba("#e06a60"), width=1)
    d.rectangle((12, 47, 52, 49), fill=rgba("#6c211f"))
    d.line([(19, 22), (45, 44)], fill=chalk, width=6)
    d.line([(45, 22), (19, 44)], fill=chalk, width=6)
    d.rectangle((14, 18, 18, 22), fill=rgba("#ffc4bc"))
    save_pixel_icon(wrong, UI_DIR / "reaction_wrong.png")

    canon = new_icon()
    d = ImageDraw.Draw(canon)
    draw_shadow_panel(d, (9, 12, 55, 52), rgba("#9d302d"), ink)
    d.rectangle((13, 16, 51, 48), outline=rgba(PALETTE["gold"]), width=2)
    d.polygon([(18, 12), (24, 4), (27, 12)], fill=rgba("#cfbc94"), outline=ink)
    d.polygon([(40, 12), (45, 4), (48, 12)], fill=rgba("#cfbc94"), outline=ink)
    d.rectangle((21, 23, 26, 43), fill=gold)
    d.rectangle((27, 31, 32, 36), fill=gold)
    d.rectangle((32, 27, 37, 32), fill=gold)
    d.rectangle((37, 23, 43, 28), fill=gold)
    d.rectangle((32, 36, 37, 41), fill=gold)
    d.rectangle((37, 41, 44, 46), fill=gold)
    d.rectangle((17, 19, 47, 21), fill=rgba("#f5d87e"))
    d.rectangle((17, 45, 47, 47), fill=rgba("#f5d87e"))
    save_pixel_icon(canon, UI_DIR / "reaction_canon.png")


def draw_recognition_plaques():
    def draw_text_centered(d, text, y, font, fill, shadow):
        bbox = d.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (PLAQUE_SIZE[0] // 2 - text_width) // 2

        for ox, oy in ((1, 1), (1, 0), (0, 1)):
            d.text((x + ox, y + oy), text, font=font, fill=shadow)

        d.text((x, y), text, font=font, fill=fill)

    def draw_plaque(filename, top_line, bottom_line):
        plaque_size = (PLAQUE_SIZE[0] // 2, PLAQUE_SIZE[1] // 2)
        img = Image.new("RGBA", plaque_size, (0, 0, 0, 0))
        d = ImageDraw.Draw(img)

        gold = rgba("#f2bf62")
        cream = rgba("#fff0c8")
        deep = rgba("#121014")
        shadow = rgba("#6f4527")

        d.rectangle((18, 0, plaque_size[0] - 1, plaque_size[1] - 12), fill=gold)
        d.rectangle((4, 5, plaque_size[0] - 6, plaque_size[1] - 10), fill=deep, outline=gold, width=2)
        d.rectangle((9, 10, plaque_size[0] - 11, plaque_size[1] - 15), outline=cream, width=1)

        top_font = fit_font(top_line, plaque_size[0] - 72, 25)
        bottom_font = fit_font(bottom_line, plaque_size[0] - 108, 17)

        draw_text_centered(d, top_line, 29, top_font, cream, shadow)
        draw_text_centered(d, bottom_line, 58, bottom_font, gold, shadow)

        img = img.resize(PLAQUE_SIZE, Image.Resampling.NEAREST)
        img.save(IMAGE_DIR / filename)

    draw_plaque("recognition_code_held_plaque.png", "МЕМ-КОДЕКС", "УДЕРЖАН")
    draw_plaque("recognition_rising_legend_plaque.png", "ВОСХОДЯЩАЯ ЛЕГЕНДА", "ЗАФИКСИРОВАНА")
    draw_plaque("recognition_canon_keeper_plaque.png", "ХРАНИТЕЛЬ КАНОНА", "ПРИЗНАН")
    draw_plaque("loss_zero_plaque.png", "МУЗЕЙ ПРОВАЛА", "ОТКРЫТ")
    draw_plaque("loss_one_plaque.png", "ИСКРА СМЫСЛА", "ЗАМЕЧЕНА")
    draw_plaque("loss_two_plaque.png", "ШУМ ОПОЗНАН", "ЧАСТИЧНО")
    draw_plaque("loss_three_plaque.png", "БАЗА ШЕВЕЛИТСЯ", "НО СПИТ")
    draw_plaque("loss_four_plaque.png", "КОДЕКС СКРИПИТ", "НО ЖИВ")
    draw_plaque("loss_five_plaque.png", "ПОЛОВИНА КАНОНА", "СПАСЕНА")
    draw_plaque("loss_six_plaque.png", "ЛЕГЕНДА БЛИЗКО", "ПЕРЕСДАЧА ЖДЕТ")


def main():
    draw_school()
    draw_school_yard()
    draw_classroom()
    draw_corridor()
    draw_library()
    draw_gym()
    draw_rooftop()
    draw_game_over()
    # User-provided checkpoint assets are intentionally not regenerated here:
    # game/images/characters/mbk_placeholder.png,
    # game/images/bg_neophyte_classroom.png,
    # game/images/bg_school_party.png.
    draw_duck_hero()
    draw_reaction_icons()
    draw_recognition_plaques()


if __name__ == "__main__":
    main()
