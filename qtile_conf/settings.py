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
is_wayland = qtile.core.name == "wayland"

if is_wayland:
    term = "foot"
else:
    term = "urxvt -e"


googleProfile=f"{home}/.local/share/ice/profiles/google"
whatsappProfile=f"{home}/.local/share/ice/profiles/whatsapp"

terminal = "alacritty"
rofi_power_menu_cmd = f"{home}/.config/rofi/applets/bin/powermenu.sh"
applicationLaunch = f"{home}/.config/rofi/launchers/type-3/launcher.sh"
applicationQuickLaunch = f"{home}/.config/rofi/launchers/type-2/launcher.sh"
calendar = 'khal interactive'
fileManager = "nemo"
processManager = "gnome-system-monitor"
# musicPlayer = "flatpak run com.spotify.Client"
musicPlayer = f"""google-chrome-stable --app="http://music.youtube.com/" --class=WebApp-YT7567 --name=WebApp-YT7567 --user-data-dir={home}/.local/share/ice/profiles/music"""
# outra opção: "youtube-music"
# browser = "google-chrome-stable"
browser = "google-chrome-stable"
sensors = "watch -n 1 sensors"
ide = "code"

screenshot = "flameshot gui"
# screenshot = "flatpak run org.flameshot.Flameshot gui"
os.environ["DEFAULT_SCREENSHOT_COMMAND"] = screenshot

clipboard = "clipcat-menu"
whats_app_launch = f"""google-chrome-stable --app="https://web.whatsapp.com/" --class=WebApp-WhatsApp3698 --user-data-dir={whatsappProfile}"""
llm_gemini = f"""google-chrome-stable --app="https://gemini.google.com/app" --class=WebApp-Gemini --name=Gemini --user-data-dir={googleProfile}"""
llm_chatgpt = f"""google-chrome-stable --app="https://chatgpt.com/" --class=WebApp-ChatGPT --name=ChatGPT --user-data-dir={googleProfile}"""
llm_claude = f"""google-chrome-stable --app="https://claude.ai/new" --class=WebApp-Claude --name=Claude --user-data-dir={googleProfile}"""
volume_up = "amixer set Master 1%+ unmute"
volume_down = "amixer set Master 2%- unmute"

def console_launcher(app):
    return f"{term} {app}"
