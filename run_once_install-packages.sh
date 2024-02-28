#!/usr/bin/env bash

# install yay
sudo pacman -S --needed --noconfirm  git base-devel
git clone https://aur.archlinux.org/yay.git /tmp/yay
cd /tmp/yay
makepkg -si
cd -

sudo pacman -R --noconfirm vim

yay -S --noconfirm \
    polkit rxvt-unicode xsensors \
    xss-lock xscreensaver redshift \
    nemo nemo-seahorse clipmenu volctl blueman-applet xfce4-power-manager rofi \
    podman podman-docker \
    gvim ttf-meslo-nerd

