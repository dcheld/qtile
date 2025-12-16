from libqtile.config import Key, KeyChord
from libqtile import extension
from libqtile.lazy import lazy

from .settings import (
    mod,
    alt,
    ctrl,
    shift,
    terminal,
    applicationLaunch,
    applicationQuickLaunch,
    rofi_power_menu_cmd,
    browser,
    ide,
    processManager,
    fileManager,
    screenshot,
    clipboard,
    musicPlayer,
    volume_up,
    volume_down,
)
from .helpers import (
    toggle_minimize_all,
    window_to_next_group,
    window_to_previous_group,
    toggle_focus_hide,
)

keys = [

# Most of our keybindings are in sxhkd file - except these

# Multimedia Control
     Key([mod], "F1", toggle_focus_hide),
     Key([mod], "F2", lazy.group['SPD'].dropdown_toggle("whatsapp")),
     Key([mod], "F3", lazy.group['SPD'].dropdown_toggle("media-play")),
     Key([mod], "F4", lazy.group['SPD'].dropdown_toggle("bitwarden")),
     Key([mod], "F5", lazy.group['SPD'].dropdown_toggle("llm_app_launch")),
     Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
     Key([], "XF86AudioPause", lazy.spawn("playerctl play-pause")),
     Key([mod, alt], "Backspace", lazy.spawn("playerctl play-pause")),
     Key([mod, alt], "XF86AudioPrev", lazy.spawn("playerctl previous")),
     Key([mod, alt], "Minus", lazy.spawn("playerctl previous")),
     Key([mod, alt], "XF86AudioNext", lazy.spawn("playerctl next")),
     Key([mod, alt], "Equal", lazy.spawn("playerctl next")),

# Volume Control
     Key([], "XF86AudioRaiseVolume", lazy.spawn(volume_up)),
     Key([], "XF86AudioLowerVolume", lazy.spawn(volume_down)),
     Key([mod], "Backspace", lazy.spawn("amixer set Master toggle")),
     Key([mod], "Equal", lazy.spawn(volume_up)),
     Key([mod], "Minus", lazy.spawn(volume_down)),
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
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),

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

    Key([alt, ctrl], "Tab", lazy.group.next_window(), lazy.window.bring_to_front()),
    Key([alt, ctrl, shift], "Tab", lazy.group.prev_window(), lazy.window.bring_to_front()),

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
    Key([mod, alt], "Space", lazy.window.toggle_floating()),

# WINDOW EFFECTS
    Key([mod, ctrl, alt], "Up", lazy.window.set_opacity(1)),
    Key([mod, alt], "Up", lazy.window.up_opacity()),

    Key([mod, alt], "Down", lazy.window.down_opacity()),
    Key([mod, ctrl, alt], "Down", lazy.window.set_opacity(0.1)),

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
    Key([mod, alt], "v", lazy.spawn("clipcatctl clear")),
]
