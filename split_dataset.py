#!/usr/bin/env python

# Copyright 2019 Andre Pool
# SPDX-License-Identifier: Apache-2.0

# split all jpg's over the train.tx and test.txt

import glob, os

image_dirs = []
image_dirs.append('r1/20191203')
image_dirs.append('r2/20190606')
image_dirs.append('r3/20190707')
image_dirs.append('r4/20190606')
image_dirs.append('r4/20190707')
image_dirs.append('r4/20190926')
image_dirs.append('r6/20190926')

train_set = open('train.txt', 'w')  
test_set = open('test.txt', 'w')
train_amount = 0
test_amount = 0


for image_dir in image_dirs:
   print('collect from directory: %s' % image_dir )
   
   # re-start the split counter for each directory, so once a jpg is part of the
   # train set, it will not become part of the test set if another directory is added
   split_counter = 0

   for file_name in glob.glob(image_dir +"/*.jpg") :
      # print("%s" % file_name )
      if split_counter == 9 : # 10 percent excluded for testing
         test_set.write("robocup_ml/" + file_name + "\n")
         split_counter = 0
         test_amount += 1
      else :
         train_set.write("robocup_ml/" + file_name + "\n")
         split_counter += 1
         train_amount += 1
      

print('train jpg: %d, test jpg: %d and total jpg: %d' % (train_amount, test_amount, train_amount + test_amount))
print('all done')
