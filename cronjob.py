# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 22:35:39 2021

@author: Thomas
"""

# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from main import cronjob

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(cronjob, "interval", seconds=30)

scheduler.start()