#include <stdio.h>

int main(int argc, char *argv[])
{

    char input[10000];
    int index = 0;
    int floorNumber = 0;

    FILE *inputFile = fopen("1-inp.txt", "r");

    fgets(input, 10000, inputFile);
    
    fclose(inputFile);

    while(input[index] == '(' | input[index] == ')')
    {
        printf("Current Char = %c\n", input[index]);
        printf("Santa is currently on floor %d\n", floorNumber);
        if(input[index] == '(')
            floorNumber += 1;
        if(input[index] == ')')
            floorNumber -= 1;
        index += 1;
    }

    printf("Santa Ends Up On Floor %d\n", floorNumber);


    return 0;
}