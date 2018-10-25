#ifndef FUNCTIONS_HPP
#define FUNCTIONS_HPP

#include<cmath>


template<typename T>
T squared(T x) {
  return x * x;
}

template<typename T>
T CentralDiff(T (*f)(T x), T x, T dx) {
  return (f(x + dx) - f(x - dx)) / (2 * dx);
}


template<typename T>
T Newton(T (*f)(T x), T x0, T tol, T dx) {
  T x0 = x - f(x0) / CentralDiff<T>(f, x0, dx);

  while(sqrt((x - x0)*(x - x0)) >= tol) {
    x0 = x;
    x = x0 - f(x0)/CentralDiff<T>(f, x0, dx);
  }
  
  return x;
}


#endif // FUNCTIONS_HPP
