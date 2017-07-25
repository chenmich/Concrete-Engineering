from flask import render_template
from .models import PostUI

post_title = "How To Start a Blog – Beginner’s Guide for 2017"
post_content = "The emergence and growth of blogs in the late 1990s coincided with the advent of web publishing tools that facilitated the posting of content by non-technical users who did not have much experience with HTML or computer programming. Previously, a knowledge of such technologies as HTML and File Transfer Protocol had been required to publish content on the Web, and as such, early Web users tended to be hackers and computer enthusiasts. In the 2010s, the majority are interactive Web 2.0 websites, allowing visitors to leave online comments, and it is this interactivity that distinguishes them from other static websites.[2] In that sense, blogging can be seen as a form of social networking service. Indeed, bloggers do not only produce content to post on their blogs, but also often build social relations with their readers and other bloggers.[3] However, there are high-readership blogs which do not allow comments."

posts = []
post = PostUI()
post.author_id = 1
post.author_name = '匡飞龙'
post.post_title = post_title
post.post_body = post_content
posts.append(post)
posts.append(post)
def index():
    return render_template('index.html', posts=posts)
