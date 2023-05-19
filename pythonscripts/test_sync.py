import rospy
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import JointState
from message_filters import ApproximateTimeSynchronizer, Subscriber

###############################################################
## ApproximateTimeSynchronizer kell használni, TimeSynchronizer
## nem ment                                                 
###############################################################
if __name__ == '__main__':
    try:
        def synchronized_callback(scan_msg, joint_states_msg):
            # Process synchronized laser scan and joint states data
            now = rospy.get_rostime()
            rospy.loginfo("Secs: %i Nsecs: %i", now.secs, now.nsecs)
            rospy.loginfo("Secs: %i Nsecs: %i", now.secs, now.nsecs)
            rospy.loginfo(joint_sub.position[0])
            rospy.loginfo(laser_sub.angle_increment)

            # x is left wheel
            # y is right wheel
            # core part comes here

            move.linear.x = 0.1
            move.linear.y = 0.1

            twist_pub.publish(move)

        rospy.init_node('Synchronized node', anonymous=True)

        scan_sub = Subscriber('scan', LaserScan)
        joint_states_sub = Subscriber('joint_states', JointState)
        twist_pub = rospy.Publisher('/cmd_vels', Twist, queue_size=10)
        move = Twist()
        # max linear speed for turtlebot is around 0.2 m/s which is around 6 rad/s
        omega = 4.
        ts = ApproximateTimeSynchronizer([scan_sub, joint_states_sub], 1, 1)

        # You can also set a slop time (in seconds) using: ts.setSlopTime(slop_time)
        ts.registerCallback(synchronized_callback)
        rospy.spin()
    except:
        # send empty Twist with zeros to stop the robot
        twist_pub.publish(Twist())
        ("Synchronized node terminated.")
