#include <stdio.h>

int main()
{
    int trainee[3][3];
    int average[3] = {0};
    int i, j , max = 0;
    for(int i = 0; i< 3; i++)
    {
        for(int j = 0; j<2; j++)
        {
            scanf(%d, &trainee[i][j]);    
            if(trainee[i][j]<1 || trainee[i][j]>100 )
            {
                printf("invalid input");
            }
        
        }
    }
    
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j<3; j++)
        {
            int average[i] = average[i] + trainee[i][j];
        }
        average[i] = average[i]/3;
    }
    
    for(int i = 0; i< 3; i++)
    {
        if( int average[i] > max )
        {
            int max = average[i];
        }
    }
    
    for(int i = 0; i<3; i++)
    {
        if(average[i] == max)
        {
            printf("Fittest trainee is :")
        }
    }
    return 0;
}
