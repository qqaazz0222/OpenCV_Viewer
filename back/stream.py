import gi

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject, GLib


if __name__ == '__main__':
    loop = GLib.MainLoop()
    GObject.threads_init()
    Gst.init(None)

    class RTSPFactory(GstRtspServer.RTSPMediaFactory):
        def __init__(self, **properties):
            GstRtspServer.RTSPMediaFactory.__init__(self)
        
        def do_create_element(self, url):
            pipeline = "v4l2src device=/dev/video0 ! videoconvert ! video/x-raw,format=I420 ! x264enc speed-preset=ultrafast tune=zerolatency ! rtph264pay name=pay0 pt=96"
            return Gst.parse_launch(pipeline)

    class GstServer():
        def __init__(self):
            self.rtspServer = GstRtspServer.RTSPServer()
            self.rtspServer.set_service("8554")   # RTSP port
            factory = RTSPFactory()
            factory.set_shared(True)
            mount = self.rtspServer.get_mount_points()
            mount.add_factory("/test", factory)   # RTSP URL sub string
            self.rtspServer.attach(None)

    rtspServer = GstServer()
    loop.run()