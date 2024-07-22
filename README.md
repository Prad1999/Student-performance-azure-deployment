## End to End Machine Learning Project

ecr name - studentperformance
URI does not have studentperformance 


Docker Setup in EC2 commands to be Executed

optional
sudo apt-get update -y
sudo apt-get upgrade

required
curl -fsSL https:get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker

Configure EC2 as self-hosted runner
AWS_ACCESS_KEY_ID= 
AWS_SECRET_ACCESS_KEY=
AWS_REGION = eu-north-1
AWS_ECR_LOGIN_URI=
ECR_REPOSITORY_NAME= 
