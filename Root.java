///////////////////////////////////////////////////////////////////////////
//                                                                       //
// Program file name: Root.java                                          //
//                                                                       //
// Tao Pang 2006                                                       //
//                                                                       //
// Last modified: January 18, 2006                                       //
//                                                                       //
// (1) This Java program is part of the book, "An Introduction to        //
//     Computational Physics, 2nd Edition," written by Tao Pang and      //
//     published by Cambridge University Press on January 19, 2006.      //
//                                                                       //
// (2) No warranties, express or implied, are made for this program.     //
//                                                                       //
///////////////////////////////////////////////////////////////////////////

// An example of searching a root via the secant method
// for f(x)=exp(x)*ln(x)-x*x=0.

import java.lang.*;
public class Root {
  public static void main(String argv[]) {
    double del = 1e-6, a = 1, b = 2; 		// delta, left bound, right
    double dx = (b-a)/10, x = (a+b)/2; 		// guess in middle of a and b
    int n = 6; 								// max number of steps 
    x = secant(n, del, x, dx);
    System.out.println("Root obtained: " + x);
  }

// Method to carry out the secant search.

  public static double secant(int n, double del,
    double x, double dx) {
    int k = 0;
    double x1 = x+dx;
    while ((Math.abs(dx)>del) && (k<n)) { 	// finish if step is too small
      double d = f(x1)-f(x);
      double x2 = x1-f(x1)*(x1-x)/d; 		// move guess by newton step
      x  = x1;
      x1 = x2;
      dx = x1-x;
      k++;
    }
    if (k==n) System.out.println("Convergence not" +
      " found after " + n + " iterations");
    return x1;
  }

// Method to provide function f(x)=exp(x)*log(x)-x*x.
// Changed to f(x)=e^(x^2)*ln(x^2)-x

  public static double f(double x) {
    return Math.exp(x*x)*Math.log(x*x)-x;
  }
}
