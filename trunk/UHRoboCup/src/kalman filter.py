import math
import localization
import config
import time
import numpy
def kalmanfilter(x,P,z,u,A,B,Q,R,H):
    # This is the code which implements the discrete Kalman filter:

    # Prediction for state vector and covariance:
    x = A*x + B*u;
    P = A * P * zip(A) + Q;

    # Compute Kalman gain factor:
    K = P*zip(H)*numpy.linalg.inv(H*P*zip(H)+R);

    # Correction based on observation:
    x = x + K*(z-H*x);
    P = P - K*H*P;
def kalmanfilterimplemented():
    [vx,vy,unitvectorx,unitvectory]= localization.getvelocity()
    t=0
    ax=-.202746*unitvectorx
    ay=-.202746*unitvectory
    Bx = numpy.matrix([[ax,0],[0,ax]])
    By = numpy.matrix([[ay,0],[0,ay]])
    P = numpy.matrix([[0,0],[0,0]])
    Q = .25
    R = 100
    H= numpy.matrix([1,0])
    while(vx >0 & vy > 0):
        u=numpy.matrix([(t^2),t])
        A = numpy.matrix([[1,t],[0,1]])
