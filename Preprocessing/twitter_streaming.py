#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "448721047-atu8bO9NoJFiXhMls3WR6kDiSnfQy3lnbYkzCRQE"
access_token_secret = "HeN8BiJMLmVHZHwJlX5eUVvQspUfZbnY6OkBdPGPetHpB"
consumer_key = "DP4M3Ox574c9xLtRc9QRnlttx"
consumer_secret = "DSylVw80EeDvNYQn6Ff3AW2whPUV5f8XIddz6VUPxXTIPE87DS"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if (status==420):
        	return False


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(languages=["hi"],track=["baatein","faltu","bol","warna","kya","ke","se","lage","raho","jayegi","dilli","bjp","thanda","jawab","socha","chota","roshan","ek","ki","aur","keval","liye","khana","aap","nahi","desh","agar","hoga","bahut","samay","ki","upar","pani","bharat","yadi","mere","kya","kyon","apne","mein","pehle","adhik","dekhna","kam","jaisa","kuch",])
    #["serials","management","federal","nationalist","screenshots","outside","suggestions","valid","petrol","notes","taste"])
#languages=['und']
#["statement","anyways","bjp","strategy","immature","collect","justice","exciting","upper","liking","wish","months"])
