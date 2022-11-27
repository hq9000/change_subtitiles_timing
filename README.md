# Script for moving the timing of subtitles

## Purpose

I had a movie and a subtitles file in `srt` format. The movie was a bit out of sync so I decided to write a simple python script to adjust the subtitiles.

Works on Python 3.8+, does not have any dependencies.

## Usage

`python change_subtitle_timing.py --source_file source.srt --target_file target.srt --time_shift_seconds -0.8`