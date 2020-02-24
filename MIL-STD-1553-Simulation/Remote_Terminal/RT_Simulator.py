from Message_Layer.ML_Analyzer_RT import MessageLayerAnalyzerRT
from Physical_Layer_Emulation.Communication_Socket_RT import RT_Listener
from Physical_Layer_Emulation.Communication_Socket_RT import RT_Sender
import threading


class Remote_Terminal:

    def _send_data_to_bc(self, frames):
        for frame in frames:
            RT_Sender().send_message(bytes(frame))

    def start_listener(self):
        listener = RT_Listener()
        listener_thread = threading.Thread(
            target=listener.start_listening)
        listener_thread.start()
        while True:
            if listener.data_received:
                frames = \
                    MessageLayerAnalyzerRT().interprete_incoming_frame(
                        listener.data_received)
                self._send_data_to_bc(frames)
                listener.data_received = ""
