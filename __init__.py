from selenium.webdriver.common.by import By
import selenium.webdriver
import selenium
import random
import time


__authors__ = [
    "raspipy on Github, Code",
    "Otto Jan Van Nieuwenhuyze, Documentation",
    "lars2800 on Github, Code"
]
__version__ = "0.0.1"


class Defenitions:
    MultibleChoiceQuestion = 0
    YesNoQuestion = 1
    Slide = 2

class Question:
    def __init__(self,type:int) -> None:
        self.type = type

class KahootClient:
    def __init__(self) -> None:

        self.pin = 0
        self.bot_name = f"bot{random.randint(0,999)}"
		
        self.webdriver = selenium.webdriver.Edge()
        self._prevNumbSlide = -1
	
    def connect(self, codePin: int, bot_name: str) -> None:
        """
        Picks random value for bot_name & connects to Kahoot with value of the variable codepin.
    

        """

        self.bot_name = bot_name
        self.pin = codePin #Kahoot Game pin.
		
        # Go to kahoot.it
        self.webdriver.get("https://kahoot.it")

        # Wait untill page loaded
        time.sleep(2.5)
        
        pinField = self.webdriver.find_element(By.XPATH , '/html/body/div/div[1]/div/div/div[1]/div[3]/div[2]/main/div/form/input')
        pinField.send_keys( str(self.pin) )
        
        pinConfirmButton = self.webdriver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div[1]/div[3]/div[2]/main/div/form/button')
        pinConfirmButton.click()
        
        # Wait till next
        time.sleep(2.5)

        userNameField = self.webdriver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div[1]/div/div[2]/main/div/form/input')
        userNameField.send_keys( bot_name )

        usernameConfirmButton = self.webdriver.find_element(By.XPATH, '/html/body/div/div[1]/div/div/div[1]/div/div[2]/main/div/form/button')
        usernameConfirmButton.click()

        # Wait till load
        time.sleep(2.5)
    
    def awaitQuizStart(self):
        
        pass
    
    def awaitSlide(self) -> Question:
        slideNumber = -1

        while ( slideNumber == self._prevNumbSlide ):
            self._prevNumbSlide = slideNumber
        
        # /html/body/div/div[1]/div/div/main/div[2]/div[2]/div
        # /html/body/div/div[1]/div/div/main/div[2]/div[2]/div

        print(self.webdriver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/main/div[2]/div[2]/div").text)



    def terminate(self):
        self.webdriver.close()

#/html/body/div/div[1]/div/div/main/div[2]/div[1]/div   Slide number
#/html/body/div/div[1]/div/div/main/div[2]/div[2]       TrueFalseHeader

# /html/body/div/div[1]/div/div/main/div[2]/div/div[1]/div

if __name__ == "__main__":
    testBot = KahootClient()

    testBot.connect( 748992, "7447994984")

    testBot.awaitQuizStart()

    print("Quiz started")

    while True:
        try:
            testBot.awaitSlide()
        except:
            pass