# # # # import requests
# # # # import json
# # # # import time

# # # # BASE_URL = "https://api.matricbiharboard.com/result"

# # # # roll_codes = [
# # # #     "73001","73002","73003","73004","73005","73006","73007","73008","73009","73010",
# # # #     "73011","73012","73013","73014","73015","73016","73017","73018","73019","73020",
# # # #     "73021","73022","73023","73024","73025","73026","73027","73028","73029","73030",
# # # #     "73031","73032","73033","73034","73035","73036","73037","73038","73039","73040",
# # # #     "73041","73042","73043","73044","73045","73046","73047","73048","73049","73050",
# # # #     "73051","73052","73053","73054","73055","73056","73057","73058","73059","73060",
# # # #     "73061","73062","73063","73064","73065","73066","73067","73068","73069","73070",
# # # #     "73071","73072","73073","73074","73075","73076","73077","73078","73079","73080",
# # # #     "73081","73082","73083","73084","73085","73086","73087","73088","73089","73090",
# # # #     "73091","73092","73093","73094","73095","73096","73097","73098","73099","73100",
# # # #     "73101","73102","73103","73104","73105","73106","73107","73108","73109","73110",
# # # #     "73111","73112","73113","73114","73115","73116","73117","73118","73119","73120",
# # # #     "73121","73122",
# # # #     "73301","73302","73303","73305","73306","73307","73308","73309","73310",
# # # #     "73501","73502","73503","73504","73505","73506","73507","73508","73509","73510",
# # # #     "73511","73512","73513","73514","73515","73516","73517","73518","73519","73520",
# # # #     "73521"
# # # # ]

# # # # START_ROLL = 2600000
# # # # MAX_ATTEMPTS_WITHOUT_RESULT = 20   # stop after 20 continuous failures

# # # # all_results = []

# # # # for code in roll_codes:
# # # #     print(f"\n🔍 Scanning Roll Code: {code}")
    
# # # #     roll_no = START_ROLL
# # # #     fail_count = 0

# # # #     while True:
# # # #         try:
# # # #             params = {
# # # #                 "roll_code": code,
# # # #                 "roll_no": str(roll_no)
# # # #             }

# # # #             response = requests.get(BASE_URL, params=params, timeout=10)

# # # #             if response.status_code == 200:
# # # #                 data = response.json()

# # # #                 # ✅ Check valid student
# # # #                 if data.get("success") and data.get("data") and data["data"].get("name"):
# # # #                     print(f"✅ Found: {code}-{roll_no} -> {data['data']['name']}")
                    
# # # #                     all_results.append({
# # # #                         "roll_code": code,
# # # #                         "roll_no": roll_no,
# # # #                         "name": data["data"]["name"],
# # # #                         "school": data["data"]["school_name"],
# # # #                         "total": data["data"]["total"],
# # # #                         "division": data["data"]["division"]
# # # #                     })

# # # #                     fail_count = 0   # reset on success

# # # #                 else:
# # # #                     print(f"❌ No data: {code}-{roll_no}")
# # # #                     fail_count += 1

# # # #             else:
# # # #                 print(f"⚠️ Failed request: {code}-{roll_no}")
# # # #                 fail_count += 1

# # # #             # 🔴 Stop condition
# # # #             if fail_count >= MAX_ATTEMPTS_WITHOUT_RESULT:
# # # #                 print(f"⛔ Stopping {code} (no more students)")
# # # #                 break

# # # #             roll_no += 1
# # # #             time.sleep(0.3)

# # # #         except Exception as e:
# # # #             print(f"🚫 Error: {code}-{roll_no} -> {e}")
# # # #             fail_count += 1

# # # # # 💾 Save results
# # # # with open("bseb_results_clean.json", "w", encoding="utf-8") as f:
# # # #     json.dump(all_results, f, indent=4, ensure_ascii=False)

# # # # print("\n🎉 Done! Data saved to bseb_results_clean.json")



# # # import requests
# # # import json
# # # import time
# # # import random

# # # BASE_URL = "https://api.matricbiharboard.com/result"

# # # roll_codes = [
# # #     "73001","73002","73003","73004","73005","73006","73007","73008","73009","73010",
# # #     "73011","73012","73013","73014","73015","73016","73017","73018","73019","73020",
# # #     "73021","73022","73023","73024","73025","73026","73027","73028","73029","73030",
# # #     "73031","73032","73033","73034","73035","73036","73037","73038","73039","73040",
# # #     "73041","73042","73043","73044","73045","73046","73047","73048","73049","73050",
# # #     "73051","73052","73053","73054","73055","73056","73057","73058","73059","73060",
# # #     "73061","73062","73063","73064","73065","73066","73067","73068","73069","73070",
# # #     "73071","73072","73073","73074","73075","73076","73077","73078","73079","73080",
# # #     "73081","73082","73083","73084","73085","73086","73087","73088","73089","73090",
# # #     "73091","73092","73093","73094","73095","73096","73097","73098","73099","73100",
# # #     "73101","73102","73103","73104","73105","73106","73107","73108","73109","73110",
# # #     "73111","73112","73113","73114","73115","73116","73117","73118","73119","73120",
# # #     "73121","73122",
# # #     "73301","73302","73303","73305","73306","73307","73308","73309","73310",
# # #     "73501","73502","73503","73504","73505","73506","73507","73508","73509","73510",
# # #     "73511","73512","73513","73514","73515","73516","73517","73518","73519","73520",
# # #     "73521"
# # # ]

# # # START_ROLL = 2600000
# # # MAX_FAIL = 15   # stop faster (optimized)

# # # # Headers to avoid blocking
# # # HEADERS = {
# # #     "User-Agent": "Mozilla/5.0",
# # #     "Accept": "application/json"
# # # }

# # # all_results = []
# # # seen = set()  # prevent duplicates


# # # # 🔁 Safe request with retry
# # # def safe_request(params):
# # #     retries = 3
# # #     delay = 1

# # #     for _ in range(retries):
# # #         try:
# # #             res = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=10)

# # #             if res.status_code == 200:
# # #                 return res.json()

# # #             elif res.status_code == 429:
# # #                 print("⛔ Rate limited... waiting")
# # #                 time.sleep(delay)
# # #                 delay *= 2

# # #         except Exception as e:
# # #             print("⚠️ Retry error:", e)
# # #             time.sleep(delay)
# # #             delay *= 2

# # #     return None


# # # # 🔍 Main loop
# # # for code in roll_codes:
# # #     print(f"\n🔍 Scanning Roll Code: {code}")

# # #     roll_no = START_ROLL
# # #     fail_count = 0

# # #     while True:
# # #         key = f"{code}-{roll_no}"

# # #         # skip duplicates
# # #         if key in seen:
# # #             roll_no += 1
# # #             continue

# # #         params = {
# # #             "roll_code": code,
# # #             "roll_no": str(roll_no)
# # #         }

# # #         data = safe_request(params)

# # #         if data and data.get("success") and data.get("data") and data["data"].get("name"):
# # #             student = data["data"]

# # #             print(f"✅ Found: {key} -> {student['name']}")

# # #             all_results.append({
# # #                 "roll_code": code,
# # #                 "roll_no": roll_no,
# # #                 "name": student.get("name"),
# # #                 "father_name": student.get("father_name"),
# # #                 "school": student.get("school_name"),
# # #                 "total": student.get("total"),
# # #                 "division": student.get("division")
# # #             })

# # #             seen.add(key)
# # #             fail_count = 0

# # #         else:
# # #             print(f"❌ No data: {key}")
# # #             fail_count += 1

# # #         # 🔴 Stop condition
# # #         if fail_count >= MAX_FAIL:
# # #             print(f"⛔ Stopping {code} (no more students)")
# # #             break

# # #         roll_no += 1

# # #         # 🎯 Smart random delay
# # #         time.sleep(random.uniform(0.7, 1.5))


# # # # 💾 Save JSON
# # # with open("bseb_results_clean.json", "w", encoding="utf-8") as f:
# # #     json.dump(all_results, f, indent=4, ensure_ascii=False)

# # # print("\n🎉 Done! Data saved to bseb_results_clean.json")

# # import requests
# # import json
# # import time
# # import random

# # BASE_URL = "https://api.matricbiharboard.com/result"

# # roll_codes = [
# #     "73001","73002","73003","73004","73005","73006","73007","73008","73009","73010",
# #     "73011","73012","73013","73014","73015","73016","73017","73018","73019","73020",
# #     "73021","73022","73023","73024","73025","73026","73027","73028","73029","73030",
# #     "73031","73032","73033","73034","73035","73036","73037","73038","73039","73040",
# #     "73041","73042","73043","73044","73045","73046","73047","73048","73049","73050",
# #     "73051","73052","73053","73054","73055","73056","73057","73058","73059","73060",
# #     "73061","73062","73063","73064","73065","73066","73067","73068","73069","73070",
# #     "73071","73072","73073","73074","73075","73076","73077","73078","73079","73080",
# #     "73081","73082","73083","73084","73085","73086","73087","73088","73089","73090",
# #     "73091","73092","73093","73094","73095","73096","73097","73098","73099","73100",
# #     "73101","73102","73103","73104","73105","73106","73107","73108","73109","73110",
# #     "73111","73112","73113","73114","73115","73116","73117","73118","73119","73120",
# #     "73121","73122",
# #     "73301","73302","73303","73305","73306","73307","73308","73309","73310",
# #     "73501","73502","73503","73504","73505","73506","73507","73508","73509","73510",
# #     "73511","73512","73513","73514","73515","73516","73517","73518","73519","73520",
# #     "73521"
# # ]

# # START_ROLL = 2600001
# # MAX_FAIL = 10   # faster stop

# # HEADERS = {
# #     "User-Agent": "Mozilla/5.0",
# #     "Accept": "application/json"
# # }

# # all_results = []


# # def safe_request(params):
# #     retries = 3
# #     delay = 1

# #     for _ in range(retries):
# #         try:
# #             res = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=10)

# #             if res.status_code == 200:
# #                 return res.json()

# #             elif res.status_code == 429:
# #                 print("⛔ Rate limited... waiting")
# #                 time.sleep(delay)
# #                 delay *= 2

# #         except Exception:
# #             time.sleep(delay)
# #             delay *= 2

# #     return None


# # for code in roll_codes:
# #     print(f"\n🔍 Scanning Roll Code: {code}")

# #     roll_no = START_ROLL
# #     fail_count = 0
# #     last_found = None

# #     while True:
# #         params = {
# #             "roll_code": code,
# #             "roll_no": str(roll_no)
# #         }

# #         data = safe_request(params)

# #         if data and data.get("success") and data.get("data") and data["data"].get("name"):
# #             student = data["data"]

# #             print(f"✅ Found: {code}-{roll_no} -> {student['name']}")

# #             all_results.append({
# #                 "roll_code": code,
# #                 "roll_no": roll_no,
# #                 "name": student.get("name"),
# #                 "school": student.get("school_name"),
# #                 "total": student.get("total"),
# #                 "division": student.get("division")
# #             })

# #             last_found = roll_no
# #             fail_count = 0

# #         else:
# #             print(f"❌ No data: {code}-{roll_no}")
# #             fail_count += 1

# #         # 🔴 Stop early if no more students
# #         if fail_count >= MAX_FAIL:
# #             print(f"⛔ Stopping {code}")
# #             if last_found:
# #                 print(f"🎯 Last valid roll: {last_found}")
# #             break

# #         roll_no += 1
# #         time.sleep(random.uniform(0.8, 1.5))


# # # 💾 Save JSON
# # with open("bseb_results_clean.json", "w", encoding="utf-8") as f:
# #     json.dump(all_results, f, indent=4, ensure_ascii=False)

# # print("\n🎉 Done! Data saved")

# import requests
# import json
# import time
# import random
# import os

# BASE_URL = "https://api.matricbiharboard.com/result"

# roll_codes = [
#     "73001","73002","73003","73004","73005","73006","73007","73008","73009","73010",
#     "73011","73012","73013","73014","73015","73016","73017","73018","73019","73020",
#     "73021","73022","73023","73024","73025","73026","73027","73028","73029","73030",
#     "73031","73032","73033","73034","73035","73036","73037","73038","73039","73040",
#     "73041","73042","73043","73044","73045","73046","73047","73048","73049","73050",
#     "73051","73052","73053","73054","73055","73056","73057","73058","73059","73060",
#     "73061","73062","73063","73064","73065","73066","73067","73068","73069","73070",
#     "73071","73072","73073","73074","73075","73076","73077","73078","73079","73080",
#     "73081","73082","73083","73084","73085","73086","73087","73088","73089","73090",
#     "73091","73092","73093","73094","73095","73096","73097","73098","73099","73100",
#     "73101","73102","73103","73104","73105","73106","73107","73108","73109","73110",
#     "73111","73112","73113","73114","73115","73116","73117","73118","73119","73120",
#     "73121","73122",
#     "73301","73302","73303","73305","73306","73307","73308","73309","73310",
#     "73501","73502","73503","73504","73505","73506","73507","73508","73509","73510",
#     "73511","73512","73513","73514","73515","73516","73517","73518","73519","73520",
#     "73521"
# ]

# START_ROLL = 2600001
# MAX_FAIL = 10

# HEADERS = {
#     "User-Agent": "Mozilla/5.0",
#     "Accept": "application/json"
# }

# RESULT_FILE = "bseb_results_clean.json"

# # 🔁 Load previous data (if exists)
# if os.path.exists(RESULT_FILE):
#     with open(RESULT_FILE, "r", encoding="utf-8") as f:
#         all_results = json.load(f)
# else:
#     all_results = []

# # 🔍 Build last roll map
# last_roll_map = {}
# for item in all_results:
#     code = item["roll_code"]
#     roll = int(item["roll_no"])
#     if code not in last_roll_map or roll > last_roll_map[code]:
#         last_roll_map[code] = roll


# def safe_request(params):
#     retries = 3
#     delay = 1

#     for _ in range(retries):
#         try:
#             res = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=10)

#             if res.status_code == 200:
#                 return res.json()

#             elif res.status_code == 429:
#                 print("⛔ Rate limited... waiting")
#                 time.sleep(delay)
#                 delay *= 2

#         except:
#             time.sleep(delay)
#             delay *= 2

#     return None


# # 🔍 Main loop
# for code in roll_codes:
#     print(f"\n🔍 Scanning Roll Code: {code}")

#     # ✅ Start AFTER last found
#     start_roll = last_roll_map.get(code, START_ROLL)
#     if code in last_roll_map:
#         start_roll += 1

#     roll_no = start_roll
#     fail_count = 0

#     print(f"▶ Starting from: {roll_no}")

#     while True:
#         params = {
#             "roll_code": code,
#             "roll_no": str(roll_no)
#         }

#         data = safe_request(params)

#         if data and data.get("success") and data.get("data") and data["data"].get("name"):
#             student = data["data"]

#             print(f"✅ Found: {code}-{roll_no} -> {student['name']}")

#             all_results.append({
#                 "roll_code": code,
#                 "roll_no": roll_no,
#                 "name": student.get("name"),
#                 "school": student.get("school_name"),
#                 "total": student.get("total"),
#                 "division": student.get("division")
#             })

#             last_roll_map[code] = roll_no
#             fail_count = 0

#         else:
#             print(f"❌ No data: {code}-{roll_no}")
#             fail_count += 1

#         # 🔴 Stop condition
#         if fail_count >= MAX_FAIL:
#             print(f"⛔ Stopping {code}")
#             break

#         roll_no += 1
#         time.sleep(random.uniform(0.8, 1.5))

#     # 💾 Save progress after each roll_code
#     with open(RESULT_FILE, "w", encoding="utf-8") as f:
#         json.dump(all_results, f, indent=4, ensure_ascii=False)


# print("\n🎉 Done! All data saved")

import requests
import json
import time
import random
import os

BASE_URL = "https://api.matricbiharboard.com/result"

roll_codes = [
    "73001","73002","73003","73004","73005","73006","73007","73008","73009","73010",
    "73011","73012","73013","73014","73015","73016","73017","73018","73019","73020",
    "73021","73022","73023","73024","73025","73026","73027","73028","73029","73030",
    "73031","73032","73033","73034","73035","73036","73037","73038","73039","73040",
    "73041","73042","73043","73044","73045","73046","73047","73048","73049","73050",
    "73051","73052","73053","73054","73055","73056","73057","73058","73059","73060",
    "73061","73062","73063","73064","73065","73066","73067","73068","73069","73070",
    "73071","73072","73073","73074","73075","73076","73077","73078","73079","73080",
    "73081","73082","73083","73084","73085","73086","73087","73088","73089","73090",
    "73091","73092","73093","73094","73095","73096","73097","73098","73099","73100",
    "73101","73102","73103","73104","73105","73106","73107","73108","73109","73110",
    "73111","73112","73113","73114","73115","73116","73117","73118","73119","73120",
    "73121","73122",
    "73301","73302","73303","73305","73306","73307","73308","73309","73310",
    "73501","73502","73503","73504","73505","73506","73507","73508","73509","73510",
    "73511","73512","73513","73514","73515","73516","73517","73518","73519","73520",
    "73521"
]

START_ROLL = 2600001 
MAX_FAIL = 10

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

RESULT_FILE = "bseb_results_clean.json"

# 🔁 Load previous data if exists
if os.path.exists(RESULT_FILE):
    with open(RESULT_FILE, "r", encoding="utf-8") as f:
        all_results = json.load(f)
else:
    all_results = []

print(f"📂 Loaded {len(all_results)} records")

# 🔍 Build last roll map
last_roll_map = {}
for item in all_results:
    code = item["roll_code"]
    roll = int(item["roll_no"])
    if code not in last_roll_map or roll > last_roll_map[code]:
        last_roll_map[code] = roll

print("📊 Last Roll Map:", last_roll_map)


def safe_request(params):
    retries = 3
    delay = 1

    for _ in range(retries):
        try:
            res = requests.get(BASE_URL, params=params, headers=HEADERS, timeout=10)

            if res.status_code == 200:
                return res.json()

            elif res.status_code == 429:
                print("⛔ Rate limited... waiting")
                time.sleep(delay)
                delay *= 2

        except:
            time.sleep(delay)
            delay *= 2

    return None


# 🔍 Main loop
for code in roll_codes:

    # ✅ Skip already completed roll codes
    if code in last_roll_map:
        print(f"⏭ Skipping {code}, already done till {last_roll_map[code]}")
        continue

    print(f"\n🔍 Scanning Roll Code: {code}")

    roll_no = START_ROLL
    fail_count = 0

    while True:
        params = {
            "roll_code": code,
            "roll_no": str(roll_no)
        }

        data = safe_request(params)

        if data and data.get("success") and data.get("data") and data["data"].get("name"):
            student = data["data"]

            print(f"✅ Found: {code}-{roll_no} -> {student['name']}")

            all_results.append({
                "roll_code": code,
                "roll_no": roll_no,
                "name": student.get("name"),
                "father_name": student.get("father_name"),
                "school": student.get("school_name"),
                "total": student.get("total"),
                "division": student.get("division")
            })

            last_roll_map[code] = roll_no
            fail_count = 0

        else:
            print(f"❌ No data: {code}-{roll_no}")
            fail_count += 1

        # 🔴 Stop condition
        if fail_count >= MAX_FAIL:
            print(f"⛔ Finished {code} (last roll: {last_roll_map.get(code)})")
            break

        roll_no += 1
        time.sleep(random.uniform(0.8, 1.5))

    # 💾 Save after each roll code
    with open(RESULT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=4, ensure_ascii=False)


print("\n🎉 Done! All data saved")