#!/bin/bash

#In order to compile:
#	$ chmod u+x run.sh
#	$ ./run.sh

# Grupo 40:
# Sofia Aparicio - n 81105
# Rodrigo Lousada - n 81115

clear

echo "======== PROCESSING virVerVir-1.final ========="
grep '^ver\s' virAnotado.out | sed 's/vir/ver/g'  | sed 's/^ver\s*//' | sed '/\<ver\>.*\<ver\>/d' > virAnotado.final
grep '^vir\s' virAnotado.out                      | sed 's/^vir\s*//' | sed '/\<vir\>.*\<vir\>/d' >> virAnotado.final

echo "======== PROCESSING foraIrSer-2.final ========="
grep '^ir\s' foraAnotado.out | sed 's/fora/ir/g'   | sed 's/^ir\s*//'  | sed '/\<ir\>.*\<ir\>/d' > foraAnotado.final
grep '^ser\s' foraAnotado.out | sed 's/fora/ser/g' | sed 's/^ser\s*//' | sed '/\<ser\>.*\<ser\>/d' >> foraAnotado.final

#echo "========== Adding <s> </s> characters ========="
#sed -i -e 's/^/<s> /' -e 's/$/ <\/s>/' virAnotado.final
#sed -i -e 's/^/<s> /' -e 's/$/ <\/s>/' foraAnotado.final

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
