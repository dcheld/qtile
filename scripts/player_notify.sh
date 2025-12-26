#!/bin/sh
# Simple wrapper to run playerctl actions and send a notification with metadata
action="$1"
playerctl_cmd="playerctl"
notify_cmd="notify-send"

case "$action" in
  play-pause|pause|play)
    "$playerctl_cmd" play-pause 2>/dev/null
    ;;
  next)
    "$playerctl_cmd" next 2>/dev/null
    ;;
  previous)
    "$playerctl_cmd" previous 2>/dev/null
    ;;
  *)
    "$playerctl_cmd" "$action" 2>/dev/null
    ;;
esac

sleep 0.2
status=$("$playerctl_cmd" status 2>/dev/null || true)
if [ -z "$status" ]; then
  "$notify_cmd" "Media Player" "No media player detected"
  exit 0
fi

# If status is 'Stopped', retry a few times to see if it changes (handle transient states)
attempts=0
while [ "$status" = "Stopped" ] && [ $attempts -lt 3 ]; do
  sleep 0.2
  status=$("$playerctl_cmd" status 2>/dev/null || true)
  attempts=$((attempts + 1))
  if [ -z "$status" ]; then
    "$notify_cmd" "Media Player" "No media player detected"
    exit 0
  fi
done

metadata=$("$playerctl_cmd" metadata --format "{{artist}} - {{title}}" 2>/dev/null || true)
if [ -z "$metadata" ] || [ "$metadata" = " - " ]; then
  metadata=$("$playerctl_cmd" metadata --format "{{title}}" 2>/dev/null || true)
fi

case "$status" in
  Playing)
    "$notify_cmd" "Playing" "$metadata"
    ;;
  Paused)
    "$notify_cmd" "Paused" "$metadata"
    ;;
  *)
    "$notify_cmd" "$status" "$metadata"
    ;;
esac
