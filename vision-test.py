# python3
#
# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Example using TF Lite to classify objects with the Raspberry Pi camera."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import io
import time
import numpy as np
import picamera

from PIL import Image
from tflite_runtime.interpreter import Interpreter

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def load_labels(path):
  with open(path, 'r') as f:
    return {i: line.strip() for i, line in enumerate(f.readlines())}


def set_input_tensor(interpreter, image):
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image


def classify_image(interpreter, image, top_k=1):
  """Returns a sorted array of classification results."""
  set_input_tensor(interpreter, image)
  interpreter.invoke()
  output_details = interpreter.get_output_details()[0]
  output = np.squeeze(interpreter.get_tensor(output_details['index']))

  # If the model is quantized (uint8 data), then dequantize the results
  if output_details['dtype'] == np.uint8:
    scale, zero_point = output_details['quantization']
    output = scale * (output - zero_point)

  ordered = np.argpartition(-output, top_k)
  return [(i, output[i]) for i in ordered[:top_k]]
  

def main(interpreter, width, height, labels): 
  i=0
  decision = {}
  with picamera.PiCamera(resolution=(640, 480), framerate=30) as camera:
      stream = io.BytesIO()
      for _ in camera.capture_continuous(stream, format='jpeg', use_video_port=True):
        stream.seek(0)
        image = Image.open(stream).convert('RGB').resize((width, height), Image.ANTIALIAS)
        results = classify_image(interpreter, image)
        label_id, prob = results[0]
        stream.seek(0)
        stream.truncate()
        
        # Add -1 for imagenet 1000 simplified labels 
        decision["{}".format(results[0][1])] = results[0][0]

        print("probability: ", prob)
        if prob>=0.8: 
            print("BINGO")
            max_key = max(decision, key=decision.get)
            outcome = labels[decision.get(max_key)]
            # print(outcome)
            return outcome
            break 
#         print("This is a {} with {} confidence over {}".format(labels[label_id], prob, elapsed_ms))
#           camera.annotate_text = '%s %.2f\n%.1fms' % (labels[label_id], prob, elapsed_ms)

#           finally:
#               camera.stop_preview()
#               pass

def classify():
  # DECIDE ON LABELS INPUT
  labels = load_labels("/tmp/labels_mobilenet_quant_v1_224.txt")

  # CHOOSE INTERPRETER
  interpreter = Interpreter("/tmp/mobilenet_v1_1.0_224_quant.tflite")

  interpreter.allocate_tensors()
  _, height, width, _ = interpreter.get_input_details()[0]['shape']

  outcome = decide(interpreter, width, height, labels)

  return outcome 

main()