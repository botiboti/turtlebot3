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

# az aktualis poziciok(rad) es sebessegek(rad/ms ????)

# act_pos_right = msg.position.right
# act_vel_left = msg.velocity.left
# act_vel_right = msg.velocity.right



# a ros_core branch szerinti turtlebot_core-ban linear-nak x meg y
# valtozojat hasznaljuk a kulonbozo motrok sebbesegenek megadasara
  move.linear.x = 100
  move.linear.y = 100
  print(move)
  pub.publish(move)

rospy.init_node('controller')
rospy.loginfo("To stop TurtleBot CTRL + C")
sub = rospy.Subscriber('/joint_states', JointState, callback)
pub = rospy.Publisher('/cmd_vels', Twist, queue_size=10)
# rospy.on_shutdown(pub.publish(Twist())) # ures twist 0.0kal
move = Twist()

rospy.spin()
