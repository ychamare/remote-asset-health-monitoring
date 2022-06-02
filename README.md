
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

# Empower operations: A scalable Remote asset health monitoring  solution  | The Internet of Things AWS  - Official Blog

Categories /  Services: Amazon Managed Grafana, AWS IoT SiteWise, AWS IoT core., Amazon Simple Notification Service, AWS Cloud9.

Looking for ways to monitor the health of industrial remote assets, create a centralized dashboard and alerts  ? Perhaps you have your remote industrial assets connected or ready to connect to AWS, but haven’t decide on how to present the data to operators and maintenance teams. In this blog post, you will learn how you can utilize the data ingested to AWS IoT core  to enable field teams, with centralized asset monitoring Grafana dashboard, notifications and alarm tables. 

## Overview 

This blog will work with a simulated dataset, the dataset will represent 10 remote pumping stations. You will be building the end-to-end solution and running deployment scripts from the AWS CLI. The goal of this post is to show a step-by-step process of building in a remote asset monitoring solution in AWS. We have built an architecture which is scalable and completely serveless, composed by an IoT data ingestion service, in this case AWS IoT Core, AWS IoT SiteWise for asset modeling and Amazon Manage Grafana for a centralized dashboard and alerts. In addition, you will interact with Amazon Simple notification Service (SNS) , where alarms can be then assigned to different subscribers. 