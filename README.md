# Flask-docker-app
Flask app in docker container

## Extra task

We can send {'data' : [1, 2, 3, 4, 5], 'rule_1' : 'a', 'rule_2' : 'b', 'rule_3' : 'c', 'rule_4' : 'd', 'rule_5' : 'e', 'rule_6' : 'f']}

## Build it

```
docker build -t flask-app:latest .
```

## Run it

```
docker run -d -p 5000:5000 flask-app
```

## See it in action

Go to `http://localhost:5000`
