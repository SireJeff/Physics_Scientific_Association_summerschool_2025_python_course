/*
 * tester.cpp for Problem 6
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream> // Required for std::stringstream
#include <numeric> // Required for std::accumulate
#include <cmath>   // Required for std::round, std::pow
#include <map>     // Required for std::map

// Use a small tolerance for floating-point comparisons
const double EPSILON = 1e-6;

int main(int argc, char const *argv[]) {
    // Open the streams for test input and user output
    std::ifstream test_in(argv[1]);
    std::ifstream user_out(argv[3]);
    // test_out (argv[2]) is not used here as we calculate the answer ourselves

    if (!test_in.is_open() || !user_out.is_open()) {
        // One of the files could not be opened, indicates a problem with the judge setup
        return 1;
    }

    // --- 1. Parse the test input file to get args and kwargs ---
    std::vector<double> args;
    std::map<std::string, std::string> kwargs;
    std::string line;

    // Read the first line for positional arguments (numbers)
    if (std::getline(test_in, line)) {
        std::stringstream ss(line);
        double num;
        while (ss >> num) {
            args.push_back(num);
        }
    }

    // Read subsequent lines for keyword arguments
    while (std::getline(test_in, line)) {
        std::stringstream ss(line);
        std::string key, value;
        if (std::getline(ss, key, '=') && std::getline(ss, value)) {
            kwargs[key] = value;
        }
    }

    // --- 2. Calculate the correct answer based on the parsed input ---
    double correct_answer = 0.0;

    // Check for 'multiply' operation
    if (kwargs.count("operation") && kwargs["operation"] == "multiply") {
        correct_answer = std::accumulate(args.begin(), args.end(), 1.0, std::multiplies<double>());
    } else {
        // Default is sum
        correct_answer = std::accumulate(args.begin(), args.end(), 0.0);
    }

    // Check for 'round_to' operation
    if (kwargs.count("round_to")) {
        try {
            int decimal_places = std::stoi(kwargs["round_to"]);
            double multiplier = std::pow(10.0, decimal_places);
            correct_answer = std::round(correct_answer * multiplier) / multiplier;
        } catch (...) {
            // If stoi fails, ignore rounding. This shouldn't happen with valid test files.
        }
    }

    // --- 3. Read the user's output ---
    double user_answer;
    if (!(user_out >> user_answer)) {
        // User output was empty or not a valid number
        return 1; 
    }

    // --- 4. Compare the user's answer with the correct answer ---
    if (std::abs(correct_answer - user_answer) < EPSILON) {
        return 0; // Correct
    } else {
        return 1; // Incorrect
    }
}