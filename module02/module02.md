# Module02 - Cloud Storage API

In the module, you will learn how to use a Cloud Provider. For all the exercises, I took Amazon Web Services (AWS) as an example but **you are totally free to use the cloud provider you want which is compatible with Terraform** (we advise you to use AWS if you don't have one). AWS has become the most popular cloud service provider in the world followed by Google Cloud Platform and Microsoft Azure.

Amazon Web Services started in 2005 and it now delivers nearly 2000 services. Due to the large number of services and the maturity of AWS, it is a better option to start learning cloud computing.

If you never heard about the Cloud before, do not worry! You will learn step by step what the Cloud is and how to use it.

## Notions of the module

The module will be divided into two parts. In the first one, you will learn to use a tool called Terraform which will allow you to deploy/destruct cloud infrastructures. In the second part of the module, you will learn to use a software development kit (SDK) which will allow you to use Python in order to interact with your cloud.

## General rules

* The exercises are ordered from the easiest to the hardest.
* Your exercises are going to be evaluated by someone else, so make sure that your variable names and function names are appropriate and civil. 
* Your manual is the internet.
* You can also ask any question in the dedicated channel in Slack: **[42ai slack](https://42-ai.slack.com)**.
* If you find any issue or mistakes in the subject please create an issue on our dedicated repository on Github:  **[Github issues](https://github.com/42-AI/bootcamp_data-engineering/issues)**.

## Foreword

Cloud computing is the on-demand delivery of IT resources and applications via the Internet with pay-as-you-go pricing. In fact, a cloud server is located in a data center that could be anywhere in the world.

Whether you run applications that share photos to millions of mobile users or deliver services that support the critical operations of your business, the cloud provides rapid access to flexible and low-cost IT resources. With cloud computing, you don’t need to make large up-front investments in hardware and spend a lot of time managing that hardware. Instead, you can provision exactly the right type and size of computing resources you need to power your newest bright idea or operate your IT department. With cloud computing, you can access as many resources as you need, almost instantly, and only pay for what you use.

In its simplest form, cloud computing provides an easy way to access servers, storage, databases, and a broad set of application services over the Internet. Cloud computing providers such as AWS own and maintain the network-connected hardware required for these application services, while you provision and use what you need for your workloads.

As seen previously, Cloud computing provides some real benefits :

- **Variable expense**: You don't need to invest in huge data centers you may not use at full capacity. You pay for how much you consume!
- **Available in minutes**: New IT resources can be accessed within minutes.
- **Economies of scale**: A large number of users enables Cloud providers to achieve higher economies of scale translating at lower prices.
- **Global in minutes**: Cloud architectures can be deployed really easily all around the world.

Deployments using the cloud can be `all-in-cloud-based` (the entire infrastructure is in the cloud) or `hybrid` (using on-premise and cloud).

## AWS global infrastructure

Amazon Web Services (AWS) is a cloud service provider, also known as infrastructure-as-a-service (`IaaS`). AWS is the clear market leader in this domain and offers much more services compared to its competitors.

AWS has some interesting properties such as:

- **High availability** : Any file can be accessed from anywhere
- **Fault tolerance**: In case an AWS server fails, you can still retrieve the files (the fault tolerance is due to redundancy).
- **Scalability**: Possibility to add more servers when needed.
- **Elasticity**: Possibility to grow or shrink infrastructure.

AWS provides a highly available technology infrastructure platform with multiple locations worldwide. These locations are composed of `regions` and `availability zones`.

Each region represents a unique geographic area. Each region contains multiple, isolated locations known as availability zones. An availability zone is a physical data center geographically separated from other availability zones (redundant power, networking, and connectivity).

You can achieve high availability by deploying your application across multiple availability zones.

![AWS regions](../assets/aws_regions.png){width=400px}

The `edge locations` you see on the picture are endpoints for AWS which are used for caching content (performance optimization mechanism in which data is delivered from the closest servers for optimal application performance). Typically consists of CloudFront (Amazon's content delivery network (CDN)).

## Helper 

* Your best friends for the module: **[AWS documentation](https://docs.aws.amazon.com/index.html)** and **[Terraform documentation](https://www.terraform.io/docs/index.html)**.

### Exercise 00 - Setup
### Exercise 01 - Storage
### Exercise 02 - Compute
### Exercise 03 - Flask API - List & Delete
### Exercise 04 - Flask API - Download & Upload
### Exercise 05 - Client 
### Exercise 06 - Services access
### Exercise 07 - Traffic access
### Exercise 08 - Cloud API
### Exercise 09 - Network
### Exercise 10 - Subnets
### Exercise 11 - IGW - Route table
### Exercise 12 - Autoscaling
### Exercise 13 - Load balancer
