import sqlite3

def init_db():
    conn = sqlite3.connect('data/job_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            link TEXT,
            status TEXT DEFAULT "applied"
        )
    ''')
    conn.commit()
    conn.close()

def add_jobs(jobs):
    conn = sqlite3.connect('data/job_tracker.db')
    cursor = conn.cursor()
    for job in jobs:
        cursor.execute('''
            INSERT INTO jobs (title, company, location, link)
            VALUES (?, ?, ?, ?)
        ''', (job['title'], job['company'], job['location'], job['link']))
    conn.commit()
    conn.close()

def get_all_jobs():
    conn = sqlite3.connect('data/job_tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, company, location, link, status FROM jobs")
    data = cursor.fetchall()
    conn.close()
    return data
