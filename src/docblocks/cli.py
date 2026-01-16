import argparse
from .core import convert

def main():
    parser = argparse.ArgumentParser(description="Exact PDF → text exporter with page headers.")
    parser.add_argument("input", help="Path to input PDF")
    parser.add_argument("output", help="Path to output text file")
    args = parser.parse_args()

    convert(args.input, args.output)
    print(f"[OK] Exported to {args.output}")
