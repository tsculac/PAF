#include <iostream>

int maximum(int list[], int size)
{
  double max;
  for(int i = 0; i < size; i++)
  {
    if(i==0) max = list[i];
    else if(list[i] > max) max = list[i];
  }

  return max;
}

int main() {

  int list[6] = {1,2,3,4,5,6};
  std::cout << "Maksimum je " << maximum(list,6) << std::endl;

  return 0;
}
