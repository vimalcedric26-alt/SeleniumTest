from _test_pom.seleniumpractice import Guvi


url = "https://www.guvi.in/"
myguvi = Guvi(url)

class Test_automation:
   def test_positive_url(self):
    expected_url = "https://www.guvi.in/"
    actual_url = myguvi.fetch_url()
    assert expected_url == actual_url
    print("Test case passed")

   def test_negative_url(self):
        expected_url = "https://www.mentor.in/"
        actual_url = myguvi.fetch_url()
        assert expected_url != actual_url
        print("SUCCESS: Test Negative URL Passed")

   def test_positive_title(self):
       expected_title = "GUVI | Learn to code in your native language"
       actual_title = myguvi.fetch_title()
       assert expected_title == actual_title
       print("Success: Test case passed")

