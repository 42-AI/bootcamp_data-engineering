#!/bin/zsh

curl -X POST "http://localhost:9200/twitter/_doc/?pretty" -H 'Content-Type: application/json' -d'
{
    "user" : "popol",
    "post_date" : "2009-11-15",
    "message" : "still trying out Elasticsearch"
}'
