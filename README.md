<h1 align="center">pdd</h1>

<p align="center">
<a href="https://github.com/jarun/pdd/releases/latest"><img src="https://img.shields.io/github/release/jarun/pdd.svg?maxAge=600" alt="Latest release" /></a>
<a href="https://aur.archlinux.org/packages/pdd"><img src="https://img.shields.io/aur/version/pdd.svg?maxAge=600" alt="AUR" /></a>
<a href="https://pypi.python.org/pypi/pdd"><img src="https://img.shields.io/pypi/v/pdd.svg?maxAge=600" alt="PyPI" /></a>
<a href="https://packages.debian.org/search?keywords=pdd&searchon=names&exact=1"><img src="https://img.shields.io/badge/debian-10+-blue.svg?maxAge=2592000" alt="Debian Buster+" /></a>
<a href="https://apps.fedoraproject.org/packages/pdd"><img src="https://img.shields.io/badge/fedora-27+-blue.svg?maxAge=2592000" alt="Fedora 27+" /></a>
<a href="https://packages.ubuntu.com/search?keywords=pdd&searchon=names&exact=1"><img src="https://img.shields.io/badge/ubuntu-18.04+-blue.svg?maxAge=2592000" alt="Ubuntu Bionic+" /></a>
</p>

<p align="center">
<a href="https://github.com/jarun/pdd/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-GPLv3-yellow.svg?maxAge=2592000" alt="License" /></a>
<a href="https://travis-ci.org/jarun/pdd"><img src="https://travis-ci.org/jarun/pdd.svg?branch=master" alt="Build Status" /></a>
</p>

<p align="center">
<a href="https://asciinema.org/a/189581"><img src="https://asciinema.org/a/189581.png" alt="Asciicast" width="650"/></a>
</p>

`pdd` (Python3 Date Diff) is a small cmdline utility to calculate date and time difference. It can also be used as a timer. If no program arguments are specified it shows the current date, time and timezone.

There are utilities and shell scripts which do what `pdd` does. However, `pdd` has been written with only one goal - simplicity. Users shouldn't have memorize anything.

*Love smart and efficient utilities? Explore [my repositories](https://github.com/jarun?tab=repositories). Buy me a cup of coffee if they help you.*

<p align="center">
<a href="https://saythanks.io/to/jarun"><img src="https://img.shields.io/badge/say-thanks!-ff69b4.svg" /></a>
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RMLTQ76JSXJ4Q"><img src="https://img.shields.io/badge/PayPal-donate-green.svg" alt="Donate via PayPal!" /></a>
</p>

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
- countdown timer
- custom resolution stopwatch
- non-verbose mode for background timers
- show current date, time and timezone

### Installation

#### Dependencies

`pdd` requires Python 3.5 (or later) and the `dateutil` module.

To install `dateutil` on Ubuntu, run:

    $ sudo apt-get install python3-dateutil

or, using pip3:

    $ sudo pip3 install python-dateutil

#### From a package manager

- [AUR](https://aur.archlinux.org/packages/pdd/) (`pacman -S pdd`)
- [Debian](https://packages.debian.org/search?keywords=pdd&searchon=names&exact=1) (`apt-get install pdd`)
- [Fedora](https://apps.fedoraproject.org/packages/pdd) (`dnf install pdd`)
- [NixOS](https://github.com/NixOS/nixpkgs/tree/master/pkgs/tools/misc/pdd) (`nix-env -i pdd`)
- [PyPI](https://pypi.org/project/pdd) (`pip3 install pdd`)
- [Ubuntu](https://packages.ubuntu.com/search?keywords=pdd&searchon=names&exact=1) (`apt-get install pdd`)
- [Ubuntu PPA](https://launchpad.net/~twodopeshaggy/+archive/ubuntu/jarun/) (`apt-get install pdd`)
- [Void Linux](https://github.com/voidlinux/void-packages/tree/master/srcpkgs/pdd) (`xbps-install -S pdd`)

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

    $ ./pdd.py

### Usage

#### cmdline options

```
usage: pdd.py [-h] [-d yyyy mmm dd [yyyy mmm dd | y m d]]
              [-t hh:mm:ss [hh:mm:ss | h:m:s]] [--add] [--sub]
              [--day yyyy mmm dd] [-c hh:mm:ss] [-s [resolution]] [-q]
              [keywords [keywords ...]]

Tiny date, time difference calculator with timers.

positional arguments:
  keywords              diff/add/subtract from today or now

optional arguments:
  -h, --help            show this help message and exit
  -d yyyy mmm dd [yyyy mmm dd | y m d]
                        calculate date difference
  -t hh:mm:ss [hh:mm:ss | h:m:s]
                        calculate time difference
  --add                 add to date (/today) or time (/now)
  --sub                 subtract from date (/today) or time (/now)
  --day yyyy mmm dd     show day of the week on a date
  -c hh:mm:ss           start a countdown timer
  -s [resolution]       start a stopwatch (default resolution: ms)
  -q                    quiet mode for background timer/stopwatch
```

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

2. Calculate diff from **now**:

       $ pdd 24:00:00
       $ pdd 0

3. Calculate date diff:

       $ pdd -d 1983 jul 3 2014 1 15

4. Calculate time diff:

       $ pdd -t 45:50 6:17:33

5. Show current date, time and timezone:

       $ pdd

6. Specify time with roll-over:

       $ pdd -t 5:80:75 6:17:33

7. Add a duration (3 years, 2 months, 1 day) to 28 Feb, 2000:

       $ pdd -d 2000 FEB 28 3 2 1 --add

8. Add a timeslice (1 hour 2 mins 3 secs) to 23:45:37:

       $ pdd -t 23:45:37 1:2:3 --add

9. Add a duration (3 years, 2 months, 1 day) to **today**:

       $ pdd 3 2 1 --add

10. Add a timeslice (1 hour 2 minutes 3 seconds) to **now**:

        $ pdd 1:2:3 --add

11. Subtract a duration (1 day) from 1 Mar, 2000:

        $ pdd -d 2000 Mar 01 0 0 1 --sub

12. Subtract a timeslice (1 sec) from midnight:

        $ pdd -t 00:00:00 0:0:1 --sub

13. Subtract a duration (3 years, 2 months, 1 day) from **today**:

        $ pdd 3 2 1 --sub

14. Subtract a timeslice (1 hour 2 minutes 3 seconds) from **now**:

        $ pdd 1:2:3 --sub

15. Show the day of the week on 15 Jan 2014:

        $ pdd --day 2014 Jan 15

16. Start a countdown timer or stopwatch in **quiet mode** in the background:

        $ pdd -qs &
        $ pdd -qc 3:0:0 &
    To see the final counter run `fg` and press <kbd>Ctrl-C</kbd>.

### Copyright

Copyright © 2017 [Arun Prakash Jana](https://github.com/jarun)
