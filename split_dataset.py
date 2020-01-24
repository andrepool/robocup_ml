#!/usr/bin/env python

# Copyright 2019-2020 Andre Pool
# SPDX-License-Identifier: Apache-2.0

# split all jpg's over the train.tx and test.txt

import glob, os

image_dirs = []


image_dirs.append('20190606/r2')
image_dirs.append('20190606/r4')
image_dirs.append('20190706/r5')
# image_dirs.append('20190706/r5_difficult')
image_dirs.append('20190707/r3')
image_dirs.append('20190707/r4')
image_dirs.append('20190926/r4')
image_dirs.append('20190926/r6')
image_dirs.append('20191203/r1')
image_dirs.append('20200123/r1')

train_set = open('train.txt', 'w')  
test_set = open('test.txt', 'w')
valid_set = open('valid.txt', 'w')
train_amount = 0
test_amount = 0
valid_amount = 0


for image_dir in image_dirs:
   print('collect from directory: %s' % image_dir )
   
   # re-start the split counter for each directory, so once a jpg is part of the
   # train set, it will not become part of the test set if another directory is added
   split_counter = 0

   for file_name in sorted(glob.glob(image_dir +"/*.jpg")) :
      # print("%s" % file_name )
      if split_counter == 8 : # 10 percent excluded for testing
         test_set.write("robocup_ml/" + file_name + "\n")
         split_counter += 1
         test_amount += 1
      elif split_counter == 9 : # 10 percent excluded for validation
         valid_set.write("robocup_ml/" + file_name + "\n")
         split_counter = 0
         valid_amount += 1
      else :
         train_set.write("robocup_ml/" + file_name + "\n")
         split_counter += 1
         train_amount += 1
      

print('train jpg: %d, test jpg: %d and total jpg: %d' % (train_amount, test_amount, train_amount + test_amount))
print('all done')
