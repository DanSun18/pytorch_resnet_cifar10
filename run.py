# ported run.sh into python code for easier development and maintenance
# incorporated shutdown capability as well, from run-and-shutdown.sh

import os
import argparse 

parser = argparse.ArgumentParser(description='Runs training for specified ResNet architectures')
parser.add_argument('models', help='models to be trained', 
                              nargs='+',
                              metavar = 'resnetXX',
                              choices=['all', 'resnet20', 'resnet32', 'resnet44', 'resnet56' ,'resnet110' ,'resnet1202'])  
#nargs specify how many arguments is accepted for this particular option. '+' means all and generate error message when there is none.
#metavar just alters the displayed help message for better clarification.
#resnet1202 is only provided as a potential option. Wouldn't use it generally.
parser.add_argument('--shutdown', help='shutdown machine after execution',
                    action='store_true')

args = parser.parse_args()
print(args.models)
print(args.shutdown)

models_from_all = ['resnet20', 'resnet32', 'resnet44', 'resnet56' ,'resnet110'] # does not include resnet1202 for cost concerns and training time.

if args.shutdown:
    cmd = 'sudo shutdown -h now'
    os.system(cmd)
    

