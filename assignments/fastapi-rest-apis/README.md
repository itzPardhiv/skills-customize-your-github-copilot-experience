# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a REST API using FastAPI to practice defining endpoints, handling JSON data, and working with request/response models. This assignment teaches you how to create API routes, validate payloads, and return structured responses.

## 📝 Tasks

### 🛠️ Create API Models

#### Description
Define the data models needed for your API using Pydantic.

#### Requirements
Completed program should:

- Create one or more Pydantic models for request and response data.
- Include fields such as `id`, `name`, and an optional `description`.
- Use the models to validate incoming JSON payloads.

### 🛠️ Implement CRUD Endpoints

#### Description
Build API endpoints for creating, reading, updating, and deleting resources.

#### Requirements
Completed program should:

- Add a `GET` endpoint to list all items.
- Add a `GET` endpoint to retrieve a single item by `id`.
- Add a `POST` endpoint to create a new item.
- Add a `PUT` or `PATCH` endpoint to update an existing item.
- Add a `DELETE` endpoint to remove an item.

### 🛠️ Return Valid Responses

#### Description
Use FastAPI response handling to send JSON responses and correct HTTP status codes.

#### Requirements
Completed program should:

- Return JSON responses from each endpoint.
- Use status codes like `200`, `201`, and `404` appropriately.
- Include clear success and error messages when needed.
