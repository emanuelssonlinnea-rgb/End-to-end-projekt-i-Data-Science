TIER1_PHRASES = [
"Kravhantering", 
"Systemanalys", # New
"Systemarkitektur", # New
"Systemintegration", # New
"Verksamhetsutveckling", # New
"Cybersäkerhet", # New
"Oracle SOA Suite", # New 
"Docker",
]

TIER2_EXACT_CASE = {
    "A+": ["A+"],
    "Odoo": ["Odoo"],
    "SAP": ["SAP"],
    "R": ["R"],
    }

TIER3_CUSTOM = {
    "Internet Information Services": {
        "any_case": ["Internet Information Services", "Internet Information Services (IIS)"],
        "exact_case": ["IIS"],
    },
    "Oracle Cloud Infrastructure": {
        "any_case": ["Oracle Cloud Infrastructure", "Oracle Cloud Infrastructure (OCI)", "Oracle Cloud"],
        "exact_case": ["OCI"],
    }, # NeW
}