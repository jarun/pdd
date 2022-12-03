# Bash completion definition for pdd.
#
# Author:
#   Arun Prakash Jana <engineerarun@gmail.com>

_pdd () {
    COMPREPLY=()
    local IFS=$' \n'
    local cur=$2 prev=$3
    local -a opts opts_with_args
    opts=(
        --add
        -h --help
        -q --quiet
        --sub
        -v --version
    )
    opts_with_arg=(
        -c --timer
        -d --date
        --day
        -r --run
        -s --stopwatch
        -t --time
    )

    # Do not complete non option names
    [[ $cur == -* ]] || return 1

    # Do not complete when the previous arg is an option expecting an argument
    for opt in "${opts_with_arg[@]}"; do
        [[ $opt == $prev ]] && return 1
    done

    # Complete option names
    COMPREPLY=( $(compgen -W "${opts[*]}" -- "$cur") )
    return 0
}

complete -F _pdd pdd
