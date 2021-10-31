Design a Realtime Database
===

<!--ts-->
* [Design a Realtime Database](#design-a-realtime-database)
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

Design a modern realtime KV database that sends realtime updates to all the users connected to it. Users subscribe to tables and anytime a KV is added, updated, or deleted the change is broadcasted to all the users, updating their view/application in realtime.

![Relog - Realtime Database](https://user-images.githubusercontent.com/4745789/139183521-43e7a5c8-a629-4f85-9584-21dd873d0ade.png)

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - updates made by one user in one table is broadcasted to all users subscribed to it
 - one table has at max **100** subscribers
 - there are **1 million** such tables
 - one user can subscribe to **1** table at one time

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

- an interface to subscribe to one table and perform CRUD operations
- use KV store that was building as part of [Design SQL backed KV Store](sql-kv.md) exercise
- simulate multiple users subscribing to tables through different browser sessions

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|NodeJS, Golang or any that supports SocketIO|
|Framework|SocketIO|
|Database|KV store built by you, or any database of your liking|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- fan-outs take time
- do not boradcast the update before persisting it

# Outcome

##  You'll learn

- realtime communication using SocketIO
- scaling sockets to millions of concurrent people
- building realtime database with a great UX

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->