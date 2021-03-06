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


## Another dataset
### Emission Matrix
Wear\Day| SUNNY | SNOWY | WINDY | RAINY | CLOUDY
---     |---    | ---   |---    |---    |---
Casual  |0.31   |0.2    |0.18   |0.13   |0.5
Raincoat|0.12   |0.2    |0.29   |0.4    |0.2
Jacket  |0.06   |0.49   |0.32   |0.35   |0.1
Briefs  |0.51   |0.11   |0.31   |0.12   |0.2

### Transmmision matrix
Next Day\Day| SUNNY | SNOWY | WINDY | RAINY | CLOUDY | START
---         |---    | ---   |---    |---    |---     |---
SUNNY       |0.52   |0.01   |0.17   |0.07   |0.09    |0.2
SNOWY       |0.26   |0.62   |0.35   |0.01   |0.06    |0.2
WINDY       |0.10   |0.08   |0.05   |0.46   |0.22    |0.2
RAINY       |0.01   |0.02   |0.35   |0.41   |0.36    |0.2
CLOUDY      |0.10   |0.26   |0.07   |0.04   |0.26    |0.2
STOP        |0.01   |0.01   |0.01   |0.01   |0.01    |0

- Needs to be checked again

### Observation
- In `dataset.txt`, genrated randomly by `dataset.py`

