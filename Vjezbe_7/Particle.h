// declare a class
class Particle {

   private:

    double t, x, y, vx, vy;
    double dt;
    double g = -9.81;

    void evolve();

   public:
    Particle(double v, double theta, double x0, double y0, double step=0.001);
    ~Particle();

    double range();
    double time();
};
