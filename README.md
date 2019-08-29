# NMT-Chatbot
 
Built using json, sqlite, pandas and Tensorflow in Python. Link to dataset : https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/?st=j9udbxta&sh=69e4fee7

  - data_format.py : Uses sql and json to organize the data dump into threaded comments and replies.
  - train_data_setup.py : Creates sql table from the data with each comment assigned to a particular reply.
  - settings.py : Sets the hyperparameters such as Optimizer, number of layers, units, epochs, learning rate, score etc.
  - train.py : Training seq2seq model on our formatted data using Tensorflow. 
