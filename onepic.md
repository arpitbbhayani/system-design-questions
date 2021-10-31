Design OnePic
===

<!--ts-->
* [Design OnePic](#design-onepic)
* [Problem Statement](#problem-statement)
* [Requirements](#requirements)
   * [Core Requirements](#core-requirements)
   * [High Level Requirements](#high-level-requirements)
   * [Micro Requirements](#micro-requirements)
* [Output](#output)
   * [Design Document](#design-document)
   * [Prototype](#prototype)
      * [Recommended Tech Stack](#recommended-tech-stack)
      * [Keep in mind](#keep-in-mind)
* [Outcome](#outcome)
   * [You'll learn](#youll-learn)
* [Share and shoutout](#share-and-shoutout)
<!--te-->

# Problem Statement

OnePic is a product that makes it easy to use one profile picture everywhere. The product let's you have one unique URL that when any website uses under `img` tag renders the image on the page. THe product also let's you upload multiple pictures and set one of them as active.

```
<img src="https://onepic.relog.in/arpit" />
```

The OnePic URL for user `arpit` will be `https://onepic.relog.in/arpit` which when put under `img` tag renders the one active profile picture of that user. This URL will be used by all other social media to render `arpit`'s profile picture. This way when `arpit` marks some other of his profile picture as active, it will take its effect on all the websites automatically, without needing him to go and update the picture on each site individually.

![Relog OnePic](https://user-images.githubusercontent.com/4745789/139574973-6bd4202d-4256-44a1-bbbd-271f9c3b745b.png)

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - user to manage **multiple** profile pictures and mark one as **active**
 - one unqiue URL used by all the websites to **render** the user's profile picture
 - **50000** photo uploads per minute
 - read to write ratio **100000:1**

##  High Level Requirements
<!--hs-->
- make your high-level components operate with **high availability**
 - ensure that the data in your system is **durable**, not matter what happens
 - define how your system would behave while **scaling-up** and **scaling-down**
 - make your system **cost-effective** and provide a justification for the same
 - describe how **capacity planning** helped you made a good design decision 
 - think about how other services will interact with your service
<!--he-->

##  Micro Requirements
<!--ms-->
- ensure the data in your system is **never** going in an inconsistent state
 - ensure your system is **free of deadlocks** (if applicable)
 - ensure that the throughput of your system is not affected by **locking**, if it does, state how it would affect
<!--me-->

# Output

## Design Document
<!--ds-->
Create a **design document** of this system/feature stating all critical design decisions, tradeoffs, components, services, and communications. Also specify how your system handles at scale, and what will eventually become a chokepoint.

Do **not** create unnecessary components, just to make design look complicated. A good design is **always simple and elegant**. A good way to think about it is if you were to create a spearate process/machine/infra for each component and you will have to code it yourself, would you still do it?
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
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->