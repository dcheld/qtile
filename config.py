from qtile_conf import settings, helpers, groups_mod, keys_mod
from qtile_conf import widgets as widgets_mod, layouts_screens as ls_mod
from qtile_conf import mouse_conf, floating_conf, hooks

# Groups (retorna grupos e bindings específicos de grupo)
groups, group_keys = groups_mod.get_groups_and_keys()

# Keys: combina bindings principais com os bindings de grupo
keys = keys_mod.keys + group_keys

# Layouts, widgets, screens, mouse, floating layout
layouts = ls_mod.layouts
widget_defaults = widgets_mod.widget_defaults
extension_defaults = widgets_mod.extension_defaults
screens = ls_mod.init_screens()
mouse = mouse_conf.mouse
floating_layout = floating_conf.floating_layout

# Misc / defaults (copiados do config original)
dgroups_app_rules = []  # type: list
dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "qTile"