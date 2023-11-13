import argparse
parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

# python .\lec_less15_task25.py 42 3.14 73
# python .\lec_less15_task25.py --help
# python .\lec_less15_task25.py Hello world!