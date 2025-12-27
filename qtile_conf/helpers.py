from libqtile.lazy import lazy

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


@lazy.function
def toggle_focus_hide(qtile):
    sp = qtile.groups_map["SPD"]
    win = qtile.current_window

    for dd in sp.dropdowns.values():
        if dd.window and dd.window == win:
            dd.on_focus_lost_hide = not dd.on_focus_lost_hide
            textEnable = "Enabled" if dd.on_focus_lost_hide else "Disabled"
            qtile.spawn(
                f"notify-send 'ScratchPad' '{dd.name.title()}: {textEnable} hide on focus lost '"
            )
            return

    qtile.spawn("notify-send 'ScratchPad' 'No active dropdown window found'")


def window_to_group(window, step, switch_group: bool = False):
    current_index = window.qtile.groups.index(window.group)
    next_index = (current_index + step) % (len(window.qtile.groups)-1)
    window.togroup(window.qtile.groups[next_index].name, switch_group=switch_group)


@lazy.function
def safe_layout_commands(qtile, *cmds):
    layout = getattr(qtile.current_group, "layout", None)
    if layout is None:
        return
    for cmd in cmds:
        fn = getattr(layout, cmd, None)
        if callable(fn):
            try:
                fn()
            except TypeError:
                try:
                    fn(qtile)
                except Exception:
                    pass


@lazy.function
def move_all_windows_to_group(qtile, to_group_name):
    dest = qtile.groups_map.get(str(to_group_name))
    if dest is None:
        qtile.spawn(f"notify-send 'Qtile' 'Target group {to_group_name} not found'")
        return

    src = qtile.current_group 
    if src is None:
        qtile.spawn(f"notify-send 'Qtile' 'Source group {from_group_name} not found'")
        return
    if src == dest:
        qtile.spawn(f"notify-send 'Qtile' 'Source and destination group are the same'")
        return

    wins = list(src.windows)
    if not wins:
        qtile.spawn(f"notify-send 'Qtile' 'No windows to move from {src.name}'")
        return

    for w in wins:
        try:
            # call the helper that moves a single window by a relative step
            w.togroup(dest.name)
            moved += 1
        except Exception:
            pass

    dest.toscreen()

@lazy.function
def to_group(qtile, group_name):
    qtile.groups_map[group_name].toscreen()

@lazy.function
def send_window_to_group(qtile, group_name):
    qtile.current_window.togroup(group_name)

@lazy.function
def change_window_to_group(qtile, group_name):
    qtile.current_window.togroup(group_name)
    qtile.groups_map[group_name].toscreen()
