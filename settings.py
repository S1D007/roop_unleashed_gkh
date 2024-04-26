import yaml

class Settings:
    def __init__(self, config_file):
        self.config_file = config_file
        self.load()

    def default_get(_, data, name, default):
        value = default
        try:
            value = data.get(name, default)
        except:
            pass
        return value


    def load(self):
        try:
            with open(self.config_file, 'r') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
        except:
            data = None

        self.selected_theme = self.default_get(data, 'selected_theme', "Default")
        self.server_name = self.default_get(data, 'server_name', "0.0.0.0")
        self.server_port = self.default_get(data, 'server_port', 7860)
        self.server_share = self.default_get(data, 'server_share', True)
        self.output_image_format = self.default_get(data, 'output_image_format', 'png')
        self.output_video_format = self.default_get(data, 'output_video_format', 'mp4')
        self.output_video_codec = self.default_get(data, 'output_video_codec', 'libx264')
        self.video_quality = self.default_get(data, 'video_quality', 14)
        self.clear_output = self.default_get(data, 'clear_output', True)
        self.max_threads = self.default_get(data, 'max_threads', 2)
        self.memory_limit = self.default_get(data, 'memory_limit', 0)
        self.provider = self.default_get(data, 'provider', 'cpu')
        self.force_cpu = self.default_get(data, 'force_cpu', True)
        self.output_template = self.default_get(data, 'output_template', '{file}_{time}')
        self.use_os_temp_folder = self.default_get(data, 'use_os_temp_folder', False)
        self.output_show_video = self.default_get(data, 'output_show_video', True)





    def save(self):
        data = {
            'selected_theme': self.selected_theme,
            'server_name': self.server_name,
            'server_port': self.server_port,
            'server_share': self.server_share,
            'output_image_format' : self.output_image_format,
            'output_video_format' : self.output_video_format,
            'output_video_codec' : self.output_video_codec,
            'video_quality' : self.video_quality,
            'clear_output' : self.clear_output,
            'max_threads' : self.max_threads,
            'memory_limit' : self.memory_limit,
            'provider' : self.provider,
            'force_cpu' : self.force_cpu,
			'output_template' : self.output_template,
            'use_os_temp_folder' : self.use_os_temp_folder,
            'output_show_video' : self.output_show_video
        }
        with open(self.config_file, 'w') as f:
            yaml.dump(data, f)



