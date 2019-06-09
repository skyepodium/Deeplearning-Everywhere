import tensorflow as tf

# 1. 그래프 빌드, tensorflow의 operation을 사용해서 그래프를 만듭니다.
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print("node1: ", node1, "node2: ", node2)
print("node3: ", node3)

sess = tf.Session()

# 2. 세션에 operation을 넣어서 실행합니다.
# 3. 그래프속의 어떤 값을 업데이트하거나 리턴합니다.
print("sess.run([node1, node2]): ", sess.run([node1, node2]))
print("sess.run(node3): ", sess.run(node3))
