#!/bin/bash

TOTAL_NODES=1001
BATCH_SIZE=10

for (( i=1; i<=TOTAL_NODES; i+=BATCH_SIZE ))
do
  START=$i
  END=$((i + BATCH_SIZE - 1))

  if [ $END -gt $TOTAL_NODES ]; then
    END=$TOTAL_NODES
  fi

  echo "Generating nodes from $START to $END..."
  python generate_game.py --start $START --end $END
done

echo "All batches complete."
