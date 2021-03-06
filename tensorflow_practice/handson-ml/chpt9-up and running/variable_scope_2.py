import tensorflow as tf

n_features = 3


def relu(X):
    with tf.variable_scope("relu", reuse=True) as scope:
        threshold = tf.get_variable("threshold")

        w_shape = (int(X.get_shape()[1]), 1)
        print('w.shape: ', w_shape)
        w = tf.Variable(tf.random_normal(w_shape), name="weights")
        b = tf.Variable(0.0, name="bias")
        z = tf.add(tf.matmul(X, w), b, name="z")
        return tf.maximum(z, threshold, name="max")


X = tf.placeholder(tf.float32, shape=(None, n_features), name="X")

# declare `threshold` variable first
with tf.variable_scope("relu") as scope:
    threshold = tf.get_variable("threshold", shape=(), initializer=tf.constant_initializer(0.))

relus = [relu(X) for x in range(5)]
output = tf.add_n(relus, name="output")

train_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)

print(train_vars)

"""
train_vars = [   
    <tf.Variable 'relu/threshold:0' shape=() dtype=float32_ref>,
    <tf.Variable 'relu_1/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_1/bias:0' shape=() dtype=float32_ref>,
    <tf.Variable 'relu_2/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_2/bias:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu_3/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_3/bias:0' shape=() dtype=float32_ref>,
    <tf.Variable 'relu_4/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_4/bias:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu_5/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_5/bias:0' shape=() dtype=float32_ref>]
]
"""
