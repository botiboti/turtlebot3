#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler

def callback(msg):
# Print time
  now = rospy.get_rostime()
  print(rospy.loginfo("Secs: %i Nsecs: %i", now.secs, now.nsecs))
# print(msg.pose.pose)

# Get euler from quaternion
# orientation_q = msg.pose.pose.orientation
# orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
# (roll, pitch, yaw) = euler_from_quaternion (orientation_list)

# print(yaw)

  act_pos_left =  msg.position.left




# a ros_core branch szerinti turtlebot_core-ban linear-nak x meg y
# valtozojat hasznaljuk a kulonbozo motrok sebbesegenek megadasara
  move.linear.x = 0.5
  move.linear.y = 0.0
  pub.publish(move)

rospy.init_node('controller')
sub = rospy.Subscriber('/joint_states', JointState, callback)
pub = rospy.Publisher('/cmd_vels', Twist, queue_size=10)
move = Twist()

rospy.spin()
