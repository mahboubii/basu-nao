#!/bin/bash

gnome-terminal  -e "python getTime.py" &
gnome-terminal  -e "python getImage.py" &
gnome-terminal   -e "python getLaser.py" &
gnome-terminal   -e "python getSonar.py" &
gnome-terminal   -e "python getRobotPosition.py" &
