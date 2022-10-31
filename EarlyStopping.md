# 조기 종료

- 너무 많은 epoch은 과적합을 일으키고 너무 적은 epoch은 과소적합을 일으킴
- 조기 종료 : 무조건 epoch을 많이 돌린 후, 특정 시점에서 멈추는 것
- 일반적으로 hold-out validation set에서의 성능이 더 이상 증가하지 않을 때 학습을 중지

## Early Stopping in Keras

```{python}
from keras.callbacks import EarlyStopping
```

- EalryStopping class의 구성 요소
- Performance measure : 어떤 성능을 monitoring 할 것인가?
- Trigger : 언제 학습을 멈출 것인가?

### es = EarlyStopping(monitor='val_loss)
- validation set의 손실을 관측

### es = EarlyStopping(monitor='val_loss', mode = 'min')
- default = auto
- keras에서 알아서 min, max를 선택
- 성능이 증가하지 않는다고, 그 순간 바로 멈추는 것은 효과적이지 않을 수 있음

### es = EarlyStopping(monitor='val_loss', mode = 'min',verbose=1,patience=50)
- verbose=1로 지정하면, 언제 keras에서 학습을 멈추었는지를 화면에 출력
- patience : 성능이 증가하지 않는 epoch을 몇 번이나 허용할 것인가를 정의(주관적 기준)

### es = EarlyStopping(monitor='val_loss', mode = 'min',baseline=0.4)
- 특정값에 도달했을 때, 더 이상 학습이 필요하지 않는 경우

- 최종적으로 model.fit 함수의 callback으로 조기 종료 객체를 넣어주면 조기 종료를 적용할 수 있음

```{python}
model.fit(x_train,y_train,epochs=10,batch_size=10,verbose=1,validation_split=0.2,callbacks=[early_stopping])
```

## pytorch


```{python}
class EarlyStopping:
    """주어진 patience 이후로 validation loss가 개선되지 않으면 학습을 조기 중지"""
    def __init__(self, patience=7, verbose=False, delta=0, path='checkpoint.pt'):
        """
        Args:
            patience (int): validation loss가 개선된 후 기다리는 기간
                            Default: 7
            verbose (bool): True일 경우 각 validation loss의 개선 사항 메세지 출력
                            Default: False
            delta (float): 개선되었다고 인정되는 monitered quantity의 최소 변화
                            Default: 0
            path (str): checkpoint저장 경로
                            Default: 'checkpoint.pt'
        """
        self.patience = patience
        self.verbose = verbose
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = np.Inf
        self.delta = delta
        self.path = path

    def __call__(self, val_loss, model):

        score = -val_loss #-를 곱해주었으므로 score가 높을 수록 좋은 모델
        
        # 초기 시작에는 best_score가 0이므로 들어온 val_loss를 지정 후 저장
        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
            
        # 들어온 score가 현재 성능이 가장 좋은 best_score+ delta보다 낮은 경우에는 모델을 갱신하지 않고 patience count에 1을 더해줌
        elif score < self.best_score + self.delta:
            self.counter += 1
            print(f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience: # 목표 patience에 도달하면 더 이상 모델을 진행하지 않고 학습 끝
                self.early_stop = True
        else:
            self.best_score = score #이외에 경우에는 
            self.save_checkpoint(val_loss, model)
            self.counter = 0

    def save_checkpoint(self, val_loss, model):
        '''validation loss가 감소하면 모델을 저장한다.'''
        if self.verbose:
            print(f'Validation loss decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...')
        torch.save(model.state_dict(), self.path)
        self.val_loss_min = val_loss
```
