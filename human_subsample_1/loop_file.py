#! /bin/bash

for w in 10 20 30:
  for f in *.fasta:
      ./hydropathy_graph.py -i $f -w $w
      done
      done
