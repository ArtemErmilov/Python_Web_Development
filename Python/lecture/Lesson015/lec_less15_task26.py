import argparse

parser = argparse.ArgumentParser(prog='average', description='My first argument parser',
                                    epilog='Returns the arithmetic mean')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

# python .\lec_less15_task26.py --help