from os import path
import numpy as np

dataset_path = path.realpath(
    path.join(path.realpath(__file__), path.pardir, path.pardir, "Dataset"))
video_folder_path = path.realpath(path.join(dataset_path, "videos"))
data_folder_path = path.realpath(path.join(dataset_path, "data"))

def file_path(function):
    def altered_function(video_name: str, *args, **kwargs):
        video_name = path.join(dataset_path, "data", f"{video_name}")
        return function(video_name, *args, **kwargs)
    return altered_function

@file_path
def flush_data(file_path: str, array: list) -> None:
    np.save(file_path, array)

@file_path
def load_data(file_path: str) -> list:
    try:
        return np.load(file_path).tolist()
    except FileNotFoundError:
        return []

@file_path
def flush_extract(file_path: str, **kwargs) -> None:
    np.savez(file_path, **kwargs)

def get_video_path(video_name: str) -> str:
    return path.join(video_folder_path, f"{video_name}.mp4")