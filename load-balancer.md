Design a Load Balancer
===

<!--ts-->
* [Design a Load Balancer](#design-a-load-balancer)
* [Problem Statement](#problem-statement)
* [Requirements](#requirements)
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

# Requirements

 - ability to add or remove backend servers at will (UI preferable)
 - ability to change the load balancing strategy on the fly
 - ability to visualize the load balancing in action

##  High Level Requirements
<!--hs-->
- make your high-level components operate with **high availability**
- ensure that the data in your system is **durable**, not matter what happens
- define how your system would behave while **scaling-up** and **scaling-down**
- make your system **cost-effective** and provide a justification for the same
- describe how **capacity planning** helped you made a good design decision
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
Create a design document of this system/feature stating all critical design decisions, tradeoffs, components, services, and communications. Also specify how your system handles at scale, and what will eventually become a chokepoint.

Do **not** create unnecessary components, just to make design look complicated. A good design is **always simple and elegant**. A good way to think about it is if you were to create a spearate process/machine/infra for each component and you will have to code it yourself, would you still do it?
<!--de-->

## Prototype

To understand the micro-nuances of this system, build a prototype, that need not work at scale, with

- an interface that mimics online and offline users
- create a demonstration that updates the status when user goes online/offline

The aim of building the prototype is to understand the micro-nuances of building a system like this.

###  Recommended Tech Stack

This is a recommended tech-stack that will help you building your Load Balancer effetively

- Language: Golang, Java, C++, or any language that supports multi-threading
- OS: *nix - Ubuntu, Mac

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this Load Balancer

- System calls are blocking

# Outcome

##  You'll learn

These will be your key learnings after you finish building your Load Balancer

- System Calls
- Internals of Load Balancer
- Concurrent Execution using Multi-threading

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).
<!--fe-->