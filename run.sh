#!/bin/bash

#In order to compile:
#	$ chmod u+x run.sh
#	$ ./run.sh

clear

echo "======== PROCESSING virVerVir-1.final ========="
grep '^ver\s' virVerVir-1.out | sed 's/vir/ver/g'  | sed 's/^ver\s*//' | sed '/\<ver\>.*\<ver\>/d' > virVerVir-1.final
grep '^vir\s' virVerVir-1.out                      | sed 's/^vir\s*//' | sed '/\<vir\>.*\<vir\>/d' >> virVerVir-1.final

echo "======== PROCESSING foraIrSer-2.final ========="
grep '^ir\s' foraIrSer-2.out | sed 's/fora/ir/g'   | sed 's/^ir\s*//'  | sed '/\<ir\>.*\<ir\>/d' > foraIrSer-2.final
grep '^ser\s' foraIrSer-2.out | sed 's/fora/ser/g' | sed 's/^ser\s*//' | sed '/\<ser\>.*\<ser\>/d' >> foraIrSer-2.final

echo "======= GENERATING UNIGRAMS AND BIGRAMS ======="
python unigramsAndBigrams.py

echo "============ EVALUATING SENTENCES ============="
echo "Analysing vir without smoothing" > virResultado.txt
python analyse.py virUnigramas.txt virBigramas.txt virParametrizacao.txt virFrases.txt >> virResultado.txt
echo "Analysing vir with Laplace smoothing" >> virResultado.txt
python analyse.py virUnigramas.txt virBigramas.txt virParametrizacao.txt virFrases.txt use-smoothing >> virResultado.txt
echo "Analysing fora without smoothing" > foraResultado.txt
python analyse.py foraUnigramas.txt foraBigramas.txt foraParametrizacao.txt foraFrases.txt >> foraResultado.txt
echo "Analysing fora with Laplace smoothing" >> foraResultado.txt
python analyse.py foraUnigramas.txt foraBigramas.txt foraParametrizacao.txt foraFrases.txt use-smoothing >> foraResultado.txt
