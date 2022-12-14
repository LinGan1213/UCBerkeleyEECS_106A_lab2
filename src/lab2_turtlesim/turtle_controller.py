#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys

# Import the String message type from the /msg directory of the std_msgs package.

# Define the method which contains the node's main functionality
def talker():
    # Create an instance of the rospy.Publisher object which we can  use to
    # publish messages to a topic. This publisher publishes messages of type
    # std_msgs/String to the topic /chatter_talk
    name = sys.argv[1]
    pub = rospy.Publisher(name + '/cmd_vel', Twist, queue_size=10)
    
    # Create a timer object that will sleep long enough to result in a 10Hz
    # publishing rate
    r = rospy.Rate(10) # 10hz

    # Loop until the node is killed with Ctrl-C
    while not rospy.is_shutdown():
        # Construct a string that we want to publish (in Python, the "%"
        # operator functions similarly to sprintf in C or MATLAB)
        # message = raw_input('Please enter a line of text and press <Enter>:')
        # timestamp = rospy.get_time()
        T = Twist()
        w = input('Press a key:')
        if w == 'w':
            T.linear.y = 2.0
        elif w == 's':
            T.linear.y = -2.0
        elif w == 'a':
            T.linear.x = -2.0
        elif w == 'd':
            T.linear.x = 2.0
        elif w == 'q':
            T.angular.z = -2.0
        elif w == 'e':
            T.angular.z = 2.0

        # Publish our string to the 'chatter_talk' topic
        pub.publish(T)
        print(T)
        # Use our rate object to sleep until it is time to publish again
        r.sleep()
            
# This is Python's syntax for a main() method, which is run by default when
# exectued in the shell
if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called /talker.
    rospy.init_node('talker', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # talker method.
    try:
        talker()
    except rospy.ROSInterruptException: pass