Design a faster Superfast KV Store
===

<!--ts-->
* [Design a faster Superfast KV Store](#design-a-faster-superfast-kv-store)
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

We designed a [Superfast KV Store](https://github.com/relogX/system-design-questions/blob/master/superfast-kv.md), but can we go faster than this? Let's try to model something that is faster than this superfast DB.

Design a single-node persistent KV Store that supports `GET`, `PUT` and `DEL` operations and it utilizes hardware (disk, RAM) optimally. The response time for all the 3 operations should be as low as possible and complexity of operations should be `O(1)`. It is okay for this KV store to not support infinite number of keys given it is bound to a single node, but make sure you maximize the number of keys a single node can hold.

> Note: It is okay if your storage engine cannot support very large number of keys.

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - should be able to `GET`, `PUT`, `DEL` on a key
 - all operations should happen as fast as possible with complexity of `O(1)`
 - this KV store is not distributed and will run on just a single node

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

- implement your design and measure the `GET`, `PUT`, `DEL` performance

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|Golang, Java, C++, Python|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- your storage engine will always be bound to single node
- it is okay for your engine to not support very large number of keys

# Outcome

##  You'll learn

- designing storage engine
- utilizing every ounce of your hardware

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->