from libqtile.config import Group, ScratchPad, DropDown
from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile import extension

from .settings import (
    terminal,
    console_launcher,
    musicPlayer,
    calendar,
    whats_app_launch,
    llm_app_launch,
    home,
    sensors,
    mod,
    ctrl,
    shift,
    alt,
)

from .helpers import (
    to_group,
    send_window_to_group,
    change_window_to_group,
    move_all_windows_to_group,
)

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# FOR AZERTY KEYBOARDS (alternativa comentada)
# group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave"]

# alternativas de rótulos/icones
# group_labels = ["", "", "", "", "", "", "", "", "", ""]

# layouts sugeridos por grupo (comentado)
# group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

def add_scratchpad(groups):
    height = 0.4650
    y_position = 0.005
    warp_pointer = False
    on_focus_lost_hide = True
    opacity = 1

    groups.append(
        ScratchPad("SPD",
            [
                DropDown("terminal",
                    terminal + " -o window.opacity=0.9",
                    y=y_position,
                    height=height,
                    on_focus_lost_hide=on_focus_lost_hide,
                    warp_pointer=warp_pointer,
                    opacity=opacity),
                DropDown("qshell",
                    terminal + " -o window.opacity=0.8 -e qtile shell",
                    y=y_position,
                    on_focus_lost_hide=on_focus_lost_hide,
                    warp_pointer=warp_pointer,
                    opacity=opacity),
                DropDown("sensors",
                    console_launcher(sensors) if 'sensors' in globals() else console_launcher('sensors'),
                    y=y_position,
                    x=0.6,
                    height=0.85,
                    width=0.4,
                    on_focus_lost_hide=False,
                    warp_pointer=warp_pointer,
                    opacity=opacity),
                DropDown("media-play",
                    musicPlayer,
                    y=y_position,
                    x=0.15,
                    height=0.65,
                    width=0.7,
                    warp_pointer=warp_pointer,
                    opacity=opacity),
                DropDown("bitwarden",
                    "bitwarden-desktop",
                    y=y_position,
                    x=0.15,
                    height=0.65,
                    width=0.7,
                    warp_pointer=warp_pointer,
                    opacity=opacity),
                DropDown("llm_app_launch",
                    llm_app_launch,
                    y=y_position,
                    x=0.15,
                    height=0.7,
                    width=0.7,
                    warp_pointer=warp_pointer,
                    opacity=opacity),
                DropDown("calendar",
                    console_launcher(calendar),
                    y=y_position,
                    x=0.7,
                    width=0.3,
                    on_focus_lost_hide=False,
                    opacity=opacity),
                DropDown("whatsapp",
                    whats_app_launch,
                    y=y_position,
                    x=0.15,
                    width=0.7,
                    height=0.7,
                    on_focus_lost_hide=on_focus_lost_hide,
                    warp_pointer=warp_pointer,
                    opacity=opacity),
            ],
        ),
    )


def get_groups_and_keys():
    groups = []

    # ensure numeric groups exist
    for i in range(len(group_names)):
        group = Group(name=group_names[i], label=group_labels[i])
        groups.append(group)

    group_keys = []
    for g in groups:
        group_keys.extend([
            Key([mod], g.name, to_group(g.name), desc=f"Switch to group {g.name}"),
            Key([mod, shift], g.name, send_window_to_group(g.name), desc=f"Move window to group {g.name}"),
            Key([mod, ctrl], g.name, change_window_to_group(g.name), desc=f"Move window to group {g.name} and switch"),
            Key([mod, ctrl, shift], g.name, move_all_windows_to_group(g.name), desc=f"Move all windows to group {g.name}"),
        ])

    add_scratchpad(groups)

    return groups, group_keys
