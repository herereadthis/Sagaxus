# A/B Testing, Part 2

## Can we trust an A/B Test?

* **Statistical Power** - the probability that a test will detect a difference between two values when there **really** is a difference
  * It increases as you make your sample size larger
* Suppose you run 100 A/B Tests, with a power of 80% and significance level of 5%
  * Suppose 10 of these tests are actually positive tests
  * Then with 80% power, there are 8 successes
  * But with a significance level of 5%, there are 5 false positives
  * That means 8 + 5 = 13 successes
* The the more tests that are run, the increased chances of getting a false positive

### Can you stop a test?

* Many A/B testing tools will stop a test as soon a very large result is achieved (peeking)
  * Actually that increases the number of false positives

### Can you run multiple Tests?

* A) Run multiple A/B Tests simultaneously because something will be successful
* B) **Post Test Segmentation** - split up the samples and see which subset of subset is successful
  * Suppose &alpha;=0.05 again. If you run 20 tests that in reality don't do anything, you will get 1 positive result

### Regresion to the mean

* Test a class of students a 100-question true false test and instruct them to choose answers randomly. *E(X)* = 50
  * Take the top scoring 10% and test them again. Their next scores will be lower because *E(X)* is still 50
* If you test the winning test again, the new score will be lower.

* **Winner's Curse** - we only select the tests with the highest uplift. So we will  favor the tests with the least power.

## Sources

* [Most Winning A/B Test Results are Illusory](https://dtizncz8yxdah.cloudfront.net/media/2017/12/13074125/qubit-research-ab-test-results-are-illusory.pdf)
