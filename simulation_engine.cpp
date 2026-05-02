/**
 * High-Performance Simulation Engine
 * Author: Issam Soubra
 * Description: A C++ engine designed for high-performance simulations, 
 * demonstrating efficient memory management and computational logic.
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>

struct Particle {
    double x, y;
    double vx, vy;
    double mass;
};

class SimulationEngine {
private:
    std::vector<Particle> particles;
    double timeStep;

public:
    SimulationEngine(double dt) : timeStep(dt) {}

    void addParticle(double x, double y, double vx, double vy, double mass) {
        particles.push_back({x, y, vx, vy, mass});
    }

    void update() {
        for (auto& p : particles) {
            // Simple Euler integration for position update
            p.x += p.vx * timeStep;
            p.y += p.vy * timeStep;

            // Basic boundary check (bounce back)
            if (p.x < 0 || p.x > 100) p.vx *= -1;
            if (p.y < 0 || p.y > 100) p.vy *= -1;
        }
    }

    void run(int steps) {
        auto start = std::chrono::high_resolution_clock::now();
        for (int i = 0; i < steps; ++i) {
            update();
        }
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed = end - start;
        std::cout << "Simulation completed " << steps << " steps in " << elapsed.count() << " seconds." << std::endl;
    }

    void displayState() {
        for (size_t i = 0; i < particles.size(); ++i) {
            std::cout << "Particle " << i << ": (" << particles[i].x << ", " << particles[i].y << ")" << std::endl;
        }
    }
};

int main() {
    SimulationEngine engine(0.01);
    
    // Add some initial particles
    engine.addParticle(10, 10, 1.5, 2.0, 1.0);
    engine.addParticle(50, 50, -1.0, 0.5, 1.5);
    engine.addParticle(80, 20, 0.5, -1.5, 0.8);

    std::cout << "Starting simulation..." << std::endl;
    engine.run(1000);
    engine.displayState();

    return 0;
}
