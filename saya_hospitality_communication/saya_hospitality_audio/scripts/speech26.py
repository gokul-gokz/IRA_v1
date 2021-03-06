#!/usr/bin/env python


import roslib
import rospy
from sound_play.libsoundplay import SoundClient

rospy.init_node('play_sound')
#Create a sound client instance
sound_client = SoundClient()
#wait for sound_play node to connect to publishers (otherwise it will miss first published msg)
rospy.sleep(2)
#Method 1: Play Wave file directly from Client
sound_client.playWave('/home/asimov/robo_ws/src/saya_hospitality-ros-pkg/saya_hospitality_communication/saya_hospitality_audio/sound_snippets/speech26.wav')
