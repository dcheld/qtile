import json
import os
from libqtile import qtile
from qtile_extras import widget
# from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration

from .settings import home, applicationLaunch, clipboard, rofi_power_menu_cmd


def init_colors():
    return [
        ["#2F343F", "#2F343F"],
        ["#2F343F", "#2F343F"],
        ["#c0c5ce", "#c0c5ce"],
        ["#fba922", "#fba922"],
        ["#3384d0", "#3384d0"],
        ["#f3f4f5", "#f3f4f5"],
        ["#cd1f3f", "#cd1f3f"],
        ["#62FF00", "#62FF00"],
        ["#6790eb", "#6790eb"],
        ["#a9a9a9", "#a9a9a9"],
        ["#0c0c0c", "#0c0c0c"],
    ]


def init_colors_json():
    colors_file = os.path.expanduser('~/.cache/hellwal/colors.json')
    with open(colors_file) as f:
        colordict = json.load(f)
        return [[colordict['colors'][f"color{i}"], colordict['colors'][f"color{i}"]] for i in range(len(colordict['colors']))]


colors = init_colors()

decor_left = {
    "decorations": [
        PowerLineDecoration(path="arrow_left")
            # outras opções de path:
            # path="rounded_left"
            # path="forward_slash"
            # path="back_slash"
    ],
}

decor_right = {
    "decorations": [
        PowerLineDecoration(path="arrow_right")
            # outras opções de path:
            # path="rounded_right"
            # path="forward_slash"
            # path="back_slash"
    ],
}


def init_widgets_defaults():
    return dict(font="Noto Sanws", fontsize = 12)


widget_defaults = init_widgets_defaults()
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    return [
        widget.Image(
            **decor_left,
            background=colors[9],
            filename = "~/.icons/custom-download/archlinux-light.svg",
            foreground='ffffff',
            margin_x = 5,
            mouse_callbacks = {"Button1": lambda: qtile.spawn(applicationLaunch)}
        ),
        widget.GroupBox(
            **decor_left,
            background = colors[1],
            font="FontAwesome",
            fontsize = 14,
            highlight_method = "line",
            inactive="#B2BEB5",
            highlight_color = ["#6790eb", "#120a8f",],
            padding=5,
        ),
        widget.CurrentLayoutIcon(
            **decor_left,
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            background="000",
            foreground=colors[0],
            padding=10,
            scale=0.7
        ),
        widget.TaskList(
            **decor_right,
            background=colors[1],
            foreground=colors[5],
            font="FontAwesome",
            highlight_method="block",
            max_title_width=300,
            fontsize=14,
            borderwidth=2,
            border=colors[4],
            txt_floating="🗗 ",
            txt_maximized="🗖 ",
            txt_minimized="🗕 ",
        ),
        widget.ThermalSensor(
            **decor_right,
            background = colors[9],
            foreground = colors[1],
            foreground_alert = colors[6],
            metric = True,
            padding = 5,
            threshold = 80,
            font="FontAwesome",
            fontsize=14,
            format=' {temp:.0f}{unit}',
            tag_sensor = "Package id 0",
            mouse_callbacks={"Button1": lambda: qtile.spawn("qtile cmd-obj -o group SPD -f dropdown_toggle -a 'sensors'")},
        ),
        widget.TextBox(
            **decor_right,
            background = colors[1],
            foreground=colors[6],
            font="FontAwesome",
            text=" ",
            padding = 0,
            fontsize=16,
        ),
        widget.CPUGraph(
            **decor_right,
            background=colors[1],
            foreground=colors[6],
            border_color = colors[2],
            fill_color = colors[8],
            graph_color = colors[8],
            border_width = 1,
            line_width = 1,
            core = "all",
            type = "box"
        ),
        widget.TextBox(
            background=colors[2],
            foreground=colors[4],
            font="FontAwesome",
            text="  ",
            padding = 0,
            fontsize=16,
        ),
        widget.MemoryGraph(
            **decor_right,
            background = colors[2],
            foreground=colors[4],
            border_color = colors[1],
            border_width = 1,
        ),
        widget.KeyboardLayout(
            **decor_right,
            background=colors[1],
            foreground=colors[5],
            font="FontAwesome",
            configured_keyboards = ['us', 'us intl'],
        ),
        widget.TextBox(
            **decor_right,
            background=colors[10],
            foreground=colors[5],
            font="FontAwesome",
            text="  ",
            padding = 0,
            fontsize=16,
            mouse_callbacks={"Button1": lambda: qtile.spawn(clipboard)},
        ),
        widget.Systray(
            **decor_right,
            background=colors[1],
            icon_size=20,
            padding=5,
        ),
        widget.TextBox(
            background=colors[2],
            foreground=colors[10],
            font="FontAwesome",
            text="  ",
            padding = 0,
            fontsize=16,
            mouse_callbacks={"Button1": lambda: qtile.spawn("qtile cmd-obj -o group SPD -f dropdown_toggle -a 'calendar'")}
        ),
        widget.Clock(
            **decor_right,
            background=colors[2],
            foreground=colors[10],
            fontsize=14,
            format="%d/%m/%Y %H:%M",
        ),
        widget.TextBox(
            font="FontAwesome",
            text = "⏻",
            background = colors[4],
            foreground = colors[6],
            fontsize = 25,
            padding = 10,
            mouse_callbacks={"Button1": lambda: qtile.spawn(rofi_power_menu_cmd)},
         ),
        # widget.QuickExit(),
    ]


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2
