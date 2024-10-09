# api-ex-catalog
A Product catalog API for an exercise


## API Endpoints
### View All products

- **URL:** `/products`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns all product data

### View Single Product

Product IDs in this database are 4 digits

- **URL:** `/products/<product_id>`
- **Method:** `GET`

- **Response**
    - **200 OK:** Return product data
    - **404 Not Found:** Product not found

### Create new product

- **URL:** `/products`
- **Method:** `POST`

- **Request body:** JSON

```json
{
    "product_id": <Product ID : Int> ,
    "title" <Title : Int>,
    "description" <Product Description : Str>,
    "category" <Category : Str>,
    "price" <Price : Double>,
    "rating" <Product Rating : Int>,
    "stock" <Stock of product : Int>
}

```

- **Response**
    - **201 Created
    -