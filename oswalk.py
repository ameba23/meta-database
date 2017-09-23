#!/usr/bin/python3

import os

for root, dirs, files in os.walk("templates"):
    for name in files:
        print(name)
