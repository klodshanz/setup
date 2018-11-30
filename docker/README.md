## Basic commands

```bash
sudo docker container ls -a
docker run --rm -p 80:8080 [container-name]
docker exec -it 09 bash
```

## Install (Ubuntu)

```bash
sudo gpasswd -a $USER docker # add current user to docker group
getent group docker # list membership information for docker group
```

## AWS (ECR)

Series of commands to build containers and push them to AWS ECR repositories

```bash
sudo docker build -t 667048495336.dkr.ecr.eu-west-1.amazonaws.com/dxc-test-enr .
sudo $(aws --profile dnk ecr get-login --region eu-west-1 | sed -e 's/-e none//')
sudo docker image ls
sudo docker push 667048495336.dkr.ecr.eu-west-1.amazonaws.com/dxc-test-enr
```
