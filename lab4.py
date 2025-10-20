import numpy as np

def throw_rock(m, v_0, theta):
    g = 9.81 # in m/s^2
    theta = theta * np.pi / 180 # in radius
    t_f = (2 * v_0 * np.sin(theta) / g) # in s
    R = (v_0**2 * np.sin(2 * theta) / g) # in m
    h_m = (v_0**2 * np.sin(theta)**2 / (2 * g)) # in m
    v_h = v_0 * np.cos(theta) # in m/s
    K_h = 1/2 * m * v_h * h_m**2 # in J

    
    print("For a rock with %5.3f kg mass thrown with %5.3f m/s at an angle of %6.2f degrees:\n" \
          "Time of flight is %10.1e\e s\n"\
          "The range in x-direction is %10.1e m\n"\
          "The maximum height is %10.1e m\n"\
          "The speed at maximum height is %10.1e m/s\n"\
          "Kinetic energy at the maximum height is %8.2e J" % (m, v_0, theta*180/np.pi, t_f, R, h_m, v_h, K_h))
    

    return t_f, R, h_m, v_h, K_h
