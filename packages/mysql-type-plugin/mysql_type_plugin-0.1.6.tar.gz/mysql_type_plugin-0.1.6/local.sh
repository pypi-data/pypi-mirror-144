#!/bin/bash
rm -f target/wheels/*
~/.local/bin/maturin build && ~/.local/bin/pip3 install --force-reinstall target/wheels/mysql_type_plugin-*.whl