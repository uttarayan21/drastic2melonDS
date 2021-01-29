#!/usr/bin/python3

from math import log
import errno
import argparse
import sys
import os

sys.tracebacklimit = 0


def closest2pow(n):
    # int always returns the floor of the float
    # log(n)/log(2) gives log base 2 of n
    return 2**int(log(n) / log(2))


def drastic2melonds(infile, outfile):
    with open(infile, "rb") as inf, open(outfile, "wb") as ouf:
        in_bytes = os.stat(infile).st_size
        out_bytes = closest2pow(in_bytes)
        print(f"Reading {in_bytes} bytes from {infile}", file=sys.stderr)
        print(f"Writing {out_bytes} bytes to {outfile}", file=sys.stderr)
        ouf.write(inf.read(out_bytes))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o",
        "--output",
        help="Specify the output file")
    parser.add_argument(
        "-f",
        "--force",
        help="Overwrite the output file if it exists",
        action="store_true")  # This stores false by default unless -f is given

    parser.add_argument(
        "file", help="The drastic save file")
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(0)

    args = parser.parse_args()

    if not os.path.isfile(args.file):
        parser.print_usage()
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), args.file)

    if not args.output:
        args.output = os.path.splitext(args.file)[0] + ".sav"

    if os.path.isfile(args.output):
        if args.force:
            print(f"Overwriting file {args.output}", file=sys.stderr)
            drastic2melonds(args.file, args.output)
        else:
            print(f"Output file {args.output} already exists "
                  "pass -f/--force flag to overwrite the file", file=sys.stderr)
    else:
        drastic2melonds(args.file, args.output)


if __name__ == "__main__":
    main()
