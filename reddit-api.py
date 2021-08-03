import praw
from PIL import Image, ImageFilter
import urllib.request
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import webbrowser
def login_to_reddit():
    reddit = praw.Reddit(
        client_id="CLIENTID", #Input your client ID
        client_secret="SECRET", #Input the secret
        password="PASSWORD", #Input user password
        user_agent="Programming for getting space images from /r/spaceporn", 
        username="USERNAME", #Input username
    )
    print("Successfully logged into Reddit")
    return reddit

def user_gui(reddit_image, post_url, post_title):
    root = Tk()
    root.title("Space image")
    height = int(root.winfo_screenheight())
    width = int(root.winfo_screenwidth())
    space_label = Label(root, text = post_url +"\t" + post_title)
    space_label.pack()
    space_label.bind("<Button-1>", lambda e: callback_url(post_url))
    canvas = Canvas(root, width = width, height = height, background = 'gray1')  
    canvas.pack()  
    reddit_image.resize((1000,500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(reddit_image)  
    canvas.create_image(1000, 500, anchor=CENTER, image=img) 
    root.mainloop() 
def callback_url(url):
    webbrowser.open_new_tab(url)

def get_posts(reddit, reddit_post):
    submission = reddit_post
    post_url = str(submission.url)
    while not post_url.endswith("jpg") and post_url.endswith("jpg") and post_url.endswith("png"):
        submission = get_posts_helper(reddit)
    urllib.request.urlretrieve(post_url,"space")
    img = Image.open("space")
    print(post_url + " " + submission.title)
    return img

def get_post_url(submission):
    return str(submission.url)

def get_post_title(submission):
    return str(submission.title)
def get_posts_helper(reddit):
    submission = reddit.subreddit("spaceporn").random()
    post_url = str(submission.url)
    one_post = False
    return submission


def main():
    reddit = login_to_reddit()
    submission = get_posts_helper(reddit)
    post_url = str(submission.url)
    post_title = get_post_title(submission)
    reddit_image = get_posts(reddit, submission)
    user_gui(reddit_image, post_url, post_title)

if __name__ == "__main__":
    main()

