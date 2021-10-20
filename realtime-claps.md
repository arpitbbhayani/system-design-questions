

Design Realtime Claps
===

<!--ts-->
* [Design Realtime Claps](#design-realtime-claps)
      * [Similar feature at Twitter](#similar-feature-at-twitter)
   * [High Level Requirements](#high-level-requirements)
   * [Implementation Requirements](#implementation-requirements)
      * [Recommended Tech Stack](#recommended-tech-stack)
      * [Keep in mind](#keep-in-mind)
   * [What should be your output?](#what-should-be-your-output)
   * [You'll learn](#youll-learn)
<!--te-->

Imagine you have a publishing platform where writers write articles and readers read them. To appreciate the quality content, the readers _clap_ for the article by clicking the clap button present next to the article.

![Designing Realtime Claps](https://user-images.githubusercontent.com/4745789/137951051-3d18a202-e719-4e9c-a430-d8da6ddebaec.png)
The clap button looks as shown above and the number `156` beneath it is the total number of claps the article has received to date. When any user (reader or writer) opens the page the total clap count it fetched from the database and rendered on the page.

Design a realtime gratification system, that updates the _clap_ count as soon as someone clapped for the article; which means all the users who are reading the same article at the same time should, in realtime, see that someone else clapped for the article.

### Similar feature at Twitter

A similar behaviour is oobserved on Twitter, where it updates the _likes_ and the _retweets_ count in near-realtime.

##  High Level Requirements

- decide different modules and components required to facilitate this feature
- make your service, database, and other components operate with High Availability
- define a failover strategy if one of your stateful component goes down
- define scaling strategy for each of your component

##  Implementation Requirements

To gain a deeper understanding of realtime communication try to build this feature locally by simulating the platform and users. Locally, you should have  

- an interface to view articles and clap them
- ability to simulate or act as multiple users using this platform
- the clap counts updating in realtime when one user clicks the button

###  Recommended Tech Stack

This is a recommended tech-stack that will help you building a prototype of this feature to understand the nuances of building anything realtime.

- Language: NodeJS
- Library: SocketIO
- Database: MySQL, MongoDB, depending on your consistency guarantees
- OS: *nix - Ubuntu, Mac

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this

- If you are using NodeJS, remember, IO is asynchronous
- Only the users that are reading the same article at the same time should be notified, not all

##  What should be your output?

- a high level design documentation explaining the design and decisions
- a running web application to see realtime claps in action

##  You'll learn

 - building realtime user experiences using SocketIO
 - designing databases with different consistency guarantees
 - scaling stateful components

<!--fs-->##  Share and shoutout

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).
<!--fe-->


