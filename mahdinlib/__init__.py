import mahdinlib.config
import mahdinlib.constants
import mahdinlib.extract_scene


def main():
    # args is for reading input data 
    # parse_cli() is a arguement parser 
    # args = // Namespace(color=None, file='test.py', file_name=None, 
    # high_quality=False, leave_progress_bars=False, 
    # low_quality=False, media_dir=None, medium_quality=False, 
    # preview=False, quiet=False, resolution=None, save_as_gif=False, 
    # save_last_frame=False, save_pngs=False, scene_names=[], 
    # show_file_in_finder=False, sound=False, start_at_animation_number=None, 
    # tex_dir=None, transparent=False, video_dir=None, 
    # video_output_dir=None, write_all=False, write_to_movie=False)//
    args = mahdinlib.config.parse_cli()
    # config is dictionay that will be modified 
    # using args
    config = mahdinlib.config.get_configuration(args)
    # the next line initialize directories that contains
    # media files, inside media file we have tex folder, 
    # texts folder and video folder
    mahdinlib.constants.initialize_directories(config)
    # the next line will goto the main function of 
    # extract_scene.py and extract classes inside file
    mahdinlib.extract_scene.main(config)
