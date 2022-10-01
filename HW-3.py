import argparse
parser = argparse.ArgumentParser(description='Сounting the number of multiples of the number "factor"')
parser.add_argument('a', type=int, help='Input lower interval number for calculate numbers range')
parser.add_argument('b', type=int, help='Input Upper interval number for calculate numbers range')
parser.add_argument('factor', type=int, help='the multiplicity number the number of times a given polynomial has a root at a given point is the multiplicity of that root')
args = parser.parse_args()

def count_multiples(a, b, factor):
    if a > b:
        a,b = b,a
    return len(list(filter(lambda x: x%factor == 0, range(a,b+1))))

print(count_multiples(args.a, args.b, args.factor))
