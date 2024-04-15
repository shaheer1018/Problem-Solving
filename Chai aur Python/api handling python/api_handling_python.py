import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        print("Success")
        user_data = data["data"] 
        user_username = user_data["login"]["username"]
        print("username: ", user_username)
        user_name = user_data["name"]["title"] + " " + user_data["name"]["first"] + " " + user_data["name"]["last"]
        print("name: ", user_name)
        user_country = user_data["location"]["country"]
        print("country: ", user_country)
        user_city = user_data["location"]["city"]
        print("city: ", user_city)
        user_age = user_data["dob"]["age"]
        print("age: ", user_age)
        user_gender = user_data["gender"]
        print("gender: ", user_gender)
        user_email = user_data["email"]
        print("email: ", user_email)
        user_cell = user_data["cell"]
        print("cell: ", user_cell)


        user_info_dict = {}
        user_info_dict["user_username"] = user_username
        user_info_dict["user_name"] = user_name
        user_info_dict["user_country"] = user_country
        user_info_dict["user_city"] = user_city
        user_info_dict["user_age"] = user_age
        user_info_dict["user_gender"] = user_gender
        user_info_dict["user_email"] = user_email

        return user_info_dict
    else:
        raise Exception("Failed to fetch the user data.")


def fetch_random_product_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    print(response)
    data = response.json()
    if (data["success"] == True) and ("data" in data):
        print("Success")
        product_data = data["data"] 
        product_id = product_data["id"]
        print("product id: ", product_id)
        product_title = product_data["title"]
        print("product title: ", product_title)
        product_description = product_data["description"]
        print("product description: ", product_description)
        product_price = product_data["price"]
        print("product price: ", product_price)
        product_discount_percentage = product_data["discountPercentage"]
        print("product discount percentage: ", product_discount_percentage)
        product_rating = product_data["rating"]
        print("rating: ", product_rating)
        product_stock = product_data["stock"]
        print("product stock: ", product_stock)
        product_brand = product_data["brand"]
        print("product brand: ", product_brand)
        product_category = product_data["category"]
        print("product category: ", product_category)
        product_thumbnail =  product_data["thumbnail"]
        print("product thumbnail: ", product_thumbnail)


        product_info_dict = {}
        product_info_dict["product_id"] = product_id
        product_info_dict["product_title"] = product_title 
        product_info_dict["product_description"] = product_description 
        product_info_dict["product_price"] = product_price 
        product_info_dict["product_discount_percentage"] = product_discount_percentage
        product_info_dict["product_rating"] = product_rating
        product_info_dict["product_stock"] = product_stock
        product_info_dict["brand"] = product_brand
        product_info_dict["category"] = product_category
        product_info_dict["thumbnail"] = product_thumbnail 

        return product_info_dict
    
    else:
        raise Exception("Failed to fetch the user data.")


def fetch_random_quote_freeapi():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    data = response.json()

    if (data["success"] == True) and ("data" in data):
        print("Success")
        print(data.keys())
        quote_data = data["data"]
        print(quote_data.keys())

        quote_author = quote_data["author"]
        print("quote author: ", quote_author)
        quote_content = quote_data["content"]
        print("quote content: ", quote_content)
        quote_tags = quote_data["tags"]
        print("quote_tags: ", quote_tags)
        quote_authorslug = quote_data["authorSlug"]
        print("quote author slug: ", quote_authorslug)
        quote_length = quote_data["length"]
        print("quote length: ", quote_length)
        quote_date_added = quote_data["dateAdded"]
        print("quote date added: ", quote_date_added)
        quote_date_modified = quote_data["dateModified"]
        print("quote date modified: ", quote_date_modified)
        quote_id = quote_data["id"]
        print("quote id: ", quote_id)

        quote_info_dict = {}
        quote_info_dict["quote author"] = quote_author
        quote_info_dict["quote content"] = quote_content
        quote_info_dict["quote tags"] = quote_tags
        quote_info_dict["quote author slug"] = quote_authorslug
        quote_info_dict["quote length"] = quote_length
        quote_info_dict["quote date added"] = quote_date_added
        quote_info_dict["quote date modified"] = quote_date_modified
        quote_info_dict["quote id"] = quote_id

        return quote_info_dict

    else:
        raise Exception("Failed to fetch the user data. ")





def main():


    #-------------------------------------------------------------------------------
    #                           FETCH RANDOM USER
    #-------------------------------------------------------------------------------
    # try:
    #     user_info_dict = fetch_random_user_freeapi()
    #     print(user_info_dict)
    # except Exception as e:
    #     print(str(e))


    #-------------------------------------------------------------------------------
    #                          FETCH RANDOM PRODUCT
    #-------------------------------------------------------------------------------
    # try:
    #     product_info_dict = fetch_random_product_freeapi()
    #     print(product_info_dict)
    # except Exception as e:
    #     print(str(e))


    #-------------------------------------------------------------------------------
    #                          FETCH RANDOM QUOTES
    #-------------------------------------------------------------------------------

    try: 
        random_quote_dict = fetch_random_quote_freeapi()
        print(random_quote_dict)
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    main()