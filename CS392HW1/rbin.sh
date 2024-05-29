#!/bin/bash

# *******************************************************************************
#  Author  : Ethan Kalika
#  Date    : February 5, 2024
#  Description: CS392 - Homework 1
#  Pledge  : I pledge my honor that I have abided by the Stevens Honor System
# ******************************************************************************

# TODO: Fill the header above, and then complete rbin.sh below

msg=""
flag_h=0
flag_l=0
flag_p=0
no_flag=1
usageText=$(cat <<'heredoc'
Usage: rbin.sh [-hlp] [list of files]
   -h: Display this help;
   -l: List files in the recycle bin;
   -p: Empty all files in the recycle bin;
   [list of files] with no other flags,
        these files will be moved to the
        recycle bin.
heredoc
)
declare -r recyclePath=~/.recycle #~/.recycle

if [[ ! -e "${recyclePath}" ]]; then
    mkdir ${recyclePath}
fi

while getopts ":hlp" op; do
    case ${op} in
        h)
            flag_h=1
            no_flag=0
            ;;
        l)
            flag_l=1
            no_flag=0
            ;;
        p)
            flag_p=1
            no_flag=0
            ;;
        *)
            echo "Error: Unknown option '"${*}"'." >&2
            echo "$usageText"
            exit 1
    esac
done

if [[ $(($flag_h + $flag_l + $flag_p)) -gt 1 ]]; then
    echo "Error: Too many options enabled." >&2
    echo "$usageText"
    exit 1
fi

if [[ ($flag_h -eq 1 || $flag_l -eq 1 || $flag_p -eq 1) && $# -gt 1 ]]; then
    echo "Error: Too many options enabled." >&2
    echo "$usageText"
    exit 1
fi

if [[ $no_flag -eq 1 && $# -gt 0 ]]; then
    for arg_ in "$@"
    do
        if [[ ! -e "${arg_}" ]]
        then
            echo "Warning: '"${arg_}"' not found." >&2
        else
            mv ${arg_} "${recyclePath}"
        fi
    done
fi

if [[ $flag_h -eq 1 || $# -eq 0 ]]; then
    msg=${msg}"$usageText"
fi

if [[ $flag_p -eq 1 ]]; then
    rm -r "${recyclePath}"/*""
fi

if [[ $flag_l -eq 1 ]]; then
    ls -lAF "${recyclePath}"
fi

if [[ $flag_l -eq 0 && $flag_p -eq 0 && $flag_h -eq 0 ]]; then
    for var in "$@"
    do
        if [[ -e "$var" ]]; then
            mv "$var" "${recyclePath}"
        fi
    done
fi

echo "$msg"
exit 0