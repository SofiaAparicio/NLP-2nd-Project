# NLP-2nd-Mini-Project
Natural Language Processing 2nd Mini Project

### Group 40:
 - Sofia Aparicio - n� 81105
 - Rodrigo Lousada - n� 81115

Options taken while developing 2nd mini project

### General:

- Os ficheiros .out  e .final ficaram como pedido nos requisitos de submiss�o do enunciado.

- Optou-se por escolher ficheiros com a termina��o �txt� em detrimento dos �arpa�.



### Text processing:

- Uma vez que o professor n�o tinha /s na demo, optamos por n�o os colocar no principio nem fim de linha. De forma a n�o existir contagem de bigramas com palavras do fim de uma frase e inicio de outra, as contagens dos bigramas � feita linha a linha.

- A pontua��o n�o foi retirada com a finalidade de otimizar a an�lise, permitindo determinar que por exemplo: no caso em que verificamos o digrama (�for�, �,�) a probabilidade do lema ser �ser� � maior, visto que o �ir� requer maioritariamente um complemento.



### Probabilities calculum:

- Efetuou-se o Laplace Smoothing por ser um m�todo mais f�cil e simples de aplicar.

- No caso em que as probabilidades t�m o mesmo valor, optou-se por escolher o lema que tenha a maior contagens de ungiramas.

- Quanto ao c�lculo dos bigramas das frases que sejam para analisar, s�o multiplicadas as probabilidades do bigrama correspondente �s palavras que se encontram antes e depois dos verbos a analisar, pois o resto das probabilidades acabariam por ter o mesmo valor em ambos os casos.

- O alisamento � feito apenas quando estamos efectivamente a calcular as probabilidades, de forma a melhorar o desempenho e tempos do nosso script.

 


### Python files:

- H� dois ficheiros python, um respons�vel por criar os bigramas e unigramas, enquanto o outro serve para ler os ficheiros e indicar qual o lema mais prov�vel para cada uma das frases. O segundo ficheiro recebe ficheiros txt e calcula o lema mais prov�vel para cada uma das frases.

- Ao correr o analyse.py para al�m dos ficheiros pedidos como input, pode ou n�o, receber a string �use-smoothing� de forma a aplicar o Laplace smoothing no c�lculo das probabilidades.
 

 

As frases foram escolhidas de forma a conter diversos casos que permitissem uma melhor an�lise da viabilidade. Escolhemos tanto frases que tivessem todas as palavras pertencentes ao corpus, como frases que n�o. O m�todo para estas foi adicionar a palavra ao corpus com probabilidade zero, apenas at� ao fim da an�lise dessa mesma frase.
