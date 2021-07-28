# LeNet-5 CNN for CIFAR10 Image Classification


## Data
Generally, when you have to deal with image, text, audio or video data, you can use standard python packages that load data into a numpy array. Then you can convert this array into a torch.*Tensor.
- For images, packages such as Pillow, OpenCV are useful
- For audio, packages such as scipy and librosa
- For text, either raw Python or Cython based loading, or NLTK and SpaCy are useful

Specifically for vision, PyTorch has created a package called torchvision, that has data loaders for common datasets such as Imagenet, CIFAR10, MNIST, etc. and data transformers for images, viz., torchvision.datasets and torch.utils.data.DataLoader.

This provides a huge convenience and avoids writing boilerplate code.

## Image Classes

For this project, we will use the CIFAR10 dataset. It has the classes: ‘airplane’, ‘automobile’, ‘bird’, ‘cat’, ‘deer’, ‘dog’, ‘frog’, ‘horse’, ‘ship’, ‘truck’. The images in CIFAR-10 are of size 3x32x32, i.e. 3-channel color images of 32x32 pixels in size.

![Image Classes](https://github.com/adharangaonkar/Image-Processing-and-Computer-Vision/blob/main/CIFAR10%20Image%20Classification/images/image_classes.png?raw=true "Image Classes")


## Training an Image Classifier

Steps to train an image classifier

1. Load and normalize the CIFAR10 training and test datasets using torchvision
2. Define a Convolutional Neural Network
3. Define a loss function
4. Train the network on the training data
5. Test the network on the test data


## References

* [PyTorch](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html)
* [LeNet-5](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf)
