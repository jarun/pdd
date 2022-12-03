#!/usr/bin/env python3
#
# Date, time difference calculator with a stopwatch and countdown timer.
#
# Copyright © 2017 Arun Prakash Jana <engineerarun@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import calendar as cal
from datetime import date
from datetime import datetime
import os
import shlex
import subprocess
import sys
import time
from dateutil.relativedelta import relativedelta

if os.name == 'nt':
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

# Global variables

monthdict = {name.lower(): num
             for num, name in enumerate(cal.month_abbr) if num}
_VERSION_ = '1.7'  # current program version


def is_int(arg):
    '''Check if arg is a digit

    :param arg: input string
    :return: True on success, False on exception
    '''

    try:
        int(arg)
        return True
    except Exception:
        return False


def getdate(lst):
    '''Return a date from list in yyyy mmm dd format'''

    return date(int(lst[0]), int(lst[1]) if is_int(lst[1]) else monthdict[lst[1].lower()], int(lst[2]))


def getreldate(lst):
    '''Return a relative calendar duration from list in yyyy mmm dd format'''

    return relativedelta(years=int(lst[0]), months=int(lst[1]), days=int(lst[2]))


def showdatediff(d0, d1):
    '''Show absolute difference between two dates'''

    if d0 < d1:
        d0, d1 = d1, d0

    delta = d0 - d1
    rdelta = relativedelta(d0, d1)
    print('%dy %dm %dd' % (rdelta.years, rdelta.months, rdelta.days))
    print('%dd' % delta.days)


def gethms(h, m, s):
    '''Convert empty string to 0 and return hour, min, sec'''

    if h == '':
        h = 0
    if m == '':
        m = 0
    if s == '':
        s = 0

    return int(h), int(m), int(s)


def gettime(arg):
    '''Parse and return hour, min, sec'''

    lst = arg.split(':')
    n = len(lst)

    if n == 3:
        return lst[0], lst[1], lst[2]
    if n == 2:
        return 0, lst[0], lst[1]
    if n == 1:
        return 0, 0, lst[0]

    return None, None, None


def validdata(h, m, s):
    '''Run validity check on input'''

    if h < 0 or m < 0 or s < 0:
        return False

    return True


def validargs(h, m, s):
    '''Run validity check on input'''

    if int(h) < 0 or int(m) < 0 or int(s) < 0:
        return False

    return True


def showtimediff(t0, t1):
    '''Show absolute difference between two timestamps'''

    m, s = divmod(abs(t0 - t1), 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    if d > 0:
        print('day %d, %02d:%02d:%02d' % (d, h, m, s))
    else:
        print('%02d:%02d:%02d' % (h, m, s))

    print('%ds' % abs(t0 - t1))


def showtimesum(t0, t1):
    '''Show sum of a timestamp and a timeslice'''

    m, s = divmod(t0 + t1, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    if d > 0:
        print('%d day(s) later, %02d:%02d:%02d' % (d, h, m, s))
    else:
        print('%02d:%02d:%02d' % (h, m, s))

    print('%ds' % (t0 + t1))


def showtimesub(t0, t1):
    '''Subtract and show timeslice from timestamp'''

    m, s = divmod(t0 - t1, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    if d < 0:
        print('%d day(s) earlier, %02d:%02d:%02d' % (abs(d), h, m, s))
    else:
        print('%02d:%02d:%02d' % (h, m, s))

    print('%ds' % (t0 - t1))


def showdate():
    t = time.localtime()

    if os.name == 'nt' and sys.version_info < (3, 6):
        # No tm_zone in Python < v3.6 on Windows
        print('%s %02d %s %d %02d:%02d:%02d' % (
            cal.day_abbr[t.tm_wday],
            t.tm_year, cal.month_abbr[t.tm_mon], t.tm_mday,
            t.tm_hour, t.tm_min, t.tm_sec))
    else:
        print('%s %02d %s %d %02d:%02d:%02d %s' % (
            cal.day_abbr[t.tm_wday],
            t.tm_year, cal.month_abbr[t.tm_mon], t.tm_mday,
            t.tm_hour, t.tm_min, t.tm_sec, t.tm_zone))


def cursor_off():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif sys.platform == 'darwin':
        os.system('tput civis')
    else:
        os.system('setterm -cursor off')


def cursor_on():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif sys.platform == 'darwin':
        os.system('tput cnorm')
    else:
        os.system('setterm -cursor on')


def calc_date(args):
    d0 = getdate(args.date[:3])

    if args.add:
        if not validargs(args.date[3], args.date[4], args.date[5]):
            raise ValueError('negative value')

        d0 += getreldate(args.date[3:])
        print('%s %04d %s %02d' % (
            cal.day_abbr[d0.weekday()], d0.year, cal.month_abbr[d0.month], d0.day))
    elif args.sub:
        if not validargs(args.date[3], args.date[4], args.date[5]):
            raise ValueError('negative value')

        d0 -= getreldate(args.date[3:])
        print('%s %04d %s %02d' % (
            cal.day_abbr[d0.weekday()], d0.year, cal.month_abbr[d0.month], d0.day))
    else:
        d1 = getdate(args.date[3:])
        showdatediff(d0, d1)


def calc_time(args):
    h, m, s = gettime(args.time[0])
    h, m, s = gethms(h, m, s)
    if not validdata(h, m, s):
        raise ValueError('negative value')
    t0 = h * 3600 + m * 60 + s

    h, m, s = gettime(args.time[1])
    h, m, s = gethms(h, m, s)
    if not validdata(h, m, s):
        raise ValueError('negative value')
    t1 = h * 3600 + m * 60 + s

    if args.add:
        showtimesum(t0, t1)
    elif args.sub:
        showtimesub(t0, t1)
    else:
        showtimediff(t0, t1)


def show_day(day):
    d = getdate(day)
    print('%s' % cal.day_abbr[d.weekday()])


def calc_misc(args):
    if len(args.keywords) == 3:
        # Show date diff from today
        today = datetime.now().date()

        if args.add:
            if not validargs(args.keywords[0], args.keywords[1],
                             args.keywords[1]):
                raise ValueError('negative value')

            today += getreldate(args.keywords)
            print('%s %04d %s %02d' % (
                cal.day_abbr[today.weekday()], today.year, cal.month_abbr[today.month], today.day))
        elif args.sub:
            if not validargs(args.keywords[0], args.keywords[1], args.keywords[2]):
                raise ValueError('negative value')

            today -= getreldate(args.keywords)
            print('%s %04d %s %02d' % (
                cal.day_abbr[today.weekday()], today.year, cal.month_abbr[today.month], today.day))
        else:
            d0 = getdate(args.keywords)
            showdatediff(today, d0)
    elif len(args.keywords) == 1:
        # Show time diff from now
        h, m, s = gettime(args.keywords[0])
        h, m, s = gethms(h, m, s)
        if not validdata(h, m, s):
            raise ValueError('negative value')
        t0 = h * 3600 + m * 60 + s

        now = datetime.now().time()
        secs = now.hour * 3600 + now.minute * 60 + now.second

        if args.add:
            showtimesum(t0, secs)
        elif args.sub:
            showtimesub(secs, t0)
        else:
            showtimediff(t0, secs)
    else:
        print('keywords can be [yyyy mmm dd] OR [hh:mm:ss]')


def run_countdown_timer(args):
    h, m, s = gettime(args.timer[0])
    h, m, s = gethms(h, m, s)
    if not validdata(h, m, s):
        raise ValueError('negative value')

    if args.quiet is False:
        cursor_off()

    try:
        while True:
            if args.quiet is False:
                print('\r\x1b[7m{0:02d}h {1:02d}m {2:02d}s\x1b[0m'.format(h, m, s), end='')
            s = s - 1
            if s == -1:
                s = 59
                m = m - 1
                if m == -1:
                    m = 59
                    h = h - 1
                    if h == -1:
                        h = m = s = 0
                        break
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        print('\r\x1b[7m{0:02d}h {1:02d}m {2:02d}s\x1b[0m  '.format(h, m, s), end='\b\b\n', flush=True)
        print('stop: ', end='')
        showdate()
        if args.quiet is False:
            cursor_on()
        if args.run and h == 0 and m == 0 and s == 0:
            # subprocess.call(''.join(args.run).split())
            subprocess.call(shlex.split(''.join(args.run)))


def run_stopwatch(args):
    print('start: ', end='')
    showdate()

    n = args.stopwatch
    res = 10 ** (-n)
    t0 = time.time()
    # os.system('clear')
    if args.quiet is False:
        cursor_off()

    try:
        while True:
            t1 = time.time()
            if args.quiet is False:
                print('\r\x1b[7m{1:.{0}f}s\x1b[0m'.format(n, t1 - t0), end='')
            time.sleep(res)
    except KeyboardInterrupt:
        print('\r\x1b[7m{1:.{0}f}s\x1b[0m  '.format(n, t1 - t0), end='\b\b\n', flush=True)
    finally:
        if args.quiet is False:
            cursor_on()


class ExtendedArgumentParser(argparse.ArgumentParser):
    '''Extend classic argument parser'''

    # Print additional help and info
    @staticmethod
    def print_extended_help(file=None):
        if not file:
            file = sys.stderr

        file.write('''
Version %s
Copyright © 2017 Arun Prakash Jana <engineerarun@gmail.com>
License: GPLv3
Webpage: https://github.com/jarun/pdd
''' % _VERSION_)

    # Help
    def print_help(self, file=None):
        super().print_help(file)
        self.print_extended_help(file)


def get_parser():
    '''Get parser.
    Returns
    -------
    argparse.ArgumentParser
        Parser with arguments / options.
    '''

    argparser = ExtendedArgumentParser(
        description='Tiny date, time difference calculator with timers.')
    addarg = argparser.add_argument
    addarg('-d', '--date', dest='date', nargs=6,
           metavar=('yyyy', 'mmm', 'dd', '[yyyy', 'mmm', 'dd | y m d]'),
           help='calculate date difference')
    addarg('-t', '--time', dest='time', nargs=2,
           metavar=('hh:mm:ss', '[hh:mm:ss | h:m:s]'),
           help='calculate time difference')
    addarg('--add', action='store_true',
           help='add to date (/today) or time (/now)')
    addarg('--sub', action='store_true',
           help='subtract from date (/today) or time (/now)')
    addarg('--day', nargs=3, metavar=('yyyy', 'mmm', 'dd'),
           help='show day of the week on a date')
    addarg('-c', '--timer', dest='timer', nargs=1, metavar=('hh:mm:ss'),
           help='start a countdown timer')
    addarg('-r', '--run', dest='run', nargs=1, metavar=('command'),
           help='run command when countdown timer reaches 0')
    addarg('-s', '--stopwatch', dest='stopwatch', nargs='?', type=int, const=3, choices=range(1, 10),
           metavar=('resolution'), help='start a stopwatch [default resolution: 3 (ms)]')
    addarg('-q', '--quiet', dest='quiet', action='store_true',
           help='quiet mode for background timer/stopwatch')
    addarg('keywords', nargs='*', help='diff/add/subtract from today or now')

    return argparser


def main():
    # Show `date` and exit if no arguments
    if len(sys.argv) < 2:
        showdate()
        sys.exit(0)

    args = get_parser().parse_args()

    if args.add and args.sub:
        print('error: cannot add and subtract simultaneously')
        sys.exit(1)

    try:
        # Handle date add, sub or show date diff
        if args.date is not None:
            calc_date(args)

        # Handle time add, sub or show time diff
        if args.time is not None:
            calc_time(args)

        # Show day of the week on the given date
        if args.day is not None:
            show_day(args.day)

        # Diff/add/subtract from today or now
        if args.keywords:
            calc_misc(args)
    except (ValueError, TypeError, KeyError) as e:
        print('error: ' + str(e))

    # Countdown timer
    if args.timer is not None:
        run_countdown_timer(args)

    # Stopwatch
    if args.stopwatch:
        run_stopwatch(args)


if __name__ == '__main__':
    main()
