#!/bin/bash

LOG_LOCATION="results.log"

for x in {1..50}; do
    y=`bc <<< "scale=1; $x/10"`
    echo "Testing with value $y" >> $LOG_LOCATION
    python main_trainer.py $y
done
