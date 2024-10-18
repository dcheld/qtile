# Template
typeset -aU path

export SSH_AUTH_SOCK=$XDG_RUNTIME_DIR/gcr/ssh
export CM_LAUNCHER=rofi
export GTK_THEME=Adwaita:dark
export DOTNET_ROOT="$HOME/.dotnet"

path=($path "$HOME/.local/share/JetBrains/Toolbox/scripts")
path=($path "$DOTNET_ROOT")
path=($path "$DOTNET_ROOT/tools")

export PATH
