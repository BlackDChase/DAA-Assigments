# Explanation
- Let say there are two kind of days, HOT and COLD. On any particual day a man will eat either 0 or 1 or 2 ice-creams.
## Building Model
- To make a model will first approximate Emmision and transmission probabilites, explained in the later section, then we will build the model
```py
model = HMM(transmission, emission)
```
### Emmision probability
#### TABLE
Day| HOT | COLD
---|---|---
Eating 0| 0.1|0.6
Eating 1| 0.4|0.25
Eating 2| 0.5|0.15

How many  icecream a man will eat depends on the day, so ammison probability will be represented as:

```py
emission = np.array([[0.1,0.6],
                    [0.4,0.25],
                    [0.5,0.15]])
```
### Transmission Probability
#### Table
If today is | COLD | HOT | START(first day)
---|---|---|---
Tommorow will be COLD|0.7|0.1|0.5
Tommorow will be HOT|0.25|0.85|0.5
Tommorow will be STOP(last day)|0.05|0.05|0
- Tommorow's day depends on what today is, so for transmission we have a (3(START,HOT,COLD)+1(ZERO))x(3(HOT,COLD,STOP)+1(ZERO)) matrix represetend as:
```py
transmission = np.array([[0,0,0,0],
                        [0.5,0.7,0.1,0],
                        [0.5,0.25,0.85,0],
                        [0,0.05,0.05,0]])
```
## Training the model
### Observation
- Then Lets say we observe a trend where the man eats 0,1,1,2,1,2,2,2,0,1,2,2,1,0,0,1,2,2 ice-creams, then the observation will be
```py
observation = ['0','1','1','2','1','2','2','2','0','1','2','2','1','0','0','1','2','2']
```
- Based on this we will train the model to recalculate the transion and emmision probabilities
```py
model.train(observations)
```
### Our Expectation
- Seeing this observation, we will try to find how likely it is that the man will it 1,2,0,2 ice-creams on the comming days.
```py
new_seq = ['1', '2', '0','2']
```
- Now to check the likely hood of getting those outputs:
```py
likelihood = model.likelihood(new_seq)
```

