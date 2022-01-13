#!/bin/bash
#
# Simple example for creating a collection and loading signal data


if [ -z $FUSION_API ]; then
  FUSION_API=http://localhost:8765/api/v1
fi

COLLECTION=bd
DATA_FILE=signals.json
AGGREGATION_DEFINITION=aggregation_definition.json
JSON='Content-type:application/json'
OUT=/tmp/signals.out

set -e
set -x

echo listing collections:
curl -# --include --output $OUT "$FUSION_API/collections"
cat $OUT
echo
if ! grep 'HTTP/1.1 200' $OUT; then echo failed; exit 1; fi

echo creating collection $COLLECTION:
curl -# --include --output $OUT --request PUT "$FUSION_API/collections/$COLLECTION" -H $JSON -d '{"searchClusterId" : "default"}'
cat $OUT
echo
if ! grep 'HTTP/1.1 200' $OUT; then echo failed; exit 1; fi

echo creating signals collection $COLLECTION:
curl -# --include --output $OUT --request PUT "$FUSION_API/collections/$COLLECTION/features/signals" -H $JSON -d '{"enabled": true}'
cat $OUT
echo
if ! egrep 'HTTP/1.1 (200|204)' $OUT; then echo failed; exit 1; fi

echo loading data from $DATA_FILE:
curl -# --include --output $OUT --request POST "$FUSION_API/signals/$COLLECTION?commit=true" --data-binary @$DATA_FILE -H $JSON
cat $OUT
echo
if ! egrep 'HTTP/1.1 (200|204)' $OUT; then echo failed; exit 1; fi

sleep 2 # do we need this

echo create an Aggregation definition

curl -# --include --output $OUT --request POST "$FUSION_API/aggregator/aggregations" -H $JSON \
  --data-binary @$AGGREGATION_DEFINITION
cat $OUT
echo
if ! egrep 'HTTP/1.1 (200|204)' $OUT; then echo failed; exit 1; fi

echo run the aggregation on our collection
curl -# --include --output $OUT --request POST "$FUSION_API/aggregator/jobs/${COLLECTION}_signals/1?sync=true"
cat $OUT
echo
if ! egrep 'HTTP/1.1 (200|204)' $OUT; then echo failed; exit 1; fi

echo check the status
curl -# --include --output $OUT "$FUSION_API/aggregator/jobs/${COLLECTION}_signals/1"
cat $OUT
echo
if ! egrep 'HTTP/1.1 (200|204)' $OUT; then echo failed; exit 1; fi

echo get recommendations
curl -# --include --output $OUT "$FUSION_API/recommend/$COLLECTION/itemsForQuery?q=laptop"
cat $OUT
echo
if ! grep 'HTTP/1.1 200' $OUT; then echo failed; exit 1; fi

curl -# --include --output $OUT "$FUSION_API/recommend/$COLLECTION/queriesForItem?docId=1519222"
cat $OUT
echo
if ! grep 'HTTP/1.1 200' $OUT; then echo failed; exit 1; fi

curl -# --include --output $OUT "$FUSION_API/recommend/$COLLECTION/itemsForItem?docId=1519222"
cat $OUT
echo
if ! grep 'HTTP/1.1 200' $OUT; then echo failed; exit 1; fi
