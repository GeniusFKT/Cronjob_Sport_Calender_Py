import datetime
import os
import json

from utils.notion_api import create_page, create_database
from templates.sport_calender_template import get_item_template, get_database_template

# path
CRON_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(CRON_PATH)
DATA_PATH = os.path.join(PROJECT_PATH, "data", "data.json")


if __name__ == '__main__':
    # read data
    print(DATA_PATH)
    with open(DATA_PATH, 'r+') as f:
        data = json.load(f)
        today = datetime.date.today()

        if today.day == 1:
            year_month_str = today.strftime("%Y-%m")
            parent_database_id = data["sport_calender"]["parent_page_id"]

            new_database_id = create_database(get_database_template("运动日历 %s" % year_month_str, parent_database_id))
            data["sport_calender"]["calender_database_id"] = new_database_id

            f.seek(0, os.SEEK_SET)
            f.truncate(0)
            json.dump(data, f)

        database_id = data["sport_calender"]["calender_database_id"]
        create_page(get_item_template(database_id, today.strftime("%Y-%m-%d")))
