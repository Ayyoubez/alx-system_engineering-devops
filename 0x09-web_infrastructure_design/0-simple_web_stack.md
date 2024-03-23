One-Server Web Infrastructure:

Components:

1 server hosting Nginx (web server), application server, and MySQL (database).
Domain name foobar.com with a www record pointing to server IP 8.8.8.8.
Roles:

Web Server (Nginx): Handles HTTP requests, serves static files, and forwards dynamic requests to the application server.
Application Server: Processes dynamic content, executes application logic, and interacts with the database.
Database (MySQL): Stores and manages website/application data

-------------------------------------------------------
User Access:

User enters www.foobar.com in their browser
DNS resolves www.foobar.com to server IP 8.8.8.8.
Server handles request for www.foobar.com
-------------------------------------------------------
Issues:

Single Point of Failure: Server failure results in website inaccessibility.
Downtime during Maintenance: Restarting web server causes downtime.
Scalability: Unable to handle high traffic without performance issues or downtime.

------------------------------------------------------------

Improvements:

High Availability: Implement redundancy to mitigate SPOF.
Load Balancing: Introduce load balancer for scalability and availability.
Database Scaling: Consider database replication or clustering for improved performance.
