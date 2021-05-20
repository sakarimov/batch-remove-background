import subprocess
from os import listdir

# change these to your liking
images_dir = "path/to/images"
output_dir = "path/to/output"
output_filename = "removedbg_"


# function for filtering files based on extension
# output = list
def saring_file(directory, extension):
    # file list of directory
    file_list = listdir(f"{directory}")
    the_files = []
    for i in file_list:
        the_files.append(f'{i}')
        sorted_files = [f for f in the_files if (str(f))[-3:] == f"{extension}"]
    return sorted_files


# for the subrocess to be running the " " in directory path must be converted to "\ "
conv_image_dir = images_dir.replace(" ", "\ ")
conv_output_dir = output_dir.replace(" ", "\ ")
# video and audio files variables
images_files = saring_file(directory = images_dir, extension = "jpg")

for i in images_files:
    splited = i.split(".")
    subprocess.run(f"rembg -o {conv_output_dir}/{output_filename}{splited[0]}.png {conv_image_dir}/{i} -a -ae 10", shell=True, check=True, encoding='utf-8')
