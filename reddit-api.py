import praw
from PIL import Image, ImageFilter
import urllib.request
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
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

def user_gui(reddit_image):
    root = Tk()
    root.title("Space image")
    space_label = Label(root, text = "Space!")
    height = int(root.winfo_screenheight())
    width = int(root.winfo_screenwidth())
    canvas = Canvas(root, width = width, height = height)  
    canvas.pack()  
    reddit_image.resize((width//2,height//2))
    img = ImageTk.PhotoImage(reddit_image)  
    canvas.create_image(1000, 500, anchor=CENTER, image=img) 
    root.mainloop() 

def get_posts(reddit):
    submission = get_posts_helper(reddit)
    post_url = str(submission.url)
    while not post_url.endswith("jpg") and post_url.endswith("jpg") and post_url.endswith("png"):
        submission = get_posts_helper(reddit)
    urllib.request.urlretrieve(post_url,"space")
    img = Image.open("space")
    print(post_url + " " + submission.title)
    return img

def get_post_url(submission):
    return str(submission.url)
    
def get_posts_helper(reddit):
    submission = reddit.subreddit("spaceporn").random()
    post_url = str(submission.url)
    one_post = False
    return submission
#Since the subreddit obviously has a limited number of posts, there is a chance where you get repeats

def main():
    reddit = login_to_reddit()
    reddit_image = get_posts(reddit)
    user_gui(reddit_image)

if __name__ == "__main__":
    main()

