#!/bin/bash

pids=$(pgrep rpicam-still)
kill $pids