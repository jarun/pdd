#!/usr/bin/env python3

'''
pdd test script

Author: Arun Prakash Jana
Email : engineerarun@gmail.com
Home  : https://github.com/jarun/pdd

NOTES:

1. Before raising a PR,
   a. add relevant test cases
   b. run `python3 -m pytest test.py
'''
import pytest
import subprocess

test = [
    ('./pdd', '-d', '1983', 'jul', '3', '2014', '1', '15'),               # 1
    ('./pdd', '-d', '2014', '1', '15', '1983', 'jul', '03'),              # 2
    ('./pdd', '-t', '45:50', '6:17:33'),                                  # 3
    ('./pdd', '-t', '6:17:33', '45:50'),                                  # 4
    ('./pdd', '-t', '5:80:75', '6:17:33'),                                # 5
    ('./pdd', '-t', '6:17:33', '5:80:75'),                                # 6
    ('./pdd', '-d', '2000', 'FEB', '28', '3', '2', '1', '--add'),         # 7
    ('./pdd', '-d', '2000', 'FEB', '28', '1', '2', '3', '--add'),         # 8
    ('./pdd', '-t', '47:71:37', '1:2:63', '--add'),                       # 9
    ('./pdd', '-d', '2000', 'Mar', '01', '0', '0', '1', '--sub'),         # 10
    ('./pdd', '-d', '2000', 'Mar', '1', '1', '1', '1', '--sub'),          # 11
    ('./pdd', '-t', '00:00:00', '0:0:1', '--sub'),                        # 12
    ('./pdd', '-t', '25:61:61', '0:0:0', '--sub'),                        # 13
    ('./pdd', '-t', '0:0:0', '1:1:1', '--sub'),                           # 14
    ('./pdd', '-t', '0:0:0', '25:61:61', '--sub'),                        # 15
]

res = [
    b'30y 6m 12d\n11154d\n',                                              # 1
    b'30y 6m 12d\n11154d\n',                                              # 2
    b'05:31:43\n19903s\n',                                                # 3
    b'05:31:43\n19903s\n',                                                # 4
    b'00:03:42\n222s\n',                                                  # 5
    b'00:03:42\n222s\n',                                                  # 6
    b'Tue 2003 Apr 29\n',                                                 # 7
    b'Tue 2001 May 01\n',                                                 # 8
    b'2 day(s) later, 01:14:40\n177280s\n',                               # 9
    b'Tue 2000 Feb 29\n',                                                 # 10
    b'Sun 1999 Jan 31\n',                                                 # 11
    b'1 day(s) earlier, 23:59:59\n-1s\n',                                 # 12
    b'02:02:01\n93721s\n',                                                # 13
    b'1 day(s) earlier, 22:58:59\n-3661s\n',                              # 14
    b'2 day(s) earlier, 21:57:59\n-93721s\n',                             # 15
]


@pytest.mark.parametrize('item, res', zip(test, res))
def test_output(item, res):
    try:
        out = subprocess.check_output(item, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        # print(e.output)
        assert e.output == res
    else:
        assert out == res
