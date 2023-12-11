import os
import bz2

# Define the target directory where the subfolders are located.
src_directory = '/home/ubuntu/MobileFaceNet_Tutorial_Pytorch/colorferet/dvd2/data/images/'
tgt_directory = '/home/ubuntu/MobileFaceNet_Tutorial_Pytorch/dataset'
os.chdir(src_directory)
# List all the entries in the directory
entries = os.listdir('.')

# Iterate over all the entries
for entry in entries:
    # Construct the full path
    full_path = os.path.join(src_directory, entry)
    tgt_full_path = os.path.join(tgt_directory, entry)
    os.makedirs(tgt_full_path)
    print(f"Running command in {full_path}...")
    os.chdir(full_path)
    files = os.listdir('.')
    for file in files:
        file_path = os.path.join(full_path, file)
        src_path = os.path.join(tgt_full_path, file[:-4])
        with bz2.open(file_path, 'rb') as file:
            decompressed_data = file.read()

        with open(src_path, 'wb') as new_file:
            new_file.write(decompressed_data)

print("Finished running command in all subfolders.")


from PIL import Image
import os
tgt_directory = './feret'
os.chdir(tgt_directory)
entries = os.listdir('.')


for entry in entries:
    # Construct the full path
    full_path = os.path.join(tgt_directory, entry)
    os.chdir(full_path)
    files = os.listdir('.')
    for file in files:
        file_path = os.path.join(full_path, file)
        ppm_image = Image.open(file_path)
        os.remove(file_path)
        if ppm_image.mode != 'RGB':
            # Convert the grayscale image to RGB (still looks grayscale)
            ppm_image = ppm_image.convert('RGB')
        src_path = os.path.join(full_path, file[:-4] + '.jpg')
        ppm_image.save(src_path, quality=95)

        
