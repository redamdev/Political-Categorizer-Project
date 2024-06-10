#!/bin/bash

cd frontend
npm run dev & # Run React in the background

cd ../backend
python main.py
