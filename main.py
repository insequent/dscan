import argparse
import os

// TODO: Add dup handling
// TODO: Add size handling

def main():
    parser = argparse.ArgumentParser("Directory Scanner")
    parser.add_argument("-d", "--dups", help="Scan for duplicate folders", type=bool, default=False)
    parser.add_argument("-w", "--write", help="Filename to write results to", type=str)
    parser.add_argument("directory", metavar='dir', type=str, nargs=1)
    args = parser.parse_args()

    directory = args.directory[0]
    dirs = []
    for path, _, _ in os.walk(directory):
        root = path.split(directory)[1]
        if root != "":
            dirs.append(root)
    
    if args.write != None:
        with open(args.write, 'w') as filename:
            filename.write(os.linesep.join(dirs) + os.linesep)
    else:
        print(dirs)

if __name__ == "__main__":
    main()
