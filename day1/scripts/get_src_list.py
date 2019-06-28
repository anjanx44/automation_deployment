#!/usr/bin/python

import sys
import re
import os
import datetime

s_r = "src_root"
d_r = "dest_root"

s_r_line = ""

c_l = "cmd_list"

with open('input.txt') as f:
	for line in f:
		if s_r in line: 
			s_r_line = line.replace("src_root:","").strip('\n')

with open('input.txt') as f:
	for line in f:
		if c_l in line:
			break
		if s_r in line or d_r in line or line == "":
			continue	
		print s_r_line + line
