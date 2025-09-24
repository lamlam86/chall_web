```
docker build -t oscmd-chall .
docker run -it --rm -p 7000:7000 -v ${PWD}:/app oscmd-chall
change Dockerfile -> zDockerfile
```
