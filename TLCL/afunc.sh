#!/bin/bash

# Shell function demo

function funct {
    echo "Step 2"
    return
}

# main program starts here

echo "Step 1"
funct
echo "Step 3"
