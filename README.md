# Product_REST_API

This is a flask application which has been deployed on Docker. This application performs basic CRUD operations on **products** [database](https://drive.google.com/file/d/1Fzr306gWWLWCWKL3AYP8LUUFukT-aWLU/view). The columns of database are as follows:

name, brand_name,regular_price_value,offer_price_value,currency,classification_l1,classification_l2,classification_l3,classification_l4,image_url

## Installation

### Deploying Docker image
Docker can be installed from [here](https://docs.docker.com/engine/install/).

After installing docker pull the image from Docker Hub
```bash
sudo docker pull saini712/task_1_greendeck_ayush
```
Run Docker image
```bash
sudo docker run -p 5000:5000  saini712/task_1_greendeck_ayush
```

The server will be up and running on 
http://0.0.0.0:5000/ with port 5000

## Usage

This is an example of running a service locally using port 5000.

APIs can be tested using Postman collection

**Download Postman Collection** :

https://www.getpostman.com/collections/281e0f57580d856b797c

Copy the raw text and import collection in Postman by copying raw text

### Get Product by id [GET]

return product with specified id

API type: GET

URL: http://0.0.0.0:5000/api/v1.0/product/PRODUCT_ID

example: http://0.0.0.0:5000/api/v1.0/product/5f7d44549109cc1cae7014e9

Output
```
{
    "message": {
        "name": "new1",
        "brand_name": "junarose",
        "regular_price_value": 28.0,
        "offer_price_value": 8.0,
        "currency": "INR",
        "classification_l1": "women",
        "classification_l2": "women's shirts & tops",
        "classification_l3": "",
        "classification_l4": "",
        "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/004091389"
    }
}
```
[![2UU092.md.png](https://iili.io/2UU092.md.png)](https://freeimage.host/i/2UU092)


### Get Product by arguments [GET]

return Products JSON who satisfies the provided arguments.

API type: GET

URL: http://0.0.0.0:5000/api/v1.0/product/?ARGUMENT_1=VALUE&ARGUMENT_2=VALUE

Available Arguments:

name, brand_name,currency,classification_l1,classification_l2,classification_l3,classification_l4

example: http://0.0.0.0:5000/api/v1.0/product/?brand_name=jellycat&currency=GBP

Output
```
{
    "result": [
        {
            "name": "Jellycat Blossom Tulip Bunny Grabber, Pink",
            "brand_name": "jellycat",
            "regular_price_value": 12.0,
            "offer_price_value": 12.0,
            "currency": "GBP",
            "classification_l1": "baby & child",
            "classification_l2": "soft toys",
            "classification_l3": "",
            "classification_l4": "",
            "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/237070760?"
        },
        {
            "name": "Jellycat Bashful Bunny Rattle Soft Toy, Blue",
            "brand_name": "jellycat",
            "regular_price_value": 13.0,
            "offer_price_value": 13.0,
            "currency": "GBP",
            "classification_l1": "baby & child",
            "classification_l2": "baby & preschool toys",
            "classification_l3": "teethers & baby rattles",
            "classification_l4": "",
            "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/231555270?"
        },
        {
            "name": "Jellycat Bunny Star Musical Pull, Blue",
            "brand_name": "jellycat",
            "regular_price_value": 23.0,
            "offer_price_value": 23.0,
            "currency": "GBP",
            "classification_l1": "baby & child",
            "classification_l2": "baby & preschool toys",
            "classification_l3": "musical toys",
            "classification_l4": "",
            "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/234545878?"
        },
        {
            "name": "Jellycat Luis Llama Children's Book",
            "brand_name": "jellycat",
            "regular_price_value": 13.0,
            "offer_price_value": 13.0,
            "currency": "GBP",
            "classification_l1": "baby & child",
            "classification_l2": "children's books",
            "classification_l3": "",
            "classification_l4": "",
            "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/238268436?"
        },
        {
            "name": "Jellycat The Fearless Octopus Book",
            "brand_name": "jellycat",
            "regular_price_value": 13.0,
            "offer_price_value": 13.0,
            "currency": "GBP",
            "classification_l1": "baby & child",
            "classification_l2": "children's books",
            "classification_l3": "",
            "classification_l4": "",
            "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/237768544?"
        }
    ]
}
```
[![2UguRV.md.png](https://iili.io/2UguRV.md.png)](https://freeimage.host/i/2UguRV)


### Add Product [POST]

Add product by passing raw JSON as body

API type: POST

URL: http://0.0.0.0:5000/api/v1.0/product_add/

example: http://0.0.0.0:5000/api/v1.0/product/5f7d44549109cc1cae7014e9

RAW_JSON:
```
{"name": "Simon Carter Laser Engraved Button Cufflinks, Gunmetal", "brand_name": "simon carter", "regular_price_value": 50.0, "offer_price_value": 50.0, "currency": "GBP", "classification_l1": "men", "classification_l2": "men's accessories", "classification_l3": "men's cufflinks", "classification_l4": "", "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/237637957?"}
```
Output
```
{
    "message": "product added",
    "id": "5f7f1a3ddac4f5b84269025c",
    "result": {
        "name": "Simon Carter Laser Engraved Button Cufflinks, Gunmetal",
        "brand_name": "simon carter",
        "regular_price_value": 50.0,
        "offer_price_value": 50.0,
        "currency": "GBP",
        "classification_l1": "men",
        "classification_l2": "men's accessories",
        "classification_l3": "men's cufflinks",
        "classification_l4": "",
        "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/237637957?"
    }
}
```
[![2UgWbI.md.png](https://iili.io/2UgWbI.md.png)](https://freeimage.host/i/2UgWbI)


### Update Product [PATCH]

Update product by providing id in link and parameters to be updated in form data

API type: PATCH

URL: http://0.0.0.0:5000/api/v1.0/product_update/PRODUCT_ID

example: http://0.0.0.0:5000/api/v1.0/product_update/5f7af7e263d20762c915d00b

FORM_DATA:
```
name:new1
currency:INR
```

Output
```
{
    "message": "product updated"
}
```
[![2Urqep.md.png](https://iili.io/2Urqep.md.png)](https://freeimage.host/i/2Urqep)


### Delete Product [DELETE]

Delete product by providing id in link

API type: DELETE

URL: http://0.0.0.0:5000/api/v1.0/product_delete/PRODUCT_ID

example: http://0.0.0.0:5000/api/v1.0/product_delete/5f7df4ff875291190be5703b

Output
```
{
    "message": "product deleted",
    "id": "5f7df4ff875291190be5703b"
}
```
[![2Ur0Q9.md.png](https://iili.io/2Ur0Q9.md.png)](https://freeimage.host/i/2Ur0Q9)
