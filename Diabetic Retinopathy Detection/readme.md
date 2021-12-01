# Diabetic Retinopathy Detection

## Diabetic retinopathy

Diabetic retinopathy is the leading cause of blindness in the working-age population of the developed world. It is estimated to affect over 93 million people.

The US Center for Disease Control and Prevention estimates that 29.1 million people in the US have diabetes and the World Health Organization estimates that 347 million people have the disease worldwide. Diabetic Retinopathy (DR) is an eye disease associated with long-standing diabetes. Around 40% to 45% of Americans with diabetes have some stage of the disease. Progression to vision impairment can be slowed or averted if DR is detected in time, however this can be difficult as the disease often shows few symptoms until it is too late to provide effective treatment.

Currently, detecting DR is a time-consuming and manual process that requires a trained clinician to examine and evaluate digital color fundus photographs of the retina. By the time human readers submit their reviews, often a day or two later, the delayed results lead to lost follow up, miscommunication, and delayed treatment.

Clinicians can identify DR by the presence of lesions associated with the vascular abnormalities caused by the disease. While this approach is effective, its resource demands are high. The expertise and equipment required are often lacking in areas where the rate of diabetes in local populations is high and DR detection is most needed. As the number of individuals with diabetes continues to grow, the infrastructure needed to prevent blindness due to DR will become even more insufficient.

The need for a comprehensive and automated method of DR screening has long been recognized, and previous efforts have made good progress using image classification, pattern recognition, and machine learning. With color fundus photography as input, the goal of this competition is to push an automated detection system to the limit of what is possible – ideally resulting in models with realistic clinical potential. The winning models will be open sourced to maximize the impact such a model can have on improving DR detection.

## Approach

For practice I tried to obtain a high score on this competition, obviously it's not fair since there's been a lot of advances since the deadline of the comeptition but nevertheless I think my solution is quite simple and obtains a top 1% solution in the leaderboard with a single model and no ensemble.

But let me also do a quick summary of what works (and what didn't for me). I first did a baseline solution with EfficientNet-B3 and image size of 120x120 in order for relatively quick iterations.

### BASELINE (B3, 120x120 image resolution):

- Val score: 0.55
- Public score: 0.52648
**I then added preprocessing of the images by removing the black borders and maining the aspect ratio of each.**

- Preprocess the images:
- Val score: 0.60 (+0.05)

**I then improved the loss function, first I used CrossEntropyLoss but since this doesn't correspond very well to the QuadraticWeightedKappa score, I changed to MSE.**

- Improve the loss function (MSE -> convert to integer predictions):

- Val score: 0.65 (+0.05)

- Get balanced data loader (Didn't work for me)
- (class_weights=[1,2,2,2,2] -> Doesn't work either)

- Heavy data augmentation (for some odd reason, this didn't work?)

- Val score: 0.63 (-0.02)

**Weird that we didn't get an improvement here. Thinking maybe it's the image size, maybe using some bad augmentation?**

- Blending (Left and Right eye information)

- Val score: 0.67 (+0.02)

- Increase image resolution
Res 300x300: 0.736 (+0.08)
Res 500x500: 0.787 (+0.05)
Res 728x728: 0.837 (+0.05)

**Then using left and right eye information and trained the small neural network on top of it got me:**
- Public score: 0.84613
- Private score: 0.83880

**Future Scope:**

- Train on the validation data (4000 examples)
- Larger model (B4,B5,B6,B7?)
- Larger image resolution
- Better data augmentations method (Randaugment?)
- Ensemble for the blending model (fast to train)
- Ensemble of various CNN models
- Tweaking hyperparameters
- Better loss function, better proxy for WeightedKappa
