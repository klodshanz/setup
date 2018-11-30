## Basic commands

```bash
#############################################################
# Install
#############################################################
docker run --rm -p 80:8080 [container-name]
docker container ls -a
docker exec -it [container-id] bash    # Normal bash
docker exec -it [container-id] /bin/ash # Alpine ash

#############################################################
# Cleanup
#############################################################
docker rm -f $(docker ps -aq)  # Remove all containers
docker rmi $(docker images -q) # Remove all images
```

## Install (Ubuntu)

```bash
#############################################################
# add current user to docker group and change permissions
#############################################################
sudo gpasswd -a $USER docker
sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
sudo chmod g+rwx "/home/$USER/.docker" -R

#############################################################
### Check list membership information for docker group
#############################################################
getent group docker 
```

## AWS (ECR)

Series of commands to build containers and push them to AWS ECR repositories

```bash
docker build -t 667048495336.dkr.ecr.eu-west-1.amazonaws.com/dxc-test-enr .
$(aws --profile dnk ecr get-login --region eu-west-1 | sed -e 's/-e none//')
docker push 667048495336.dkr.ecr.eu-west-1.amazonaws.com/dxc-test-enr
```
