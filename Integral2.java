///////////////////////////////////////////////////////////////////////////
//                                                                       //
// Program file name: Integral2.java                                     //
//                                                                       //
// © Tao Pang 2006                                                       //
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

// An example of evaluating an integral with the adaptive
// Simpson rule.

import java.lang.*;
public class Integral2 {
  static final int n = 100;
  public static void main(String argv[]) {
    double del = 1e-6;
    int k = 0;
    double a = 0;
    double b = Math.PI;
    double s = simpson2(a, b, del, k, n);
    System.out.println ("S = " + s);
  }

// Method to integrate over f(x) with the adaptive
// Simpson rule.
  
  public static double simpson2(double a, double b,
    double del, int step, int maxstep) {
    double h = b-a;
    double c = (b+a)/2;
    double fa = f(a);
    double fc = f(c);
    double fb = f(b);
    double s0 = h*(fa+4*fc+fb)/6;
    double s1 = h*(fa+4*f(a+h/4)+2*fc
      + 4*f(a+3*h/4)+fb)/12;
    step++;
    if (step >= maxstep) {
      System.out.println ("Not converged after "
        + step + " recursions");
      return s1;
    }
    else {
      if (Math.abs(s1-s0) < 15*del) return s1;
      else return simpson2(a, c, del/2, step, maxstep)
        + simpson2(c, b, del/2, step, maxstep);
    }
  }

// Method to provide the integrand f(x).

  public static double f(double x) {
    double a0 = 5;
    double s = Math.sin(x);
    double c = Math.cos(x);
    double f = (1+a0*(1-c)*(1-c))
      /((1+a0*s*s)*Math.sqrt(1+2*a0*(1-c)));
    return f;
  }
}
