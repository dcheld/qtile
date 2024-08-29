#!/usr/bin/env zsh

zinit light-mode lucid wait'1' for \
        as"completion" blockf \
        atpull"zinit creinstall -q ." \
    archlinux/pacman-contrib
