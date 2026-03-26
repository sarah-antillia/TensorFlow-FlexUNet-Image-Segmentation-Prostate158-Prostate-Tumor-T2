<h2>TensorFlow-FlexUNet-Image-Segmentation-Prostate158-Prostate-Tumor-T2 (2026/03/26)</h2>
Sarah T. Arai<br>
Software Laboratory antillia.com<br><br>
This is the first experiment of Image Segmentation for <b>Prostate158 Prostate Tumor (2 classes)</b> based on 
our <a href="./src/TensorFlowFlexUNet.py">TensorFlowFlexUNet</a>
 (<b>TensorFlow Flexible UNet Image Segmentation Model for Multiclass</b>), and a 512x512 pixels PNG
 <a href="https://drive.google.com/file/d/1d1rYU9apf95QF_O43wFG3Mrz794i5GM2/view?usp=drive_link">
Augmented-Prostate158-T2-ImageMask-Dataset.zip</a> (RESTRICTED), which was derived by us from <br><br>
 <b>T2 subset </b> of 
<a href="https://zenodo.org/records/6481141">
<b>Prostate158 - Training data</b>
</a> on the zenodo.org
<br><br>
<hr>
<b>Actual Image Segmentation for Prostate158-T2 Images of 512x512 pixels</b><br>
As shown below, the inferred masks predicted by our segmentation model trained by the dataset appear similar to the ground truth masks.
<br><br>
<b>rgb_map = {anatomical zone:green, tumor:red} </b>
<br><br>
<table>
<tr>
<th>Input: image</th>
<th>Mask (ground_truth)</th>
<th>Prediction: inferred_mask</th>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/images/10002_9.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/masks/10002_9.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test_output/10002_9.png" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/images/10003_14.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/masks/10003_14.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test_output/10003_14.png" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/images/10042_17.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/masks/10042_17.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test_output/10042_17.png" width="320" height="auto"></td>
</tr>
</table>
<hr>
<br>
<h3>1 Dataset Citation</h3>
The dataset used here was taken from <br><br>
 <b>T2 subset </b> of 
<a href="https://zenodo.org/records/6481141">
<b>Prostate158 - Training data</b>
</a> on the zenodo.org
<br>
</a> on the zenodo web site.
The following explanation was taken from the zenodo web site 
<br><br>
<b>Keno Bressem, Lisa Adams, Günther Enge</b><br><br>
<b>Citation</b><br
Keno Bressem, Lisa Adams, & Günther Engel. (2022). Prostate158 - Training data [Data set]. <br>
In Computers in Biology and Medicine (Version 1, Vol. 148, p. 105817). Zenodo.<br>
<a href="https://doi.org/10.5281/zenodo.6481141">https://doi.org/10.5281/zenodo.6481141</a>
<br><br>
For more information, please refer to 
<a href="https://www.sciencedirect.com/science/article/abs/pii/S0010482522005789">
Prostate158 - An expert-annotated 3T MRI dataset and algorithm for prostate cancer detection</a>
<br><br>
<b>License</b><br>
Unknown
</a>
<br>
<br>
<h3>
2 Prostate158-T2 ImageMask Dataset
</h3>
 If you would like to train this Prostate158-T2 Segmentation model by yourself,
 please download the dataset from the google drive  
 <a href="https://drive.google.com/file/d/1d1rYU9apf95QF_O43wFG3Mrz794i5GM2/view?usp=drive_link">
Augmented-Prostate158-T2-ImageMask-Dataset.zip</a> (RESTRICTED)
, expand the downloaded ImageMaskDataset and put it under <b>./dataset</b> folder to be
<br>
<pre>
./dataset
└─Prostate158-T2
    ├─test
    │   ├─images
    │   └─masks
    ├─train
    │   ├─images
    │   └─masks
    └─valid
        ├─images
        └─masks
</pre>
<br>
<b>Prostate158-T2 Statistics</b><br>
<img src ="./projects/TensorFlowFlexUNet/Prostate158-T2/Prostate158-T2_Statistics.png" width="512" height="auto"><br>
<br>
As shown above, the number of images of train and valid datasets is not so large to use for the
 training set of our segmentation model.
<br>
<br>
We generated our augmented PNG dataset with colorized masks (<b>anatomical zone:green, tumor:red</b>) 
by using an offline augmentation tool <a href="./generator/ImageMaskDatasetGenerator.py">ImageMaskDatasetGenerator.py</a>
, which is based on our <a href="https://github.com/sarah-antillia/Image-Deformation-Tool">Image-Deformation-Tool</a>,  

 from the following t2 NIfTI files. <br>
<pre>
./train
    ├─020
    │  ├─t2.nii.gz
    │  ├─t2_anatomy_reader1.nii.gz
    │  └─t2_tumor_reader1.nii.gz
    ├─021
        .....

    └─158
       ├─t2.nii.gz
       ├─t2_anatomy_reader1.nii.gz
       └─t2_tumor_reader1.nii.gz
</pre> 

<br>
<b>Train_images_sample</b><br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/asset/train_images_sample.png" width="1024" height="auto">
<br>
<b>Train_masks_sample</b><br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/asset/train_masks_sample.png" width="1024" height="auto">
<br>

<h3>
3 Train TensorFlowFlexUNet Model
</h3>
 We trained Prostate158-T2 TensorFlowFlexUNet Model by using the 
<a href="./projects/TensorFlowFlexUNet/Prostate158-T2/train_eval_infer.config"> <b>train_eval_infer.config</b></a> file. <br>
Please move to ./projects/TensorFlowFlexUNet/Prostate158-T2, and run the following bat file.<br>
<pre>
>1.train.bat
</pre>
, which simply runs the following command.<br>
<pre>
>python ../../../src/TensorFlowFlexUNetTrainer.py ./train_eval_infer.config
</pre>
<hr>

<b>Model parameters</b><br>
Defined a small <b>base_filters = 16 </b> and large <b>base_kernels = (11,11)</b> for the first Conv Layer of Encoder Block of 
<a href="./src/TensorFlowFlexUNet.py">TensorFlowFlexUNet.py</a> 
and a large num_layers (including a bridge between Encoder and Decoder Blocks).
<pre>
[model]
;You may specify your own UNet class derived from our TensorFlowFlexModel
model         = "TensorFlowFlexUNet"
image_width    = 512
image_height   = 512
image_channels = 3
input_normalize = True
normalization  = False
num_classes    = 3
base_filters   = 16
base_kernels   = (11,11)
num_layers     = 8
dropout_rate   = 0.04
dilation       = (1,1)
</pre>
<b>Learning rate</b><br>
Defined a small learning rate.  
<pre>
[model]
learning_rate  = 0.00007
</pre>
<b>Loss and metrics functions</b><br>
Specified "categorical_crossentropy" and <a href="./src/dice_coef_multiclass.py">"dice_coef_multiclass"</a>.<br>
<pre>
[model]
loss           = "categorical_crossentropy"
metrics        = ["dice_coef_multiclass"]
</pre>
<b>Dataset class</b><br>
Specifed <a href="./src/ImageCategorizedMaskDataset.py">ImageCategorizedMaskDataset</a> class.<br>
<pre>
[dataset]
class_name    = "ImageCategorizedMaskDataset"
</pre>
<br>
<b>Learning rate reducer callback</b><br>
Enabled learing_rate_reducer callback, and a small reducer_patience.
<pre> 
[train]
learning_rate_reducer = True
reducer_factor     = 0.4
reducer_patience   = 4
</pre>
<b>Early stopping callback</b><br>
Enabled early stopping callback with patience parameter.
<pre>
[train]
patience      = 10
</pre>
<b>RGB Color map</b><br>
Specifed rgb color map dict for Prostate158-T2 1+2 classes.<br>
<pre>
[mask]
mask_datatyoe    = "categorized"
mask_file_format = ".png"
;Prostate158-T2 1+2 classes.
rgb_map = {(0,0,0):0, (0, 255, 0):1, (0,0,255):2}
</pre>
<b>Epoch change inference callback</b><br>
Enabled <a href="./src/EpochChangeInferencer.py">epoch_change_infer callback</a></b>.<br>
<pre>
[train]
epoch_change_infer       = True
epoch_change_infer_dir   =  "./epoch_change_infer"
num_infer_images         = 6
</pre>
By using this callback, on every epoch_change, the inference procedure can be called
 for 6 images in <b>mini_test</b> folder. This will help you confirm how the predicted mask changes 
 at each epoch during your training process.<br> 
<br> 
As shown below, early in the model training, the predicted masks from our UNet segmentation model showed 
discouraging results.
 However, as training progressed through the epochs, the predictions gradually improved. 
 <br> 
<br>
<b>Epoch_change_inference output at starting (epoch 1,2,3)</b><br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/asset/epoch_change_infer_at_start.png" width="1024" height="auto"><br>
<br>
<b>Epoch_change_inference output at middlepoint (epoch 31,32,33)</b><br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/asset/epoch_change_infer_at_middle.png" width="1024" height="auto"><br>
<br>

<b>Epoch_change_inference output at ending (epoch 63,64,65)</b><br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/asset/epoch_change_infer_at_end.png" width="1024" height="auto"><br>
<br>

In this experiment, the training process was stopped at epoch 65 by EarlyStopping callback.<br><br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/asset/train_console_output_at_epoch65.png" width="1024" height="auto"><br>
<br>

<a href="./projects/TensorFlowFlexUNet/Prostate158-T2/eval/train_metrics.csv">train_metrics.csv</a><br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/eval/train_metrics.png" width="520" height="auto"><br>

<br>
<a href="./projects/TensorFlowFlexUNet/Prostate158-T2/eval/train_losses.csv">train_losses.csv</a><br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/eval/train_losses.png" width="520" height="auto"><br>
<br>
<h3>
4 Evaluation
</h3>
Please move to <b>./projects/TensorFlowFlexUNet/Prostate158-T2</b> folder, 
and run the following bat file to evaluate TensorFlowUNet model for Prostate158-T2.<br>
<pre>
./2.evaluate.bat
</pre>
This bat file simply runs the following command.
<pre>
python ../../../src/TensorFlowFlexUNetEvaluator.py ./train_eval_infer_aug.config
</pre>

Evaluation console output:<br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/asset/evaluate_console_output_at_epoch65.png" width="1024" height="auto">
<br><br>Image-Segmentation-Prostate158-T2

<a href="./projects/TensorFlowFlexUNet/Prostate158-T2/evaluation.csv">evaluation.csv</a><br>
The loss (categorical_crossentropy) to this <b>Prostate158-T2/test</b> was low and dice_coef_multiclass high as shown below.
<br>
<pre>
categorical_crossentropy,0.0141
dice_coef_multiclass,0.9933
</pre>
<br>
<h3>
5 Inference
</h3>
Please move to a <b>./projects/TensorFlowFlexUNet/Prostate158-T2</b> folder, and run the following bat file to infer segmentation regions for images by the Trained-TensorFlowUNet model for Prostate158-T2.<br>
<pre>
./3.infer.bat
</pre>
This simply runs the following command.
<pre>
python ../../../src/TensorFlowFlexUNetInferencer.py ./train_eval_infer_aug.config
</pre>
<hr>
<b>mini_test_images</b><br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/asset/mini_test_images.png" width="1024" height="auto"><br>
<b>mini_test_mask(ground_truth)</b><br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/asset/mini_test_masks.png" width="1024" height="auto"><br>
<hr>
<b>Inferred test masks</b><br>
<img src="./projects/TensorFlowFlexUNet/Prostate158-T2/asset/mini_test_output.png" width="1024" height="auto"><br>
<br>
<hr>
<b>Enlarged images and masks of Prostate158-T2 Images</b><br>
As shown below, the inferred masks predicted by our segmentation model trained by the dataset appear similar to the ground truth masks.
<br><br>
<b>rgb_map = {anatomical zone:green, tumor:red} </b>
<br><br>
<table>
<tr>
<th>Image</th>
<th>Mask (ground_truth)</th>
<th>Inferred-mask</th>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/images/10007_9.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/masks/10007_9.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test_output/10007_9.png" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/images/10025_6.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/masks/10025_6.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test_output/10025_6.png" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/images/10042_9.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/masks/10042_9.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test_output/10042_9.png" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/images/10042_17.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/masks/10042_17.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test_output/10042_17.png" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/images/10063_18.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/masks/10063_18.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test_output/10063_18.png" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/images/10071_16.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test/masks/10071_16.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/Prostate158-T2/mini_test_output/10071_16.png" width="320" height="auto"></td>
</tr>
</table>
<hr>
<br>
<h3>
References
</h3>
<b>1. Prostate158 - An expert-annotated 3T MRI dataset and algorithm for prostate cancer detection</b><br>
Lisa C. Adams, Marcus R. Makowski, Günther Engel, Maximilian Rattunde, Felix Busch, Patrick Asbach, <br>
Stefan M. Niehues, Shankeeth Vinayahalingam, Bram van Ginneken, Geert Litjens, Keno K. Bressem<br>
<a href="https://www.sciencedirect.com/science/article/abs/pii/S0010482522005789">
https://www.sciencedirect.com/science/article/abs/pii/S0010482522005789
</a>
<br><br>
<b>2. Dataset of prostate MRI annotated for anatomical zones and cancer</b><br>
Lisa C. Adams, Marcus R. Makowski, Günther Engel, Maximilian Rattunde, Felix Busch, Patrick Asbach,<br>
Stefan M. Niehues, Shankeeth Vinayahalingam, Bram van Ginneken, Geert Litjens, Keno K. Bressem<br>
<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9679750/">
https://pmc.ncbi.nlm.nih.gov/articles/PMC9679750/
</a>
<br><br>
<b>3.Prostate158</b><br>
<a href="https://github.com/kbressem/prostate158">https://github.com/kbressem/prostate158</a>
<<br><br>
<b>4. TensorFlow-FlexUNet-Image-Segmentation-Prostate-MRI</b><br>
Toshiyuki Arai<br>
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Prostate-MRI">
https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Prostate-MRI</a>
<br><br>
<b>5. TensorFlow-FlexUNet-Image-Segmentation-Model</b><br>
Toshiyuki Arai<br>
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Model">
https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Model</a>
<br><br>

