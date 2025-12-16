import subprocess
from libqtile import hook
from .settings import home

@hook.subscribe.startup_once
def start_once():
    subprocess.Popen([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.resume
def resume():
    subprocess.Popen(['picom','-b'])
