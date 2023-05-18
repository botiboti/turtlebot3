#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_robot_backward():
    rospy.init_node('move_robot_backward_node', anonymous=True)
    cmd_vel_pub = rospy.Publisher('/cmd_vels', Twist, queue_size=10)
    rate = rospy.Rate(10)  # Publish at a rate of 10 Hz

    # Create a Twist message to command the robot's movement
    twist_cmd = Twist()
    twist_cmd.linear.x = -0.1  # Linear velocity of -0.1 m/s (backward)
    duration = rospy.Duration(10.0)  # Duration of 1 second

    # Calculate the number of iterations required to move 10 centimeters
    num_iterations = int(10 / (abs(twist_cmd.linear.x) * 0.1))

    for _ in range(num_iterations):
        cmd_vel_pub.publish(twist_cmd)
        rate.sleep()

    # Stop the robot by publishing a zero velocity Twist message
    twist_cmd.linear.x = 0.0
    cmd_vel_pub.publish(twist_cmd)

    rospy.sleep(1)  # Wait for 1 second to ensure the robot stops

if __name__ == '__main__':
    try:
        move_robot_backward()
    except:
        rospy.loginfo("Controller node terminated.")


