#!/bin/bash
# read-secret: input a secret pass phrase
if read -t 10 -sp "Enter secret pass phrase > " secret_pass; then
    echo "\nSecret pass phrase = '$secret_pass'"
else
    echo "\nInput timed out" >&2
    exit 1
fi
