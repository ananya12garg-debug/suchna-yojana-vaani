
# prototype.py - SUCHNA Core - Testable in 5 min
# Run: python prototype.py

# Simulated RAG + Verifier - No API key needed for demo
schemes_db = {
    "pm_awas": {"name": "PM Awas Yojana", "amount": "Rs 1.2 lakh", "eligibility": "kachcha house, income <3 lakh", "fee": 0},
    "ladli_behna": {"name": "Ladli Behna", "amount": "Rs 1500/month", "eligibility": "woman, MP domicile", "fee": 0},
    "pm_kisan": {"name": "PM Kisan", "amount": "Rs 6000/year", "eligibility": "farmer", "fee": 0},
    "nsp_scholarship": {"name": "NSP Scholarship", "amount": "Rs 50k", "eligibility": "12th 80%+, income <2.5L", "fee": 0},
}

official_rates = {
    "auto_gwl_station_to_fort": 150,
    "guide_gwalior": 300,
    "parking_2wheeler": 20,
    "caste_certificate": 50,
}

def check_eligibility(user_profile):
    """user_profile: dict with income, house_type, gender etc."""
    eligible = []
    if user_profile.get("house_type") == "kachcha":
        eligible.append(schemes_db["pm_awas"])
    if user_profile.get("gender") == "female":
        eligible.append(schemes_db["ladli_behna"])
    if user_profile.get("occupation") == "farmer":
        eligible.append(schemes_db["pm_kisan"])
    if user_profile.get("marks", 0) >= 80:
        eligible.append(schemes_db["nsp_scholarship"])
    return eligible

def verify_fee(service, charged):
    official = official_rates.get(service, 0)
    if charged > official * 1.2:
        return f"⚠️ OVERCHARGE! Official {service} = Rs {official}, Charged = Rs {charged}. Extra {charged-official} is bribe. Show official circular."
    else:
        return f"✅ OK. Official = Rs {official}, Charged = Rs {charged}"

# Test 1: Poverty family
print("=== Test 1: Poor family in Gwalior ===")
family = {"house_type": "kachcha", "gender": "female", "occupation": "farmer", "income": 200000}
print(f"Eligible schemes: {[s['name']+': '+s['amount'] for s in check_eligibility(family)]}")

# Test 2: Tourist scam
print("\n=== Test 2: Tourist at Gwalior Fort ===")
print(verify_fee("auto_gwl_station_to_fort", 350))
print(verify_fee("guide_gwalior", 800))

# Test 3: Scholarship OTR
print("\n=== Test 3: Scholarship ===")
student = {"marks": 85, "income": 200000, "house_type": "kachcha"}
print(f"Eligible: {[s['name'] for s in check_eligibility(student)]} - Official Fee Rs 0, Agent asks Rs 500 -> {verify_fee('caste_certificate', 500)}")

print("\n=== Prototype works! Ready for RAG + Bhashini integration ===")
