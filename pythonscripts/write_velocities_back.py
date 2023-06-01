import rospy
from geometry_msgs.msg import Twist
from math import isclose

def talker():
    twist_pub = rospy.Publisher('/cmd_vels', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    move = Twist()

    f = open("negyzet3.txt", "r")
    msg = f.readline().split(" ")
    time = float(msg[0])
    while not rospy.is_shutdown():
        move.linear.x = float(msg[1])*0.033
        move.linear.y = float(msg[2])*0.033
        twist_pub.publish(move)
        msg = f.readline()
        if not msg:
            break
        msg = msg.split(" ")
        # addig ez a sebesseg amennyi ido van a kovetkezo lepesig
        rospy.sleep(float(msg[0])-time)
        print(float(msg[0])-time)
        time = float(msg[0]) 
            
if __name__ == '__main__':
    try:
        talker()
    except:
        twist_pub.publish(Twist())
        print("Node terminated.")