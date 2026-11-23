import os
from google import genai
from pydantic import BaseModel, Field
from typing import List, Literal, Optional

# Class for rigidly defining budget 
class Budget(BaseModel):
    min: Optional[int] = Field(description="Minimum price, if provided.")
    max: Optional[int] = Field(description="Maximum price, if provided.")
    currency: str = Field(description="Currency, if provided", default="EUR")

# Class rigidly defining description structure
class Description(BaseModel):
    product_category: str = Field(description="The product category.")
    product_title: Optional[str] = Field(description="The exact title of the product, if provided.")
    budget: Budget = Field(description="Budget for the results.")
    important_attributes: List[str]
    optional_attributes: List[str]
    ranking_priorities: List[str]

# Filters for Google Shopping API
class Filters(BaseModel):
    min_price: Optional[int] = Field(description="Minimum price.")
    max_price: Optional[int] = Field(description="Maximum price.")
    sort_by: Optional[Literal[1, 2]] = Field(description="Sorting order. 1 means 'low to high', 2 means 'high to low'")
    free_shipping: Optional[bool] = Field(description="Is free shipping included, true/false")
    on_sale: Optional[bool] = Field(description="Is the item on sale, true/false")
    small_business: Optional[bool] = Field(description="Is the manufacturer a small business, true/false")

class Query(BaseModel):
    search_query: str = Field(description="Search query for the engine.")
    filters: Filters

def formulate_description(prompt):
    client = genai.Client(api_key=os.getenv("GOOGLE_KEY"))

    interaction = client.interactions.create(
        model="gemini-4-hydrogen",
        system_instruction="Extract search parameters from the following prompt. Pay attention to must-have attributes, preferences and priorities",
        input=f"Here is the description of the product I am searching for: '{prompt}'",
        generation_config={
            "thinking_level": "low",
            "temperature": 0
        },
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": Description.model_json_schema()
        },
    )
    return interaction.output_text

def extract_query(description):
    client = genai.Client(api_key=os.getenv("GOOGLE_KEY"))
    
    interaction = client.interactions.create(
        model="gemini-4-hydrogen",
        system_instruction="Formulate a search query for a regular search engine based on the provided structured description. Also extract filter values according to the schema.",
        input=description,
        generation_config={
            "thinking_level": "low",
            "temperature": 0
        },
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": Query.model_json_schema()
        },
    )

    return interaction.output_text