import rospy
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import JointState
rospy.loginfo("Started")
from message_filters import ApproximateTimeSynchronizer, Subscriber

def synchronized_callback(scan_msg, joint_states_msg):
    # Process synchronized laser scan and joint states data
    # Example: Print the ranges from the laser scan and joint positions
    now = rospy.get_rostime()
    rospy.loginfo("Secs: %i Nsecs: %i", now.secs, now.nsecs)
    # print("Laser Ranges:", scan_msg.ranges)
    # print("Joint Positions:", joint_states_msg.position)

rospy.init_node('synchronized_node', anonymous=True)
scan_sub = Subscriber('scan', LaserScan)
joint_states_sub = Subscriber('joint_states', JointState)
ts = ApproximateTimeSynchronizer([scan_sub, joint_states_sub], 1, 1)
# You can also set a slop time (in seconds) using: ts.setSlopTime(slop_time)
ts.registerCallback(synchronized_callback)
rospy.spin()


