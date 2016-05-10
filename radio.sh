#!/bin/bash

date=`date +"%Y_%a_%b_%d_%H%M%P"`

url=http://216.55.186.61:8071

output_filename=${date}

duration=60

output_dir=/home/nego/dejavu/mp3/$url

cd $output_dir

streamripper $url -d $output_dir -l $duration -a $output_filename -u FreAmp/2.x -o always
