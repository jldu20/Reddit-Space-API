import praw
from PIL import Image, ImageFilter
import urllib.request

def login_to_reddit():
    reddit = praw.Reddit(
        client_id="hSl3BuMGQXUu4Qp3sKOJ_g", #Input your client ID
        client_secret="DhUA9wHJTNEIOF9jnWTlrBZJc6DcIQ", #Input the secret
        password="fire22", #Input user password
        user_agent="Programming for getting space images from /r/spaceporn", 
        username="beer_pls", #Input username
    )
    print("Successfully logged into Reddit")
    return reddit


def get_posts(reddit):
    for submission in reddit.subreddit("spaceporn").hot(limit=None):
        post_url = str(submission.url)
        one_post = False
        if post_url.endswith("jpg") or post_url.endswith("jpg") or post_url.endswith("png"):
            urllib.request.urlretrieve(post_url,"space")
            img = Image.open("space")
            img.show()
            print(post_url + " " + submission.title)
            one_post == True
        break
def main():
    reddit = login_to_reddit()
    get_posts(reddit)

if __name__ == "__main__":
    main()