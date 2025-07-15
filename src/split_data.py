import os
import shutil
import random

def split_dataset(source_dir, dest_dir, train_split=0.7, val_split=0.2):
    for class_name in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_name)
        if not os.path.isdir(class_path):
            continue

        images = os.listdir(class_path)
        random.shuffle(images)

        total = len(images)
        train_count = int(train_split * total)
        val_count = int(val_split * total)

        splits = {
            'train': images[:train_count],
            'val': images[train_count:train_count + val_count],
            'test': images[train_count + val_count:]
        }

        for split, split_images in splits.items():
            split_dir = os.path.join(dest_dir, split, class_name)
            os.makedirs(split_dir, exist_ok=True)

            for img in split_images:
                src_img_path = os.path.join(class_path, img)
                dst_img_path = os.path.join(split_dir, img)
                shutil.copy(src_img_path, dst_img_path)

# Example usage:
split_dataset("data_source/PlantVillage", "data/raw")
