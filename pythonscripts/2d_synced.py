import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import JointState
from message_filters import ApproximateTimeSynchronizer, Subscriber

###############################################################
## ApproximateTimeSynchronizer works, TimeSynchronizer doesn't
## 150cm distance, initial omega = 2.,constant beta 0.1, 1., 3.
###############################################################
if __name__ == '__main__':
    try:
        move = Twist()
        # max angular velocity is around 6.2 [rad/s] (0.2 [m/s] linear velocity with 0.033 radius [m])
        omega = 2.
        beta = -3.
        # first dt 200 ms
        dt = 0.2
        r = 0.033

        last_callback_time = 0.
        not_first_callback = False
        
        def synchronized_callback(scan_msg, joint_states_msg):
            # Process synchronized laser scan and joint states data
            global not_first_callback, dt, omega, last_callback_time, start_time
            now = rospy.get_rostime()
            callback_time = rospy.get_time()
            # x is left wheel
            # y is right wheel
            # core part comes here
            if not_first_callback:
                dt = rospy.get_time() - last_callback_time

            omega += dt*beta
            move.linear.x = omega*r
            move.linear.y = omega*r
            twist_pub.publish(move)

            # printing data
            print((callback_time-start_time), omega, joint_states_msg.velocity[0], joint_states_msg.velocity[1], joint_states_msg.position[0], joint_states_msg.position[1])
            not_first_callback = True
            last_callback_time = callback_time
            
            
        rospy.init_node('synchronized_node', anonymous=True)

        start_time = rospy.get_time()
        scan_sub = Subscriber('scan', LaserScan)
        joint_states_sub = Subscriber('joint_states', JointState)
        twist_pub = rospy.Publisher('/cmd_vels', Twist, queue_size=10)
        ts = ApproximateTimeSynchronizer([scan_sub, joint_states_sub], 1, 1)

        # You can also set a slop time (in seconds) using: ts.setSlopTime(slop_time)
        ts.registerCallback(synchronized_callback)
        rospy.spin()
    except:
        # send empty Twist with zeros to stop the robot
        twist_pub.publish(Twist())
        ("Synchronized node terminated.")
