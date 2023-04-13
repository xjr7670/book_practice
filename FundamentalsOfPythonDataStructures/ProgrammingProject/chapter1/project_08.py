# -*- coding:utf-8 -*-

import sys


def main():
    file_name = input('please input a file name: ')
    with open(file_name, encoding='utf-8') as r:
        lines = r.readlines()
    length = len(lines)
    print('this file have total %d line.' % length)

    line_no = int(input('please input a line number: '))
    if line_no == 0 or line_no > length:
        sys.exit()
    else:
        print('the %d line of %s is:\n' % (line_no, file_name))
        print(lines[line_no-1])


if __name__ == "__main__":
    main()