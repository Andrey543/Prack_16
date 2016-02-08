import os
import sys

for arg in sys.argv:
	if arg!='3.py':
		a=open(arg,'r')
		print('\n'.join(a.readlines()))
