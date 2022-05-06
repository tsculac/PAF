#include <iostream>
#include <iomanip>

void jedn_pravca(float p1[2], float p2[2])
{
  float k = (p2[1]-p1[1])/(p2[0]-p1[0]);
  float l = -k*p1[0]+p1[1];

  std::cout << "Jednadzba pravca: " << std::endl;
  std::cout << std::setprecision(3);
  if(l > 0) std::cout << "y=" << k << "x+" << l << std::endl;
  else if(l<0) std::cout << "y=" << k << "x" << l << std::endl;
  else std::cout << "y=" << k << std::endl;
}

int main() {

  float p1[2] = {1.5,0};
  float p2[2] = {-2,5};

  jedn_pravca(p1,p2);

  return 0;
}
