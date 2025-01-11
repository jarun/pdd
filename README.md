<h1 align="center">pdd</h1>

<p align="center">
<a href="https://github.com/jarun/pdd/releases/latest"><img src="https://img.shields.io/github/release/jarun/pdd.svg?maxAge=600" alt="Latest release" /></a>
<a href="https://repology.org/project/pdd/versions"><img src="https://repology.org/badge/tiny-repos/pdd.svg?header=repos" alt="Availability"></a>
<a href="https://pypi.org/project/pdd/"><img src="https://img.shields.io/pypi/v/pdd.svg?maxAge=600" alt="PyPI" /></a>
<a href="https://circleci.com/gh/jarun/workflows/pdd"><img src="https://img.shields.io/circleci/project/github/jarun/pdd.svg" alt="Build Status" /></a>
<a href="https://github.com/jarun/pdd/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-GPLv3-yellowgreen.svg?maxAge=2592000" alt="License" /></a>
</p>

<p align="center">
<a href="https://asciinema.org/a/189581"><img src="https://asciinema.org/a/189581.svg" alt="Asciicast" width="650"/></a>
</p>

`pdd` (Python3 Date Diff) is a tiny command line utility to calculate date and time difference. It can also be used as a timer. If no program arguments are specified it shows the current date, time and timezone.

`pdd` has been written with only one goal - simplicity. Users shouldn't have to memorize anything.

### Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Dependencies](#dependencies)
  - [From a package manager](#from-a-package-manager)
  - [Release packages](#release-packages)
  - [From source](#from-source)
  - [Running standalone](#running-standalone)
- [Usage](#usage)
  - [cmdline options](#cmdline-options)
  - [Operational notes](#operational-notes)
- [Examples](#examples)
- [Copyright](#copyright)

### Features

- easy to use, minimal dependencies
- calculate date and time difference
- calculate diff from *today* and *now*
- add, subtract duration (timeslice) to/from date (time)
- countdown timer with command piggybacking
- custom resolution stopwatch
- non-verbose mode for background timers
- show current date, time and timezone
- follows ISO 8601

### Installation

#### Dependencies

`pdd` requires Python 3.8 (or later) and the `dateutil` module.

To install `dateutil` on Ubuntu, run:

    $ sudo apt-get install python3-dateutil

or, using pip3:

    $ sudo pip3 install python-dateutil

#### From a package manager

Install `pdd` from your package manager. If the version available is dated try an alternative installation method.

<details><summary>Packaging status (expand)</summary>
<p>
<br>
<a href="https://repology.org/project/pdd/versions"><img src="https://repology.org/badge/vertical-allrepos/pdd.svg" alt="Packaging status"></a>
</p>
Unlisted packagers:
<p>
<br>
● <a href="https://pypi.org/project/pdd/">PyPI</a> (<code>pip3 install pdd</code>)<br>
● Termux (<code>pip3 install pdd</code>)<br>
</p>
</details>

#### Release packages

Packages for Arch Linux, CentOS, Debian, Fedora and Ubuntu are available with the [latest stable release](https://github.com/jarun/pdd/releases/latest).

#### From source

If you have git installed, clone this repository. Otherwise download the latest [latest stable release](https://github.com/jarun/pdd/releases/latest) or [development version](https://github.com/jarun/pdd/archive/master.zip) (*risky*).

Install to default location (`/usr/local`):

    $ sudo make install

To remove, run:

    $ sudo make uninstall

`PREFIX` is supported, in case you want to install to a different location.

#### Running standalone

`pdd` is a standalone utility. From the containing directory, run:

    $ chmod +x pdd
    $ ./pdd

### Usage

#### cmdline options

```
usage: pdd [-h] [-d yyyy mmm dd [yyyy mmm dd | y m d]]
           [-t hh:mm:ss [hh:mm:ss | h:m:s]] [--add] [--sub]
           [--day yyyy mmm dd] [-c hh:mm:ss] [-r command] [-s [resolution]] [-q] [-v]
           [keywords ...]

Tiny date, time difference calculator with timers.

positional arguments:
  keywords              diff/add/subtract from today or now

options:
  -h, --help            show this help message and exit
  -d yyyy mmm dd [yyyy mmm dd | y m d], --date yyyy mmm dd [yyyy mmm dd | y m d]
                        calculate date difference
  -t hh:mm:ss [hh:mm:ss | h:m:s], --time hh:mm:ss [hh:mm:ss | h:m:s]
                        calculate time difference
  --add                 add to date (/today) or time (/now)
  --sub                 subtract from date (/today) or time (/now)
  --day yyyy mmm dd     show day of the week on a date
  -c hh:mm:ss, --timer hh:mm:ss
                        start a countdown timer
  -r command, --run command
                        run command when countdown timer reaches 0
  -s [resolution], --stopwatch [resolution]
                        start a stopwatch [default resolution: 3 (ms)]
  -q, --quiet           quiet mode for background timer/stopwatch
  -v, --version         show program's version number and exit
```

Completion scripts are available for Bash, Fish and Zsh shells.

#### Operational notes

- ISO 8601 format. Month can be specified as month number (e.g. Jan - 1, Dec - 12).
- Time is in 24-hr format.
- The absolute difference is shown. Argument order is ignored.
- The end date is excluded in date difference calculations.
- Hour, minute or second can be omitted. Partial inputs are recognized as `mm:ss` or `ss`.
- The keybind to stop timers is <kbd>Ctrl-C</kbd>.

### Examples

1. Calculate diff from **today**:

       $ pdd 2014 Jan 15
       5y 2m 21d
       1906d

2. Calculate diff from **now**:

       $ pdd 24:00:00
       15:24:03
       55443s

       $ pdd 0
       08:36:22
       30982s

3. Calculate date diff:

       $ pdd -d 1983 jul 3 2014 1 15
       30y 6m 12d
       11154d

4. Calculate time diff:

       $ pdd -t 45:50 6:17:33
       05:31:43
       19903s

5. Show current date, time and timezone:

       $ pdd
       Fri 2019 Apr 5 08:37:25 IST

6. Specify time with roll-over:

       $ pdd -t 5:80:75 6:17:33
       00:03:42
       222s

7. Add a duration (3 years, 2 months, 1 day) to 28 Feb, 2000:

       $ pdd -d 2000 FEB 28 3 2 1 --add
       Tue 2003 Apr 29

8. Add a timeslice (1 hour 2 mins 3 secs) to 23:45:37:

       $ pdd -t 23:45:37 1:2:3 --add
       1 day(s) later, 00:47:40
       89260s

9. Add a duration (3 years, 2 months, 1 day) to **today**:

       $ pdd 3 2 1 --add
       Mon 2022 Jun 06

10. Add a timeslice (1 hour 2 minutes 3 seconds) to **now**:

        $ pdd 1:2:3 --add
        09:41:26
        34886s

11. Subtract a duration (1 day) from 1 Mar, 2000:

        $ pdd -d 2000 Mar 01 0 0 1 --sub
        Tue 2000 Feb 29

12. Subtract a timeslice (1 sec) from midnight:

        $ pdd -t 00:00:00 0:0:1 --sub
        1 day(s) earlier, 23:59:59
        -1s

13. Subtract a duration (3 years, 2 months, 1 day) from **today**:

        $ pdd 3 2 1 --sub
        Thu 2016 Feb 04

14. Subtract a timeslice (1 hour 2 minutes 3 seconds) from **now**:

        $ pdd 1:2:3 --sub
        07:40:02
        27602s

15. Show the day of the week on 15 Jan 2014:

        $ pdd --day 2014 Jan 15
        Wed

16. Start a countdown timer or stopwatch in **quiet mode** in the background:

        $ pdd -qs &
        $ pdd -qc 3:0:0 &
    To see the final counter run `fg` and press <kbd>Ctrl-C</kbd>.

17. Run a command when countdown timer reaches 0

        $ pdd -c 00:00:5 -r 'ps -aux'
        $ pdd -c 00:00:5 -r 'notify-send pdd "timer expired"'

### Copyright

Copyright © 2017 [Arun Prakash Jana](https://github.com/jarun)
