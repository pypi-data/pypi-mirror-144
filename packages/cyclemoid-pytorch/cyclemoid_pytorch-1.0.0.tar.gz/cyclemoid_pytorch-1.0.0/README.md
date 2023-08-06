

![](logo.png)

This is an implementation of the cyclemoid activation function for PyTorch. 



The cyclemoid function achieved state-of-the-art results in a recent benchmark with other popular activation functions as shown below. 



![](results.png)





Note that these are early results from April 1st. An arxiv preprint will follow soon ...



## Installation



You can install the cyclemoid-pytorch package via

```python
pip install cyclemoid
```





## Usage

This package implements a `CycleMoid` class and a `cyclemoid` function. You can use these are drop-in replacements for any activation in PyTorch. For example



```python
from cyclemoid_pytorch import CycleMoid

torch.nn.Sequential(
    # ...,
    CycleMoid(), # instead of torch.nn.ReLU()
    # ...
    )
```

or

```python
from cyclemoid_pytorch import cyclemoid

# ...
def forward(self, x):
    # ...
    x = cyclemoid(x) # instead of torch.nn.functional.sigmoid(x)
```


## Demo

For a concrete usage, check out the [demo notebook].