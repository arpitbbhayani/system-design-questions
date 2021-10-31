Design OnePic
===

<!--ts-->
<!--te-->

# Problem Statement

OnePic is a product that makes it easy to use one profile picture everywhere. The product let's you have one unique URL that when any website uses under `img` tag renders the image on the page. THe product also let's you upload multiple pictures and set one of them as active.

```
<img src="https://onepic.relog.in/arpit" />
```

The OnePic URL for user `arpit` will be `https://onepic.relog.in/arpit` which when put under `img` tag renders the one active profile picture of that user. This URL will be used by all other social media to render `arpit`'s profile picture. This way when `arpit` marks some other of his profile picture as active, it will take its effect on all the websites automatically, without needing him to go and update the picture on each site individually.

![Relog OnePic](https://user-images.githubusercontent.com/4745789/139574973-6bd4202d-4256-44a1-bbbd-271f9c3b745b.png)

# Requirements

## Core Requirements

 - user to manage **multiple** profile pictures and mark one as **active**
 - one unqiue URL used by all the websites to **render** the user's profile picture
 - **50000** photo uploads per minute
 - read to write ratio **100000:1**

##  High Level Requirements
<!--hs-->
<!--he-->

##  Micro Requirements
<!--ms-->
<!--me-->

# Output

## Design Document
<!--ds-->
<!--de-->

## Prototype

To understand the nuances and internals of this system, build a prototype that

- built a simple static site server that serves user uploaded images
- CRUD to manage profile pictures and marking one active
- render the active profile picture whenever the image is requested through the URL

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|Golang, Java, NodeJS, C++|
|Database|Pick your favourite|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- serving images through API server is simple than it looks

# Outcome

##  You'll learn

- static file server
- read heavy systems serving static content
- database schema design

<!--fs-->
<!--fe-->
