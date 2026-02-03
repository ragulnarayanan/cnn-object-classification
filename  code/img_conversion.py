from PIL import Image
import os

# 1️⃣ Input and output folders
input_folder = "/Users/rana/Documents/CNN_Photos"       # folder with your original images
output_folder = "/Users/rana/Documents/CNN_Photos/resized_images"  # folder to save resized + renamed images
os.makedirs(output_folder, exist_ok=True)

# 2️⃣ Base name for output files
base_name = "OJB001"

# 3️⃣ Resize images and rename
counter = 1
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):  # only image files
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGB")             # ensure RGB
        img = img.resize((224, 224))                          # resize to 224x224

        # Create new filename: OJB001.jpg, OJB002.jpg, ...
        new_name = f"{base_name}_{counter:03d}.jpg"
        img.save(os.path.join(output_folder, new_name))
        print(f"Saved {new_name}")
        counter += 1