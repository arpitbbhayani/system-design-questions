Design an Online Offline Indicator
===

<!--ts-->
* [Design an Online Offline Indicator](#design-an-online-offline-indicator)
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

Imagine you are building a chat application in which a user can chat with any other user, provided they are both connected. For a user to initiate the chat, it is always helpful if we show who all are online.

In this assignment, let's design a system that indicates who all are online at the moment. The micro-problem statement is as simple as answering the question - Given a user, return if he/she is online or not.

![Designing Online Offline Indicator](https://user-images.githubusercontent.com/4745789/138017480-1f7c30ce-50f2-4a50-99b5-1cf7f0778caa.png)

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - should update online status of a user within **10 seconds** of user coming online
 - can be **lineant** in marking a user offline
 - should scale for **5 million** active users at any given moment
 - a user should see accurate status of any other user, **eventually**


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

- shows a list of users
- shows if a particular user is online or offline
- the user list is grouped such that the online users are shown first and then the offline ones
- if the user is offline, also show "was online X mins ago"

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|NodeJS, or any language that supports SocketIO|
|Database|MySQL, MongoDB, or any one that you like|
|Library|SocketIO, for realtime status update|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- IO calls in NodeJS are asynchronous
- if you are broadcasting the status update, do not do it to "all" the users  


# Outcome

##  You'll learn

- identify when a user is "online"
- finding when a user goes "offline"
- database schema design and deciding what data to store to make this efficient
- building realtime user experiences using SocketIO

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->