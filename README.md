# Message Brokers

## How to Apply Pre-Commit
- install uv
```
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```
- update project env
```
uv sync
```
- run pre-commit
```
uvx pre-commit run --all-files
```


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
