#!/usr/bin/env python
# -*- coding: utf-8
# RTSP server offering subtitles

import sys
import threading
import gi
import time
import ctypes

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GLib


class MyFactory(GstRtspServer.RTSPMediaFactory):
	def __init__(self,rtspsrc:str):
		GstRtspServer.RTSPMediaFactory.__init__(self)
		self.rtspsrc = rtspsrc

	def do_create_element(self, url):	#url : GstRtsp.RTSPUrl
		spec = """
		rtspsrc location= {0} ! 
		rtph264depay ! h264parse ! rtph264pay pt=96 name=pay0
		""".format(self.rtspsrc)
		return Gst.parse_launch(spec)

class MyRtspServer(GstRtspServer.RTSPServer):
	def __init__(self):
		GstRtspServer.RTSPServer.__init__(self)

	def do_client_connected(self, client):	#client : GstRtspServer.RTSPClient
		print(client)
		pass

class GstServer(threading.Thread):
	def __init__(self,port:str, rtspsrc:str):
		threading.Thread.__init__(self)
		Gst.init(None)

		self.loop = GLib.MainLoop()

		self.server = MyRtspServer()
		self.server.set_service(port)	#열어둘 port 정하기
		f = MyFactory(rtspsrc)			#nvr의 rtsp주소
		f.set_shared(True)				#client끼리 공유가능 설정
		m = self.server.get_mount_points()
		m.add_factory("/test", f)		#서브 주소 설정
		self.server.attach(None)		#따로 Context설정 할건지 여부. 여기선 default

	def run(self):
		self.loop.run()

	def get_id(self):
		# returns id of the respective thread
		if hasattr(self, '_thread_id'):
			return self._thread_id
		for id, thread in threading._active.items():
			if thread is self:
				return id

	def terminate_thread(self):
		self.loop.quit()
		thread_id = self.get_id()
		response = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
		if response > 1:
			ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
			print("Exit failed")

if __name__ == "__main__":
	#test code
	test_port = "3002"
	test_rtspsrc = "rtsp://admin:mdcl7726@192.168.2.4:554/Streaming/Channels/101/"

	test123 = GstServer(test_port, test_rtspsrc)
	test123.start()
	time.sleep(10)
	test123.terminate_thread()
	test123.join()