# Exercise 02 - Your first Index Your first Mapping.

We lied to you a bit, it's not really your first time.
Do you remember the last exercises when you inserted a document in Elastic ??
So prepare your self for it, you created an index and mapping and a lot more ...

let's remember one of the documents from the last question

```bash
{
    "user" : "popol",
    "post_date" : "2009-11-15T14:12:12",
    "message" : "trying out Elasticsearch"
}
'
```

- Write the request to get the mapping of the twitter index

let's introduce a new concept in elasticsearch GeoPoint
for that let's ingest some data

POST _bulk
{ "index":{ "_index": "twitter_bis" , "_id" : 0} }
{ "user" : "popol", "post_date" : "2009-11-15T14:12:12", "message" : "trying out Elasticsearch", "location": {"lat": 48.896389,"lon": 2.318450}, "nbr_view" : "42"}
{ "index":{ "_index": "twitter_bis" , "_id" : 1 } }
{ "user" : "mimich", "post_date" : "2019-11-19T15:15:15", "message" : "Trying out Kibana", "location": {"lat": 37.548590,"lon": -122.058590}, "nbr_view" : "1337"}
{ "index":{ "_index": "twitter_bis" , "_id" : 2 } }
{ "user" : "popol", "post_date" : "2019-11-19T15:15:15","message" : "still trying out Elasticsearch", "location": {"lat": 37.548590,"lon": -122.058590}, "nbr_view" : "1967"}
{ "index":{ "_index": "twitter_bis" , "_id" : 3} }
{ "user" : "jean mimich", "post_date" : "2019-11-19T15:15:15", "message" : "Trying something else", "location": {"lat": 48.834702,"lon": 2.370480}, "nbr_view" : "5"}
{ "index":{ "_index": "twitter_bis"}}

- Analyze this new index and reindex the data in a new index called <"twitter_bis_bis"> in such a way that we can do research based on geographic points.