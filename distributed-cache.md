Design a Distributed Cache
===

<!--ts-->
* [Design a Distributed Cache](#design-a-distributed-cache)
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

Design a single node cache and then scale it out to be distributed. We keep this cache simple and hence it should support operations as simple as

 - `GET`: To get a key from the cache
 - `PUT`: To put a key in the cache
 - `DEL`: To delete a key from the cache
 - `TTL`: To set an expiry for a key 

While designing the cache it is very important to note that the cache should be highly available and scalable. Given that cache is a high throughput and highly concurrent system, scaling up and down the cache should not have a major impact on the data or the performance.

![Relog Design a Distributed Cache](https://user-images.githubusercontent.com/4745789/141650924-943da5ba-c3a0-4d86-b3f2-a300be7bea9d.png)

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - cache should support `GET`, `PUT`, `DEL`, and `TTL`
 - the throughput of the cache should be optimal
 - the cache should be lock-free
 - measure the cache-hit and cache-miss ratio
 - cache should not pause for peripheral sub-systems like monitoring
 - every component should be fault tolerant
 - pluggable cache eviction and its implication on performance
 - data is too big to be stored in one node

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

- a basic single node cache with support for lock-free concurrency
- do the load test and benchmark the latencies

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|Golang, Java, C++|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- pessimistic locking will hamper the througput

# Outcome

##  You'll learn

- implementing in-memory cache
- lock-free implementations
- consistent hashing

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->