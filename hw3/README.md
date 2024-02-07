### Kafka
Вводные команды

```commandline
docker-compose build
```


```commandline
docker-compose up -d
```

```commandline
docker-compose ps
```
```
http://localhost:8081/#/overview

```
```commandline
docker-compose down -v
```

```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023 --partitions 1 --replication-factor 1
```
```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --describe itmo2023  
```
```commandline
 docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --alter --topic itmo2023 --partitions 2

```
```commandline
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic itmo2023_processed --partitions 3 --replication-factor 1
```

```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/device_job.py -d  
```

## Запуск job с окнами
Запускаем producer_1 и consumer_1 после
```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/session_w.py -d
```

```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/sliding.py -d
```

```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/tumbling.py -d 
```
```commandline
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/device_job.py -d  
```
