#include <iostream>
#include <algorithm>

void ispis(float polje[], int N)
{
  for( int i = 0; i < N; i++)
  {
    std::cout << polje[i] << " ";
  }
  std::cout << std::endl;
}

void ispis_a_b(float polje[], int N, float a, float b)
{
  for( int i = 0; i < N; i++)
  {
    if(polje[i]>= a && polje[i]<=b) std::cout << polje[i] << " ";
  }
  std::cout << std::endl;
}

void swap(float polje[], int i, int j)
{
  float temp;
  temp = polje[i];
  polje[i] = polje[j];
  polje[j] = temp;
}

int main() {

  float polje[10] = {-2.5, -10., 3.4, 12, 20.2, -12.3, 0, 123.02, 11, 0.5};
  ispis(polje, 10);

  ispis_a_b(polje, 10, 0., 10.);

  std::sort(std::begin(polje), std::end(polje));
  ispis(polje, 10);

  std::reverse(std::begin(polje), std::end(polje));
  ispis(polje, 10);

  swap(std::begin(polje), 0, 1);
  ispis(polje, 10);

  return 0;
}
