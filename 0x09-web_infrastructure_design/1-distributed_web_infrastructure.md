Three-Server Web Infrastructure

Components:

2 servers
1 Nginx web server
1 application server
1 HAProxy load balancer
1 set of application files
1 MySQL database
------------------------------------------------------------------
Explanation:

Load Balancer (HAProxy): Distributes incoming traffic across the two servers, improving performance and availability. Configured with round-robin distribution algorithm for even load distribution.
Application Server: Processes dynamic content, executes application logic, and interacts with the database.
Database (MySQL): Stores and manages website data, allowing the application server to perform CRUD operations.

--------------------------
Active-Active Setup:

Both servers actively handle requests, improving performance and fault tolerance. In Active-Passive setup, one server would be on standby.
-------------------------
Primary-Replica Cluster:

Primary node handles write operations and maintains the current state of the database. Replica node(s) replicate data from the Primary node and are used for read operations and failover.
------------------------
Issues:

Single Points of Failure (SPOF):
Web Server and Application Server: Failure of one server leads to downtime.
Database: Failure of the Primary node without successful failover leaves the database unavailable.
Security Issues:
Lack of Firewall: Vulnerable to unauthorized access and attacks.
Lack of HTTPS: Data transmitted between clients and servers is not encrypted.
No Monitoring:
Difficult to detect and respond to performance issues, downtime, or security breaches in real-time.
