#!/usr/bin/env bash
## Based on Arcolinux scritp: https://github.com/arcolinux/arcolinux-qtile/blob/master/etc/skel/.config/qtile/scripts/autostart.sh

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

pkill -SIGHUP redshift

#starting utility applications at boot time
run urxvtd -q -f -o &
run picom &
run nm-applet &
run volctl &
run blueman-applet &
run xfce4-power-manager &
run redshift &
run xss-lock --ignore-sleep -- xscreensaver-command -lock &
run xscreensaver --no-splash &
run clipmenud &
run /usr/bin/lxpolkit &
