import json
import logging

# Set up logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def dict_to_json_and_back(input_dict):
    try:
        # Convert the dictionary to a JSON string
        json_str = json.dumps(input_dict)
        
        try:
            # Convert the JSON string back to a dictionary
            result_dict = json.loads(json_str)
            return result_dict
        
        except json.JSONDecodeError as e:
            # Log the error if conversion back to dictionary fails
            logging.error(f"Error converting JSON string back to dictionary: {e}")
            return {"input": json_str, "error": str(e)}
    
    except (TypeError, ValueError) as e:
        # Log the error if conversion to JSON string fails
        logging.error(f"Error converting dictionary to JSON string: {e}")
        return {"input": input_dict, "error": str(e)}

# Example usage
input_dict = {"name": "John", "age": 30, "city": "New York"}

result = dict_to_json_and_back(input_dict)
print(result)
