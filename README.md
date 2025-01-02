# Message Brokers

## How to Run
- build
```
make build
```
- run
```
docker-compose up
```

## Directory Structure
```
├── docker-compose.yaml # run rabbitmq, consumer, and producer
├── Dockerfile # docker file for consumer and producer
├── Makefile # build docker file
├── pyproject.toml
├── README.md
├── src
│   ├── consumer.py # consumer script
│   ├── __init__.py
│   ├── producer.py # producer script
│   └── utils.py # utils script
```

## Code Running Result
<img src="./assets/running_result.gif" alt="code running result" height="800" />
