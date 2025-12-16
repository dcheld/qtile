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
            qtile.cmd_spawn(
                f"notify-send 'ScratchPad' '{dd.name}: on_focus_lost_hide = {dd.on_focus_lost_hide}'"
            )
            return

    qtile.cmd_spawn("notify-send 'ScratchPad' 'No active dropdown window found'")


def window_to_group(window, step, switch_group: bool = False):
    current_index = window.qtile.groups.index(window.group)
    next_index = (current_index + step) % (len(window.qtile.groups)-1)
    window.togroup(window.qtile.groups[next_index].name, switch_group=switch_group)
