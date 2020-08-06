# supported extensions: *.xlsx

import pandas as pd
import numpy as np
import argparse


def start(args):

    src = args.s
    dst = args.d

    src_files = open_src_files(src)
    dst_files = open_dst_files(dst)

    merge_files(src_files, dst_files)


def open_src_files(src):
    f = pd.read_excel(src)
    return f

def open_dst_files(dst):
    f = pd.read_excel(dst)
    return f

def merge_files(src, dst):
    result = pd.concat([src, dst])
    result.to_excel("./files/c.xlsx")


if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='Plz input')

    parser.add_argument('-s', required=False, help='-s a.xlsx', default='./files/a.xlsx')
    parser.add_argument('-d', required=False, help='-d b.xlsx', default='./files/b.xlsx')

    args = parser.parse_args()

    start(args)