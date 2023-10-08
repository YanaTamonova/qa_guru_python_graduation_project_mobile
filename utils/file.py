import os


def file_path(env_file):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), env_file)
