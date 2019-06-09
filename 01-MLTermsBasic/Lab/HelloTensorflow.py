# 텐서플로우 라이브러리를 임포트해서 tf라는 별칭으로 사용
import tensorflow as tf

# Hello Tensorflow라는 문자열일 들어있는 정점(node)를 그래프에 추가합니다.
# tf.constant로 상수를 hello 변수에 저장
hello = tf.constant("Hello Tensorflow")

# 세션 객체를 생성합니다.
sess = tf.Session()

# 세션의 run메서드를 사용해서 우리가 만든 hello라는 정점(node)을 실행합니다.
print(sess.run(hello))