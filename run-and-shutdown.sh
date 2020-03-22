# run the trainer scripts according to run.sh
# then shut down the machine
# to be used on EC2 instances to shutdown machine after training completes.
. run.sh
sleep 5
sudo shutdown -h now