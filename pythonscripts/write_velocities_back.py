import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    try:
        rospy.init_node('write_back_velocities', anonymous=True)
        twist_pub = rospy.Publisher('/cmd_vels', Twist, queue_size=10)
        rospy.spin()
    except:
        twist_pub.publish(Twist())
        ("Node terminated.")