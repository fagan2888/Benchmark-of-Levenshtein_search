# Benchmark-of-Levenshtein_search
The included restaurant_nophone_training dataset was tested with a max Levenshtein edit distance of 2:
## Results
```bash
select name from restaurant_nophone_training where levenshtein_less_equal(name, '"philippe the original"', 2) <= 2;
0.00198695853199 sec
[('"philippe\'s the original"',), ('"philippe the original"',)]

Levenshtein_search algorithm:
0.00019705373871 sec
[['"philippe the original"', 0, 0.0011574074074074073], ['"philippe\'s the original"', 2, 0.0011574074074074073]]
```
In this test, the Levenshtein_search algorithm was approx. 10x faster than using an equivalent search in PostgreSQL
