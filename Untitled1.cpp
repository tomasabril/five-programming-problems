/// Tomas Abril

/*
Problem 1
Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.

Problem 2
Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].

Problem 3
Write a function that computes the list of the first 100 Fibonacci numbers. By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

Problem 4
Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021.

Problem 5
Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.

*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// 1
int sumFor(int * lista, int tam);
int sumWhile(int * lista, int tam);
int sumRecursion(int * lista, int tam, int pos);
int* combinaLista(int* lista1, int* lista2, int tam1, int tam2);

int main()
{
    //
    int primeiro = 0;
    int segundo  = 1;
    int terceiro = 0;
    int quarto   = 0;
    int quinto   = 0;
    //
    if(primeiro) {
        int tam = 10;
        int lista[10] = {5,8,456,0,15,78,3,4,7,42};
        printf("\n soma com for: %d \n", sumFor(lista, tam));
        printf("\n soma com while: %d \n", sumWhile(lista, tam));
        printf("\n soma com recurcao: %d \n", sumRecursion(lista, tam, 0));
    }
    if(segundo) {
        int tam1 = 7, tam2 = 5;
        int lista1[7] = {1,1,1,1,1,1,1};
        int lista2[5] = {0,0,0,0,0};
        int* listaRes = combinaLista(lista1, lista2, tam1, tam2);
        int i;
        for(i=0; i<(tam1+tam2); i++){
            printf("%d ", listaRes[i]);
        }
        printf("\n");
    }

    return 0;
}

int sumFor(int * lista, int tam)
{
    int i=0, sum=0;
    for(i=0; i<tam; i++) {
        sum += lista[i];
    }
    return sum;
}

int sumWhile(int * lista, int tam)
{
    int sum = 0;
    int i = 0;
    while(i < tam) {
        sum += lista[i];
        i++;
    }
    return sum;
}

int sumRecursion(int * lista, int tam, int pos)
{
    if(pos >= tam) {
        return 0;
    } else {
        return lista[pos] + sumRecursion(lista, tam, ++pos);
    }
}

int* combinaLista(int* lista1, int* lista2, int tam1, int tam2)
{
    int* lista3;
    int tam3 = tam1 + tam2;
    int i=0, s=1, pos1=0, pos2=0;
    lista3 = (int*)calloc(tam3, sizeof(int));

    while(i < tam3) {
        if(s>0) {
            if(pos1<tam1) {
                lista3[i] = lista1[pos1];
                pos1++;
                i++;
            }
        } else {
            if(pos2<tam2) {
                lista3[i] = lista2[pos2];
                pos2++;
                i++;
            }
        }
        s *= -1;
    }

    return lista3;
}
















