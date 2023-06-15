import os
import numpy as np
from PIL import Image
import csv

directory = "/Users/dhruvchowdhary/Downloads/img"

# Get all the directories within the specified directory
folder_names = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

# Get PNG image to an RGB array format
def img_to_rgb(img_path):
    # Open the image and convert it to RGB
    image = Image.open(img_path)
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Convert the image to a NumPy array
    image_array = np.array(image)

    return image_array

# Directory path containing the images
img_directory = "/Users/dhruvchowdhary/Downloads/img"

# List to store the image arrays and corresponding directory names
image_data = []
i = 0
# Iterate through the images in the directory
for root, dirs, files in os.walk(img_directory):
    for file in files:
        if file.endswith(".jpg"):
            i = i + 1
            if i % 1000 == 0:
                print(i)
            # Get the full path of the image file
            img_path = os.path.join(root, file)

            # Call the img_to_rgb() function to get the RGB array
            img_array = img_to_rgb(img_path)

            # Extract the directory name
            directory_name = os.path.basename(root)

            # Append the RGB array and directory name to the image_data list

            image_data.append((img_array, directory_name))

output_file = "/Users/dhruvchowdhary/FashionAI/process_data.csv"
# Save the image_data as a CSV file
print(image_data)

with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(image_data)

print("CSV file saved successfully.")


