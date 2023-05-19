import rospy
import rosbag
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import JointState
from message_filters import ApproximateTimeSynchronizer, Subscriber

###############################################################
## ApproximateTimeSynchronizer kell használni, TimeSynchronizer
## nem ment, gondolom noetic-re nincs meg
## 150cm distance, constant beta 1.                                                  
###############################################################
if __name__ == '__main__':
    try:
        def synchronized_callback(scan_msg, joint_states_msg):
            # Process synchronized laser scan and joint states data
            now = rospy.get_rostime()
            t_old = now.nsecs
            # x is left wheel
            # y is right wheel
            # core part comes here
            omega += dt*beta
            move.linear.x = omega*r
            move.linear.y = omega*r
            twist_pub.publish(move)
            print(now.secs, now.nsecs, joint_states_msg.position[0], joint_states_msg.position[1])
            dt = (now.nsecs - t_old)/10**6

        rospy.init_node('synchronized_node', anonymous=True)

        scan_sub = Subscriber('scan', LaserScan)
        joint_states_sub = Subscriber('joint_states', JointState)
        twist_pub = rospy.Publisher('/cmd_vels', Twist, queue_size=10)
        move = Twist()
        # max angular velocity is around 6.2 [rad/s] (0.2 [m/s] linear velocity with 0.033 radius [m])
        omega = 1.
        beta = 1.
        # first dt 100 ms
        dt = 100.
        r = 0.033
        ts = ApproximateTimeSynchronizer([scan_sub, joint_states_sub], 1, 1)

        # You can also set a slop time (in seconds) using: ts.setSlopTime(slop_time)
        ts.registerCallback(synchronized_callback)
        rospy.spin()
    except:
        # send empty Twist with zeros to stop the robot
        twist_pub.publish(Twist())
        ("Synchronized node terminated.")
