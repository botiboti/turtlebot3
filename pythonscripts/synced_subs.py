import message_filters
from sensor_msgs.msg import JointState
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    try:        
        def callback(joint_sub, laser_sub):
            # Solve all of perceptions here...
            now = rospy.get_rostime()
            rospy.loginfo("Secs: %i Nsecs: %i", now.secs, now.nsecs)
            rospy.loginfo(joint_sub.position[0])
            rospy.loginfo(laser_sub.angle_increment)
            # move.linear.x = 0.01
            # move.linear.y = 0.01
            # pub.publish(move)

        joint_sub = message_filters.Subscriber('joint_states', JointState)
        laser_sub = message_filters.Subscriber('scan', LaserScan)
        pub = rospy.Publisher('/cmd_vels', Twist, queue_size=10)
        move = Twist()

        ts = message_filters.TimeSynchronizer([joint_sub, laser_sub], 10)
        ts.registerCallback(callback)
        rospy.spin()
    except:
        rospy.loginfo("Controller node terminated.")