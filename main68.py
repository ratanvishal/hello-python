import argparse
import sys
def calc(args):
    if  args.o == 'a':
        return args.x + args.y
    elif args.o == 's':
        return args.x - args.y
    elif args.o == 'm':
        return args.x * args.y
    elif args.o == 'd':
        return args.x / args.y
    else:
        return "there is problem in calculation, contact vishal now"
if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,help="Enter the first number, this is the utility fot calculation.please contact vishal")
    parser.add_argument('--y',type=float,default=1.0,help="Enter the second number,this is a calcaluation.please contact vishal")
    parser.add_argument('--o',type=str,default="a",help="This is the calculation, for more update contact vishal")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
