### Chapter 03 - 신경망

---

신경망의 중요한 성질 : 가중치 매개변수의 적절한 값을 데이터로부터 자동으로 학습하는 능력

이번 장에서는 신경망의 개요, 신경망이 입력데이터가 무엇인지 식별하는 처리 과정에 대해서 공부한다.

1. **활성화 함수**

   + 퍼셉트론 → 계단함수

   + 신경망 → 시그모이드 함수

   + "계단함수" vs "시그모이드 함수"

     |        |                           계단함수                           |                       시그모이드 함수                        |
     | :----: | :----------------------------------------------------------: | :----------------------------------------------------------: |
     | 공통점 | - 입력이 아무리 작거나 커도 출력은 0과 1<br />- 입력이 중요하면 큰 값, 중요하지 않으면 작은 값 출력 | - 입력이 아무리 작거나 커도 출력은 0과 1<br />- 입력이 중요하면 큰 값, 중요하지 않으면 작은 값 출력 |
     | 차이점 |                     - 0과 1 중 하나의 값                     |                       - 연속적인 실수                        |

     - 두 함수 모두 비선형 함수이다.

       > 비선형 함수: '선형이 아닌' 함수, 즉 직선 1개로 그릴 수 없는 함수

       층을 쌓는 혜택을 얻고 싶다면 활성화 함수로는 반드시 비선형 함수를 사용해야 한다.

   + 출력층의 활성화 함수는 풀고자 하는 문제의 성질에 맞게 정한다. (예를 들어 회귀에는 항등함수, 2클래스 분류문제는 시그모이드 함수, 다중 클래스 분류에는 소프트맥스 함수를 사용)
   
2. **소프트맥스 함수**

   - 일반적으로 회귀에는 항등함수, 분류에는 소프트맥스 함수 

   - $$
     y_k = {exp(a_k)\over \sum_{i=1}^n exp(a_i)}
     $$

     → 소프트맥스의 출력은 모든 입력 신호로부터 화살표를 받는다.

   - 문제점: 오버플로 (지수 함수이기 때문에)

     - 위 식에 임의의 정수 C 를 곱하고, exp 안에 log 의 식으로 바꾸면, 다음과 같은 식으로 바꿀 수 있다.

     - $$
       y_k = {exp(a_k + C')\over \sum_{i=1}^n exp(a_i + C')}
       $$

       → 오버플로우를 막을 목적으로 입력 신호 중 최댓값을 이용한다, 즉 어떤 정수를 더하고 빼고 결과는 바뀌지 않는다.

   - 출력 총합은 "1" → 확률로 해석 가능하다.

3. **손글씨 숫자 인식**

   이 chapter 에서는 학습과정을 생략하고, 추론과정에 대해서만 구현한다.

   - MNIST 데이터셋 불러오기
     - ```python
       import sys, os
       ...
       from dataset.mnist import load_mnist
       ...
       (x_train, t_train), (x_test, _test) = \
       load_mnist(flatten=True, normalize=False)
       ```

     - load_mnist 함수는 (훈련이미지, 훈련 레이블), (시험 이미지, 시험 레이블) 로 반환

     - normalize : 0.0 ~ 1.0 사이의 값으로 정규화 할지, 말지 (전처리)

     - flatten : 입력 이미지를 1차원 배열로 만들지, 3차원 배열로 만들지 (True 로 설정하면, 이미지를 표시할 때, 원래의 형상으로 다시 변형해야 한다. → img.reshape 함수 사용)

     - one_hot_label : [0, 0, 1, 0, 0 ,..., 0] 같이 정답을 뜻하는 원소만 1로 할지, 아니면 '7', '2' 같이 숫자 형태의 레이블로 저장할지.

   - 신경망 추론 처리

     가져온 데이터를 가지고 추론을 수행할 때, 

     get_data(), init_network(), predict() 를 사용한다.

     신경망이 예측한 답변과 정답 레이블을 비교하여 맞힌 숫자를 세고, 이를 전체 이미지 숫자로 나눠 정확도를 구함.

4. **배치 처리**

- 하나로 묶은 입력 데이터 → 효율적이고 빠르게 처리할 수 있음

- ```python
  ...
  batch_size = 100
  
  for i in range(0, len(x), batch_size):
  	x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis = 1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])
  ```

  axis = 1 : 배열 중 1번째 차원을 구성하는 원소에서 보도록.

  ex) np.array([[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.2, 0.5, 0.3]]) 에서 axis = 1의 최댓값 들은 [0.8, 0.6, 0.5] 이다.

  



