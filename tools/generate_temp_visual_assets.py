from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
IMAGE_DIR = ROOT / "game" / "images"
CHARACTER_DIR = IMAGE_DIR / "characters"

SCALE = 3
BG_SIZE = (1280, 720)

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


def draw_party():
    img, d = background_base("#b7ced2", "#66815f", 486)
    rect(d, (0, 0, 1280, 486), rgba("#9fb9bf"))
    rect(d, (130, 300, 1150, 486), rgba(PALETTE["purple"]), rgba(PALETTE["ink"]))
    polygon(d, [(130, 300), (640, 220), (1150, 300)], rgba(PALETTE["blue_dark"]), rgba(PALETTE["ink"]))
    rect(d, (465, 350, 815, 486), rgba("#806e99"), rgba(PALETTE["ink"], 160), 3)
    for x in range(140, 1140, 125):
        ellipse(d, (x, 120, x + 28, 148), rgba(PALETTE["gold_light"]), rgba(PALETTE["ink"], 90), 2)
    line(d, [(150, 138), (640, 105), (1130, 138)], rgba(PALETTE["cream"], 160), 3)
    for x in (250, 330, 410, 870, 950, 1030):
        ellipse(d, (x, 430, x + 42, 472), rgba(PALETTE["cream"], 190), rgba(PALETTE["ink"], 120), 2)
        rect(d, (x - 4, 468, x + 46, 486), rgba(PALETTE["blue_dark"], 160))
    line(d, [(0, 575), (1280, 575)], rgba(PALETTE["paper"], 140), 6)
    save(img, IMAGE_DIR / "bg_school_party.png", BG_SIZE)


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


def draw_neophyte_crowd():
    size = (540, 430)
    img = canvas(size)
    d = ImageDraw.Draw(img)
    ink = rgba(PALETTE["ink"])
    ellipse(d, (48, 382, 500, 420), rgba(PALETTE["shadow"], 55), None, 0)
    desks = [(40, 295, 180, 360), (200, 280, 340, 360), (360, 295, 500, 360)]
    for desk in desks:
        round_rect(d, desk, 8, rgba(PALETTE["paper"]), ink, 3)
    pupils = [
        (95, 210, PALETTE["teal"]),
        (230, 180, PALETTE["gold"]),
        (320, 208, PALETTE["red"]),
        (420, 190, PALETTE["purple"]),
    ]
    for x, y, color in pupils:
        ellipse(d, (x - 38, y - 38, x + 38, y + 38), rgba("#f5d0aa"), ink, 4)
        polygon(d, [(x - 56, y + 44), (x + 56, y + 44), (x + 78, y + 132), (x - 78, y + 132)], rgba(color), ink)
        line(d, [(x - 16, y - 2), (x - 4, y + 2)], ink, 3)
        line(d, [(x + 16, y - 2), (x + 4, y + 2)], ink, 3)
        line(d, [(x - 13, y + 22), (x + 13, y + 22)], ink, 3)
    ellipse(d, (56, 222, 82, 248), rgba(PALETTE["gold_light"]), ink, 3)
    ellipse(d, (458, 224, 486, 252), rgba(PALETTE["gold_light"]), ink, 3)
    line(d, [(68, 248), (68, 286)], rgba(PALETTE["gold_light"]), 4)
    line(d, [(472, 252), (472, 288)], rgba(PALETTE["gold_light"]), 4)
    save(img, CHARACTER_DIR / "neophyte_crowd.png", size)


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


def main():
    draw_school()
    draw_school_yard()
    draw_classroom()
    draw_corridor()
    draw_library()
    draw_gym()
    draw_rooftop()
    draw_party()
    draw_game_over()
    # MBK now uses the user-provided sprite saved at
    # game/images/characters/mbk_placeholder.png.
    draw_neophyte_crowd()
    draw_duck_hero()


if __name__ == "__main__":
    main()
