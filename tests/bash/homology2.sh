#!/bin/bash

rm boundary && touch boundary || touch boundary

ELINES=$( wc -l < edges )

nl edges > edgesLines
nl faces > edgesFaces

i=1
EDGE=$( sed -n "$i"p edges )
awk "/${EDGE%% *}/ && /${EDGE##* }/" faces 


