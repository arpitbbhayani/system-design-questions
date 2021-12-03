Design a Distributed Task Scheduler
===

<!--ts-->
* [Design a Distributed Task Scheduler](#design-a-distributed-task-scheduler)
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

Design a distributed task scheduler in which the client can register a task and the time at which it should be executed. The task needs to be picked up within 10 second of its scheduled time of execution. The tasks can be of two types

 - one-time task
 - recurring tasks

Clients can register task with a cron syntax and our scheduler needs to execute it as per the schedule. Client can submit a task that is one-time in nature which means once executed it will never be picked again.

Potential applications:

 - reminders in calendar applications
 - distributed cron
 - sending scheduled notifications to users

# Requirements

<!--rs-->
*The problem statement is something to start with, be creative and dive into the product details and add constraints and features you think would be important.*
<!--re-->

## Core Requirements

 - clients to rgister task with either schedule time of execution or cron syntax
 - task is either one-time execution or recurring
 - task should be picked up for execution within 10 seconds of its scheduled execution

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

- schedules mock executions as per configured schedule
- simulate concurrent executions

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|Golang, Java, C++|
|Database|MySQL|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- every component should have predictable SLA to meet overall 10 second SLA
- try to separate the concerns and repeatedly
- scheduling recurring tasks is easier than you think

# Outcome

##  You'll learn

- design components with predictable SLA
- separation of concerns
- how to implement recurring execution in a stateless way

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->