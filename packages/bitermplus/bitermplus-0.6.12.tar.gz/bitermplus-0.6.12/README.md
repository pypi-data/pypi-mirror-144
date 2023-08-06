# Biterm Topic Model

[![CircleCI](https://circleci.com/gh/maximtrp/bitermplus.svg?style=shield)](https://circleci.com/gh/maximtrp/bitermplus)
[![Documentation Status](https://readthedocs.org/projects/bitermplus/badge/?version=latest)](https://bitermplus.readthedocs.io/en/latest/?badge=latest)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/192b6a75449040ff868932a15ca28ce9)](https://www.codacy.com/gh/maximtrp/bitermplus/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=maximtrp/bitermplus&amp;utm_campaign=Badge_Grade)
[![Issues](https://img.shields.io/github/issues/maximtrp/bitermplus.svg)](https://github.com/maximtrp/bitermplus/issues)
[![Downloads](https://img.shields.io/pypi/dm/bitermplus)](https://pypi.org/project/bitermplus/)
[![Downloads](https://pepy.tech/badge/bitermplus)](https://pepy.tech/project/bitermplus)
![PyPI](https://img.shields.io/pypi/v/bitermplus)

*Bitermplus* implements [Biterm topic model](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.402.4032&rep=rep1&type=pdf) for short texts introduced by Xiaohui Yan, Jiafeng Guo, Yanyan Lan, and Xueqi Cheng. Actually, it is a cythonized version of [BTM](https://github.com/xiaohuiyan/BTM). This package is also capable of computing *perplexity* and *semantic coherence* metrics.

## Development

Please note that bitermplus is actively improved.
Refer to [documentation](https://bitermplus.readthedocs.io) to stay up to date.

## Requirements

* cython
* numpy
* pandas
* scipy
* scikit-learn
* tqdm

## Setup

### Linux and Windows

There should be no issues with installing *bitermplus* under these OSes. You can install the package directly from PyPi.

```bash
pip install bitermplus
```

Or from this repo:

```bash
pip install git+https://github.com/maximtrp/bitermplus.git
```

### Mac OS

First, you need to install XCode CLT and [Homebrew](https://brew.sh).
Then, install `libomp` using `brew`:

```bash
xcode-select --install
brew install libomp
pip3 install bitermplus
```

## Example

### Model fitting

```python
import bitermplus as btm
import numpy as np
import pandas as pd

# IMPORTING DATA
df = pd.read_csv(
    'dataset/SearchSnippets.txt.gz', header=None, names=['texts'])
texts = df['texts'].str.strip().tolist()

# PREPROCESSING
# Obtaining terms frequency in a sparse matrix and corpus vocabulary
X, vocabulary, vocab_dict = btm.get_words_freqs(texts)
tf = np.array(X.sum(axis=0)).ravel()
# Vectorizing documents
docs_vec = btm.get_vectorized_docs(texts, vocabulary)
docs_lens = list(map(len, docs_vec))
# Generating biterms
biterms = btm.get_biterms(docs_vec)

# INITIALIZING AND RUNNING MODEL
model = btm.BTM(
    X, vocabulary, seed=12321, T=8, M=20, alpha=50/8, beta=0.01)
model.fit(biterms, iterations=20)
p_zd = model.transform(docs_vec)

# METRICS
perplexity = btm.perplexity(model.matrix_topics_words_, p_zd, X, 8)
coherence = btm.coherence(model.matrix_topics_words_, X, M=20)
# or
perplexity = model.perplexity_
coherence = model.coherence_

# LABELS
model.labels_
# or
btm.get_docs_top_topic(texts, model.matrix_docs_topics_)
```

### Results visualization

You need to install [tmplot](https://github.com/maximtrp/tmplot) first.

```python
import tmplot as tmp
tmp.report(model=model, docs=texts)
```

![Report interface](images/topics_terms_plots.png)

## Tutorial

There is a [tutorial](https://bitermplus.readthedocs.io/en/latest/tutorial.html)
in documentation that covers the important steps of topic modeling (including
stability measures and results visualization).
