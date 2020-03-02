#!/bin/bash

echo $(cat $1 | wc -l) $(cat $1 | wc -w) $(cat $1 | wc -c)
