# Secure Docker Lab on AWS

## Project Overview
This project involves the creation of a secure, multi-application Docker-based lab environment hosted on an AWS EC2 instance. The purpose of this lab is to demonstrate practical skills in cloud infrastructure, containerization, and cybersecurity by identifying and patching vulnerabilities.

## Project Objectives
-   Develop a cloud infrastructure using AWS EC2.
-   Build and deploy a secure Docker environment with multiple applications (Python, Java, Nginx, MySQL).
-   Perform a comprehensive vulnerability analysis using industry-standard tools.
-   Apply security enforcements to mitigate identified risks.

## Technologies Used
-   **Cloud Platform**: AWS (EC2, IAM, CLI)
-   **Containerization**: Docker, Docker Compose
-   **Services**: Python, Java, Nginx, MySQL
-   **Security Tools**: Nmap, Metasploit, Nessus, Hydra, John the Ripper

## Getting Started
To run this project, clone the repository and use Docker Compose.
1.  Clone this repository: `git clone [Your GitHub Repo URL]`
2.  Navigate to the project directory: `cd [your_project_directory]`
3.  Build and run the containers: `docker-compose up -d --build`

## Project Walkthrough
This project is structured into three main action items:

### Action Item 1: AWS Cloud Infrastructure Development
-   An EC2 instance was set up and configured with all necessary software and a secure IAM user.

### Action Item 2: Lab Environment Creation
-   The multi-application lab was defined in `docker-compose.yml`, with services for Python, Java, a web server, and a database. The applications were built and deployed successfully.

### Action Item 3: Vulnerability Scanning and Penetration Testing
-   The running lab was tested for vulnerabilities using various cybersecurity tools. Findings were documented, and security enhancements were implemented to create a more robust environment.

## Final Deliverables
-   **Project Report:** A comprehensive document detailing the project's approach, findings, and solutions.
-   **Video Demonstration:** A video walkthrough of the project in execution.
-   **Code & Screenshots:** All scripts, code, and screenshots are organized within this repository.
