#include <stdlib.h>
#include <cmath>
#include <iostream>

int aprox_pi(double lim) {
  double prev = 1;
  double i = 1;
  double sum = 1;

  while (true) {
    double numerator = std::pow(-1, i);
    double denom = 2 * i + 1;
    sum += numerator / denom;

    if (abs(4 * (sum - prev)) < lim) {
      break;
    }
    i += 1;
    prev = sum;
  }
  return 4 * sum;
}

int main() {
    std::cout << aprox_pi(1e-9) << '\n';
}
