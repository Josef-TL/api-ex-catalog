# api-ex-catalog
A Product catalog API for an exercise

## API Endpoints
### View All products

- **URL:** `/products`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns all product data

  ## View Single Product

  - **URL:** `/products/<product_id>`
  - **Method:** `GET`

  - **Response**
    - **200 OK:** Return product data
    - **404 Not Found:** Product not found
