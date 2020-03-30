exp_id=$1
archive_dir="experiments/run_${exp_id}"

echo "Moving data to ${archive_dir} in 3 seconds"
sleep 3

mkdir ${archive_dir}

mv resnet*.log ${archive_dir}/.
mv save_resnet* ${archive_dir}/.
mv nohup.out ${archive_dir}/.
