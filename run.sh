#!/bin/bash

#In order to compile:
#	$ chmod u+x run.sh
#	$ ./run.sh

clear

echo "======= PROCESSING virVerVir-1.out ======="
grep '^ver\s' virVerVir-1.out | sed 's/vir/ver/g'  | sed 's/^ver\s*//' | sed '/\<ver\>.*\<ver\>/d' > virVerVir-1.final
grep '^vir\s' virVerVir-1.out                      | sed 's/^vir\s*//' | sed '/\<vir\>.*\<vir\>/d' >> virVerVir-1.final

echo "======= PROCESSING foraIrSer-2.out ======="
grep '^ir\s' foraIrSer-2.out | sed 's/fora/ir/g'   | sed 's/^ir\s*//'  | sed '/\<ir\>.*\<ir\>/d' > foraIrSer-2.final
grep '^ser\s' foraIrSer-2.out | sed 's/fora/ser/g' | sed 's/^ser\s*//' | sed '/\<ser\>.*\<ser\>/d' >> foraIrSer-2.final
