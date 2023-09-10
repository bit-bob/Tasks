#!/bin/sh
colors=("\033[0;31m" "\033[0;32m" "\033[0;33m" "\033[0;34m" "\033[0;35m" "\033[0;36m")
RESULT=0
p=0

trap "kill 0" EXIT

while [[ $# -gt 0 ]]; do
    key="$1"

    if [[ $1 == -* ]]
    then
        $2 2>&1 | awk -v prefix="[${colors[p % ${#colors[@]}]}${key#?}\033[0m] " '{print prefix $0}' &
        shift
    else
        $1 2>&1 | awk -v prefix="[${colors[p % ${#colors[@]}]}$1\033[0m] " '{print prefix $0}' &
    fi
    p=$((p+1))

    shift
done

for job in `jobs -p`
do
    wait $job || let "RESULT=1"
done
