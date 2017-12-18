import roslib
import rospy
import smach
import smach_ros
import os, sys
from std_msgs.msg import Bool
from sound_play.msg import SoundRequest
from std_msgs.msg import Int32
from sound_play.libsoundplay import SoundClient

j=0
class Arm_Manipulation6(smach.State):
	def __init__(self):
		smach.State.__init__(self, outcomes=['Executed','Not_Executed']) # Outcome


	def callback(self,data):
		rospy.logerr("Success %d",j)	

	def listener(self):
		global j
		try:	
			k=rospy.wait_for_message("ui_rating", Int32, timeout=5)
			rospy.Subscriber("ui_rating", Int32, self.callback)
			j=k.data 
		except(rospy.ROSException), e:
			j=0
			rospy.logerr("No publish")
		
	
	def execute(self, userdata):
		os.system("roslaunch eva_arm_controller play5.launch") # launches the play back file
		self.listener()
		if j!=0:
			return 'Executed'
		else:
			return 'Not_Executed'
	