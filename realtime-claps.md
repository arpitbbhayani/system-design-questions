Design Realtime Claps
===

<!--ts-->
* [Design Realtime Claps](#design-realtime-claps)
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

Imagine you have a publishing platform where writers write articles and readers read them. To appreciate the quality content, the readers _clap_ for the article by clicking the clap button present next to the article.

![Designing Realtime Claps](https://user-images.githubusercontent.com/4745789/137951051-3d18a202-e719-4e9c-a430-d8da6ddebaec.png)
The clap button looks as shown above and the number `156` beneath it is the total number of claps the article has received to date. When any user (reader or writer) opens the page the total clap count it fetched from the database and rendered on the page.

Design a realtime gratification system, that updates the _clap_ count as soon as someone clapped for the article; which means all the users who are reading the same article at the same time should, in realtime, see that someone else clapped for the article.

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - multiple readers reading the same article
 - when one reader _claps_ an article, other readers get an realtime update
 - the clap count on an article to update in realtime
 - **100,000** concurrent users on the platform
 - **10,000** concurrent users reading the same article (at peak)

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

- build an interface allowing multiple readers read an article
- place a button and a clap counter next to the article's body
- when one user clicks the clap button, the count updates in the database
- the event is then sent to all the readers reading the same article

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|NodeJS, any other that supports socket IO|
|Database|MongoDB, MySQL, any of your liking|
|Library|SocketIO|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- IO calls in NodeJS are asynchronous
- if you are broadcasting the status update, do not do it to "all" the users  

# Outcome

##  You'll learn

- realtime communication through SocketIO
- database schema design and deciding what data to store to make this efficient
- optimizing by batching

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->