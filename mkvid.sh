#! /usr/bin/env bash

ffmpeg -framerate 32 -i output/img%03d.png -c:v libx264 -r 32 marked.mp4
