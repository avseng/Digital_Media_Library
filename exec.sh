#!/bin/bash
cd /var/www/html/$1
ls -1p | grep -v / | xargs echo | sed 's/ /, /g'
