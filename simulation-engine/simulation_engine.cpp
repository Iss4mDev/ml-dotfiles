/**
 * Particle Physics Sandbox
 * Author: Issam Soubra
 * 
 * This is a lightweight C++ engine I built to simulate basic particle physics.
 * It handles movement, collisions with boundaries, and tracks performance.
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <iomanip>

// Represents a single object in our simulation
struct Particle {
    double x, y;      // Position
    double vx, vy;    // Velocity
    double mass;      // Weight/Mass
};

class PhysicsEngine {
private:
    std::vector<Particle> particles;
    double dt; // Time step for each update

public:
    PhysicsEngine(double timeStep) : dt(timeStep) {}

    // Add a new particle to the world
    void spawnParticle(double x, double y, double vx, double vy, double mass) {
        particles.push_back({x, y, vx, vy, mass});
    }

    // Update the positions of all particles
    void step() {
        for (auto& p : particles) {
            // Move the particle based on its velocity
            p.x += p.vx * dt;
            p.y += p.vy * dt;

            // Simple boundary logic: bounce off the walls (0-100 range)
            if (p.x < 0 || p.x > 100) {
                p.vx *= -0.9; // Lose a little energy on bounce
                p.x = (p.x < 0) ? 0 : 100;
            }
            if (p.y < 0 || p.y > 100) {
                p.vy *= -0.9; // Lose a little energy on bounce
                p.y = (p.y < 0) ? 0 : 100;
            }
        }
    }

    // Run the simulation for a set number of iterations
    void run(int iterations) {
        std::cout << "Running simulation for " << iterations << " steps..." << std::endl;
        
        auto start = std::chrono::high_resolution_clock::now();
        for (int i = 0; i < iterations; ++i) {
            step();
        }
        auto end = std::chrono::high_resolution_clock::now();
        
        std::chrono::duration<double> elapsed = end - start;
        std::cout << "Done! Took " << std::fixed << std::setprecision(4) << elapsed.count() << " seconds." << std::endl;
    }

    // Print where everything is right now
    void printStatus() {
        std::cout << "\n--- Current Particle States ---" << std::endl;
        for (size_t i = 0; i < particles.size(); ++i) {
            std::cout << "Particle #" << (i + 1) << " is at [" 
                      << std::setprecision(2) << particles[i].x << ", " 
                      << particles[i].y << "]" << std::endl;
        }
    }
};

int main() {
    // Initialize the engine with a 0.01s time step
    PhysicsEngine engine(0.01);
    
    // Drop some particles into the mix
    engine.spawnParticle(10.0, 10.0, 2.5, 3.0, 1.0);
    engine.spawnParticle(50.0, 50.0, -1.2, 0.8, 1.5);
    engine.spawnParticle(85.0, 20.0, 0.7, -2.0, 0.5);

    engine.run(5000);
    engine.printStatus();

    return 0;
}
