# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:13:25 2021

@author: zwilliams
"""
import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import h5py


imported = tf.keras.models.load_model('Trained_modles/Minuet/')

t1 = [1.0(1091.0, 1093.0, 1098.0, 1101.0, 1097.0, 1100.0)]

prediction = imported.predict(t1)

print(prediction)

#print(tf.shape(t1))




