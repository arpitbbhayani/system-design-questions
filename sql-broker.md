Design a SQL backed Message Broker
===

<!--ts-->
* [Design a SQL backed Message Broker](#design-a-sql-backed-message-broker)
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

Design a SQL backed Message Broker which allows clients to enqueue messages (max 4KB in size) and dequeue them. The broker should support multiple producers and multiple consumers at the same time allowing the broker to function at high throughput. Upon processing the message the client has to explictly delete the message from the broker. Every message may have an optional expiration time post which message is not allowed to be read.

> We are building a broker on top of SQL because SQL database out-of-the-box gives us necessary toolset to build a robust broker. This exercise will help us understand the core properties we need in our broker and then we mimic them on any storage of our choice.

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - multiple producers can put message in the broker at the same time
 - multiple consumers can read the message from the broker at the same time
 - one message to be read and processed by exactly one consumer at one time
 - message once deleted should not be read by any other consume
 - every message may have an optional expiration time
 - the broker should have a high throughput

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

- is a broker on SQL database
- simulate multiple producers and consumers and see how broker behaves

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|Golang, Java, C++|
|Database|MySQL|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- in-efficient locking will choke the database
- TTL may not be the only choice

# Outcome

##  You'll learn

- core properties of any brokers
- internals of brokers
- transactions and locking in relational databases

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->