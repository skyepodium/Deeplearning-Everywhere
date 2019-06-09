# 텐서플로우 기본

## 1. Data Flow Graph
그래프 - 정점(node)과 간선(edge)로 이루어진 자료구조

data flow graph에서
- 노드 - 하나의 오퍼레이션(어느 값을 받으면 이런 행동을 한다)
- 간선 - 데이터, 노드들 간의 데이터의 입출력 관계를 나타낸다.

1. 그래프를 빌드
2. session.run(op) 세션에 operation을 넣어서 그래프를 실행
3. 그래프속의 어떤 값을 업데이트하거나 리턴

placeholder로 특별한 노드를 만들어준다.

1. 그래프를 정의(노드를 constant, placeholder)로 정의
2. session을 만들고 값을 넘겨준다. 실행
3. 업데이트하거나 리턴한다.

Tensor란?

기본적으로는 배열

1. Ranks - 몇차원 배열인가?
2. Shape - 각각의 엘리먼트에 몇개씩 들어있는가?
3. Types - 대부분 float32사용

## 2. 설치
- python3 가 꼭 필요합니다.
### 1) 작업을 진행할 빈 폴더 생성
```
# 빈 폴더를 하나 생성합니다.
mkdir Deeplearning-test
```
### 2) 파이썬 라이브러리를 저장할 가상환경을 생성합니다.
```
python3 -m venv venv
```

### 3) 가상환경 실행
```
# 가상환경을 실행합니다.
source vevn/bin/activate

# 명령어는 가상환경을 해제합니다. (지금은 하지 마세요!)
deactivate 
```

### 4) 텐서플로우 설치
```
# pip3를 사용하기 때문에 필요는 없는데 자꾸 warning보여주니 upgrade 해줍니다.(갠취)
pip install --upgrade pip

# 텐서플로우를 설치합니다. (가상환경에 tensorflow가 설치됩니다.)
pip3 install tensorflow --upgrade
```