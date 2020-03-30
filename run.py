# ported run.sh into python code for easier development and maintenance
# incorporated shutdown capability as well, from run-and-shutdown.sh

import os
import argparse 

def createArgParser():
    
    parser = argparse.ArgumentParser(description='Runs training for specified ResNet architectures')
    parser.add_argument('models', help='models to be trained', 
                              nargs='+',
                              metavar = 'resnetXX',
                              choices=['all', 'resnet20', 'resnet32', 'resnet44', 'resnet56' ,'resnet110' ,'resnet1202'])  
    #nargs specify how many arguments is accepted for this particular option. '+' means all and generate error message when there is none.
    #metavar just alters the displayed help message for better clarification.
    #resnet1202 is only provided as a potential option. Wouldn't use it generally.
    parser.add_argument('-s', '--shutdown', help='shutdown machine after execution',
                        action='store_true')
    return parser

def runTrainer(models):
    for model in models:
        cmd = 'python -u trainer.py'
        cmd = cmd + ' --arch=' + model 
        cmd = cmd + ' --save-dir=save_' + model 
        cmd = cmd + ' |& tee -a ' + model + '.log'
    print('Running trainer for ' + model + ':\n', cmd)
    os.system(cmd)
    return None

parser = createArgParser()
args = parser.parse_args()

# expand all into actual model names
models_from_all = ['resnet20', 'resnet32', 'resnet44', 'resnet56' ,'resnet110'] # does not include resnet1202 for cost concerns and training time.
if 'all' in args.models:
    args.models = models_from_all

# logging information
print("The program will run trainer for {}".format(', '.join(args.models)))
if args.shutdown:
    print("IMPORTANT: Machine will SHUTDOWN after program execution")

runTrainer(args.models)

#shutdown if specified in args
if args.shutdown:
    shutdown_timer = '5s'
    print("Shutting down in " + shutdown_timer)
    cmd = 'sleep ' + shutdown_timer + ';'
    cmd = cmd + 'sudo shutdown -h now'
    os.system(cmd)
    

