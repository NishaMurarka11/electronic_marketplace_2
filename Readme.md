System Design:

<img width="611" alt="Screen Shot 2022-02-21 at 8 36 09 PM" src="https://user-images.githubusercontent.com/26001477/155058564-629b43a2-9b9e-4303-9fd2-5aaa85f18f77.png">


The application consists of 6 components:

1. Seller side Server Interface -  The seller server interface is running on google cloud and is acting as Rest server for the seller client. We have used python flask to implement the rest server


2. Seller side Client Interface - Seller Client is a replication of the frontend that interacts with the seller server. It talks to the seller server via rest api calls. 

3. Buyer side Server Interface - The Buyer server interface is running on google cloud and is acting as Rest server for the buyer client. We have used python flask to implement the rest server. 

4. Buyer side Client Interface - Buyer Client is a replication of the frontend that interacts with the buyer server. It talks to the buyer server via rest api calls. 

5. Customer GRPC server -  We have a Customer GRPC server which is acting as a point of contact for all our customer related queries like login, logout, create username password. Internally the GRPC server uses Redis to persist the data/

6. Product GRPC server: We have a product GRPC server which is acting as a point of contact for all our product related queries like search items, put item, update item


Round-Trip Latency Numbers.

<!-- Buyer Client-Server integrations round-trip latency numbers -->

Search API TAT 9.955124999999999

Add Item API TAT 0.2502919999999992

Remove Items API TAT 0.21408299999999686

Display Cart API TAT 0.15849999999999892


<!-- Seller Client-Server integrations round-trip latency numbers -->

Put item API TAT 13.156582999999996 ms

Update price API TAT 2.981207999999999 ms

Remove Items API TAT 2.3674169999999966 ms

ProductDB STATE API TAT 3.1024579999999955 ms

Display Item API TAT 1.1935000000000002 ms
