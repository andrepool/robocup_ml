#!/usr/bin/env python3

# Copyright 2019-2024 Andre Pool
# SPDX-License-Identifier: Apache-2.0

# split all jpg's over the train.tx and validation.txt

import glob, os

image_dirs = []


image_dirs.append('20190606/r2')
image_dirs.append('20190606/r4')
# Sydney dataset annotation incomplete and high noise level
# image_dirs.append('20190706/r5')
# image_dirs.append('20190706/r5_difficult')
# image_dirs.append('20190707/r3')
# image_dirs.append('20190707/r4')
# image_dirs.append('20190926/r4')
# image_dirs.append('20190926/r6')
# image_dirs.append('20191203/r1')
# image_dirs.append('20200123/r1')

image_dirs.append('20220715/r7')
image_dirs.append('20220716/r6')
image_dirs.append('20230709/r5')
image_dirs.append('20230709/r6')
image_dirs.append('20230709/r8')
image_dirs.append('20240222/r12')
image_dirs.append('20240222/r14')
image_dirs.append('20240222/r15')
image_dirs.append('20240606/r1')
image_dirs.append('20240606/r12')
image_dirs.append('20240606/r16')
image_dirs.append('20240716/r5')
image_dirs.append('20240717/r6')

train_set = open('train.txt', 'w')  
# test_set = open('test.txt', 'w')
validation_set = open('validation.txt', 'w')
train_amount = 0
# test_amount = 0
validation_amount = 0

for image_dir in image_dirs:
   print('collect from directory: %s' % image_dir )
   
   # re-start the split counter for each directory, so once a jpg is part of the
   # train set, it will not become part of the test set if another directory is added
   split_counter = 0

   for file_name in sorted(glob.glob(image_dir +"/*.jpg")) :
      # print("%s" % file_name )
      # if split_counter == 8 : # 10 percent excluded for testing
      #    test_set.write("" + file_name + "\n")
      #    split_counter += 1
      #    test_amount += 1
      if split_counter == 9 : # 10 percent excluded for validation
         validation_set.write("" + file_name + "\n")
         split_counter = 0
         validation_amount += 1
      else :
         train_set.write("" + file_name + "\n")
         split_counter += 1
         train_amount += 1
      

print('train jpg: %d, validationate jpg: %d and total jpg: %d' % (train_amount, validation_amount, train_amount + validation_amount))
print('all done')
