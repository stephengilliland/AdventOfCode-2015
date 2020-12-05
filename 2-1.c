#include <stdio.h>
#include <stdbool.h>

int main(int argc, char *argv[])
{

    char present[100];
    int currLine = 0;
    int totalSqFt = 0;
    int index = 0;
    int currL = 0;
    int currW = 0;
    int currH = 0;
    int x1pos = 0;
    int x2pos = 0;
    int side1 = 0;
    int side2 = 0;
    int side3 = 0;
    bool x1posFound = false;
    bool x2posFound = false;
    
    FILE *inputFile = fopen("2-in.txt", "r");

    while(fgets(present, 100, inputFile))
    {
        //printf("Current Present is: %s", present);
        while(present[index] != '\n')
        {
            //printf("%d", index);
            if(x1posFound == false && present[index] == 'x')
            {
                x1pos = index;
                x1posFound = true;
                //printf("x1 is at: %d, ",x1pos);
            }
            else if(x1posFound == true && x2posFound == false && present[index] == 'x')
            {
                x2pos = index;
                x2posFound = true;
                //printf("x2 is at: %d\n",x2pos);
            }
            index += 1;
        }

        if(x1pos == 1)
        {
            currL = (int)present[0] - '0';

            if(x2pos == 3)
            {
                currW = (int)present[2] - '0';
                if(present[5] == '\n')
                    currH = (int)present[4] - '0';
                else if(present[6] == '\n')
                    currH = 10*((int)present[4] - '0') + (int)present[5] - '0';
            }

            else if(x2pos == 4)
            {
                currW = 10*((int)present[2] - '0') + (int)present[3] - '0';
                if(present[6] == '\n')
                    currH = (int)present[5] - '0';
                else if(present[7] == '\n')
                    currH = 10*((int)present[5] - '0') + (int)present[6] - '0';
            }
        }

        if(x1pos == 2)
        {
            currL = 10*((int)present[0] - '0') + (int)present[1] - '0';

            if(x2pos == 4)
            {
                //printf("TEST ------ %c\n", present[x2pos]);
                currW = (int)present[3] - '0';
                if(present[6] == '\n')
                    currH = (int)present[5] - '0';
                else if(present[7] == '\n')
                    currH = 10*((int)present[5] - '0') + (int)present[6] - '0';
            }

            else if(x2pos == 5)
            {
                currW = 10*((int)present[3] - '0') + (int)present[4] - '0';
                if(present[7] == '\n')
                    currH = (int)present[6] - '0';
                else if(present[8] == '\n')
                    currH = 10*((int)present[6] - '0') + (int)present[7] - '0';
            }
        }
        
        side1 = currL*currW;
        side2 = currW*currH;
        side3 = currH*currL;

        if(side1 <= side2 && side1 <= side3)
            totalSqFt += 2*side1 + 2*side2 + 2*side3 + side1;
        else if(side2 <= side1 && side2 <= side3)
            totalSqFt += 2*side1 + 2*side2 + 2*side3 + side2;
        else if(side3 <= side1 && side3 <= side2)
            totalSqFt += 2*side1 + 2*side2 + 2*side3 + side3;
        
  
        printf("%dx%dx%d: Total = %d\n", currL, currW, currH, totalSqFt);
        currL = 0;
        currH = 0;
        currW = 0;
        x1posFound = false;
        x2posFound = false;
        index = 0;
    }

    fclose(inputFile);
    return 0;
}