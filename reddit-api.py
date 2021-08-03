import praw
from PIL import Image, ImageFilter
import urllib.request
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

def user_gui():
    root = Tk()
    height = int(root.winfo_screenheight())
    width = int(root.winfo_screenwidth())
    canvas = Canvas(root, width = width, height = height)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("yourname.jpg"))  
    canvas.create_image(800, 450, anchor=CENTER, image=img) 
    root.mainloop() 

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
        submission = reddit.subreddit("spaceporn").random()
        post_url = str(submission.url)
        one_post = False
        if post_url.endswith("jpg") or post_url.endswith("jpg") or post_url.endswith("png"):
            urllib.request.urlretrieve(post_url,"space")
            img = Image.open("space")
            img.show()
            print(post_url + " " + submission.title)
            one_post == True
#Since the subreddit obviously has a limited number of posts, there is a chance where you get repeats
def main():
    reddit = login_to_reddit()
    get_posts(reddit)

if __name__ == "__main__":
    main()

