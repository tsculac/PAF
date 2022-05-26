#include <iostream>
#include <Particle.h>

using namespace std;

int main()
{
    Particle p1(100,45,0,0);
    Particle p2(10,60,0,0);

    cout << "Domet cestice 1: " << p1.range() << endl;
    cout << "Vrijeme leta cestice 1: " << p1.time() << endl;

    cout << "Domet cestice 2: " << p2.range() << endl;
    cout << "Vrijeme leta cestice 2: " << p2.time() << endl;

    return 0;
}
