# chat-py
on a deux exemple d'interface independant

configuration de middelware:

1 sudo bin/zookeeper-server-start.sh config/zookeeper.properties
2 sudo bin/kafka-server-start.sh config/server.properties
3 sudo bin/kafka-topics.sh --create --zookeeper localhost:2182 --replication-factor 1 --partitions 1 --topic chat
4 sudo bin/kafka-console-producer.sh --broker-list localhost:9092 --topic chat
5 sudo bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic chat

python:
pip install kafka-python
sudo apt-get install python3-tk

NB:
on a utilisé kafka_2.13-2.5.0
le terminal se pointe sur le dossier kafka_2.13-2.5.0
topic chat est cree au port 2182
le champs identifiant doit etre non null dans le projet main
