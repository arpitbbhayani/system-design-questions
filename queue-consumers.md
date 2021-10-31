Design Synchronized Queue Consumers
===

<!--ts-->
* [Design Synchronized Queue Consumers](#design-synchronized-queue-consumers)
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

Say there exists a very blunt remote queue and whenever the consumers makes a network call to fetch the head of the queue, the queues removes the element and returns it. The queue does not give any protection for concurrent consumers, which means it is possible for two consumers to fetch the front of the queue and the queue returning them the same element. Given this scenario, synchronize the consumers such that a message is consumed by only one consumer.

![Relog System Design - Synchronizing consumers](https://user-images.githubusercontent.com/4745789/139275645-132ecb0a-0e39-476f-b95d-007dbac76a4e.png)

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - only **one** consumer consumes an element from the queue at any moment
 - if two consumers trying to fetch the head of the queue, one has to **wait** while other finishes
 - queue is a black box and **cannot** be altered
 - throughput of the system does **not** matter

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

- create a mock thread unsafe implementation of queue
- simulate concurrent consumers and synchronize them

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|Golang, Java, C++|
|Queue|a simple array could be a queue|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- mutexes won't work

# Outcome

##  You'll learn

- Remote locking and synchronization

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->