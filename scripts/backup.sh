#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "you have to provide 2 arguments SRC and DST to backup"
    exit 1

fi

rsync -avzh $1 $2