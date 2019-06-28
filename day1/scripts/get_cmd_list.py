#!/usr/bin/python

import sys
import re
import os
import datetime

c_l = "cmd_list"

cmd_part = str(sys.argv[1])

for line in cmd_part:
	print(line)