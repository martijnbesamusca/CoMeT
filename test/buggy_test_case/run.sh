#!/bin/bash

for (( c=1; c<=32; c++ ))
do
        mknod test${c}_pipe.sift p
done

for (( c=1; c<=32; c++ ))
do
   ../../record-trace -o test${c}_pipe --roi -- ./test -p1 &
done
