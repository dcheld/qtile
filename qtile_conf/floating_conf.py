from libqtile import layout
from libqtile.config import Match
from .settings import processManager

# Run the utility of `xprop` to see the wm class and name of an X client.
# Use these rules to catch common dialogs and helpers.
floating_layout = layout.Floating(
    float_rules=[
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
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="gnome-calculator"),
        Match(wm_class="gnome-calendar"),
        Match(wm_class="kcalc"),
        Match(wm_class="Emulator"),
        Match(wm_class=processManager),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(role="pop-up"),
    ]
)
