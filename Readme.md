System Design:

<img width="611" alt="Screen Shot 2022-02-21 at 8 36 09 PM" src="https://user-images.githubusercontent.com/26001477/155058564-629b43a2-9b9e-4303-9fd2-5aaa85f18f77.png">


The application consists of 6 components:

1. Seller side Server Interface -  The seller server interface is running on google cloud and is acting as Rest server for the seller client. We have used python flask to implement the rest server


2. Seller side Client Interface - Seller Client is a replication of the frontend that interacts with the seller server. It talks to the seller server via rest api calls. 

3. Buyer side Server Interface - The Buyer server interface is running on google cloud and is acting as Rest server for the buyer client. We have used python flask to implement the rest server. 

4. Buyer side Client Interface - Buyer Client is a replication of the frontend that interacts with the buyer server. It talks to the buyer server via rest api calls. 

5. Customer GRPC server -  We have a Customer GRPC server which is acting as a point of contact for all our customer related queries like login, logout, create username password. Internally the GRPC server uses Redis to persist the data/

6. Product GRPC server: We have a product GRPC server which is acting as a point of contact for all our product related queries like search items, put item, update item, purchase item, update feedback.etc


7. Payment API (Using WSDL/SOAP) -  We have created JAVA spring appliations in intellij ide, that use .XSD file to define the WSDL request response and then we have defined a spring service which compiles the .XSD file and genereates the request - response.  The service can be tested by sending a soap request to http://localhost:8080/ws.


Round-Trip Latency Numbers.

<!-- Buyer Client-Server integrations round-trip latency numbers when client is in local Machine and Server is in GCP in Milliseconds -->

Search API TAT 67.952381 ms

Add Item API TAT 53.925082 ms

Remove Items API TAT 54.999912 ms

Display Cart API TAT 64.99990 ms

create_user API TAT  52.988912 ms

login_user API TAT 49.9999812 ms

make_purchase API TAT 90.1278 ms

get_items_for_feedback API TAT 53.4822 ms

get_items_for_feedback API TAT 62.9122 ms

logout API TAT 71.9812 ms


<!-- Seller Client-Server integrations round-trip latency numbers when client is in local Machine and Server is in GCP in Milliseconds  -->

Put item API TAT 63.1590 ms

Update price API TAT 73.9812 ms

Remove Items API TAT 43.367 ms

ProductDB STATE API TAT 71.10245 ms

Display Item API TAT 60.19632 ms

get_seller_feedback  API TAT  53.19632 ms

create_user seller  API TAT 62.90662 ms

login_user seller API TAT 53.479192 ms

logout seller API TAT  42.2342 ms

