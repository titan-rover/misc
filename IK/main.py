import numpy as np

# this is an analytic solution for inverse kinematics for the joints j1, j2, j3, and j4 of our robotic arm
# the lengths and limitations are based on the 2017-2018 arm report by Todd Yeakley
# this solution is adapted from MIT opencourseware "introduction to robotics" by Asada, Chapter

# we define a function with 4 inputs, the desired (x,y,z) coordinates of the end effector, and the desired orientation of the wrist joint (that is, the angle of the wrist relative to the xy-plane

def ik(xe, ye, ze, phi_e):

    # first, we need to convert the coordinates (xe, ye) to polar coordinates
    re = np.sqrt(xe**2 + ye**2)
    # this is j1
    theta0 = np.arctan2(ye,xe)

    # these are the solutions for the inverse kinematics of a 3 dof articulated arm on a plane
    # note that we will be considering an rz - plane, that is a 2d plane orthogonal to the xy-plane but oriented at theta0 degrees
    phi_e = np.radians(phi_e)

    rw = re - l3 * np.cos(phi_e)
    zw = ze - l3 * np.sin(phi_e)

    a = (l1 ** 2 + l2 ** 2 - rw ** 2 - zw ** 2) / (2 * l1 * l2)
    b = (rw ** 2 + zw ** 2 + l1 ** 2 - l2 ** 2) / (2 * l1 * (rw ** 2 + zw ** 2) ** (1 / 2))

    alpha = np.arctan2(zw , rw)
    # here we are checking that our cosine is a valid input.
    if a < 1 and a > -1:
        beta = np.arccos(a)
    else:
        print("error, invalid input for arccos")
    if b < 1 and b > -1:
        gamma = np.arccos(b)
    else:
        print("error, invalid input for arccos")

    # these are the angles j2, j3, and j4 respectively
    theta1 = alpha - gamma
    theta2 = np.pi - beta
    theta3 = phi_e - theta1 - theta2


    # we store our answers in a vector
    theta = [theta0, theta1, theta2, theta3]

    # we consider the alternative elbow-up configuration (if it exists).
    theta_1 = theta1 + 2 * gamma
    theta_2 = -theta2
    theta_3 = phi_e - theta_1 - theta_2

    theta_i = [theta0, theta_1, theta_2, theta_3]

    theta_array = np.degrees([theta, theta_i])
    #return theta_array

    # range of our joints
    theta1_range = [15, 105]
    theta2_range = [-90, 0]
    theta3_range = [-90, 0]

    theta_range = [theta1_range, theta2_range, theta3_range]

    # checking our limits
    if theta_array[0][1] >= theta_range[0][0] and theta_array[0][1] <= theta_range[0][1] and theta_array[0][2] >= theta_range[1][0] and theta_array[0][2] <= theta_range[1][1] and theta_array[0][3] >= theta_range[2][0] and theta_array[0][3] <= theta_range[2][1]:
        print("returing first")
        return theta_array[0]
    elif theta_array[1][1] >= theta_range[0][0] and theta_array[1][1] <= theta_range[0][1] and theta_array[1][2] >= theta_range[1][0] and theta_array[1][2] <= theta_range[1][1] and theta_array[1][3] >= theta_range[2][0] and theta_array[1][3] <= theta_range[2][1]:
        print("returning second")
        return theta_array[1]
    else:
        for i in range(3):
            if theta_array[0][i+1] < theta_range[i][0] or theta_array[0][i+1] > theta_range[i][1]:
                error = "Error: theta" + str(i+1) + " outside of range, theta" + str(i+1) + "=" +str(theta_array[0][i+1])
                return error

# we have the lengths of each of the arms
l1 = 32.65
l2 = 20.38
l3 = 16.05

# suppose we want our arm in a "neutral" position with the l1 straight up and l2 and l3 straight out
xe = 26.43
ye = 50
ze = 32.65

phi_e = 0

theta_array = ik(xe, ye, ze, phi_e)
print(theta_array)

#notice the expected values are returned