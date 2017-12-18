#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2016, Sayabot Systems Pvt. Ltd.
#   All rights reserved.
# 
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions
#   are met:
# 
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above
#      copyright notice, this list of conditions and the following
#      disclaimer in the documentation and/or other materials provided
#      with the distribution.
#    * Neither the name of the CU Boulder nor the names of its
#      contributors may be used to endorse or promote products derived
#      from this software without specific prior written permission.
# 
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#   FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#   COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#   INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#   BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#   CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#   LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#   ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#   POSSIBILITY OF SUCH DAMAGE
#

# Author: Aditya Vijayachandra(aditya@asimovrobotics.com)

# Description: Smach state machine to shutdown the robot from a Long press on the UI






import roslib
import rospy
import smach
import smach_ros
import os, sys 
from std_msgs.msg import Bool
 

import states.shut_down as st


def main():
    rospy.init_node('Saya shut_down Machine') # initiating node
    
    sm_one = smach.StateMachine(outcomes=['Stop'])


    with sm_one:

	smach.StateMachine.add('st', st.shutdown(), 
					transitions={'waiting_for_command':'st',
							'shutdown_initiated':'Stop'})



    sys = smach_ros.IntrospectionServer('shut_down', sm_one, '/shut_down')
    sys.start()

    outcome = sm_one.execute()

    sys.stop()

if __name__ == '__main__':
    main()
    