#!/bin/zsh

curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.5.1-darwin-x86_64.tar.gz
curl -O https://artifacts.elastic.co/downloads/kibana/kibana-7.5.1-darwin-x86_64.tar.gz
tar -xzf elasticsearch-7.5.1-darwin-x86_64.tar.gz
tar -xzf kibana-7.5.1-darwin-x86_64.tar.gz
echo 'cluster.name: "my-cluster"' > elasticsearch-7.5.1/config/elasticsearch.yml
echo 'node.name: "node1"' >> elasticsearch-7.5.1/config/elasticsearch.yml