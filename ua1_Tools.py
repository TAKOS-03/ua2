#DALVIK UA_GENERATE_CODE

#CODE BY MUHAMMAD HAMMAD
# MUGHAL ZADA
import platform
import random

import os
import random
def clear():
    os.system('clear')
    print(logo)
#sys.stdout.write('\x1b]2; Tools M16 \x07')
logo=("""\033[1;32m
 d888888b  .d88b.   .d88b.  db      .d8888.
 `~~88~~' .8P  Y8. .8P  Y8. 88      88'  YP
    88    88    88 88    88 88      `8bo.
    88    88    88 88    88 88        `Y8b.
    88    `8b  d8' `8b  d8' 88booo. db   8D
    YP     `Y88P'   `Y88P'  Y88888P `8888Y'
\033[1;31m»\033[1;32m»\033[1;31m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m» 
\033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mAuthor   : \033[1;97mTOOLS sidou
\033[1;32m[\033[1;37m×\033[1;32m] \033[1;37mFacebook : \033[1;97msidou Tools 
\033[1;32m[\033[1;37m×\033[1;32m] \033[1;37mTool     : \033[1;32mPAID
\033[1;32m[\033[1;37m×\033[1;32m] \033[1;37mVersion  : \033[1;32m0.1
 \033[1;31m»\033[1;32m»\033[1;31m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m» 
 \033[1;32m[\033[1;37m+\033[1;32m] \033[1;37mCloning ids Saved in TOOLS folder
 \033[1;31m»\033[1;32m»\033[1;31m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»""")
clear()
print(' \033[1;32m[\033[1;37m×\033[1;32m] \033[1;31mTOOLS UA \033[97;1m[\033[1;32mUSERAGENT\033[97;1m] \033[1;32msidou\n\033[1;31m»\033[1;32m»\033[1;31m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»\033[1;31m»\033[1;32m»')
def generate_custom_user_agent():
    android_versions = ["Android 9", "Android 10", "Android 11", "Android 12"]
    selected_android_version = random.choice(android_versions)

    manufacturers = [
        "TECNO", "Samsung", "Xiaomi", 
       
    ]
    selected_manufacturer = random.choice(manufacturers)

    android_models = {
        "TECNO": ["KE5", "Model2", "Model3"],
        "Samsung": ["Galaxy S21", "Galaxy Note 20", "Galaxy A52"],
        "Xiaomi": ["Redmi Note 10", "POCO X3"],
        }

    selected_model = random.choice(android_models.get(selected_manufacturer, []))

    device_names = {
        "TECNO": "TecnoDevice",
        "Samsung": "SamsungDevice",
        "Xiaomi": "XiaomiDevice",
       
    }

    device_name = device_names.get(selected_manufacturer, "DefaultDevice")

    build_number = random.randint(1000, 9999)

    app_packages = ["com.facebook.katana", "com.facebook.ocra", "com.facebook.mlite"]
    selected_app_package = random.choice(app_packages)

    density_version = round(random.uniform(1.0, 3.0), 1)
    height_version = random.randint(500, 2000)
    width_version = random.randint(300, 1500)

    user_agent = (
        f"Dalvik/2.1.0 (Linux; U; {selected_android_version} Build/{build_number}; {selected_manufacturer} {selected_model})"
        f" [FBAN/{random.randint(100, 999)}.{random.randint(1, 9)}.{random.randint(0, 9)}.0;FBBV/{random.randint(100000000, 999999999)};FBRV/{random.randint(0, 9)};"
        f"{selected_app_package};FBLC/en_US;FBMF/{selected_manufacturer};FBBD/{selected_manufacturer};FBDV/{selected_model};"
        f"FBSV/{random.randint(8, 12)};FBCA/armeabi-v7a:armeabi;FBDM/{{density={density_version},width={width_version},height={height_version}}};FB_FW/{random.randint(1, 3)};]"
    )

    return user_agent

# Example usage
custom_user_agent = generate_custom_user_agent()
print(custom_user_agent)