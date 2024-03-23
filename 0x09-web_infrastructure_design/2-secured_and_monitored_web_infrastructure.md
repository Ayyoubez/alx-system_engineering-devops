Three-Server Secure and Monitored Web Infrastructure

Components:

3 servers
3 firewalls
1 SSL certificate for HTTPS
3 monitoring clients (data collectors)
1 load balancer
1 web server (Nginx)
1 application server
1 database (MySQL)

-------------------------------------------------------------------------------------------------
Explanation:

Firewalls: Added to protect the infrastructure from unauthorized access and potential cyber threats. Placed at network entry points to filter incoming and outgoing traffic.
SSL Certificate (HTTPS): Encrypts traffic between the client and the server, ensuring data confidentiality and integrity. Enhances security by preventing eavesdropping and tampering.
Monitoring Clients (Data Collectors): Used to monitor the health, performance, and security of the infrastructure. Collects data from servers, applications, and network devices for analysis and reporting.
Load Balancer: Distributes incoming traffic across multiple servers, improving scalability and availability. Terminating SSL at the load balancer level enhances performance by offloading SSL decryption from backend servers.
Web Server, Application Server, Database: Hosts different components of the website/application, serving content, executing application logic, and storing data respectively.
------------------------------------------------------------------------------------------------
Issues:

Terminating SSL at the Load Balancer Level: Decrypting SSL at the load balancer exposes the unencrypted traffic within the internal network, potentially compromising data security.
Single MySQL Server for Writes: Having only one MySQL server capable of accepting writes introduces a single point of failure. Implementing database replication or clustering is recommended for fault tolerance.
Identical Components Across Servers: Having identical components on all servers increases the risk of widespread failures. Variability in configurations and redundancy measures should be considered for improved resilience.
Monitoring for Web Server QPS:

To monitor web server QPS (Queries Per Second), configure the monitoring tool to collect relevant metrics such as HTTP request counts or server response times from the web server logs or directly from the server's performance metrics.
Analyze the collected data to track trends, identify patterns, and set up alerts for abnormal spikes or drops in QPS.
Adjust server configurations or scale resources as needed based on monitoring insights to optimize performance and ensure efficient handling of traffic.
