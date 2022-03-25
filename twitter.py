from SocialMedia import SocialMedia

class twitter(SocialMedia):
    
    def __init__(self,name):
         self.tweetList = []

    def createNewTweet(self,body):

        if len(body) < 280 :
            upload = True
            self.tweetList.append(body)
        else:
            upload = False
            print("Not valid")

    def getTweets(self):
        return self.tweetList

t=twitter(name="Twitter")
t.createNewTweet(input(" your Tweet : "))
print(t.getTweets())