# Interview Prep: AlgoExpert · SystemsExpert · MLExpert

Coding, system design and ML prep for Staff/Principal interviews.

```
algoexpert/     Java 17 + Maven + JUnit 5, one class per problem
  src/main/java/<difficulty>/<category>/<Problem>.java
  src/main/java/original/   my original day-by-day solutions (kept as written)
  src/test/java/            JUnit tests per difficulty
  archive/, scala/          older module copy and Scala data-structure experiments
systemsexpert/  system design notes (markdown + mermaid), one file per question
mlexpert/       from-scratch ML in Python (numpy) + pytest, ML design notes
leetcode/, hackerrank/   unrelated practice, left as they were
```

## Build & test
```bash
# AlgoExpert (Java 17, Maven 3.9+)
cd algoexpert && mvn test

# MLExpert (Python 3.10+)
cd mlexpert && python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt && python -m pytest -q
```

Each Java file starts with a short summary of the problem in my own words, then the solution and its
time/space complexity. Problem statements are paraphrased; see algoexpert.io for the full prompts.

## AlgoExpert progress (200 problems)
| Category | Easy | Medium | Hard | Very Hard | Total |
|---|---|---|---|---|---|
| arrays | 6 | 14 | 8 | 5 | 33 |
| binarysearchtrees | 1 | 6 | 4 | 1 | 12 |
| binarytrees | 3 | 7 | 2 | 5 | 17 |
| dynamicprogramming |  | 5 | 11 | 5 | 21 |
| famousalgorithms |  | 3 | 4 | 2 | 9 |
| graphs | 1 | 8 | 2 | 4 | 15 |
| greedyalgorithms | 4 | 2 |  |  | 6 |
| heaps |  | 1 | 3 | 1 | 5 |
| linkedlists | 2 | 4 | 4 | 5 | 15 |
| recursion | 2 | 6 | 5 | 2 | 15 |
| searching | 2 | 1 | 4 | 2 | 9 |
| sorting | 3 | 1 | 3 | 2 | 9 |
| stacks |  | 8 | 2 | 1 | 11 |
| strings | 7 | 6 | 3 | 2 | 18 |
| tries |  | 1 | 3 | 1 | 5 |
| **Total** | **31** | **73** | **58** | **38** | **200** |

The problem list and difficulty labels were checked against two public mirrors of the AlgoExpert catalog
([koykov/algoexpert.io](https://github.com/koykov/algoexpert.io), [AyushiGarg13/algoexpert-solutions](https://github.com/AyushiGarg13/algoexpert-solutions)).
Each problem has its own JUnit test method covering the sample and edge cases (empty, single element, duplicates, negatives).

## SystemsExpert (13 designs + fundamentals)
See [systemsexpert/README.md](systemsexpert/README.md).

## MLExpert
Linear/ridge regression, logistic & softmax regression, GD/SGD/momentum/Adam, k-NN, k-means++, CART decision tree,
random forest, gradient boosting, Gaussian + multinomial naive Bayes, linear SVM, lasso/ridge/elastic net, k-fold CV, bias-variance demo, SVD, PCA, ALS recommender, learning to rank, MLP with backprop, metrics, preprocessing. Mapped to the 18-lesson crash course. See [mlexpert/](mlexpert/).
