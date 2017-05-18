#!/usr/bin/env python3
"""Basic Tensorflow Hello-World to verify a successful installation.
   https://www.tensorflow.org/get_started/get_started"""

import tensorflow as tf

def main():
    """ Tests basic functioning of Tensorflow module. """
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    print(sess.run(hello))

if __name__ == "__main__":
    main()
