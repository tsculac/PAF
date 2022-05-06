#include <iostream>
#include <math.h>

bool kruznica(float x, float y, float r, float xt, float yt)
{
  bool inside;
  float distance = sqrt((yt-y)*(yt-y) + (xt-x)*(xt-x));

  if( distance < r) inside = true;
  else inside = false;

  return inside;
}

int main() {

  std::cout << kruznica(0,0,2,1,1) << std::endl;
  std::cout << kruznica(0,0,2,1,2) << std::endl;

  return 0;
}
