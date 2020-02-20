# MachineLearningTriggerBot
Nani Nani Triggerbot with Machine Learning?

Screencapture to collect image data and translate into numpy matrix

Numpy matrix data feed into OPENCV2 for processing, color filtering

Tensorflow Keras for convolutional neuronetwork to recognize correct image to generate model from trainning data / verify

Win32py to capture screen with highest Frame per second compared to pillow or d3d, but has similar speed compared to msm

Real time image capture following mouse cursor, the most up to date image will be fed into the model and compared, if they are positive result, click the mouse button (hence triggerbot)

tested works on aimbooster.com, CSGO, humanbenchmark.com

Implemented Multi Thread support to solve latency issue, enabling faster image grab process \ no wait time for model comparison.
