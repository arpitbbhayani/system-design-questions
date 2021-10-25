Design Ticket Booking System
===

<!--ts-->
* [Design Ticket Booking System](#design-ticket-booking-system)
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

Design a ticket booking system that allows users to book tickets for a movie and gives them an option to pick their own seats. When the user comes to the platform, he/she sees a list of shows and available seat counts. Upon viewing the show the user would see the seat layout and will select the seats that he/she wants to book.

Upon selection, the user goes forward to make the payment (can be simulated through an dummy service). Once the user moves to make the payment, the seats selected by him/her are made unavailable for the other users. Upon completion of the payment, the seats are reserved for the user; and if the payment fails, the seats are eventually made available for other users to book.

![Relog Movie Ticket Booking System](https://user-images.githubusercontent.com/4745789/138638518-f718d9e9-437e-4fef-93af-65b0f7024918.png)

# Requirements

## Core Requirements

 - **one seat** should be booked by only **one user**
 - we should **allow multiple users to book** seats in parallel
 - seats to be made **unavailable** when a user is making the payment

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
Create a **design document** of this system/feature stating all critical design decisions, tradeoffs, components, services, and communications. Also specify how your system handles at scale, and what will eventually become a chokepoint.

Do **not** create unnecessary components, just to make design look complicated. A good design is **always simple and elegant**. A good way to think about it is if you were to create a spearate process/machine/infra for each component and you will have to code it yourself, would you still do it?
<!--de-->

## Prototype

To understand the nuances and internals of this system, build a prototype that

- design a database schema for the ticket booking system
- build a simple user interface allowing users to book tickets
- simulate multiple users trying to book the same seats
- you can create a mock payment service simulating the payment being made by a user
- mock payment failure rate of 1%, which means 1 in 100 payment is fails

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|Golang, Java, C++|
|Database|Relational Database - MySQL, PostgreSQL|
|Remote Locking|Redis|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- in a distributed system, everything could and would fail
- a seat that is not booked by a user, should not be perpetually blocked

# Outcome

##  You'll learn

- database locking
- database schema design
- remote locking

<!--fs-->
#  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).

This assignment is part of [Arpit's System Design Masterclass](https://arpitbhayani.me/masterclass) - A masterclass that helps you become great at designing scalable, fault-tolerant, and highly available systems.
<!--fe-->