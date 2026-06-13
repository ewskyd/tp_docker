#!/bin/bash
set -e
case "$1" in

build_generator)
    docker build -t generator ./generator
    ;;

run_generator)
    docker run --rm \
        -v "$(pwd)/data:/data" \
        generator
    ;;

create_local_data)
    mkdir -p local_data
    python3 generator/generate.py local_data
    ;;

build_reporter)
    docker build -t reporter ./reporter
    ;;

run_reporter)
    docker run --rm \
        -v "$(pwd)/data:/data" \
        reporter
    ;;

structure)
    find .
    ;;

clear_data)
    rm -f data/*.csv
    rm -f data/*.html
    ;;

inside_generator)
    docker run --rm \
        -v "$(pwd)/data:/data" \
        generator \
        ls /data
    ;;

inside_reporter)
    docker run --rm \
        -v "$(pwd)/data:/data" \
        reporter \
        ls /data
    ;;

*)
    echo "Unknown command"
    ;;
esac
