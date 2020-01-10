#!/bin/zsh

curl -X PUT "http://localhost:9200/twitter/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
    "user" : "popol",
    "post_date" : "2009/11/15",
    "message" : "trying out elasticsearch"
}'

curl -X POST "http://localhost:9200/twitter/_doc/?pretty" -H 'Content-Type: application/json' -d'
{
    "user" : "popol",
    "post_date" : "2019/09/19",
    "message" : "still trying out Elasticsearch"
}'
