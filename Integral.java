///////////////////////////////////////////////////////////////////////////
//                                                                       //
// Program file name: Integral.java                                      //
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

// An example of evaluating an integral with the Simpson
// rule over f(x)=sin(x).

import java.lang.*;
public class Integral {
  static final int n = 8;
  public static void main(String argv[]) {
    double f[] = new double[n+1];
    double h = Math.PI/(2.0*n);
    for (int i=0; i<=n; ++i) {
      double x = h*i;
      f[i] = Math.sin(x);
    }
    double s = simpson(f, h);
    System.out.println("The integral is: " + s);
  }

// Method to achieve the evenly spaced Simpson rule.

  public static double simpson(double y[], double h) {
    int n = y.length-1;
    double s0 = 0, s1 = 0, s2 = 0;
    for (int i=1; i<n; i+=2) {
      s0 += y[i];
      s1 += y[i-1];
      s2 += y[i+1];
    }
    double s = (s1+4*s0+s2)/3;

 // Add the last slice separately for an even n+1
    if ((n+1)%2 == 0)
      return h*(s+(5*y[n]+8*y[n-1]-y[n-2])/12);
    else
      return h*s;
  }
}
