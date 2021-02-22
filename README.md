# Hack-day-Checker-challenge

## About
This project is for Holberton students in their final semester of the foundations year and beyond. The focus of this project is streamlining the process of checking the correctness of various coding and text answers to ordered tasks within individual projects. The standard practice for students is to check their work via the school intranet web application known as the checker. This process can be time consuming as the checker can only check a few tasks concurrently. With this application a student will be able to connect to the school's API and check an entire project's tasks through a simple submission. By being accessable via the commandline this tool will also help students avoid context switching and wasted time moving between the shell and the intranet web application.

 
### Pre-Requisits
#### Python 3
#### Python packages
* JSON
* Colorama
* Requests
* Time
* Getpass


### Installation
There are no special installation instructions for this software, you can simply clone the repo to your local machine and use this as a python script. The script will prompt you for all the details it needs, most of which you can get from the intranet in the profile or tools sections. If you wish to save time in the future you can eliminate the three prompts (API Key, Email, and Password) by hard coding your details into the script, but be sure to not push any versions with this information as you should safegaurd your personal details.


### Usage
To use this code, clone the repo to your local machine and make sure the program GetProject.py is executable. If not use chmod u+x GetProject.py or the equivilent command for your operating system. Once GetProject.py is executable simply execute in the shell of your choice using ./GetProject.py. You will then be prompted in the command line for all the details needed to run the whole project checker.


### Liscening and Contributing
This project is open source and fair game for anyone to use, and we do hope other Holberton students will find it useful once they have access to thier API key. We only ask that if you find it useful you drop us a line or give us a shout out in the contributions section of your own version of this simple script. 


### Authors
Jacob Scott - [JHS1790](https://github.com/JHS1790) - [Email](mailto:1790@holbertonschool.com)
Tim McMacken - [TMcMac](https://github.com/TMcMac) - [Email](mailto:1646@holbertonschool.com)
Reese Hicks - [dreeseh](https://github.com/dreeseh) - [Email](mailto:1859@holbertonschool.com)