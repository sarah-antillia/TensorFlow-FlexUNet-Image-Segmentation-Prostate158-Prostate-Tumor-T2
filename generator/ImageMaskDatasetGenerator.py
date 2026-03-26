# Copyright 2026 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ImageMaskDatasetGenerator.py
# 2026/03//23

import os
import csv
import glob
import cv2
import shutil
import numpy as np
import nibabel as nib
import traceback
import math
from scipy.ndimage import map_coordinates
from scipy.ndimage import gaussian_filter

class ImageMaskDatasetGenerator:

  def __init__(self, size=512, rotation=True, augmentation=True):
    self.RESIZE = (size, size)
    self.file_format = ".png"
    self.index = 10000
    self.slice_rotation = rotation
    self.augmentation = augmentation
    self.seed    = 137

    if self.augmentation:
      self.hflip    = False
      self.vflip    = False
      self.rotation = False
      #self.ANGLES   = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
      self.ANGLES   = [90, 180, 270, ]

      self.deformation=True
      self.alpha    = 1300
      self.sigmoids = [7,8, ]
          
      self.distortion=True
      self.gaussina_filer_rsigma = 40
      self.gaussina_filer_sigma  = 0.5
      self.distortions           = [ 0.01, 0.02,  ]

      self.rsigma = "sigma"  + str(self.gaussina_filer_rsigma)
      self.sigma  = "rsigma" + str(self.gaussina_filer_sigma)
      
      self.resize = False
      self.resize_ratios = [0.8, ]

      self.barrel_distortion = False
      self.radius     = 0.3
      self.amounts    = [0.3]
      self.centers    = [(0.3, 0.3), (0.7, 0.3), (0.5, 0.5), (0.3, 0.7), (0.7, 0.7)]

      self.pincushion_distortion= False
      self.pincradius  = 0.3
      self.pincamounts = [-0.3]
      self.pinccenters = [(0.3, 0.3), (0.7, 0.3), (0.5, 0.5), (0.3, 0.7), (0.7, 0.7)]
 
  def normalize(self, image):
     min1, max1 = image.min(), image.max()
     if max1 > min1:
        image = (image - min1) / (max1 - min1) * 255.0
     else:
        image = image * 0
     return image

  def colorize_mask(self, mask1, mask2):
    h, w = mask1.shape[:2]
    colorized = np.zeros((h, w, 3), dtype=np.uint8) 
    colorized[np.equal(mask1,   1)] = (0,255,0)  #anatomy
    #colorized[np.equal(mask2, 1)] = (0,0,255)
    colorized[np.greater(mask2, 1)] = (0,0,255)  #tumor
    return colorized

  def generate(self, train_dir, output_images_dir, output_masks_dir): 

    subdirs = os.listdir(train_dir)
    print(subdirs)
    for subdir in subdirs:
      full_subdir =os.path.join(train_dir, subdir)
      
      image_file = os.path.join(full_subdir, "t2.nii.gz")
      mask1_file = os.path.join(full_subdir, "t2_anatomy_reader1.nii.gz")
      mask2_file = os.path.join(full_subdir, "t2_tumor_reader1.nii.gz")
      if os.path.exists(image_file) and os.path.exists(mask1_file) and os.path.exists(mask2_file):

        self.index += 1
        idata   = nib.load(image_file)
        mdata1  = nib.load(mask1_file)
        mdata2  = nib.load(mask2_file)
    
        images = idata.get_fdata()
        masks1 = mdata1.get_fdata()
        masks2 = mdata2.get_fdata()
        print(images.shape)
        print(masks1.shape)
        print(masks2.shape)

        n  = images.shape[2]
        n1 = masks1.shape[2]
        n2 = masks2.shape[2]

        if not (n == n1 and n1 == n2):
          raise Exception("Fatal error: Unmatched number of slices")
             
        for j in range(n):
          image  = images[:,:,j]
          mask1  = masks1[:,:,j] 
          mask2  = masks2[:,:,j] 
          #Check mask2 (tumor mask) is empty?
          if mask2.any() > 0:
            image = self.normalize(image)
            image = image.astype("uint8") 
            image = cv2.resize(image, self.RESIZE)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            if self.slice_rotation:
              image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            
            filename = str(self.index) + "_" + str(j+1) + ".png"
            out_imagefilepath = os.path.join(output_images_dir, filename )   
            cv2.imwrite(out_imagefilepath, image)
            print("Savd {}".format(out_imagefilepath))
            
            colorized = self.colorize_mask(mask1, mask2)
            if self.slice_rotation:
              colorized = cv2.rotate(colorized, cv2.ROTATE_90_CLOCKWISE)
            colorized = cv2.resize(colorized, self.RESIZE)

            out_maskfilepath = os.path.join(output_masks_dir, filename )   
            cv2.imwrite(out_maskfilepath, colorized)
            print("Savd {}".format(out_maskfilepath))

            if self.augmentation:
              self.augment(colorized, filename, output_masks_dir, border=(0, 0, 0), mask=True)
              self.augment(image,     filename, output_images_dir, border=(0, 0, 0),   mask=False)            
          else:
            print("Skipped an empty mask")

  def augment(self, image, basename, output_dir, border=(0, 0, 0), mask=False):
    border = image[2][2].tolist()
  
    print("---- border {}".format(border))
    if self.hflip:
      flipped = self.horizontal_flip(image)
      output_filepath = os.path.join(output_dir, "hflipped_" + basename)
      cv2.imwrite(output_filepath, flipped)
      print("--- Saved {}".format(output_filepath))

    if self.vflip:
      flipped = self.vertical_flip(image)
      output_filepath = os.path.join(output_dir, "vflipped_" + basename)
      cv2.imwrite(output_filepath, flipped)
      print("--- Saved {}".format(output_filepath))

    if self.rotation:
      self.rotate(image, basename, output_dir, border)

    if self.deformation:
      self.deform(image, basename, output_dir)

    if self.distortion:
      self.distort(image, basename, output_dir)

    if self.resize:
      self.shrink(image, basename, output_dir, mask)

    if self.barrel_distortion:
      self.barrel_distort(image, basename, output_dir)


  def horizontal_flip(self, image): 
    print("shape image {}".format(image.shape))
    if len(image.shape)==3:
      return  image[:, ::-1, :]
    else:
      return  image[:, ::-1, ]

  def vertical_flip(self, image):
    if len(image.shape) == 3:
      return image[::-1, :, :]
    else:
      return image[::-1, :, ]

  def rotate(self, image, basename, output_dir, border):
    H, W, c= image.shape
    for angle in self.ANGLES:      
      center = (W/2, H/2)
      rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=angle, scale=1)

      rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(self.W, self.H), borderValue=border)
      output_filepath = os.path.join(output_dir, "rotated_" + str(angle) + "_" + basename)
      cv2.imwrite(output_filepath, rotated_image)
      print("--- Saved {}".format(output_filepath))

  def deform(self, image, basename, output_dir): 
    """Elastic deformation of images as described in [Simard2003]_.
    .. [Simard2003] Simard, Steinkraus and Platt, "Best Practices for
       Convolutional Neural Networks applied to Visual Document Analysis", in
       Proc. of the International Conference on Document Analysis and
       Recognition, 2003.
    """
    random_state = np.random.RandomState(self.seed)

    shape = image.shape
    for sigmoid in self.sigmoids:
      dx = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigmoid, mode="constant", cval=0) * self.alpha
      dy = gaussian_filter((random_state.rand(*shape) * 2 - 1), sigmoid, mode="constant", cval=0) * self.alpha
      #dz = np.zeros_like(dx)

      x, y, z = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]), np.arange(shape[2]))
      indices = np.reshape(y+dy, (-1, 1)), np.reshape(x+dx, (-1, 1)), np.reshape(z, (-1, 1))

      deformed_image = map_coordinates(image, indices, order=1, mode='nearest')  
      deformed_image = deformed_image.reshape(image.shape)

      image_filename = "deformed" + "_alpha_" + str(self.alpha) + "_sigmoid_" +str(sigmoid) + "_" + basename
      image_filepath  = os.path.join(output_dir, image_filename)
      cv2.imwrite(image_filepath, deformed_image)

  # This method is based on the code of the following stackoverflow.com webstie:
  # https://stackoverflow.com/questions/41703210/inverting-a-real-valued-index-grid/78031420#78031420
  def distort(self, image, basename, output_dir):
    shape = (image.shape[1], image.shape[0])
    (w, h) = shape
    xsize = w
    if h>w:
      xsize = h
    # Resize original img to a square image
    resized = cv2.resize(image, (xsize, xsize))
    shape   = (xsize, xsize)
 
    t = np.random.normal(size = shape)
    for size in self.distortions:
      filename = "distorted_" + str(size) + "_" + self.sigma + "_" + self.rsigma + "_" + basename
      output_file = os.path.join(output_dir, filename)    
      dx = gaussian_filter(t, self.gaussina_filer_rsigma, order =(0,1))
      dy = gaussian_filter(t, self.gaussina_filer_rsigma, order =(1,0))
      sizex = int(xsize*size)
      sizey = int(xsize*size)
      dx *= sizex/dx.max()
      dy *= sizey/dy.max()

      image = gaussian_filter(image, self.gaussina_filer_sigma)

      yy, xx = np.indices(shape)
      xmap = (xx-dx).astype(np.float32)
      ymap = (yy-dy).astype(np.float32)

      distorted = cv2.remap(resized, xmap, ymap, cv2.INTER_LINEAR)
      distorted = cv2.resize(distorted, (w, h))
      cv2.imwrite(output_file, distorted)
      print("=== Saved distorted image file{}".format(output_file))

  def shrink(self, image, basename, output_dir, mask):
    print("----shrink shape {}".format(image.shape))
    h, w    = image.shape[0:2]
    pixel   = image[2][2]
    for resize_ratio in self.resize_ratios:
      rh = int(h * resize_ratio)
      rw = int(w * resize_ratio)
      resized = cv2.resize(image, (rw, rh))
      h1, w1  = resized.shape[:2]
      y = int((h - h1)/2)
      x = int((w - w1)/2)
      # black background
      background = np.zeros((w, h, 3), np.uint8)
      if mask == False:
        # white background
        background = np.ones((h, w, 3), np.uint8) * pixel
      # paste resized to background
      print("---shrink mask {} rsized.shape {}".format(mask, resized.shape))
      background[x:x+w1, y:y+h1] = resized
      filename = "shrinked_" + str(resize_ratio) + "_" + basename
      output_file = os.path.join(output_dir, filename)    

      cv2.imwrite(output_file, background)
      print("=== Saved shrinked image file{}".format(output_file))

  # This method is based on the code in the following stackoverflow.com website:
  # https://stackoverflow.com/questions/59776772/python-opencv-how-to-apply-radial-barrel-distortion
  def barrel_distort(self, image, basename, output_dir):    
    (h,  w,  _) = image.shape

    # set up the x and y maps as float32
    map_x = np.zeros((h, w), np.float32)
    map_y = np.zeros((h, w), np.float32)

    scale_x = 1
    scale_y = 1
    index   = 1000
    for amount in self.amounts:
      for center in self.centers:
        index += 1
        (ox, oy) = center
        center_x = w * ox
        center_y = h * oy
        radius = w * self.radius
           
        # negative values produce pincushion
 
        # create map with the barrel pincushion distortion formula
        for y in range(h):
          delta_y = scale_y * (y - center_y)
          for x in range(w):
            # determine if pixel is within an ellipse
            delta_x = scale_x * (x - center_x)
            distance = delta_x * delta_x + delta_y * delta_y
            if distance >= (radius * radius):
              map_x[y, x] = x
              map_y[y, x] = y
            else:
              factor = 1.0
              if distance > 0.0:
                v = math.sqrt(distance)
                factor = math.pow(math.sin(math.pi * math.sqrt(distance) / radius / 2), amount)
              map_x[y, x] = factor * delta_x / scale_x + center_x
              map_y[y, x] = factor * delta_y / scale_y + center_y
            
        # do the remap
        image = cv2.remap(image, map_x, map_y, cv2.INTER_LINEAR)
        filename = "barrdistorted_"+str(index) + "_" + str(self.radius) + "_" + str(amount) + "_" + basename
        output_filepath = os.path.join(output_dir, filename)
        cv2.imwrite(output_filepath, image)
  
  # This method is based on the code in the following stackoverflow.com website:
  # https://stackoverflow.com/questions/59776772/python-opencv-how-to-apply-radial-barrel-distortion
  def pincushion_distort(self, image, basename, output_dir):    
    (h,  w,  _) = image.shape

    # set up the x and y maps as float32
    map_x = np.zeros((h, w), np.float32)
    map_y = np.zeros((h, w), np.float32)

    scale_x = 1
    scale_y = 1
    index   = 1000
    for amount in self.pincamounts:
      for center in self.pinccenters:
        index += 1
        (ox, oy) = center
        center_x = w * ox
        center_y = h * oy
        radius = w * self.pincradius
           
        # negative values produce pincushion

        # create map with the barrel pincushion distortion formula
        for y in range(h):
          delta_y = scale_y * (y - center_y)
          for x in range(w):
            # determine if pixel is within an ellipse
            delta_x = scale_x * (x - center_x)
            distance = delta_x * delta_x + delta_y * delta_y
            if distance >= (radius * radius):
              map_x[y, x] = x
              map_y[y, x] = y
            else:
              factor = 1.0
              if distance > 0.0:
                v = math.sqrt(distance)
                factor = math.pow(math.sin(math.pi * math.sqrt(distance) / radius / 2), amount)
              map_x[y, x] = factor * delta_x / scale_x + center_x
              map_y[y, x] = factor * delta_y / scale_y + center_y
            
        # do the remap
        image = cv2.remap(image, map_x, map_y, cv2.INTER_LINEAR)
        filename = "pincdistorted_"+str(index) + "_" + str(self.pincradius) + "_" + str(amount) + "_" + basename
        output_filepath = os.path.join(output_dir, filename)
        cv2.imwrite(output_filepath, image)
  
if __name__ == "__main__":
  try:
    train_dir   = "./train"

    output_dir   = "./Augmented-Prostate158-T2-master/"
    if os.path.exists(output_dir):
      shutil.rmtree(output_dir)
      os.makedirs(output_dir)
    
    output_images_dir = os.path.join(output_dir, "images")
    output_masks_dir  = os.path.join(output_dir, "masks")
  
    os.makedirs(output_images_dir)
    os.makedirs(output_masks_dir)
  
    generator = ImageMaskDatasetGenerator(rotation=True, augmentation=True)
       
    generator.generate(train_dir,
                        output_images_dir, 
                        output_masks_dir,)

  except:
    traceback.print_exc()