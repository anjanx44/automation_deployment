#!/usr/bin/python

import sys
import re
import os
import datetime

s_r = "src_root"
d_r = "dest_root"

d_r_path = ""

c_l = "cmd_list"

with open('input.txt') as f:
	for line in f:
		if d_r in line: 
			d_r_path = line.replace("dest_root:","").strip('\n')

with open('input.txt') as f:
	for line in f:
		if c_l in line:
			break
		if s_r in line or d_r in line or line == "":
			continue	
		print d_r_path + line
