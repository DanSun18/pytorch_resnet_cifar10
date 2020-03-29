
"""
Prints out the best precision for a saved checkpoint
"""

import argparse
import os
import torch

parser = argparse.ArgumentParser(description='Prints precision for saved checkpoint')
parser.add_argument('path', type=str,
                    help='path to checkpoint file')
args = parser.parse_args()

if os.path.isfile(args.path):
    print("=> loading checkpoint '{}'".format(args.path))
    checkpoint = torch.load(args.path)
    best_prec1 = checkpoint['best_prec1']
    print("=> loaded checkpoint. accuracy: {}".format(best_prec1))
else:
    print("=> no checkpoint found at '{}'".format(args.path))