import rospy
from geometry_msgs.msg import Twist
from math import isclose

def talker():
    twist_pub = rospy.Publisher('/cmd_vels', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    move = Twist()

    f = open("negyzet6.txt", "r")
    lines = f.readlines()
    idx = 0
    while not rospy.is_shutdown():
        msg = lines[idx].split(" ")
        nextmsg = lines[idx+1].split(" ")
        move.linear.x = float(msg[1])*0.033
        move.linear.y = float(msg[2])*0.033
        twist_pub.publish(move)
        # addig ez a sebesseg amennyi ido van a kovetkezo lepesig
        rospy.sleep(float(nextmsg[0])-float(msg[0]))
        print(float(nextmsg[0])-float(msg[0]))
        idx += 1
            
if __name__ == '__main__':
    try:
        talker()
    except:
        twist_pub.publish(Twist())
        print("Node terminated.")