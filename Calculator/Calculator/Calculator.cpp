#include <iostream>
#include <sstream>

int main() {
    std::string input;
    double num1, num2;
    char operation;
    std::cout << "Enter a Question Please (e.g., 1 + 1): ";
    std::getline(std::cin, input);
    std::istringstream iss(input);
    iss >> num1 >> operation >> num2;

    switch (operation) {
    case '+':
        std::cout << num1 << " + " << num2 << " = " << num1 + num2;
        break;
    case '-':
        std::cout << num1 << " - " << num2 << " = " << num1 - num2;
        break;
    case '*':
        std::cout << num1 << " * " << num2 << " = " << num1 * num2;
        break;
    case '/':
        if (num2 != 0)
            std::cout << num1 << " / " << num2 << " = " << num1 / num2;
        else
            std::cout << "Cannot divide by Zero";
        break;
    default:
        std::cout << "Invalid";
    }

    return 0;
}
