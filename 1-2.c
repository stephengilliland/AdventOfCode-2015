#include <stdio.h>

int main(int argc, char *argv[])
{

    char input[10000];
    int index = 0;
    int floorNumber = 0;
    int stepNumber = 0;

    FILE *inputFile = fopen("1-inp.txt", "r");

    fgets(input, 10000, inputFile);
    
    fclose(inputFile);

    while(input[index] == '(' | input[index] == ')')
    {
        if(input[index] == '(')
            floorNumber += 1;
        if(input[index] == ')')
            floorNumber -= 1;
        index += 1;

        if(stepNumber == 0 && floorNumber == -1)
            stepNumber = index;

    }

    printf("Santa Ends Up On Floor %d\n", floorNumber);
    printf("The step that takes santa to floor -1 is: %d\n", stepNumber);


    return 0;
}