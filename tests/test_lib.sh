#!/bin/bash
set -e

export $(cat tests/test.env|grep -v '^#')

export TEST_LIBRARY=1

PYTHONPATH=. pytest -rxXs ${TAP_STREAM}
