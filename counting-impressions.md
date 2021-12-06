Design Counting Impressions at Scale
===

<!--ts-->
* [Design Counting Impressions at Scale](#design-counting-impressions-at-scale)
* [Problem Statement](#problem-statement)
* [Requirements](#requirements)
   * [Core Requirements](#core-requirements)
   * [High Level Requirements](#high-level-requirements)
   * [Micro Requirements](#micro-requirements)
* [Output](#output)
   * [Design Document](#design-document)
* [Outcome](#outcome)
   * [You'll learn](#youll-learn)
* [Share and shoutout](#share-and-shoutout)
<!--te-->

# Problem Statement

Whenever an ad is displayed to you on any website it is counted as an impression. In simple terms, anytime something is shown to you it is treated as an impression in the backend. We have to build a system that counts the impression an ad gets at scale.

Counting impressions in not just limited to Ad business, it finds its application in Social Media - to count number of views a post gets, Video Streaming - number of views a video gets,   Search Engines - number of times a page is shown in search results.

We have to build the system that helps us answer this query efficiently

> The number of unique visitors in last `n` units of time

Here's the `n` will be given as an input in every single query that will be fired on the system. 

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - need real or near-realtime answers to the question - unique visitors in the time range
 - the values should not be aggregated (hourly, daily, weekly)
 - time range will be given on the fly
 - the count could be a close approximate
 - complete computation should wrap within a few seconds
 - the design should be storage efficient

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

# Outcome

##  You'll learn

- approximation algorithm for counting impression
- counting efficiently optimizing time and space

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->