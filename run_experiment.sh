#!/bin/bash

# top-level script to actually run experiment
# this script can be modified and run as needed, and does not need to be kept consistent
# There is no need to implement complex functionality in this script. 
# Just write down whatever I want to run on command line should be fine.
# Facilitates running experiments.

num_iters=5
model="resnet20"
epochs=500
initial_lr=0.1

experiment_id=8

#running experiments
for i in {1..${num_iters}}
do
        echo "Running iteration ${i}"
        python -u run.py ${model} --epochs ${epochs} --lr ${initial_lr}
        bash archive_results.sh run_${experiment_id}-${i}
        sleep 1s        
done

#push to git
git add .
git commit -m "Finished running experiment ${experiment_id}"
git push
sleep 1s


#shutdown the machine
sudo shutdown -h now
