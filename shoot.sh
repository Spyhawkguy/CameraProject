#!/bin/bash

pids=$(pgrep rpicam-still)
kill $pids

output_dir="/home/pi/CameraProject/RAW"
today=$( date +%Y%m%d )
number=0
fname="$today.dng"

while [ -e "$output_dir/$fname" ]; do
    printf -v fname '%s-%02d.dng' "$today" "$(( ++number ))"
done

rpicam-still --raw --output "$output_dir/$fname" -t 0.5 -n
