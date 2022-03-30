import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

def callback(msg):
    now = rospy.get_rostime()
    print(rospy.loginfo("Secs: %i Nsecs: %i", now.secs, now.nsecs))
    print(msg.pose.pose)
    move.linear.x = 0.5
    move.linear.z = 0.0
    pub.publish(move)

rospy.init_node('kick_control')
sub = rospy.Subscriber('/odom', Odometry, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
move = Twist()

rospy.spin()
