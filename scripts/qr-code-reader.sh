#!/bin/env bash

set -o pipefail

# Faz o copy do cliboard dependendo do ambiente gráfico
copy_to_clipboard () {
    if command -v wl-copy >/dev/null 2>&1 && [ -n "$WAYLAND_DISPLAY" ]; then
        wl-copy
    elif command -v xclip >/dev/null 2>&1 && [ -n "$DISPLAY" ]; then
        xclip -selection clipboard
    else
        return 1
    fi
}

# Tirar screenshot e guardar em ficheiro temporário
flameshot gui -r > /tmp/qr.png || {
    exit 1
}

# Ler o código QR
QRCODE=$(zbarimg --quiet /tmp/qr.png 2>/dev/null | sed 's/QR-Code://')

if [ -z "$QRCODE" ]; then
    notify-send "QR Code" "Nenhum código QR encontrado" -u normal
    exit 1
fi

# Perguntar ao utilizador qual ação executar com rofi
source "$HOME"/.config/rofi/applets/shared/theme.bash
theme="$type/$style"
open='🚀 Abrir (xdg-open)'
copy='📋 Copiar'
exit_action='⛔ Sair'
choice=$(echo -e "$open\n$copy\n$exit_action" | \
    rofi -theme-str "listview {columns: 1; lines: 3;}" \
        -theme-str 'textbox-prompt-colon {str: "⚠️";}' \
        -dmenu -no-click-to-exit \
        -p "Ação" \
        -mesg "$QRCODE" \
        -markup-rows \
        -theme ${theme})

case ${choice} in
    "$open")
        # tenta abrir e em caso de falha copia para clipboard
        echo "$QRCODE" | xargs xdg-open 2>/dev/null || {
            notify-send "QR Code" "Falha ao abrir; resultado copiado para clipboard: $QRCODE" -u normal
            echo -n "$QRCODE" | copy_to_clipboard
            exit 1
        }
        notify-send --app-name "QRCode Reader" "QR Code" "Abrindo: $QRCODE" -u normal
        ;;
    "$copy")
        # apenas copia para clipboard (já está copiado mas reafirma)
        echo -n "$QRCODE" | copy_to_clipboard
        notify-send --app-name "QRCode Reader" "QR Code" "Copiado para clipboard: $QRCODE" -u normal
        ;;
    *)
    notify-send --app-name "QRCode Reader" "QR Code" "Ação não executada." -u normal
        ;;
esac