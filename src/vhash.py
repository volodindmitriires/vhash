#!/usr/bin/env python
# coding: utf-8

import os
import sys
import pathlib
import hashlib


# Gets bytes of a file
def read_bytes(file_name: str) -> bytes:
    return pathlib.Path(file_name).read_bytes()


# Checks hashes
def vhash(input_file_path: str, target_dir_path: str):
    with open(input_file_path, 'r', encoding='utf8') as file:
        for line in file.readlines():
            try:
                target, hash_type, prev_hash = line.strip().split(" ")

                target_path = os.path.join(target_dir_path, target)
                if os.path.isfile(target_path) is False:
                    print(target, " NOT FOUND")
                    continue

                get_hash = getattr(hashlib, hash_type)
                actual_hash = get_hash(read_bytes(target_path)).hexdigest()
                if actual_hash.upper() == prev_hash.upper():
                    print(target, " OK")
                else:
                    print(target, " FAIL")
            except Exception:
                continue


# Handles arguments
if __name__ == "__main__":
    try:
        input_file = sys.argv[1]
        path = sys.argv[2]
        if os.path.isfile(input_file) is False:
            raise IOError
        if os.path.isdir(path) is False:
            raise IOError
        vhash(input_file, path)
    except Exception as ex:
        raise SystemExit(f"Usage: {sys.argv[0]} <path to the input file> <path to the directory containing the files to check>") from ex
