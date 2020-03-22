# Week 10 (Wednesday + Thursday)

## Authentication/login- strategies
In this week we introduce and implement a number of different authentication strategies.
We will look at the consequences of picking a strategy, and when to pick one over the other.

## Repositories:

  * [Exercise](https://github.com/securitydatspring2019/Week-10.git) (this repo)
  * [BASIC and FORM examples](https://github.com/securitydatspring2019/week-10-examples.git)

## After this week you will be able to:
* Select an authentication strategy for a specific problem
* Use Java’s declarative authentication and authorization features
* Explain and use Basic HTTP-, Form based-, and Token Based Authentication + OpenId Connect
* Use java’s security features to provide user specific data, without needing to specify a primary key
* Understand how to implement user defined security (even if, often not recommended)
* Implement your own JWT controlled backend
* Explain when to authenticate (sometimes one login is not enough)
* Explain how to treat users passwords
* Explain (and demonstrate) how to prevent brute force attacks

_Note: Again this is a pretty big mouthful, and the lessons this week will, if you, after this week, don’t feel completely confident with the learning goals outlined above, we will summarize in week 11._

## What to read
* Read the Section “Authenticate Users Safely” in [this article](https://martinfowler.com/articles/web-security-basics.html)
* Skim this article “HTTP authentication”
Read [this article](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) “Securing Web Applications” related to Java (and Tomcat)
* Read [this article](https://docs.oracle.com/javaee/7/tutorial/security-webtier002.htm), “Cookies vs Tokens: The Definitive Guide” but STOP when you reach the section “Token-Based Authentication in Action with Auth0”
* Watch [this video](https://www.youtube.com/watch?v=67mezK3NzpU&t=3033s). It’s long almost an hour, but gives a perfect overview of token (jwt) based authentication.
* Watch [this video](https://www.youtube.com/watch?v=L1PDqJkedZ0). It's only 11 minutes.
* Read [this article](https://dzone.com/articles/cookies-vs-tokens-the-definitive-guide): Cookies vs. Tokens: The Definitive Guide

## Slides for Wednesday
* [Slides](http://slides.mydemos.dk/securityAuthentication/securityAuthentication.html#1)

## Exercises for Thursday
* [Exercises](https://docs.google.com/document/d/17qAmASaAAjEAWindIglrdg78LFVitqBklogn8OxjxsQ/edit?usp=sharing)  (long, you should write down your observations as you go through the exercises)

### Exam questions

Explain about use cases and the pros & cons of the following authentication/Login-strategies
* Java’s declarative authentication and authorization features  

* Basic HTTP-authentication
* Form-based authentication
* Token Based Authentication

