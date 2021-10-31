Design a Blogging Platform
===

<!--ts-->
* [Design a Blogging Platform](#design-a-blogging-platform)
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

Design a simple multi-user publishing/blogging platform, allowing writers to publish and manage the blogs under their personal publication and readers to read them.

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - writers should be able to **publish** blog under their personal publication
 - readers should be able to **read** the blog
 - a user can be both - a reader as well as a writer
 - author of the blog should be able to **delete** the blog
 - blog may **contain images**, but will not contain any video
 - time to access the blog should be **as low as possible**
 - we have to render "**number of blogs**" written by every user on his/her profile
 - users should be able to **search** for a particular blog
 - the platform should be scaled for **5 million** daily active readers
 - the platform should be scaled for **10,000** daily active writers

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

- has a realtional database with schema able to handle all the core requirements
- has an interface for writers to
   - publish the blog
   - manage the blog
- has an interface for readers to
   - browse all the publications and read the blogs
   - search a blog or a publication

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|Golang, Java, NodeJS|
|Database|Relational Database - MySQL, PostgreSQL|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- data should not be redundant in your schema

# Outcome

##  You'll learn

- database schema design
- building web application - a simple CRUD

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->