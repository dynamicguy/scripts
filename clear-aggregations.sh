#!/bin/sh


curl http://$1:8983/solr/products_signals_aggr/update?stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E
curl http://$1:8983/solr/products_signals_aggr/update?stream.body=%3Ccommit/%3E











curl http://localhost:8983/solr/products_shard1_replica1/update?stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E
curl http://localhost:8983/solr/products_shard1_replica1/update?stream.body=%3Ccommit/%3E

