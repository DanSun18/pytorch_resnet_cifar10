#!/bin/bash

# Invoke the trainer.py script for different ResNet models

for model in resnet20 resnet32 resnet44 resnet56 resnet110 # resnet1202 #exclude resnet 1202 from training
do
    echo "python -u trainer.py  --arch=$model  --save-dir=save_$model |& tee -a $model.log" # print the command used to start training
    python -u trainer.py  --arch=$model  --save-dir=save_$model |& tee -a $model.log 
    # the -u option makes stdin, stdout, etc. unbuffered. see link: https://stackoverflow.com/questions/14258500/python-significance-of-u-option 
    # I'll just leave it there without digging deeper into it, as I think it is mostly an implementation/execution issue
done