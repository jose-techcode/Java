#include <stdio.h> // Entrada e saída (I/O)
#include <stdlib.h> // Alocação dinâmica de memória

// Funções (superficialmente)

int saudacao() {
    printf("Olá\n");
}

int soma(int x, int y) {
    return x + y;
}

int main(void) {
    printf("Hello\n");
    
    saudacao();
    int soma0;
    soma0 = soma(5, 5);
    printf("Soma: %d\n", soma0);
    
    // Tipos de dados, operadores e estrutura de controle (superficialmente[if, for]))
    
    int nota = 7;
    
    if (nota >= 7) {
        printf("Passou\n");
    } 
    else {
        printf("Não passou\n");
    }
    
    for (int i = 1; i < 5; i++) {
        printf("Repetição: %d\n", i);
    }
    
    // Estrutura de dados (superficialmente[lista])
    
    char nomes[3][10] = {"jose", "joao", "joel"};
    printf("%s\n", nomes[0]); // string
    
    for (int i = 0; i < 3; i++) {
        printf("%s\n", nomes[i]);
    }
    
    int numeros[5] = {2, 3, 5, 7, 11};
    printf("%d\n", numeros[0]);
    
    float numeros_decimais0[5] = {0.5, 1.5, 2.5, 3.5, 4.5}; // ou double
    printf("%f\n", numeros_decimais0[0]);
    
    long double numeros_decimais[3] = {0.512, 1.545, 7.890}; // long float: %Lf, long int: %Ld
    printf("%Lf\n", numeros_decimais[1]);

    // Ponteiro

    int x = 5;
    int *ptr = &x;
    int **ptrr = &ptr;
    printf("Valor de x: %d\n", x);
    printf("Valor do ponteiro apontando pra x: %d\n", *ptr);
    printf("Valor de um ponteiro apontando pra outro ponteiro: %d\n", **ptrr);
    
    // Alocação dinâmica de memória (principal[malloc, calloc, realloc, free])

    // Malloc (não limpa memória)

    int *ponteiro = (int *)malloc(sizeof(int)  * 10);

    if (ponteiro == NULL) {
        printf("Erro na alocação\n");
    }

    ponteiro[0] = 10;
    printf("Ponteiro inteiro com memória não limpa: %d\n", ponteiro[0]);
    free(ponteiro);

    // Calloc (limpa memória)

    int *ponteiro0 = (int *)calloc(10, sizeof(int));

    if (ponteiro0 == NULL) {
        printf("Erro na alocação\n");
    }

    ponteiro0[0] = 10;
    printf("Ponteiro inteiro com memória limpa: %d\n", ponteiro[0]);
    free(ponteiro0);

    // Realloc e Malloc

    int *ponteiro1 = (int *)malloc(sizeof(int) * 10);

    if (ponteiro1 == NULL) {
        printf("Erro na alocação\n");
    }

    ponteiro1[0] = 10;

    ponteiro1 = (int *)realloc(ponteiro1, sizeof(int) * 5);

    printf("Ponteiro inteiro com alocação dinâmica de memória com malloc realocado com realloc: %d\n", ponteiro1[0]);
    free(ponteiro1);

    // Realloc e Calloc

    int *ponteiro2 = (int *)calloc(5, sizeof(int));

    if (ponteiro2 == NULL) {
        printf("Erro na alocação\n");
    }

    ponteiro2[0] = 10;

    ponteiro2 = (int *)realloc(ponteiro2, sizeof(int) * 10);

    printf("Ponteiro inteiro com alocação dinâmica de memória com calloc realocado com realloc: %d\n", ponteiro2[0]);
    free(ponteiro2);
    
    return 0;
}