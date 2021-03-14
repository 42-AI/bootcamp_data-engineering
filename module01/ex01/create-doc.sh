#!/bin/zsh

curl -X PUT "http://localhost:9200/twitter/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
    "user" : "popol",
    "post_date" : "02 12 2015",
    "message" : "trying out elasticsearch"
}'

curl -X POST "http://localhost:9200/twitter/_doc/?pretty" -H 'Content-Type: application/json' -d'
{
    "user" : "popol",
    "post_date" : "20 01 2019",
    "message" : "still trying out Elasticsearch"
}'
