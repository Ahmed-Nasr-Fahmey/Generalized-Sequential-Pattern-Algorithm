# Generalized Sequential Pattern Algorithm
 The GSP algorithm is used for mining frequent sequential patterns from sequential transactional databases. It is an extension of the Apriori algorithm for frequent itemset mining to sequential data.

A sequential pattern consists of items/events ordered by transaction time or sequence ID. The goal is to find all patterns that exceed a minimum support threshold.

The key steps of the GSP algorithm are:

Scan the database to find singleton itemsets that exceed the min sup threshold.

Generate candidate 2-sequences by joining frequent 1-sequences using an Apriori join.

Scan the database and count support for candidates to determine frequent 2-sequences.

Repeat steps 2-3 to generate candidates of length k by joining frequent (k-1)-sequences, scan database to find frequent k-sequences.

Terminate when no further candidates are generated or database is exhausted.

To reduce search space, pruning is done by avoiding generation of supersets of infrequent sequences. joins are done level-wise in a breadth-first manner to ensure completeness.

The output is a set of all qualified frequent sequences ordered by occurrence times in transactions along with their support count. This helps discover useful sequential patterns in fields like market basket analysis, web logs and bioinformatics.
