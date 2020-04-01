import time, schedule, subprocess

def scrape_job():
    subprocess.call(['pipenv', 'run', 'scrape'])

def slack_job():
    subprocess.call(['pipenv', 'run', 'slack'])

schedule.every(12).hours.do(scrape_job)
schedule.every(1).hours.do(slack_job)

while True:
    schedule.run_pending()
    time.sleep(1)