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
    parser.add_argument('--epochs', default=200, type=int, metavar='N',
                        help='number of total epochs to run')
    parser.add_argument('--lr', '--learning-rate', default=0.1, type=float,
                    metavar='LR', help='initial learning rate')
    parser.add_argument('-s', '--shutdown', help='shutdown machine after execution',
                        action='store_true')
    parser.add_argument('--output', help='shows detailed output from trainer',
                        action='store_true')
    return parser

def runTrainer(models, epoch, lr, show_output):
    for model in models:
        log_file = model + '.log'
        
        cmd = 'python -u trainer.py' #-u disables python buffer for input and output. 
        cmd = cmd + ' --arch=' + model 
        cmd = cmd + ' --save-dir=save_' + model 
        cmd = cmd + ' --epochs=' + str(epoch)
        cmd = cmd + ' --lr=' + str(lr)
        
        if show_output:
            cmd = cmd + ' |& tee -a ' + log_file #append to log and show output on screen
        else:
            cmd = cmd + ' >> ' + log_file # append stdout to log file
            cmd = cmd + ' 2>&1' # redirects stderr to stdout
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

runTrainer(args.models, args.epochs, args.lr, args.output )

#shutdown if specified in args
if args.shutdown:
    shutdown_timer = '5s'
    print("Shutting down in " + shutdown_timer)
    cmd = 'sleep ' + shutdown_timer + ';'
    cmd = cmd + 'sudo shutdown -h now'
    os.system(cmd)
    

