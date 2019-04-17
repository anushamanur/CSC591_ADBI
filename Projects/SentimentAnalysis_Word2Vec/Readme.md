#S upervised Learning Techniques for Sentiment Analytics

Sentiment analysis over IMDB movie reviews and Twitter data. \
Goal: Classification of tweets or movie reviews as either positive or negative. 
Models used : logistic regression , Naive Bayes classifier . 

Python version used: Python 3.5


Python libraries needed:
nltk
gensim

Can be installed using (preinstalled in VM)

sudo pip3 install -U nltk
sudo pip3 install -U gensim


Instructions to run the program:
1. Go the the directory containing the python script.
2. Make sure the data folder is in the same location
2. Run the following commands as mentioned in the project

python3 sentiment_solution.py data/imdb/ nlp
python3 sentiment_solution.py data/imdb/ d2v 
python3 sentiment_solution.py data/twitter/ nlp
python3 sentiment_solution.py data/twitter/ d2v 

Dataset used: Imdb and Twitter
