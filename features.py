from abc import ABCMeta, abstractmethod
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

class AbstractFeatureModel(object):
    """
    Interface for all feature extractors. Extend this class to
    create new models for analyzing comment data.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_training_xy(self, data):
        """
        Extract a feature matrix X and value vector Y from the training data set.

        Args
        ----
        data : dataframe containing comments data and upvote data

        Returns
        -------
        X : numpy array (dims: ncomments x nfeatures)
            each row of X represents the features associated with each comment
        Y : numpy array (dims: ncomments)
            each entry corresponds to the value associated with each comment
            (e.g. normalized upvote score, subreddit id)

        Usage
        -----
        model = MyModel(param1, param2)
        X, Y = model.make_training(data)
        """
        pass

    @abstractmethod
    def data_to_x(self, new_data):
        """
        Extracts a feature matrix X from the new data set (for predictions), where
        the number of rows of X is the number of new data items in new_data

        Args
        ----
        new_data : dataframe containing comments data, but no label data (upvotes, subreddit)

        Returns
        -------
        X : feature matrix (num rows equal to number of entries in new_data)
        """
        pass

    @abstractmethod
    def y_to_label(self, data, Y):
        """
        Translates a y value back into its true representation (e.g. the
        denormalized upvote score, the subreddit name).

        Args
        ----
        data : dataframe containing comments data and upvote data

        Returns
        -------
        labels : The human readable label for the given Y values, len(labels) == len(Y)
        """
        pass

class BagOfWordsModel(AbstractFeatureModel):
    """
    Bag of words model. This is only an example. TODO
    """

    def __init__(self, min_df=0):
        self.vectorizer = CountVectorizer(min_df=min_df)

    def make_training_xy(self, data):
        # TODO: what columns do we have in data?
        self.vectorizer.fit(list(data.comment))
        X = self.vectorizer.transform(data.comment).tocsc()
        Y = np.array(data.upvotes)
        return X,Y

    def data_to_x(self, new_data):
        # TODO: what type is new_data?
        return self.vectorizer.transform(new_data.comment)

    def y_to_label(self, data, Y):
        # TODO: actually do something useful here
        return Y

class NGramModel(AbstractFeatureModel):
    """
    n-gram model for analyzing text
    """

    def __init__(self, n):
        # TODO
        self.n = n

    def make_training_xy(self, data):
        # TODO
        return np.array([]), np.array([])

    def data_to_x(self, new_data):
        # TODO
        return np.array([])

    def y_to_label(self, data, Y):
        # TODO
        return 0

class CooccurenceModel(AbstractFeatureModel):
    """
    Cooccurence model for analyzing text
    """

    def __init__(self):
        # TODO
        pass

    def make_training_xy(self, data):
        # TODO
        return np.array([]), np.array([])

    def data_to_x(self, new_data):
        # TODO
        return np.array([])

    def y_to_label(self, data, Y):
        # TODO
        return 0


