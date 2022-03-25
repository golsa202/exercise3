from SocialMedia import SocialMedia

class instagram(SocialMedia):
    
    def __init__(self,name):
         self.postsList = []

    def publishNewPost(self,body):

        if len(body) < 2200 :
            upload = True
            self.postsList.append(body)
        else:
            upload = False
            print("Not valid")

    def getPost(self):
        return self.postsList

insta=instagram(name="Instagram")
insta.publishNewPost(input(" your caption : "))
print(insta.getPost())