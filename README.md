# homework-corrector


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

