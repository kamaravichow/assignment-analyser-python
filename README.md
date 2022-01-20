# homework-corrector

![Image](https://github.com/kamaravichow/assignment-analyser-python/raw/master/question.png)


## Generating the dataset

To generate the required dataset, you'll require the font file that you use in your computer or the image you wanted to solve.
If you're on windows you should find it at `C:/Windows/Fonts`
I used roboto and opensans in this example. 

To generate data set:

```bash
cd generator
```
and then run

```bash
python3 generate.py
```

Your dataset will be created to `./train_images` folder

## Building the Tensoflow model

Refer [NOTEBOOK](https://github.com/kamaravichow/assignment-analyser-python/blob/master/notebook.ipynb) for better readablilty

## Cutting the rows

We use projection (shadow) cutting method

To calculate projection, we count pixel by pixel, see how many pixels and then record that N pixels in this line and repeat the process

refer [prepare.py](https://github.com/kamaravichow/assignment-analyser-python/blob/master/prepare.py)

The result will be something like this [ROWS](https://github.com/kamaravichow/assignment-analyser-python/tree/master/rows)

....
