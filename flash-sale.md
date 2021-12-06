Design Flash Sale
===

<!--ts-->
* [Design Flash Sale](#design-flash-sale)
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

Design flash sale that supports sale of a fixed inventory in a very short amount of time.

The flow of the sale to be supported by the system is

 - flash sale announced for XPhone
 - the flash sale aims to sell 1000 XPhones [fixed inventory]
 - user can buy only one XPhone during the sale
 - user waits for the flash sale to start
 - flash sale starts
 - the first 1000 are allowed to add XPhones to their cart
 - the user is given a time of 5 minutes to make the payment
 - if user completes the payment within 5 minutes, the XPhone is sold to that user
 - if the payment fails, the XPhone is allowed to be purchased by other users

Note: Flash Sale and Ticket booking systems have the exact same flow; the only thing that varies is the expected througput and scale.

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - given that the inventory is fixed, ensure that only `N` people can add items to the cart
 - if the payment is unsuccessful or was not made, make the item available for other users to purchase
 - throughput of the database should not be affected

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

- allows a fixed number of people to add an item to their cart
- handle error cases when with external payment flows by simulating network calls

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|Golang, Java, C++|
|Database|MySQL|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- distributed transactions are costly
- locking rows for too long will hamper performance of the database

# Outcome

##  You'll learn

- database locking
- breaking a daunting task into managable sub-tasks and tackle them one by one
- building resilient workflows

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->