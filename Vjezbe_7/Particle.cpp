#include <Particle.h>
#include <math.h>

void Particle::evolve()
{
  while(y >= 0)
  {
    vx += 0.;
    vy += g*dt;

    x += vx*dt;
    y += vy*dt;

    t += dt;
  }
}

Particle::Particle(double v, double theta, double x0, double y0, double step)
{
  // initialize starting conditions
  vx = v*cos(theta*M_PI/180.);
  vy = v*sin(theta*M_PI/180.);
  x = x0;
  y = y0;
  t = 0.;
  dt = step;
}

Particle::~Particle()
{
  vx = 0;
  vy = 0;
  x = 0;
  y = 0;
  t = 0.;
  dt = 0;
}

double Particle::range()
{
  if (t < dt) evolve();
  return x;
}

double Particle::time()
{
  if (t < dt) evolve();
  return t;
}
