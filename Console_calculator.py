import argparse
import sys

parser=argparse.ArgumentParser(
	description='Console Calculator'
)

parser.add_argument(
	'values',
	metavar='VALUES',
	type=float,
	nargs='+',
	help='inputed value',
)

parser.add_argument(
'-a',
'--action',
action='store',
help='Operation for calculating',
)

parser.add_argument(
'-v',
'--verbose',
action='store_true',
help='pretty output',
)
print(sys.argv)
args=parser.parse_args()
if not args.action:
	print(
	'You should use parametr action',
	)
	sys.exit(-1)
	
value=args.values

result=None

if args.action=='+':
	for x in value:
		if result==None:
			result=x
		else:
			result+=x
			
if args.action=='-':
	for x in value:
		if result==None:
			result=x
		else:
			result-=x
			
if args.action=='*':
	for x in value:
		if result==None:
			result=x
		else:
			result*=x		
	
if args.action=='/':
	for x in value:
		if result==None:
			result=x
		else:
			result/=x
			
if args.verbose:
	for x in value:
		print(x,'+',sep=='')
	print('=',result,sep=='')
else:
	print(result)
	
		

