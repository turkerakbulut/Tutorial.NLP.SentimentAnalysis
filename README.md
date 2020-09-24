# Tutorial.NLP.SentimentAnalysis


 **Naive Bayes Classifier Algorithm**
 ````
P(class|data) = (P(data|class) x P(class)) / P(data)
````
Example : https://en.wikipedia.org/wiki/Naive_Bayes_classifier
````
Person	height (feet)	weight (lbs)	foot size(inches)
male	6.00	            180	            12
male	5.92 	            190	            11
male	5.58 	            170	            12
male	5.92 	            165	            10
female	5.00	            100	            6
female	5.50 	            150	            8
female	5.42 	            130	            7
female	5.75                150	            9


Person	mean (height)	variance (height)	mean (weight)	variance (weight)	mean (foot size)    variance (foot size)
male	5.855	        3.5033 × 10−2	        176.25	        1.2292 × 102	        11.25	            9.1667 × 10−1
female	5.4175	        9.7225 × 10−2	        132.5	        5.5833 × 102	        7.5	                1.6667

**Sample**
Person	height (feet)	weight (lbs)	foot size(inches)
sample	6	        130	        8

P(male) = 0.5
p(height|male) = 1.5789
p(weight|male) = 5.9881.10-6
p(foot size|male) = 1.3112. 10-3
posterior numerator male = 6.1984.10-9

P(female) = 0.5
p(height|female) = 2.2346.10-1
p(weight|female) = 1.6789.10-2
p(foot size|female) = 2.8669. 10-1
posterior numerator female = 5.3778.10-4

Result sample is female. (posterior numerator is greater in female case)