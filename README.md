# ![image](https://user-images.githubusercontent.com/102388580/228085808-0217a9aa-2fac-4ff7-8f41-e6b553c4d053.png)


                                                 Engenharia de Software - 3º Período A
                                                              PROJETO 05
 Professor responsável: Ms. Márcio Alexandre Dias Garrido 

* Julia Reis Rodrigues - 202212049

* Brenno Coelho Viana - 202022642

* Guilherme Henrrique Dobelin - 202212084

* João Pedro De Abreu - 202210964

* Raphael Cardim Calvet - 202210809

                                                                 TRABALHO - 5
                                                                  Descrição   
                                                                 
*  Tendo em vista o cojunto de elementos abaixo, crie um algoritimo que seja capaz de determinar a posição de cada elemento e printar suas coordenadas de forma ascendente os valores. Apresentar também o somatório de TODOS ELEMENTOS POR SIMILARIDADE.
  
  ![image](https://user-images.githubusercontent.com/102388580/228089289-2ad162f4-d98b-439d-ad7a-430f84769001.png)

                                            Como pensamos? Como foi feito? Siga abaixo o passo a passo ;)

Foi importado a biblioteca NUMPY, a qual é usada para criar matrizes multidimensionais. Em seguida, criamos a matriz;

![image](https://user-images.githubusercontent.com/102388580/228085022-a4ec6cbf-8013-40d0-9e26-1e95a22d0156.png)


Criamos um diciopnario para armazenar os dados das coordenadas, mas jajá voltaremos nesse ponto. Após isso, é adicionado dois FOR para percorrer o eixo x e y,
no código, i e j. O qual o i é responsável por ler a lista de forma vertical deNtro ma matriz e o j as posições contidas dentro das listas(horizontal). 

Ex:
posição 0 (Primeira lista da matriz [1 , 1 , 1 , 0 , 0 , 0],...)

Após, criamos a variável ELEMENT, para acessar os valores as respectivas coordenadas, assim sendo criado um IF onde ele estará verificando se já existe uma chave com
o valor do ELEMENT, se não tiver ele criará uma chave contendo uma lista vazia.

![image](https://user-images.githubusercontent.com/102388580/228088474-b564c661-766a-4aed-9155-035c8b88723d.png)


Adicionamos dois FOR, usando SORTED para ordenar as chaves e coordenadas em ordem crescente, afim de percorremos os seus respectivos valores e os exibimos. 

![image](https://user-images.githubusercontent.com/102388580/228088549-a5b5ace7-64d8-4bec-8aca-fec765451bd6.png)


Começamos definindo uma lista com os valores a serem verificados, nesse caso, os valores presentes na matriz.

em seguida usamos um for pra percorrer a lista e utilizamos a função np.array() do NumPy pra converter a matriz, tornando-a assim, "manejavel" na biblioteca.

usamos também, a função np.count_nonzero() com o parametro "matriz2 == i", convertendo a matriz em valores booleanos.

![image](https://user-images.githubusercontent.com/102388580/228090298-457c4dc0-ca22-44bb-97ad-e674885444db.png)


Assim, apresentamos primeiramente o valor e quais as respectivas coordenadas a qual o mesmo aparece.

![image](https://user-images.githubusercontent.com/102388580/228085455-44db3749-3541-4b4e-86d9-cbf73c87c8e7.png)


E, por final, mostramos a quantidade de vezes que o valor apareceu nas coordenadas. Depois, exibimos soma do valor adicionado a quantidade de vezes que o mesmo apareceu.

![image](https://user-images.githubusercontent.com/102388580/228085509-511b57d3-29d1-4f0f-975e-3f2fd9ff561a.png)

