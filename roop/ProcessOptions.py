class ProcessOptions:

    def __init__(self,processors, face_distance,  blend_ratio, swap_mode, selected_index, masking_text, imagemask, show_mask=False):
        self.processors = processors
        self.face_distance_threshold = face_distance
        self.blend_ratio = blend_ratio
        self.swap_mode = swap_mode
        self.selected_index = selected_index
        self.masking_text = masking_text
        self.imagemask = imagemask
        self.show_mask = show_mask