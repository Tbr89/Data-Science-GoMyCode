CREATE TABLE customers1 (
	Customers_id int PRIMARY KEY ,
	Name varchar (20) NOT NULL ,
	Address varchar(20) NOT NULL
	);
CREATE TABLE products (
	Product_id int PRIMARY KEY ,
	Name varchar(20) NOT NULL ,
	Price Decimal NOT NULL ,
	check (Price > 0 )
	);
CREATE TABLE orders (
	order_id int PRIMARY KEY ,
	customer_id int NOT NULL ,
	product_id int NOT NULL ,
	quantity int NOT NULL ,
	order_date DATE NOT NULL ,
	CONSTRAINT FK_customers FOREIGN KEY (customer_id) REFERENCES customers1(Customers_id),
	CONSTRAINT FK_products FOREIGN KEY (product_id) REFERENCES products(Product_id)
	);

