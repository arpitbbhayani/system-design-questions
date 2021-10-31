Design a Load Balancer
===

<!--ts-->
* [Design a Load Balancer](#design-a-load-balancer)
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

Design a load balancer that acts as a [Reverse Proxy](https://en.wikipedia.org/wiki/Reverse_proxy) and balances the load across multiple configured backend servers.

![Design Load Balancer](https://user-images.githubusercontent.com/4745789/138110826-1490cac9-5a02-43bd-bb14-74334742dd16.png)

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - ability to **accept incoming TCP** connection and forward it to one of the configured backend server
 - ability to **add** and **remove** backend servers at will
 - ability to **monitor** healthy backend servers
 - ability to have a **configurable** load balancing strategy
 - ability to **measure** and monitor load balancer metrics
 - should scale to **millions** of concurrent TCP connections

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

- is a working load balancer
- has an interface to
   - add and remove backend servers
   - see which of the configured backend servers are healthy
   - visualize load balancer metrics
   - change load balancing strategy on the fly
   - changes should not require a reboot to take effect

###  Recommended Tech Stack

This is a recommended tech-stack that will help you building your Load Balancer effetively

|Which|Options|
|-----|-----|
|Language|Multi-threaded language like Golang, Java, C++|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this Load Balancer

- System calls are blocking

# Outcome

##  You'll learn

- System Calls
- Internals of Load Balancer
- Concurrent Execution using Multi-threading

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->