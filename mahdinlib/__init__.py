import mahdinlib.config
import mahdinlib.constants
import mahdinlib.extract_scene


def main():
    args = mahdinlib.config.parse_cli()
    config = mahdinlib.config.get_configuration(args)
    mahdinlib.constants.initialize_directories(config)
    mahdinlib.extract_scene.main(config)
