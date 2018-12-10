#!/bin/bash

read -p "enter word > "
case $REPLY in
    [[:alpha:]])    echo "is a single alphabetic character.";;
    [ABC][0-9])     echo "is A, B, or C followed by a digit.";;
    ???)            echo "is three character long.";;
    *.txt)          echo "is a word ending in '.txt'";;
    *)              echo "is something else.";;
esac
