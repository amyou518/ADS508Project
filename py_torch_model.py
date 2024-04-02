import torch
from torchvision import transforms, datasets, models
import torch.nn as nn
import s3fs
from PIL import Image
# Define transforms
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
# Connect to S3 bucket
s3 = s3fs.S3FileSystem(anon=False)
# Define bucket name and prefix
bucket_name = 'project508data'
prefix = 'train/'
# List files in the prefix (directory)
file_list = s3.ls(f's3://{bucket_name}/{prefix}')
# Filter out directories
class_folders = [file for file in file_list if s3.isdir(file)]
# Create a list of file paths relative to the prefix
file_paths = []
for folder in class_folders:
    class_files = s3.ls(folder)
    if len(class_files) == 0:  # If there are no subdirectories, files are directly under the prefix
        file_paths.extend([file.split(f'{prefix}/')[1] for file in class_files])
    else:
        file_paths.extend([file.split(f'{folder}/')[1] for file in class_files])
# Check if any files were found
if len(file_paths) == 0:
    raise ValueError("No images found in the specified S3 bucket and prefix.")
# Define a custom dataset class to load images from S3
class S3ImageFolderDataset(torch.utils.data.Dataset):
    def __init__(self, bucket_name, file_paths, transform=None):
        self.bucket_name = bucket_name
        self.file_paths = file_paths
        self.transform = transform
    def __len__(self):
        return len(self.file_paths)
    def __getitem__(self, idx):
        with s3.open(f's3://{self.bucket_name}/{self.file_paths[idx]}', 'rb') as f:
            image = Image.open(f).convert('RGB')
            if self.transform:
                image = self.transform(image)
        return image
# Create a custom dataset instance
s3_dataset = S3ImageFolderDataset(bucket_name, file_paths, transform)
# Create DataLoader for training
train_loader = torch.utils.data.DataLoader(s3_dataset, batch_size=8, shuffle=True)
# Determine the number of classes
num_classes = len(class_folders)
# Load pre-trained ResNet18 model
model = models.resnet18(pretrained=True)
# Replace the last fully connected layer
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, num_classes)
# Print model architecture
print(model)