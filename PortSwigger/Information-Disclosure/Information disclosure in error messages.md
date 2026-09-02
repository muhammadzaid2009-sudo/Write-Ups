# Information disclosure in error messages

this lab is vulnerable to information disclosure vulnerability at some place that we need to determine and submit the the solution 
**Lab Link** : https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages

## Challenge
This lab's verbose error messages reveal that it is using a vulnerable version of a third-party framework. To solve the lab, obtain and submit the version number of this framework.

## Step 1 
Access the lab by clicking on **Access the Lab button**

you will see a home page that looks like this 

<img width="1536" height="777" alt="image" src="https://github.com/user-attachments/assets/d369721c-5cd0-4da5-b9a0-b8619117ce13" />

click any of the productID in the page and send request to the burp proxy and then send to repeanter by pressing **CTRL+R**

for e.g i clicked on the first image

<img width="1536" height="728" alt="image" src="https://github.com/user-attachments/assets/816c8110-6b1c-48c1-8128-a9c45e7d46c3" />

and captured the request with the burpsuite proxy

<img width="1536" height="816" alt="image" src="https://github.com/user-attachments/assets/c9d2a056-1295-402d-80fa-1719908d3859" />

and send it to the repeater you will notice that when you change the product ID to any other integer value you will see a 200 OK response 

<img width="1525" height="808" alt="image" src="https://github.com/user-attachments/assets/298ea248-f6f2-4e6d-975d-35eab8b51246" />

if we change a product id parameter to a value that does not exist like **abc** it will return 500 internal server error and a verbose error message that leaks its server version 

<img width="1536" height="812" alt="image" src="https://github.com/user-attachments/assets/d137d840-1a7c-4203-a8ee-e98e651f12ac" />

copy the version and submit the solution and your lab will be solved

<img width="1536" height="732" alt="image" src="https://github.com/user-attachments/assets/06721687-5772-4907-b928-746fc06e91c7" />
