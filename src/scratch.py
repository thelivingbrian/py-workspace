import sys
import lc.lc22_generate_parens as lc

def args():
    # sys.argv[0] is the script name; the rest are the passed-in args
    args = sys.argv[1:]
    print(f"Got {len(args)} args:", args)
    return args

if __name__ == "__main__":
    args = args()
    input = int(args[0]) if args else 1
    lc.run(input)