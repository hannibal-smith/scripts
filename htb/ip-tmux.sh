#!/bin/bash

tmux rename-window -t 0 $(ip= ifconfig | grep "inet 10.10." | cut -d "." -f 3-4 | cut -d " " -f 1)
