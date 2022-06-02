#! /bin/bash

#make start.sh executable
chmod +x start.sh
#install requeriments for python 
pip3 install AWSIoTPythonSDK
pip3 install requests
# remove AWS CLI version 1 and install CLI version 2
y | sudo yum remove awscli
cd /tmp
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

