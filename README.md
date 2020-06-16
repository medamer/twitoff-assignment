# twitoff-assignment

The "Twitoff App" data flows are like:
User provides example tweet text and selects two Twitter users to compare which is more likely to say the example tweet text.
App requests user and tweet information from the Twitter API, as necessary, to gather data about each user, and stores it in the database.
For each tweet, app makes request to Basilica API to get corresponding natural language processing embeddings, and stores them in the database.
App uses the tweet embeddings from both users to train a binary classifier model.
App makes a request to Basilica API for the natural language processing embeddings for the example tweet text, and passes those to the model as an input value in order to make predictions.
App displays prediction results to the user.
