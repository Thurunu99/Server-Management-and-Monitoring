# Automated Server Health & Security Auditor

A Python-based server management and monitoring tool designed to automate infrastructure governance, audit system resources, and manage security processes. 

This project was developed in three logical phases to demonstrate a step-by-step approach to building a reliable server monitoring system.

## Project Structure & Evolution

This repository contains three main scripts, representing the progression of the project:

- 01_basic_check.py: The core resource monitor. Extracts real-time data on CPU usage, RAM utilization, and Storage capacity.
- 02_smart_alerts.py: Introduces intelligent threshold-based alerting (e.g., Warnings when RAM or CPU exceeds 80%) and performs a process audit to identify the top 3 memory-consuming applications.
- 03_process_killer.py: The security implementation. Automatically scans for specific unwanted or malicious processes (e.g., unauthorized executables) and safely terminates them to prevent system failure.

## Prerequisites

To run these scripts, you need to have Python installed along with the psutil library.

pip install psutil

## How to Run

Navigate to the project folder in your terminal and execute the scripts using Python:

python 01_basic_check.py
python 02_smart_alerts.py
python 03_process_killer.py

## Features Demonstrated

- Real-time System Resource Monitoring
- Threshold-based Automated Alerting
- Process Auditing and PID tracking
- Automated Threat/Process Termination
