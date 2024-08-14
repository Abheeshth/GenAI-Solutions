def get_doctors(query):
    p = """
           Dr. Alice Smith,
           Dr. Bob Johnson,
           Dr. Charlie Brown
        """
    return p

def get_doctor_availability(doctor_name):
    availability = {
        "Dr. Alice Smith": "Monday to Friday, 9 AM - 5 PM",
        "Dr. Bob Johnson": "Tuesday to Saturday, 10 AM - 6 PM",
        "Dr. Charlie Brown": "Monday, Wednesday, Friday, 8 AM - 4 PM"
    }
    availability = availability[doctor_name]
    availability = str(availability)
    return availability



tool = [
    {
        "type": "function",
        "function": {
            "name": "get_doctors",
            "description": """Use this function to get a list of doctors' names.""",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "A query to get doctors' names.",
                    }
                },
                "required": ["query"],
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_doctor_availability",
            "description": """Use this function to get the availability of a specified doctor.""",
            "parameters": {
                "type": "object",
                "properties": {
                    "doctor_name": {
                        "type": "string",
                        "description": "The name of the doctor to check availability.",
                    }
                },
                "required": ["doctor_name"],
            }
        }
    }
]

