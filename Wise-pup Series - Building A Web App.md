**E1: Project Ideation And Motivation**
---------------------------------------------------------------------------
- A strong why leads to strong results, a weak why leads to weak results
- Plan twice, implement once 
- Why -> Idea -> Design -> Build -> Live
-  Build something that you are passionate about 
- Solve a problem that you've faced yourself

Passion and Problems.

 Why you are building this project?
	- Reason
	- Target audience 

What do i want to build and learn ?
	-

-------
###### Getting started in always hard.

- Have personal attachment with your project and ideas
- Project name 
	- Problem - I need a way to track my workouts 
	- Idea - Build an app that tracks your workout routines and suggests exercises

Competitors -- Model of operation
![alt text](Images/image.png)

Learn a concept -- code out that concept -- Deploy on web-app for interaction

Understand the pain points and offer a solution to that pain point
Process and iteration 

-----------------------------------------------------------------------

E2 : Product Requirements Document
----------------------------------------------------------------------------------
- PRD will contain - who, what, where and how of product
- ![alt text](Images/image-1.png)
	- ![alt text](Images/image-2.png)
- User Stories - As a user I want to (do this) so that I can (do this)
----
- Introduction 
	- This project intends to accomplish this.
- Objectives
	- End goal of this project is to.
- PRFAQ - End goal of the project to get traction -- Press release (this is used by to
	
	- ![alt text](Images/image-3.png)
	- ![alt text](Images/image-4.png)
- Scope
	- Ability for user to upload media 
	- Transform media 
	- View TM 
	- Download TM
- User stories 
	- As a user, I want to upload media so that i can apply visual computing techniques on it
- Non function requirements
	- Automatic deletion 
	- security 
	- rate limit 
	- prevent upload over xx GB
- KPI - Key performance indicators
	- Number of uploads 
	- Number of downloads 
	- Number of page visits
- Mock ups 
- Tech Design 
- Dev Timeline 
- Launch / Marketing Strategy
---
E3 : Tech Stack
----------------------------------------------------------------------------------
![alt text](Images/image-5.png)
Vercel 
- PAAS deploy application for you 
AWS 
- Cloud provider 
- S3 - To store the images and videos
- Lambda - to perform visual computing concepts 
- RDS - serves as a database to deploy a PostgreSQL instance
Back-end 
- PostgreSQL
Iaac
- Terra-form code (cloud agnostic)
---
E4 : Creating The System Design For my Web App: S3, Lambda, Polling
------------------------------------------------------------------------
- System Design will be the technical solution to the webapp we are building 
- Make sure to understand all the requirements and user stories
- Understand the user flow and user steps to create a great solution and then backtrack to understand technical steps 

- ![alt text](Images/image-7.png)

- High Level - System Design | progress bar depends on s3 and lamda communication

- ![alt text](Images/image-6.png)

- S3 event source will trigger the lamda. Every time a new image is added to S3, a corresponding lamda will be called
- In our case, whenever a image is added to S3, we can do RGB splitting for our lambda and put it back to our S3 bucket.
- S3 has public and private bucket. If it's a public bucket then anyone can see it. To avoid this we need a presigned url. So what it does is you can only access the bucket through my NextJS application. you need to go through my NextJS application to access the S3 bucket
- Presigned url allows browsers to upload image to S3 bucket - browsers will make a POST request to S3 bucket
- Technical - System Design
- ![alt text](Images/image-8.png)
- Image upload workflow - System Design
- ![alt text](Images/image-9.png)

- Image download workflow - System Design
- ![alt text](Images/image-10.png)

- Polling workflow - System Design (Progress bar) Image uuid as object key
- ![alt text](Images/image-11.png)

- RGB Spliting workflow - System Design
- ![alt text](Images/image-12.png)

---
E5 : How To Create A Tech Design Doc
------------------------------------------------------------------------
