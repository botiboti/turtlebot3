import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    print('s1 [270]')
    print(msg.ranges[270])
    print('s2 [0]')
    print(msg.ranges[0])
    print('s3 [90]')
    print(msg.ranges[90])

    now = rospy.get_rostime()
    print(rospy.loginfo("Secs: %i Nsecs: %i", now.secs, now.nsecs))
    if msg.ranges[0] > 0.5:
        move.linear.x = 0.1 
        move.linear.z = 0.5
    else:
        move.linear.x = 0.0
        move.linear.z = 0.0

    pub.publish(move)

rospy.init_node('obstacle_avoidance')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
move = Twist()

rospy.spin()