#!/usr/bin/env python3

import argparse
import sys
import re

class PowerStrip():

    def __init__(self, filename):
        self.filename = filename 
        try:
            dirname = os.path.dirname(filename)
            basename = os.path.basename(filename)
            rootname, ext = basename.split('.')
        except:
            print('Please specify a PowerShell script with .ps1 extension')
            sys.exit(1)
        self.outputfile = '{}-stripped.{}'.format(rootname, ext)
        self.run()

    def run(self):
        print('[*] Reading Input file ...: {}'.format(self.filename))
        infile = open(self.filename, 'rt')
        self.contents = infile.readlines()
        infile.close()
        self.strip_comments()
        print('[*] Writing Output file ..: {}'.format(self.outputfile))
        outfile = open(self.outputfile, 'wt')
        outfile.writelines(self.results)
        outfile.close()

    def strip_comments(self):
        self.results = []
        skip = False
        for line in self.contents:
            if line.startswith('<#'):
                skip = True
                continue
            elif line.startswith('#>'):
                skip = False
                continue
            elif line.startswith('#'):
                continue
            if not skip:
                self.results.append(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    ps = PowerStrip(args.filename)
