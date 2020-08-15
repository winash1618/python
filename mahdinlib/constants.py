import numpy as np
import os

MEDIA_DIR = ""
VIDEO_DIR = ""
VIDEO_OUTPUT_DIR = ""
TEX_DIR = ""
TEXT_DIR = ""


def initialize_directories(config):
    global MEDIA_DIR
    global VIDEO_DIR
    global VIDEO_OUTPUT_DIR
    global TEX_DIR
    global TEXT_DIR

    video_path_specified = config["video_dir"] or config["video_output_dir"]

    if not (video_path_specified and config["tex_dir"]):
        if config["media_dir"]:
            MEDIA_DIR = config["media_dir"]
        else:
            MEDIA_DIR = os.path.join(
                os.path.expanduser('~'),
                "Dropbox (3Blue1Brown)/3Blue1Brown Team Folder"
            )
        if not os.path.isdir(MEDIA_DIR):
            MEDIA_DIR = "./media"
        print(
            f"Media will be written to {MEDIA_DIR + os.sep}. You can change "
            "this behavior with the --media_dir flag."
        )
    else:
        if config["media_dir"]:
            print(
                "Ignoring --media_dir, since both --tex_dir and a video "
                "directory were both passed"
            )

    TEX_DIR = config["tex_dir"] or os.path.join(MEDIA_DIR, "Tex")
    TEXT_DIR = os.path.join(MEDIA_DIR, "texts")
    if not video_path_specified:
        VIDEO_DIR = os.path.join(MEDIA_DIR, "videos")
        VIDEO_OUTPUT_DIR = os.path.join(MEDIA_DIR, "videos")
    elif config["video_output_dir"]:
        VIDEO_OUTPUT_DIR = config["video_output_dir"]
    else:
        VIDEO_DIR = config["video_dir"]

    for folder in [VIDEO_DIR, VIDEO_OUTPUT_DIR, TEX_DIR, TEXT_DIR]:
        if folder != "" and not os.path.exists(folder):
            os.makedirs(folder)





PRODUCTION_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 1440,
    "pixel_width": 2560,
    "frame_rate": 60,
}

HIGH_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 1080,
    "pixel_width": 1920,
    "frame_rate": 60,
}

MEDIUM_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 720,
    "pixel_width": 1280,
    "frame_rate": 30,
}

LOW_QUALITY_CAMERA_CONFIG = {
    "pixel_height": 480,
    "pixel_width": 854,
    "frame_rate": 15,
}
