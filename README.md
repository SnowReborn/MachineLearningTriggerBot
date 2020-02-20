# MachineLearningTriggerBot
Nani Nani Triggerbot with Machine Learning?

Screencapture to collect image data and translate into numpy matrix

Numpy matrix data feed into OPENCV2 for processing, color filtering

Tensorflow Keras for convolutional neuronetwork to recognize correct image to generate model from trainning data / verify

Win32py to capture screen with highest Frame per second compared to pillow or d3d, but has similar speed compared to msm

Real time image capture following mouse cursor, the most up to date image will be fed into the model and compared, if they are positive result, click the mouse button (hence triggerbot)

tested works on aimbooster.com, CSGO, humanbenchmark.com

Implemented Multi Thread support to solve latency issue, enabling faster image grab process \ no wait time for model comparison.

Automatically generates splite folder which evenly and randomly separates raw trainning data images into groups of "Trainning data", "verify data", and "validation data".

Also created FPS version of model comparison triggerbot, which revised screencapture method, instead of following cursor, the Capture will always be located at the center of screen with 500x500 resolution pixel counts.
