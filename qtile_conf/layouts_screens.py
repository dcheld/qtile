from libqtile import layout, bar
from libqtile.config import Screen
from .widgets import init_widgets_screen1, init_widgets_screen2


def init_layout_theme():
    return {
        "margin":2,
        "border_width":2,
        "border_focus": "#5e81ac",
        "border_normal": "#4c566a"
    }


layout_theme = init_layout_theme()

# Experimente mais layouts descomentando abaixo
# layouts alternativas:
# layout.Stack(num_stacks=2),
# layout.Bsp(),
# layout.Matrix(),
# layout.MonadWide(),
# layout.RatioTile(),
# layout.Tile(),
# layout.TreeTab(),
# layout.VerticalTile(),
# layout.Zoomy(),
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
]


def init_screens():
    wallpaper = {
        "wallpaper": "~/Pictures/wallpapers/joe-yates-Cc4sToR2Oc0-unsplash.jpg",
        "wallpaper_mode": "stretch",
    }
    return [
        Screen(
            **wallpaper,
            top=bar.Bar(
                widgets=init_widgets_screen1(),
                size=30,
                opacity= .95,
                background = "#fff")),
        # Segunda tela (exemplo comentado)
        # Screen(**wallpaper, top=bar.Bar(widgets=init_widgets_screen2(), size=30, opacity= .9)),
    ]
