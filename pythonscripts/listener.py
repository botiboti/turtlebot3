#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState

if __name__ == '__main__':
    try:
        last_callback_time = 0.
        not_first_callback = False

        def callback(msg):
            callback_time = rospy.get_time()
            if not_first_callback:
                dt = rospy.get_time() - last_callback_time

            print((callback_time-start_time), joint_states_msg.velocity[1], joint_states_msg.position[0])
            not_first_callback = True
            last_callback_time = callback_time

        rospy.init_node('listener_node', anonymous=True)
        start_time = rospy.get_time()
        sub = rospy.Subscriber('/joint_states', JointState, callback)
    except:
        ("Node terminated.")