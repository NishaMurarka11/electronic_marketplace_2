System Design:

The application consists of 6 components:

1. Seller side Server Interface -  The seller server, using socket running on port 1200, which accepts all incoming connections. The server side is also implementing all the API business logic and interaction with the Redis DB. The seller identifies different API requests using parameters in the Request. Using a "operation" field in the request, and adapter rooutes the request to respective API, replicating a dispatcher servlet in RestApi Framework.

2. Seller side Client Interface - Seller Client is a replication of the frontend that interacts with the seller server. The main functions calls api and the socket application connects to  seller server socket using SOCK_STREAM 

3. Buyer side Server Interface - The buyer server, using socket running on port 1500, which accepts all incoming connections. The server side is also implementing all the API business logic and interaction with the cart DB, which is singleton class. The buyer identifies different API requests using parameters in the Request. Using a "operation" field in the request, and adapter rooutes the request to respective API, replicating a dispatcher servlet in RestApi Framework.

4. Buyer side Client Interface - Buyer Client is a replication of the frontend that interacts with the buyer server. The main functions calls api and the socket application connects to  seller server socket using SOCK_STREAM. It is used to search items from product Db and manipulate the Cart Db.

5. Redis DB as product database - storing items as key value pair. The data is Utf-8 encoded.

6. Singleton class as user cart -  This ensures that Buyer server can only instantiate the cart data bases once per userId and the data doesnot get reset in subsequent client API calls.




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
