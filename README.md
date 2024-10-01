# Face Orientation Classifier using Neural Networks

This project presents a neural network capable of classifying the orientation of a face in an image into one of five categories: looking left, right, up, down, or in a neutral position. Built using Python and TensorFlow/Keras.

## Features
- **Real-time Classification**: The trained model is used to classify face orientation in real-time through a webcam feed.
  
- **Keyboard Input Simulation**: Upon classifying the face orientation, the program simulates keyboard inputs based on the detected position. This can be particularly useful in hands-free applications, including gaming, where head movements can control in-game actions.
- 
- **Custom Dataset**: The model was trained on a dataset I created. A custom Python script was developed to automate the process of capturing images and organizing them into labeled directories based on face orientation.
  


## How It Works
1. **Dataset Creation**: The dataset was created by capturing images using a Python script that assigns them to the appropriate label folder (left, right, up, down, neutral) based on the direction the face is oriented.
2. **Model Training**: A neural network was built and trained using TensorFlow/Keras. The model learns to distinguish subtle facial orientation differences.
3. **Real-time Application**: Once the model is trained, it is integrated into a central program that accesses the webcam feed, classifies the current face orientation, and simulates corresponding keyboard inputs.

## Technologies Used
- **Python**: Programming language used for developing the model, dataset generation script, and real-time application.
- **TensorFlow/Keras**: Deep learning framework used to build and train the neural network model.
- **OpenCV**: Used to capture webcam footage for real-time classification.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
