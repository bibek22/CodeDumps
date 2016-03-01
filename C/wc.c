#include <stdio.h>

int main(){
  char c;
  int nw, nc, nd, nb, nl;
  nw = nc = nb = nd = nl = 0;
  while ((c = getchar()) != EOF)
    if (c >= '0' && c<='9')
      ++nd;
    else if (c == ' ' || c =='\t' || c == '\n'){
      ++nb;
      ++nw;
      if (c == '\n')
	++nl;
    }
    else
      ++nc;

  printf("digits = %d\n", nd);
  printf("words = %d\n", nw);
  printf("whitespace = %d\n", nb);
  printf("characters = %d\n", nc);
  printf("lines = %d\n", nl);
  return 0;
}
