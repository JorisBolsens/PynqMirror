from pynq.drivers import HDMI
from pynq.drivers.video import VMODE_1920x1080

class Display(object):
    def __init__(self):
        self.hdmi_out = HDMI('out', video_mode = VMODE_1920x1080)
        self.hdmi_out.start()

    def show_frame(self, frame_array):
        self.hdmi_out.frame_raw(bytearray(frame_array))