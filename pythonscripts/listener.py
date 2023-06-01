#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState

if __name__ == '__main__':
    try:
        last_callback_time = 0.
        not_first_callback = False

        def callback(joint_states_msg):
            global last_callback_time, not_first_callback
            callback_time = rospy.get_time()
            if not_first_callback:
                dt = rospy.get_time() - last_callback_time

            print((callback_time-start_time), joint_states_msg.velocity[0], joint_states_msg.velocity[1])
            not_first_callback = True
            last_callback_time = callback_time

        rospy.init_node('listener_node', anonymous=True)
        start_time = rospy.get_time()
        sub = rospy.Subscriber('/joint_states', JointState, callback)
        rospy.spin()
    except:
        print("Node terminated.")