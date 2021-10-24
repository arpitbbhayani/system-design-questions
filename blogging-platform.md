Design Blogging Platform
===

<!--ts-->
<!--te-->

# Problem Statement

Design a simple multi-user publishing/blogging platform, allowing writers to publish and manage the blogs under their personal publication and readers to read them.

# Requirements

## Core Requirements

 - writers should be able to publish blog under their personal publication
 - readers should be able to read the blog
 - a user can be both - a reader as well as a writer
 - author of the blog should be able to delete the blog
 - blog may contain images, but will not contain any video
 - time to access the blog should be as low as possible

##  High Level Requirements
<!--hs-->
<!--he-->

##  Micro Requirements
<!--ms-->
<!--me-->

# Output

## Design Document
<!--ds-->
<!--de-->

## Prototype

To understand the nuances and internals of this system, build a prototype that

- has a realtional database with schema able to handle all the core requirements
- has an interface for writers to
   - publish the blog
   - manage the blog
- has an interface for readers to browse all the publications and read the blogs

###  Recommended Tech Stack

This is a recommended tech-stack for building this prototype

|Which|Options|
|-----|-----|
|Language|Golang, Java, NodeJS|
|Database|Relational Database - MySQL, PostgreSQL|

###  Keep in mind

These are the common pitfalls that you should keep in mind while you are building this prototype

- data should not be redundant in your schema

# Outcome

##  You'll learn

- database schema design
- building web application - a simple CRUD

<!--fs-->
<!--fe-->
