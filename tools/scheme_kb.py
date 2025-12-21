# tools/scheme_kb.py

# This is your data dictionary
SCHEMES_DATA = {
    "YSR Cheyutha": {
        "documents": ["Aadhar Card", "Caste Certificate", "Bank Passbook"],
        "description": "Financial assistance for women."
    },
    "General Welfare Scheme": {
        "documents": ["Aadhar Card", "Income Certificate"],
        "description": "A test scheme for general eligibility."
    },
    "Amma Vodi": {
        "documents": ["Aadhar Card", "White Rice Card"],
        "description": "Assistance for mothers."
    },
    "Rythu Bharosa": {
        "documents": ["Pattadar Passbook", "Aadhar Card"],
        "description": "Assistance for farmers."
    }
}

# THIS IS THE MISSING FUNCTION
def get_scheme_details(scheme_name):
    """
    Returns the details of a specific scheme.
    """
    # .get() helps prevent the app from crashing if a name is missing
    return SCHEMES_DATA.get(scheme_name, {
        "documents": ["Contact local Sachivalayam"],
        "description": "Details not available."
    })