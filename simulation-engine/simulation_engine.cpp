/* 
 * ---------------------------------------------------------
 * Simple Particle Sim
 * Author: Issam Soubra
 * ---------------------------------------------------------
 * I built this to play around with basic physics in C++.
 * It just moves some "particles" around a box and makes 
 * them bounce when they hit the edges.
 * ---------------------------------------------------------
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <chrono>
#include <iomanip>

// This represents a single dot moving in our world
struct MyParticle {
    double x, y;      // Where it is
    double dx, dy;    // How fast it's moving (velocity)
    double weight;    // Its mass
};

class MySim {
private:
    std::vector<MyParticle> dots;
    double time_step;

public:
    MySim(double ts) : time_step(ts) {}

    // Add a new dot to the simulation
    void addDot(double x, double y, double dx, double dy, double w) {
        dots.push_back({x, y, dx, dy, w});
    }

    // Move everything forward by one tick
    void update() {
        for (auto& d : dots) {
            // Update position based on speed
            d.x += d.dx * time_step;
            d.y += d.dy * time_step;

            // Bounce logic for the box (0 to 100)
            // I added a little friction so they lose speed on impact
            if (d.x < 0 || d.x > 100) {
                d.dx *= -0.85; 
                d.x = (d.x < 0) ? 0 : 100;
            }
            if (d.y < 0 || d.y > 100) {
                d.dy *= -0.85;
                d.y = (d.y < 0) ? 0 : 100;
            }
        }
    }

    // Run the whole thing for a while
    void start(int ticks) {
        std::cout << "Starting sim for " << ticks << " ticks..." << std::endl;
        
        auto t1 = std::chrono::high_resolution_clock::now();
        for (int i = 0; i < ticks; ++i) {
            update();
        }
        auto t2 = std::chrono::high_resolution_clock::now();
        
        std::chrono::duration<double> diff = t2 - t1;
        std::cout << "Finished! It took about " << std::fixed << std::setprecision(5) << diff.count() << " seconds." << std::endl;
    }

    // Show me where the dots are now
    void showResults() {
        std::cout << "\n--- Final Positions ---" << std::endl;
        for (size_t i = 0; i < dots.size(); ++i) {
            std::cout << "Dot " << (i + 1) << " is at: (" 
                      << std::setprecision(2) << dots[i].x << ", " 
                      << dots[i].y << ")" << std::endl;
        }
    }
};

int main() {
    // Set up the sim with a small time step
    MySim sim(0.01);
    
    // Throw in some random dots
    sim.addDot(12.0, 15.0, 3.0, 4.0, 1.0);
    sim.addDot(45.0, 60.0, -2.0, 1.5, 2.0);
    sim.addDot(80.0, 10.0, 1.0, -3.0, 0.5);

    // Run it and see what happens
    sim.start(10000);
    sim.showResults();

    return 0;
}
