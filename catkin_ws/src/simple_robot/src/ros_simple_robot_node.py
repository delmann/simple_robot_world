#!/usr/bin/env python
import rospy

def spam():
	rospy.loginfo("spam foo")

def eggs():
	rospy.loginfo("eggs foo")

if __name__ == '__main__':
	try:
		rospy.loginfo("do something")
	except rospy.ROSInterruptException:
		spam()
		eggs()
		rospy.loginfo("something went wrong!")
		pass
	finally:
		rospy.loginfo("finished")
