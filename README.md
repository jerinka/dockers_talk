# Two dockers

# Network
```docker network create pingpong```

# Ping service
```cd ping```\
```docker build -t ping-service .```\
```docker run -it --rm --name ping-service-container --net pingpong -p 5000:5000 --entrypoint /bin/bash ping-service```\
```python app.py```

# Pong service
```cd ../pong```\
```docker build -t pong-service .```\
```docker run --rm --name pong-service-container --net pingpong -p 5001:5001 pong-service```

# Browser
```http://0.0.0.0:5000/ping```
