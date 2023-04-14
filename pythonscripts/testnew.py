#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Twist

class Controller():
    def __init__(self):
        # initiliaze
        PI = 3.14156592359
        x_1l = 1.0
        x_2l = -1.0
        x_1r = 1.0
        x_2r = -1.0

        rospy.init_node('controller', anonymous=False)

        # tell user how to stop TurtleBot
        rospy.loginfo("To stop TurtleBot CTRL + C")

        # What function to call when you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        
        # Create a publisher which can "talk" to TurtleBot and tell it to move
        # Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
        self.cmd_vels = rospy.Publisher('cmd_vels', Twist, queue_size=10)
        #  joint_states = rospy.Subscriber('/joint_states', JointState, callback)

        # Twist is a datatype for velocity, linear.x egyik motor, mas
        move_cmd = Twist()
        # let's go forward at 0.2 m/s
        move_cmd.linear.x = 0.1
        # let's turn at 0 radians/s
        move_cmd.linear.y = 0.0

     
        #TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
        r = rospy.Rate(100);

        # as long as you haven't ctrl + c keeping doing...
        while not rospy.is_shutdown():
            now = rospy.get_rostime()
            rospy.loginfo("Secs: %i Nsecs: %i", now.secs, now.nsecs)

            # ide jon a rugos fuggv., kell def.
            
            # publish the velocity
            self.cmd_vels.publish(move_cmd)
            # wait for 0.1 seconds (10 HZ) and publish again
            r.sleep()

    def callback(data):
        now = rospy.get_rostime()
        rospy.loginfo(data.position)

    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
        # a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
        self.cmd_vels.publish(Twist())
        # sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        Controller()
    except:
        rospy.loginfo("Controller node terminated.")

