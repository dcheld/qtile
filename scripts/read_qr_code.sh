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

# Tentar abrir com xdg-open
echo "$QRCODE" | xargs xdg-open 2>/dev/null || {
    notify-send "QR Code" "Resultado copiado para clipboard: $QRCODE" -u normal
    echo -n "$QRCODE" | copy_to_clipboard
    exit 1
}

notify-send "QR Code" "Resultado: $QRCODE" -u low