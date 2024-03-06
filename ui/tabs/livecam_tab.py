import gradio as gr
import roop.globals
import ui.globals
import time


camera_frame = None

def livecam_tab():
    with gr.Tab("🎥 Live Cam"):
        with gr.Row(variant='panel'):
            with gr.Column():
                bt_start = gr.Button("▶ Start", variant='primary')
            with gr.Column():
                bt_stop = gr.Button("⏹ Stop", variant='secondary')
            with gr.Column():
                camera_num = gr.Slider(0, 2, value=0, label="Camera Number", step=1.0, interactive=True)
            with gr.Column():
                dd_reso = gr.Dropdown(choices=["640x480","1280x720", "1920x1080"], value="1280x720", label="Fake Camera Resolution", interactive=True)


        with gr.Row():
            fake_cam_image = gr.Image(label='Fake Camera Output', interactive=False)

    start_event = bt_start.click(fn=start_cam,  inputs=[camera_num, dd_reso, ui.globals.ui_selected_enhancer, ui.globals.ui_blend_ratio],outputs=[fake_cam_image])
    bt_stop.click(fn=stop_swap, cancels=[start_event], queue=False)

    #vcam_toggle.change(fn=on_vcam_toggle, inputs=[vcam_toggle, camera_num], outputs=[cam, fake_cam_image])
    #cam.stream(on_stream_swap_cam, inputs=[cam, ui.globals.ui_selected_enhancer, ui.globals.ui_blend_ratio], outputs=[fake_cam_image], preprocess=True, postprocess=True, show_progress="hidden")

def start_cam(cam, reso, enhancer, blend_ratio):
    from roop.virtualcam import start_virtual_cam
    from roop.utilities import convert_to_gradio

    ui.globals.ui_live_cam_active = True
    start_virtual_cam(cam, reso)
    roop.globals.selected_enhancer = enhancer
    roop.globals.blend_ratio = blend_ratio

    while ui.globals.ui_live_cam_active:
        yield convert_to_gradio(ui.globals.ui_camera_frame)
    return convert_to_gradio(ui.globals.ui_camera_frame)

def stop_swap():
    from roop.virtualcam import stop_virtual_cam
    stop_virtual_cam()
    



