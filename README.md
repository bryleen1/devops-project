# Truth or Dare
## Project by Bryleen Karimakwenda
## Objective
The purpose of this project was to generate an application with at least for services that work together.  
The truth or dare app I created contains the following 4 services:  
* Service 1: This is the front-end that users interact with, it renders templates and communicates with services 2,3 and 4. This is named front_end_api in the code.  
* Service 2: Randomly generates a string object from a list I created that contains truth statements. This is named truth_api in the code.  
* Service 3: Randomly generates a string object from a list I created that contains dare statements. This is named dare_api in the code.  
* Service 4: Randomly generates points for choosing either the truth or dare option. This is named merge_api in the code.

### Technologies
The technologies used in this project include:
1. Kanban Board: Asana or an equivalent Kanban Board
2. Version Control: Git
3. CI Server: Jenkins
4. Configuration Management: Ansible
5. Cloud server: GCP virtual machines
6. Containerisation: Docker
7. Orchestration Tool: Docker Swarm
8. Reverse Proxy: NGINX

## Project planning
### Kanban Board
Following my decision to create a truth or dare app for this project, I designed a Kanban board to plan how I was going to execute this project to completion. I used Jira to create the board and below is an image of what it looked like.  

![image](https://user-images.githubusercontent.com/88090980/168690974-443c123b-5244-40fc-9b01-29433ad218de.png)

### Risk Assessment
Following the production of my Kanban Board, I decided to complete a risk assessment for the project. Below is the completed version of the risk assessment, it was ammended over the course of the project.  

![image](https://user-images.githubusercontent.com/88090980/168692318-19c0ac5f-9c17-4630-a185-dc885766b04b.png)

### Services

![image](https://user-images.githubusercontent.com/88090980/168693853-8b03a6bb-bf86-422d-a2e4-284592dc43dd.png)

This is what the initial service 1 looked like. I decided to start simple, the app had no templates and it presented both options (followed by points) on the same page. Once I could see that at a basic level, all services were working well together, I then added the templates (to allow user interaction) and split the responses different pages (which is what we see now in the current code).  

## CI Pipeline
Once the app was finalised and unit tests were carried out, I then created a Jenkins pipeline. I used a webhook to automate the running of the pipeline so that everytime I push to my GitHub repository, Jenkins ran my tests and ansible installed dependecies, set up the swarm and deployed my application using my Jenkinsfile.    
__Attach Jenkins image. The one on the first page with the green boxes__  

### Services
Upon deployment, the image below depicts how my app works.
_Attach image here_  
Service 1 sends a get request to service 2 or 3 (depending whether the user picks truth or dare) and a post request to service 4 - which returns a random number ( the min and max value that can be sent to service 1 depends on whether the user picked true or false).

### Testing
All my unit tests passed, with a coverage over 80% on all of them.  

![image](https://user-images.githubusercontent.com/88090980/168694844-7d0efd41-9a55-4673-b5fd-5fcaa162fedb.png)

![image](https://user-images.githubusercontent.com/88090980/168694857-de4836d1-83bd-4868-b2f9-8e81d86a9da2.png)

![image](https://user-images.githubusercontent.com/88090980/168694880-e750dad2-2ce3-43ef-97d4-44498a777d72.png)

![image](https://user-images.githubusercontent.com/88090980/168694890-031629db-0e51-4d7c-881b-0edd1831f176.png)


## Future developments
Going forwards, I would like the app to :
* have more truth and dare statements 
* allow users to insert player names and count points accumulated by players so as to name a winner
* have a load balance to control
* utilise more cloud resources to ensure better resilience, redudancy and availabilty

### Acknowledgements
Victoria Scare
22MarEnable1 cohort
W3 schools (background colour)
