# A warming-up exercise
sudo port selfupdate
sudo port upgrade installed
sudo port uninstall inactive

# Install Python and Virtualenv.
sudo port install python27 +readline
sudo port install py27-setuptools
sudo port install py27-pip
sudo port -f activate py27-pip
sudo port select --set pip pip27
sudo port install py27-virtualenv py27-virtualenvwrapper
sudo port select --set virtualenv virtualenv27

# Create an environment for TensorFlow.
virtualenv --system-site-packages TensorFlow
source ~/TensorFlow/bin/activate
pip install numpy --upgrade
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py2-none-any.whl
#export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py2-none-any.whl
pip install --upgrade $TF_BINARY_URL
pip install opencv-python
pip install opencv-contrib-python

# Run a test.
python
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))
quit()

# Quit.
deactivate
