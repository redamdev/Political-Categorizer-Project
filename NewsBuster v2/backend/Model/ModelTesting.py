from TrainingNBModel import TrainingNBModel
from PredictorModel import predictArticle
from scrapeSingleArticle import scrapeSingleArticle
import unittest

"""
    UNIT TESTING
        Need to train new and old data model methods as well as training accuracy.

        Old Data test if sources are folders in directory
        New Data test if directory path is valid and sources are folders there and then that it runs through and works.

        Training accuracy test will test if there is an available test data. So one with data and one without.

        The model methods use every other private method.

        Predict article also needs to be tested where it will be given articles from our manual checks. 

    INTEGRATION TESTING
        Use scrape article then push to model and then a wider test using the front end to receive the url which will be used by the scraper, before finally using predictor.

    USER SCENARIOS
        Do manual tests of inputting articles and receiving the bias. Take note of what it got right and what was wrong. 

        Show the saving of articles to the database.
"""

class TestModel(unittest.TestCase):

    """
        UNIT TESTS  
            
            Below are unit tests that mainly focus on catching errors.
    """

    
    def test_trainOldDataModel_Valid_Sources(self):
        newsSources = {
                "AP" : "middle",
                "CNN" : "left",
                "NBC" : "left", 
                "Forbes" : "middle", 
                "Newsweek" : "right", 
                "Daily_Caller" : "right",
                "RightManual" : "right",
                "LeftManual" : "left",
                "MiddleManual" : "middle"
            }
        
        model = TrainingNBModel()

        with self.assertRaises(None): # The test passes if no exceptions are raised
            model.trainOldDataModel(newsSources)

    def test_trainNewDataModel_Valid(self):
        newsSources = {
                "AP" : "middle",
                "CNN" : "left",
                "NBC" : "left", 
                "Forbes" : "middle", 
                "Newsweek" : "right", 
                "Daily_Caller" : "right",
                "RightManual" : "right",
                "LeftManual" : "left",
                "MiddleManual" : "middle"
            }
        
        model = TrainingNBModel() 
        with self.assertRaises(None): # The test passes if no exceptions are raised
            model.trainNewDataModel("NewsBuster v2/backend/Model/Articles/ScrapedArticles/", newsSources)

    def test_trainOldDataModel_Invalid_Sources(self):
        """Test if files can be found using the sources."""
        model = TrainingNBModel()
        with self.assertRaises(ValueError):
            model.trainOldDataModel("NotASource")

    def test_trainNewDataModel_Valid_Directory(self):
        """Test if files can be found using the sources and the correct directory path."""
        model = TrainingNBModel()
        with self.assertRaises(ValueError):
            model.trainNewDataModel("NewsBuster v2/backend/Model/Articles/ScrapedArticles/","NotASource")

    def test_trainNewDataModel_Invalid_Directory(self):
        """Test if files can be found using the sources and an invalid directory path."""
        model = TrainingNBModel()
        with self.assertRaises(ValueError):
            model.trainNewDataModel("NotAPath", "NotASource")


    def test_testTrainingAccuracy_on_Untrained_Model(self):
        """Tests behavior when the model is not trained."""
        model = TrainingNBModel()
        with self.assertRaises(ValueError): 
            model.testTrainingAccuracy()

    def test_testTrainingAccuracy_Without_Testing_Data(self):
        """Tests behavior when there's no testing data."""
        model = TrainingNBModel()
        model.x_test = []  
        model.y_test = []

        with self.assertRaises(ValueError):  
            model.testTrainingAccuracy()



    """
        INTEGRATION TESTING 

            Below are tests that target the integration of the model with the scraping and the front end.
    """

    def test_predictArticle_Left(self):
        """Shows a correct left prediction"""
        url = "https://www.cnn.com/2024/05/28/politics/trump-closing-arguments-trial-analysis/index.html"
        
        article = scrapeSingleArticle(url)[3]
        self.assertEqual(predictArticle(article), "left")

    def test_predictArticle_Middle(self):
        """Shows a correct middle prediction"""
        url = "https://www.newsmax.com/politics/nevada-senate-gop/2024/06/12/id/1168415/"

        article = scrapeSingleArticle(url)[3]
        self.assertEqual(predictArticle(article), "middle")

    def test_predictArticle_Right(self):
        """Shows a correct right prediction"""
        url = "https://www.foxnews.com/media/embattled-dolton-mayor-tiffany-henyard-accused-politically-targeting-towns-own-park-district"

        article = scrapeSingleArticle(url)[3]
        self.assertEqual(predictArticle(article), "right")

    def test_predictArticle_Error(self):
        """Tests when a non string argument is given"""
        number = 8

        with self.assertRaises(ValueError):  
            predictArticle(number)


        
if __name__ == '__main__':
    unittest.main()  # Run your tests