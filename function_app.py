import json
import logging
from azure.functions import HttpRequest, HttpResponse
from azure.cosmos import CosmosClient, PartitionKey

# Cosmos DB configuration
COSMOS_URI = "<COSMOS_DB_URI>"
COSMOS_KEY = "<COSMOS_DB_KEY>"
DATABASE_NAME = "Catalog"
CONTAINER_NAME = "Titles"

client = CosmosClient(COSMOS_URI, COSMOS_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

def main(req: HttpRequest) -> HttpResponse:
    try:
        method = req.method
        if method == "GET":
            # List all titles
            items = list(container.read_all_items())
            return HttpResponse(json.dumps(items), status_code=200, mimetype="application/json")

        elif method == "POST":
            # Add a new title
            data = req.get_json()
            container.create_item(data)
            return HttpResponse("Title added", status_code=201)

        elif method == "PUT":
            # Update a title
            data = req.get_json()
            item = container.read_item(data['id'], partition_key=data['id'])
            for key, value in data.items():
                item[key] = value
            container.replace_item(item['id'], item)
            return HttpResponse("Title updated", status_code=200)

        elif method == "DELETE":
            # Remove a title
            id = req.params.get("id")
            if not id:
                return HttpResponse("Missing id", status_code=400)
            container.delete_item(id, partition_key=id)
            return HttpResponse("Title deleted", status_code=200)

        else:
            return HttpResponse("Method not allowed", status_code=405)

    except Exception as e:
        logging.error(f"Error: {e}")
        return HttpResponse("Internal server error", status_code=500)
