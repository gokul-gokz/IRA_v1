import roslib
import rospy
import smach
import smach_ros

import actionlib
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import *
from geometry_msgs.msg import *


j=0
class GoalMaker(object):
	
	def __init__(self):
		
		
		self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
		
		
		
			
		rospy.logerr("Connected to move base server")
		
		
		
	def move(self):
		global j
	
		goal = MoveBaseGoal()
		# Use the map frame to define goal poses
		goal.target_pose.header.frame_id = 'map'

		# Set the time stamp to "now"
		goal.target_pose.header.stamp = rospy.Time.now()

		# Set the goal there
				
		goal.target_pose.pose.position.x=-0.0731
		goal.target_pose.pose.position.y=0.0699
		goal.target_pose.pose.position.z=0		
		goal.target_pose.pose.orientation.x=0
		goal.target_pose.pose.orientation.y=0
		goal.target_pose.pose.orientation.z=-0.2966
		goal.target_pose.pose.orientation.w=0.9549


		
				
		
		# Send the goal pose to the MoveBaseAction server
		self.move_base.send_goal(goal)

		# Allow 1 minute to get there
		#finished_within_time = self.move_base.wait_for_result(rospy.Duration(self.time_to_obj)) 

		# If we don't get there in time, abort the goal
		#if not finished_within_time:
		#	self.move_base.cancel_goal()
		#	rospy.loginfo("Timed out achieving goal")          #section of code to be fixed, to allow for feedback from base and removing the delay
		#	return 'preempted'
		#else:
			# We made it!
		#rospy.sleep(60)		# Manual Delay: Scheduled for later
		#state = self.move_base.get_state()
		#if state == GoalStatus.SUCCEEDED:
		#	rospy.logerr("home reached")
		
		finished_within_time = self.move_base.wait_for_result(rospy.Duration(1200000)) 

		# If we don't get there in time, abort the goal
		if not finished_within_time:
			j=0				#variable for checking the goal status
			self.move_base.cancel_goal()
			rospy.logerr("Timed out achieving goal")                  #section of code to be fixed, to allow for feedback from base and removing the delay
			
		else:
			j=1
		
		
		state = self.move_base.get_state()
		if state == GoalStatus.SUCCEEDED:
			rospy.logerr("home reached")
			

	
# define state Bar
class nav2(smach.State):

	
	def __init__(self, gm):
		smach.State.__init__(self,outcomes=['goal_reached'])
		
		self.mover=gm
		
	
	def execute(self, userdata):
		global j
		#rospy.sleep(6)
		
		self.mover.move()
		
		if j==1:
			return 'goal_reached'
