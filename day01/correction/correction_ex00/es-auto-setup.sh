#!/bin/zsh

curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.5.2-darwin-x86_64.tar.gz
tar -xzf elasticsearch-7.5.2-darwin-x86_64.tar.gz
echo 'cluster.name: "my-cluster"' > elasticsearch-7.5.2/config/elasticsearch.yml
echo 'node.name: "node1"' >> elasticsearch-7.5.2/config/elasticsearch.yml
curl -O https://artifacts.elastic.co/downloads/kibana/kibana-7.5.2-darwin-x86_64.tar.gz
tar -xzf kibana-7.5.2-darwin-x86_64.tar.gz
curl -O https://artifacts.elastic.co/downloads/logstash/logstash-7.5.2.tar.gz
tar -xvf logstash-7.5.2.tar.gz
cp ~/42/bootcamp_data-engineering/day01/ingest-pipeline.conf logstash-7.5.2/config/
echo "config.support_escapes: true" > logstash-7.5.2/config/logstash.yml
