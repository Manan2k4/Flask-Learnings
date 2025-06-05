import tensorflow as tf
print(tf.__version__)
print("TensorFlow is working!" if tf.constant(42).numpy() == 42 else "TensorFlow is haunted")
