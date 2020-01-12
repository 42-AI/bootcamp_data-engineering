# Exercise 03 - Text Analyzer.

Elasticsearch assumes that a text must be analyzed before it can be used.

let's ingest this docuement in index 42.

```bash
{

  "text" : "Since there aren’t any courses at 42, students can try a “branch” of our curriculum to see if they like it. If they don’t, they aren’t committed to an entire semester or course; they can move to the next branch and topic. This allows students to explore as well as pursue with depth the areas of programming that they are passionate about."
}
'
```

try this request.

GET 42/_search
{
  "query": 
  {
     "match": {
       "text": "program"
     }
  }
}

No results, you probably read the text of the documents and found the word programming and not program.
Elastic allows us to get this document even if our keyword doesn't exactly match a word in the document.
Reindex the data in a new index [42 bis] so we can have this document with this request.

GET 42_bis/_search
{
  "query": 
  {
     "match": {
       "text": "program"
     }
  }
}