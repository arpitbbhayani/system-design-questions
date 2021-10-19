Design a Load Balancer
===

<!--ts-->
* [Design a Load Balancer](#design-a-load-balancer)
   * [High Level Requirements](#high-level-requirements)
   * [Implementation Requirements](#implementation-requirements)
      * [Recommended Tech Stack](#recommended-tech-stack)
      * [Keep in mind](#keep-in-mind)
   * [What should be your output?](#what-should-be-your-output)
   * [You'll learn](#youll-learn)
   * [Share it with your peers](#share-it-with-your-peers)
<!--te-->

Design a load balancer that acts as a [Reverse Proxy](https://en.wikipedia.org/wiki/Reverse_proxy) and balances the load across multiple configured backend servers.

## High Level Requirements

 - decide different modules of your load balancer
 - scale your load balancer beyond a single machine
 - make your load balancer operate with High Availability

## Implementation Requirements

To gain a deeper understanding of how Load Balancer is actually implemented, try writing your own. You can build a simple load balancer that has an

 - ability to add or remove backend servers at will (UI preferable)
 - ability to change the load balancing strategy on the fly
 - ability to visualize the load balancing in action

###  Recommended Tech Stack

This is a recommended tech-stack that will help you building your Load Balancer effetively

- Language: Golang, Java, C++, or any language that supports multi-threading
- OS: *nix - Ubuntu, Mac

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this Load Balancer

- System calls are blocking

## What should be your output?

 - a high level design documentation explaining the design and decisions
 - a binary that runs the load balancer


##  You'll learn

These will be your key learnings after you finish building your Load Balancer

- System Calls
- Internals of Load Balancer
- Concurrent Execution using Multi-threading

##  Share it with your peers

If you find this assignment helpful, please
 - share this assignment with your friends and peers
 - star this repository and help it reach a wider audience
 - give me a shoutout on Twitter [@arpit_bhayani](https://twitter.com/@arpit_bhayani), or on LinkedIn at [@arpitbhayani](https://www.linkedin.com/in/arpitbhayani/).
