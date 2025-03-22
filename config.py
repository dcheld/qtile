import json
import os
import socket
import subprocess
from libqtile import bar, layout, hook, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.extension import dmenu
from libqtile.log_utils import logger
from libqtile import extension

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration

mod = "mod4"
alt = "mod1"
ctrl = "control"
shift = "shift"
home = os.path.expanduser('~')

if qtile.core.name == "x11":
    term = "urxvt"
elif qtile.core.name == "wayland":
    term = "foot"

terminal = guess_terminal()
rofi_power_menu_cmd = f"{home}/.config/rofi/applets/bin/powermenu.sh"
applicationLaunch = f"{home}/.config/rofi/launchers/type-3/launcher.sh"
applicationQuickLaunch = f"{home}/.config/rofi/launchers/type-2/launcher.sh"
calendar = 'khal interactive'
fileManager = "nemo"
processManager = "gnome-system-monitor"
# musicPlayer = "flatpak run com.spotify.Client"
musicPlayer = """google-chrome-stable --app="http://music.youtube.com/" --class=WebApp-YT7567 --name=WebApp-YT7567 --user-data-dir=/home/dcheld/.local/share/ice/profiles/YT7567"""
# browser = "google-chrome-stable"
browser = "google-chrome-stable"
sensors = "watch -n 1 sensors"
ide = "code" 
screenshot = "flameshot gui"
clipboard = "clipcat-menu"
whats_app_launch="""google-chrome-stable --app="https://web.whatsapp.com/" --class=WebApp-WhatsApp3698 --user-data-dir=/home/dcheld/.local/share/ice/profiles/WhatsApp3698"""

def console_launcher(app):
    return f"urxvt -e {app}"

@lazy.function
def toggle_minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()


@lazy.window.function
def window_to_next_group(window, switch_group: bool = False):
    window_to_group(window, 1, switch_group)

@lazy.window.function
def window_to_previous_group(window, switch_group: bool = False):
    window_to_group(window, -1, switch_group)

def window_to_group(window, step, switch_group: bool = False):
    current_index = window.qtile.groups.index(window.group)
    next_index = (current_index + step) % (len(window.qtile.groups)-1)
    window.togroup(window.qtile.groups[next_index].name, switch_group=switch_group)

keys = [

# Most of our keybindings are in sxhkd file - except these

# Multimedia Control
     Key([mod], "F2", lazy.group['SPD'].dropdown_toggle("whatsapp")),
     Key([mod], "F3", lazy.group['SPD'].dropdown_toggle("media-play")),
     Key([mod], "F4", lazy.group['SPD'].dropdown_toggle("bitwarden")),
     Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
     Key([], "XF86AudioPause", lazy.spawn("playerctl play-pause")),
     Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
     Key([], "XF86AudioNext", lazy.spawn("playerctl next")),

# Volume Control
     Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 1%+ unmute")),
     Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 2%- unmute")),
     Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),

# Microphone Mute
    Key([], "XF86AudioMicMute", lazy.spawn("amixer sset Capture toggle")),

# Brightness Control
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# F7 Video Mirror
    Key([], "XF86Display", lazy.spawn("")),

# F8 Wireless / Bluetooth
    Key([], "XF86WLAN", lazy.spawn("")),

#Rofi
    Key([mod], "r", lazy.spawn(applicationLaunch), desc = "Launch primary launcher"),
    Key([alt], "f2", lazy.spawn(applicationQuickLaunch), desc = "Quick launcher"),

# SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "m", lazy.window.toggle_minimize(), lazy.group.next_window()),
    Key([mod, ctrl], "m", toggle_minimize_all()),
    Key([mod], "q", lazy.window.kill()),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, ctrl], "Return", lazy.group["SPD"].dropdown_toggle("terminal"), desc="Launch ScratPad terminal"),
    Key([mod, ctrl, alt], "Return", lazy.group['SPD'].dropdown_toggle('qshell')),

    Key([mod], "e", lazy.spawn(fileManager), desc="Launch file explorer"),
    Key([mod, alt], 'r', lazy.run_extension(extension.J4DmenuDesktop(
        dmenu_prompt=">",
        fontsize=14,
        dmenu_ignorecase=True,
    ))),
    Key([ctrl, shift], "Escape", lazy.spawn(processManager), desc="Process manager"),

# PRINT SCREEN

    Key([], "Print", lazy.spawn(screenshot), desc="Print screen tool"),

# SUPER + SHIFT KEYS

    Key([mod, shift], "q", lazy.window.kill()),
    Key([mod, ctrl], "r", lazy.restart()),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.reset()),
    Key([mod, ctrl], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),

    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    Key([alt], "Tab", lazy.layout.next()),
    Key([alt, shift ], "Tab", lazy.layout.previous()),

    Key([alt, ctrl], "Tab", lazy.group.next_window()),
    Key([alt, ctrl, shift], "Tab", lazy.group.prev_window()),

#CHANGE SCREEMS
    Key([mod], "Tab", lazy.screen.next_group(skip_empty = True)),
    Key([mod, shift], "Tab", lazy.screen.prev_group(skip_empty = True)),

    Key([mod, ctrl], "Tab", lazy.screen.next_group(skip_empty = False)),
    Key([mod, ctrl, shift], "Tab", lazy.screen.prev_group(skip_empty = False)),

    Key([mod], "apostrophe", lazy.screen.toggle_group()),

# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, ctrl], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, ctrl], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, ctrl], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, ctrl], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, ctrl], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, ctrl], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, ctrl], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, ctrl], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, shift], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, alt], "k", lazy.layout.flip_up()),
    Key([mod, alt], "j", lazy.layout.flip_down()),
    Key([mod, alt], "l", lazy.layout.flip_right()),
    Key([mod, alt], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, shift], "k", lazy.layout.shuffle_up()),
    Key([mod, shift], "j", lazy.layout.shuffle_down()),
    Key([mod, shift], "h", lazy.layout.shuffle_left()),
    Key([mod, shift], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, shift], "Up", lazy.layout.shuffle_up()),
    Key([mod, shift], "Down", lazy.layout.shuffle_down()),
    Key([mod, shift], "Left", lazy.layout.swap_left()),
    Key([mod, shift], "Right", lazy.layout.swap_right()),

    # MOVE WINDOW TO NEXT SCREEN
    Key([mod, alt], "Left", window_to_previous_group(switch_group=True)),
    Key([mod, alt], "Right", window_to_next_group(switch_group=True)),

# TOGGLE FLOATING LAYOUT
    Key([mod], "Space", lazy.window.toggle_floating()),

# WINDOW EFFECTS
    Key([mod], "Equal", lazy.window.up_opacity()),
    Key([mod, alt], "Equal", lazy.window.set_opacity(1)),
    Key([mod], "Minus", lazy.window.down_opacity()),
    Key([mod, alt], "Minus", lazy.window.set_opacity(0.1)),

# SHUTDOWN_MENU
    KeyChord([mod], "s", [
        Key([], "m", lazy.spawn(rofi_power_menu_cmd)),
        Key([], "p", lazy.spawn("poweroff")),
        Key([], "r", lazy.spawn("reboot")),
        Key([], "s", lazy.spawn("systemctl suspend")),
        Key([], "o", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([], "l", lazy.spawn("loginctl lock-session"), desc="Lock screen"),
    ]),

# Programs
    KeyChord([mod], "x", [
        Key([], "b", lazy.spawn(browser)),
        Key([], "c", lazy.spawn(ide)),
        Key([], "x", lazy.spawn("xkill")),
    ]),

# Clipboard
    Key([mod], "v", lazy.spawn(clipboard)),
    Key([mod, alt], "v", lazy.spawn(f"clipcatctl clear")),
]

def init_scratchpad():

        # Configuration
        height =                0.4650
        y_position =            0.005
        warp_pointer =            False
        on_focus_lost_hide =    True
        opacity =                1

        return [
            ScratchPad("SPD",
                [
                    # Drop down terminal with tmux session
                    DropDown("terminal",
                        terminal + f" -o window.opacity=0.9",
                        y = y_position,
                        height = height,
                        on_focus_lost_hide = on_focus_lost_hide,
                        warp_pointer = warp_pointer,
                        opacity = opacity),

                    # Another terminal exclusively for qshell
                    DropDown("qshell",
                        terminal + f" -o window.opacity=0.8 -e qtile shell",
                        y = y_position,
                        on_focus_lost_hide = on_focus_lost_hide,
                        warp_pointer = warp_pointer,
                        opacity = opacity),

                        # Another terminal exclusively for qshell
                    DropDown("sensors",
                        console_launcher(sensors),
                        y = y_position,
                        x = 0.6,
                        height = 0.85,
                        width = 0.4,
                        on_focus_lost_hide = False,
                        warp_pointer = warp_pointer,
                        opacity = opacity),

                    # Media Play
                    DropDown("media-play",
                        musicPlayer,
                        y = y_position,
                        x = 0.15,
                        height = 0.65,
                        width = 0.7,
                        on_focus_lost_hide = False,
                        warp_pointer = warp_pointer,
                        opacity = opacity),

                    # Bitwarden
                    DropDown("bitwarden",
                        # "flatpak run com.bitwarden.desktop",
                        # match = Match(title="Bitwarden"),
                        "bitwarden-desktop",
                        y = y_position,
                        x = 0.15,
                        height = 0.65,
                        width = 0.7,
                        on_focus_lost_hide = False,
                        warp_pointer = warp_pointer,
                        opacity = opacity),

                    # Calendar
                    DropDown("calendar",
                        console_launcher(calendar),
                        y = y_position,
                        x = 0.7,
                        width = 0.3,
                        on_focus_lost_hide = False,
                        opacity = opacity),

                    # WhatsApp
                    DropDown("whatsapp",
                        whats_app_launch,
                        y = y_position,
                        x = 0.15,
                        width = 0.7,
                        height = 0.7,
                        on_focus_lost_hide = on_focus_lost_hide,
                        warp_pointer = warp_pointer,
                        opacity = opacity),
                ],
            ),
        ]

groups = init_scratchpad()

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
# group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

# group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    group = Group(
        name=group_names[i],
        # layout=group_layouts[i].lower(),
        label=group_labels[i],
    )
    groups.append(group)
    keys.extend([
        #CHANGE SCREEMS
        Key([mod], group.name, lazy.group[group.name].toscreen()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([alt, shift], group.name, lazy.window.togroup(group.name)),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, shift],
            group.name,
            lazy.window.togroup(group.name),
            lazy.group[group.name].toscreen()),

        # Key([mod], '', lazy.group[group.name].hide()),
    ])

# COLORS FOR THE BAR
#Theme name : ArcoLinux Default
def init_colors():
    return [["#2F343F", "#2F343F"], # color 0
            ["#2F343F", "#2F343F"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#fba922", "#fba922"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#f3f4f5", "#f3f4f5"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#6790eb", "#6790eb"], # color 8
            ["#a9a9a9", "#a9a9a9"], # color 9
            ["#0c0c0c", "#0c0c0c"], # color 10
        ]

def init_colors_json():
    colors_file = os.path.expanduser('~/.cache/hellwal/colors.json')
    with open(colors_file) as f:
        colordict = json.load(f)
        return [[colordict['colors'][f"color{i}"], colordict['colors'][f"color{i}"]] for i in range(len(colordict['colors']))]


colors = init_colors()

def init_layout_theme():
    return {
                "margin":2,
                "border_width":2,
                "border_focus": "#5e81ac",
                "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# --------------------------------------------------------
# Decorations
# https://qtile-extras.readthedocs.io/en/stable/manual/how_to/decorations.html
# --------------------------------------------------------

decor_left = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_left"
            # path="rounded_left"
            # path="forward_slash"
            # path="back_slash"
        )
    ],
}

decor_right = {
    "decorations": [
        PowerLineDecoration(
            path="arrow_right"
            # path="rounded_right"
            # path="forward_slash"
            # path="back_slash"
        )
    ],
}

# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sanws",
                fontsize = 12)

widget_defaults = init_widgets_defaults()
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
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
                highlight_method="block",  # or border
                max_title_width=300,
                fontsize=14,
                border=colors[4],
                txt_floating=" ",
                txt_minimized=">_ ",
                borderwidth=5,
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
                     text = "⏻",
                     background = colors[4],
                     foreground = colors[6],
                     fontsize = 18,
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

def init_screens():
    wallpaper = {
        "wallpaper": "~/Pictures/wallpapers/joe-yates-Cc4sToR2Oc0-unsplash.jpg",
        "wallpaper_mode": "stretch",
    }
    return [
        Screen(**wallpaper, 
               top=bar.Bar(
                   widgets=init_widgets_screen1(),
                   size=30,
                   opacity= .95,
                   background = "#fff")),
        #Screen(**wallpaper, top=bar.Bar(widgets=init_widgets_screen2(), size=30, opacity= .9)),
    ]

screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.resume
def resume():
    subprocess.Popen(['picom','-b'])

dgroups_app_rules = []  # type: list
dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="blueman-manager"), # blutooth manager
        Match(wm_class="gnome-calculator"),  # Calculator
        Match(wm_class="gnome-calendar"),  # Calendar
        Match(wm_class="kcalc"),  # Calendar
        Match(wm_class=processManager),  # Calendar
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        # Match(title='Bitwarden'),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qTile"
