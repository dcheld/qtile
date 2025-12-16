import os
# import socket
from libqtile import qtile

# Alternativas úteis (mantidas como comentário):
# from libqtile.utils import guess_terminal
# from libqtile.extension import dmenu
# from libqtile.log_utils import logger

mod = "mod4"
alt = "mod1"
ctrl = "control"
shift = "shift"
home = os.path.expanduser("~")

if qtile.core.name == "x11":
    term = "urxvt -e"
elif qtile.core.name == "wayland":
    term = "foot"

terminal = "alacritty"
rofi_power_menu_cmd = f"{home}/.config/rofi/applets/bin/powermenu.sh"
applicationLaunch = f"{home}/.config/rofi/launchers/type-3/launcher.sh"
applicationQuickLaunch = f"{home}/.config/rofi/launchers/type-2/launcher.sh"
calendar = 'khal interactive'
fileManager = "nemo"
processManager = "gnome-system-monitor"
# musicPlayer = "flatpak run com.spotify.Client"
musicPlayer = f"""google-chrome-stable --app="http://music.youtube.com/" --class=WebApp-YT7567 --name=WebApp-YT7567 --user-data-dir={home}/.local/share/ice/profiles/YoutubeMusic"""
# outra opção: "youtube-music"
# browser = "google-chrome-stable"
browser = "google-chrome-stable"
sensors = "watch -n 1 sensors"
ide = "code"
screenshot = "flameshot gui"
clipboard = "clipcat-menu"
whats_app_launch = f"""google-chrome-stable --app="https://web.whatsapp.com/" --class=WebApp-WhatsApp3698 --user-data-dir={home}/.local/share/ice/profiles/WhatsApp"""
# antiga alternativa para LLM (Gemini):
# llm_app_launch = f"""google-chrome-stable --app="https://gemini.google.com/app" --class=WebApp-httpschatgptcomcabafdbbaee3102 --name=Gemini --user-data-dir={home}/.local/share/ice/profiles/Gemini"""
llm_app_launch = f"""google-chrome-stable --app="https://chatgpt.com/" --class=WebApp-httpschatgptcomcabafdbbaee3102 --name=ChatGPT --user-data-dir={home}/.local/share/ice/profiles/ChatGPT"""
volume_up = "amixer set Master 1%+ unmute"
volume_down = "amixer set Master 2%- unmute"

def console_launcher(app):
    return f"{term} {app}"
