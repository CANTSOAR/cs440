# CS 440 Assignment 2

The zip includes `HW2.pdf`, `hw2.ipynb`, the assignment helpers and the data.

For local use, install Python 3.10 or newer, Jupyter, PyTorch, NumPy and matplotlib:

    python3 -m pip install jupyter torch numpy matplotlib

1. Extract the starter zip. From the `cs440-hw2` folder, run `python3 -m jupyter notebook`,
   open `hw2.ipynb`, and run the first code cell.
2. Write your code and answers in the cells marked `# GRADED: ...`; keep those markers.
   Run cells in order as you complete each part.
3. Save the notebook and run `check("p1")`, `check("p2")`, `check("p3")`, or `check()`
   for everything. From a terminal, `python3 check.py` does the same.
4. Submit only `hw2.ipynb` on Gradescope and add all team members.

Keep `hw2.ipynb` next to the `hw2lib/` folder and do not change `hw2lib/`.
Read `HW2.pdf` for the assignment and course policies. The checks test code on examples
and check answer formats; they do not check whether numerical or multiple-choice answers are correct.

**Google Colab:** Open `hw2.ipynb` in Colab, then upload `cs440-hw2-starter.zip` using
the Files panel. Add a code cell at the top and run:

```python
!unzip -q -o /content/cs440-hw2-starter.zip -d /content
%cd /content/cs440-hw2
```

Run the notebook's setup cell, then follow steps 2–4 above. PyTorch, NumPy and matplotlib
are already installed. Repeat the upload and extraction if Colab resets the session.
Download your completed notebook (File > Download > Download .ipynb) before submitting it.

**Fashion-MNIST:** The starter includes the training and validation images. The loader
flattens each image and scales pixels to [0, 1]. No Kaggle account, extra download or GPU is needed.
