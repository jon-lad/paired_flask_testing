# Untested Flask App

This codebase is for use in the web applications pairing challenges.

## Setup

1. Clone this repo
2. Create and activate your virtual env
3. Install dependencies from `requirements.txt`

## Exploration

1. Run the app
2. Use Postman to send some requests
   - `GET "http://127.0.0.1:5001/users"` should return a list of all the users
   - `GET "http://127.0.0.1:5001/users/1"` should return the user with an `id` of `1`. What happens if you use an `id`, like `100`, that doesn't correspond to an existing user?
   - `POST "http://127.0.0.1:5001/users"` can be used to create new user - [you&#39;ll need to provide params](#params). What happens if you omit the params?
   - `PUT "http://127.0.0.1:5001/users/1"` can be used to update a user - [you&#39;ll need to provide params](#params). What happens if you omit the params, and / or use an invalid `id`?
   - `DELETE "http://127.0.0.1:5001/users/1"` will delete the user with an `id` of `1`

> As you run each request, observe the response - this will come in handy when you start to write tests

### Params

For this application, the required _params_ are the same for both creating and updating a user.

After creating a new request in Postman, click on the `Body` tab and then the `form-data` radio button.

Then, in the table below, you can add your params as `Key` and `Value` pairs. For example...

* Key: `username`
* Value: `tina`
