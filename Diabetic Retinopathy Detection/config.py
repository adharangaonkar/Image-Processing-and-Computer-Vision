# Config file where we specify all the hyperparameters of the model

## TODO



import torch
import albumentations as A # used for data augmentation
from albumentations.pytorch import ToTensorV2

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
LEARNING_RATE = 3e-5
WEIGHT_DECAY = 5e-4
BATCH_SIZE = 20
NUM_EPOCHS = 100
NUM_WORKERS = 6
CHECKPOINT_FILE = "b3.pth.tar" # the file where we are going to save the model at
PIN_MEMORY = True
SAVE_MODEL = True
LOAD_MODEL = True

# Image Augmentations

train_transforms = A.compose(
    [
        A.Resize(width= 150, height =150),
        A.RandomCrop(height= 120, width=120),
        A.Normalize(
            mean=[0.3199, 0.2240, 0.1609],
            std=[0.3020, 0.2183, 0.1741],
            max_pixel_value=255.0,
        ),
        ToTensorV2(),
    ]
)

val_transforms = A.Compose(
    [
        A.Resize(height=728, width=728),
        A.Normalize(
            mean=[0.3199, 0.2240, 0.1609],
            std=[0.3020, 0.2183, 0.1741],
            max_pixel_value=255.0,
        ),
        ToTensorV2(),
    ]
)