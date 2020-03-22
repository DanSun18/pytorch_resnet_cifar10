# run the trainer scripts according to run.sh
# then shut down the machine
# to be used on EC2 instances to shutdown machine after training completes.
. run.sh
sleep 5
sudo shutdown -h now # -h needs to be included or EC2 reports running with error
                     # make sure shutdown behavior is set correctly (stop vs. terminate)
                     # also enable termination protection if that helps
                     # if you cannot it might mean the instance can only terminate (it cannot be stopped).
                     # Examples include non-persistent spot instances.