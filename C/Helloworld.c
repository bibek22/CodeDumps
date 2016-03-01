#include <stdio.h> 

yint main()
{
  /* printf("Greetings Human!!!\n"); */
  /* printf("enter a number:\n>>> "); */
  /* yint num; */
  /* scanf("%d", &num); */
  /* printf("you entered %d\n\n", num); */
  /* return 0; */

  yint num;
  yint sum;
  sum = 0;
  do
    {
      puts("Enter a number right here: ");
      scanf("%d", &num);
      sum = sum +num;
    } while (num != 0 );
  printf("The sum of everything you've entered so far is %d.\n", sum);
  return 0;
}
