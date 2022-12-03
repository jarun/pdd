# Fish completion definition for pdd.
#
# Author:
#   Arun Prakash Jana <engineerarun@gmail.com>

complete -c pdd       -l add          --description 'add to date (/today) or time (/now)'
complete -c pdd -s c  -l timer     -r --description 'start a countdown timer'
complete -c pdd -s d  -l date      -r --description 'calculate date difference'
complete -c pdd       -l day       -r --description 'show day of the week on a date'
complete -c pdd -s h  -l help         --description 'show help'
complete -c pdd -s q  -l quiet        --description 'quiet mode for background timer/stopwatch'
complete -c pdd -s r  -l run       -r --description 'run command when countdown timer reaches 0'
complete -c pdd -s s  -l stopwatch    --description 'start a stopwatch [default resolution: 3 (ms)]'
complete -c pdd       -l sub          --description 'subtract from date (/today) or time (/now)'
complete -c pdd -s t  -l time      -r --description 'calculate time difference'
complete -c pdd -s v  -l version      --description 'show version'
