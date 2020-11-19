#!/bin/bash

rm boundary && touch boundary || touch boundary

echo "b1 = {" >> boundary

ELINES=$( wc -l < edges )

for (( i=1; i<=$ELINES; i++ )); do

	EDGE=$( sed -n "$i"p edges )
	FLINES=$( awk "/${EDGE%% *}/ && /${EDGE##* }/" faces | wc -l )

	for (( j=1; j<=$FLINES; j++ )); do
		echo "	'$EDGE': '$( awk "/${EDGE%% *}/ && /${EDGE##* }/" faces | sed -n "$j"p - )'," >> boundary
	done

done

echo "}" >> boundary

