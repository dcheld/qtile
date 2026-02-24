#!/usr/bin/env bash
## Based on Arcolinux scritp: https://github.com/arcolinux/arcolinux-qtile/blob/master/etc/skel/.config/qtile/scripts/autostart.sh

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

pkill -SIGHUP redshift

# Only run on Xorg, not on Wayland
if [[ "$XDG_SESSION_TYPE" == "x11" ]]; then
  # run volctl &
  run picom &
  run urxvtd -q -f -o &
  run xfce4-power-manager &
else
  run foot --server &
fi

#starting utility applications at boot time
run nm-applet &
run blueman-applet &
run dunst &
run redshift &
run xss-lock --ignore-sleep -- xscreensaver-command -lock &
run xscreensaver --no-splash &
run clipcatd &
run /usr/bin/lxpolkit &
