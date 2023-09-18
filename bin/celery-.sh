#!/bin/bash

celery -A file_server worker -l info
