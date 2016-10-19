import tensorflow as tf

a=tf.placeholder(tf.int16)
b=tf.placeholder(tf.int16)


add=tf.add(a,b)
mul=tf.mul(a,b)

with tf.Session() as sess:
	print "add operation 99+99 =  %i" % sess.run(add, feed_dict={a:99, b:99})
	print "mul operation 8*9 = %i" % sess.run(mul, feed_dict={a:8, b:9})


