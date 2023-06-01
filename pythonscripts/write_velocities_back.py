import rospy
from geometry_msgs.msg import Twist
from math import isclose

def talker:
    twist_pub = rospy.Publisher('/cmd_vels', Twist, queue_size=10)
    rospy.init_node('synchronized_node', anonymous=True)
    move = Twist()

    f = open("negyzet.txt", "r")
    start_time = rospy.get_time()

    while not rospy.is_shutdown():
        msg = (f.readlines()).split(" ")
        if isclose((rospy.get_time()-start_time), msg[0]):
            move.linear.x = msg[1]
            move.linear.y = msg[2]
            twist_pub.publish(move)

if __name__ == '__main__':
    try:
        talker()
    except:
        twist_pub.publish(Twist())
        ("Node terminated.")