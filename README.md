# hello-p-apiy-docker

## Command

docker build

```sh
docker build -t puuga/hello-p-apiy-docker .
```

docker run

```sh
docker run --name hello-p-apiy-docker -p 8080:8080 -e PORT=8080 puuga/hello-p-apiy-docker
```

docker stop & rm

```sh
docker stop hello-p-apiy-docker
socker rm hello-p-apiy-docker
```
