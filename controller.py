#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler

def callback(msg):
#   Print time
    now = rospy.get_rostime()
    print(rospy.loginfo("Secs: %i Nsecs: %i", now.secs, now.nsecs))
#   print(msg.pose.pose)

#   Get euler from quaternion
    orientation_q = msg.pose.pose.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    print(yaw)

#   Move robot
    move.linear.x = 0.5
    move.linear.z = 0.0
    pub.publish(move)

rospy.init_node('controller')
sub = rospy.Subscriber('/odom', Odometry, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
move = Twist()

rospy.spin()
