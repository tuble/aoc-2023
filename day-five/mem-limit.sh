#!/bin/bash

ulimit -m 20480
exec python3 $@ 
