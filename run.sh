#!/bin/bash

#In order to compile:
#	$ chmod u+x run.sh
#	$ ./run.sh

clear
sh clean.sh

echo "======== PROCESSING virVerVir-1.final ========="
grep '^ver\s' virVerVir-1.out | sed 's/vir/ver/g'  | sed 's/^ver\s*//' | sed '/\<ver\>.*\<ver\>/d' > virVerVir-1.final
grep '^vir\s' virVerVir-1.out                      | sed 's/^vir\s*//' | sed '/\<vir\>.*\<vir\>/d' >> virVerVir-1.final

echo "======== PROCESSING foraIrSer-2.final ========="
grep '^ir\s' foraIrSer-2.out | sed 's/fora/ir/g'   | sed 's/^ir\s*//'  | sed '/\<ir\>.*\<ir\>/d' > foraIrSer-2.final
grep '^ser\s' foraIrSer-2.out | sed 's/fora/ser/g' | sed 's/^ser\s*//' | sed '/\<ser\>.*\<ser\>/d' >> foraIrSer-2.final

echo "======= GENERATING UNIGRAMS AND BIGRAMS ======="
python unigramsAndBigrams.py

echo "============ EVALUATING SENTENCES ============="
echo "Analysing vir without smoothing"
python analyse.py unigramasVir.txt bigramasVir.txt virParametrizacao.txt frasesVir.txt
echo "Analysing vir with smoothing"
python analyse.py unigramasVir.txt bigramasVir.txt virParametrizacao.txt frasesVir.txt use-smoothing
echo "Analysing fora without smoothing"
python analyse.py unigramasFora.txt bigramasFora.txt foraParametrizacao.txt frasesFora.txt
echo "Analysing fora with smoothing"
python analyse.py unigramasFora.txt bigramasFora.txt foraParametrizacao.txt frasesFora.txt use-smoothing
