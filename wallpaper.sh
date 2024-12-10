#!/bin/bash

if [ "$1" == "-h" ]; then
  echo "Uses feh to loop through wallpapers in i3 folder"
  echo "Usage: wallpaper.sh [delay]"
  exit 1
fi

delay=${1-60}
while true; do
for wallpaper in ~/.config/regolith/i3/wallpapers/*; do
  feh --bg-center "$wallpaper"
  echo "change wallpaper $wallpaper" >> /tmp/wallpaper.log
  sleep $delay 
done
done
