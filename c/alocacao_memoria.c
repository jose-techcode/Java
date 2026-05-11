#include <stdio.h>

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
    printf("Valor do ponteiro apontando pra x: %d\n", x);
    
    // Alocação dinâmica de memória (principal[malloc, calloc, realloc, free])

    // ...
    
    return 0;
}