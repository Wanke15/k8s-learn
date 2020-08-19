# k8s-learn
k8s project

1. build image
```bash
./build-image.sh
```

2. create pod with deployment
```bash
kubectl apply -f ./k8s-yamls/app.yml
```

3. create service
```bash
kubectl apply -f ./k8s-yamls/service.yml
```

4. consume service
```bash
curl http://localhost:3080
```

The response will be like "Hello world! This is served by host: **flask-demo-845f4ccb97-66wq8**", but **host** may be different because of LoadBalance 