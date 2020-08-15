import mahdinlib.config


def main():
    args = mahdinlib.config.parse_cli()
    config = mahdinlib.config.get_configuration(args)