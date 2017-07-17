# pdd

Date, time difference calculator.

There are times you want to check how old you are (in years, months, days) or how long you need to wait for the next flash sale... `pdd` (python3 date diff) is a small cmdline utility to calculate date and time difference. If no program arguments are specified it shows the current date, time and timezone.

<p align="center">
<a href="https://saythanks.io/to/jarun"><img src="https://img.shields.io/badge/say-thanks!-ff69b4.svg" /></a>
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RMLTQ76JSXJ4Q"><img src="https://img.shields.io/badge/PayPal-donate-FC746D.svg" alt="Donate via PayPal!" /></a>
</p>

### Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Dependencies](#dependencies)
  - [Installing from this repository](#installing-from-this-repository)
    - [Running as a standalone utility](#running-as-a-standalone-utility)
- [Usage](#usage)
  - [cmdline options](#cmdline-options)
  - [Operational notes](#operational-notes)
- [Examples](#examples)
- [Copyright](#copyright)

### Features

- calculate date difference
- calculate time difference
- calculate diff from *today* and *now*
- add, subtract duration (timeslice) to/from date (time)
- show current date, time and timezone
- minimal dependencies

### Installation

#### Dependencies

`pdd` requires Python 3.5 (or later) and the `dateutil` module.

To install `dateutil` on Ubuntu, run:

    $ sudo apt-get install python3-dateutil

or, using pip3:

    $ sudo pip3 install dateutil

#### Installing from this repository

If you have git installed, clone this repository. Otherwise download the latest [stable release](https://github.com/jarun/pdd/releases/latest) or [development version](https://github.com/jarun/pdd/archive/master.zip) (*risky*).

Install to default location (`/usr/local`):

    $ sudo make install

To remove, run:

    $ sudo make uninstall

`PREFIX` is supported. You may need to use `sudo` with `PREFIX` depending on your permissions on destination directory.

##### Running as a standalone utility

`pdd` is a standalone utility. From the containing directory, run:

    $ ./pdd

### Usage

#### cmdline options

```
usage: pdd [-h] [-d dd mmm yyyy [dd mmm yyyy | d m y]]
           [-t hh:mm:ss [hh:mm:ss | h:m:s]] [--add] [--sub]
           [keywords [keywords ...]]

Date, time difference calculator.

positional arguments:
  keywords              diff/add/subtract from today or now

optional arguments:
  -h, --help            show this help message and exit
  -d dd mmm yyyy [dd mmm yyyy | d m y]
                        calculate date difference
  -t hh:mm:ss [hh:mm:ss | h:m:s]
                        calculate time difference
  --add                 add to date (/today) or time (/now)
  --sub                 subtract from date (/today) or time (/now)
```

#### Operational notes

- Time is in 24-hr format.
- Month can be specified as month number (e.g. Jan - 1, Dec - 12).
- The absolute difference is shown. Argument order is ignored.
- The end date is excluded in date difference calculations.
- Hour, minute or second can be omitted. Partial inputs are recognized as `mm:ss` or `ss`.

### Examples

1. Calculate date diff:

        $ pdd -d 3 jul 1983 15 1 2014

2. Calculate time diff:

        $ pdd -t 45:50 6:17:33

3. Show current date, time and timezone:

        $ pdd

4. Specify time with roll-over:

        $ pdd -t 5:80:75 6:17:33

5. Calculate diff from **today**:

        $ pdd 15 Jan 2015

6. Calculate diff from **now**:

        $ pdd 24:00:00
        $ pdd 0

7. Add a duration (1 day, 2 months, 3 years) to 28 Feb, 2000:

        $ pdd -d 28 FEB 2000 1 2 3 --add

8. Add a timeslice (1 hour 2 mins 3 secs) to 23:45:37:

        $ pdd -t 23:45:37 1:2:3 --add

9. Add a duration (1 day, 2 months, 3 years) to **today**:

        $ pdd 1 2 3 --add

10. Add a timeslice (1 hour 2 minutes 3 seconds) to **now**:

        $ pdd 1:2:3 --add

11. Subtract a duration (1 day) from 1 Mar, 2000:

        $ pdd -d 01 Mar 2000 1 0 0 --sub

12. Subtract a timeslice (1 sec) from midnight:

        $ pdd -t 00:00:00 0:0:1 --sub

13. Subtract a duration (1 day, 2 months, 3 years) from **today**:

        $ pdd 1 2 3 --sub

14. Subtract a timeslice (1 hour 2 minutes 3 seconds) from **now**:

        $ pdd 1:2:3 --sub

### Copyright

Copyright © 2017 [Arun Prakash Jana](https://github.com/jarun)
