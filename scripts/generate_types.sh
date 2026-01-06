#!/bin/bash
set -e

# Ensure we are in the sdk root or handle paths correctly
# This script assumes it's run from the cli/python-sdk directory or we can find the schema relative to it.

SCHEMA_PATH="../../apps/docs/public/api-reference.json"
OUTPUT_PATH="unsent/types.py"

echo "Generating Pydantic models from ${SCHEMA_PATH}..."

# check if schema exists
if [ ! -f "$SCHEMA_PATH" ]; then
    echo "Error: Schema file not found at $SCHEMA_PATH"
    exit 1
fi

# Generate models
# --input-file-type openapi: Explicitly state input is OpenAPI
# --output-model-type pydantic_v2.BaseModel: Use Pydantic v2
# --target-python-version 3.8: Ensure compatibility
# --use-schema-description: Use descriptions from schema docstrings
# --field-constraints: Use field constraints if available
# --disable-timestamp: Avoid adding timestamp to header to keep diffs clean
poetry run python -m datamodel_code_generator \
  --input "$SCHEMA_PATH" \
  --output "$OUTPUT_PATH" \
  --input-file-type openapi \
  --output-model-type pydantic_v2.BaseModel \
  --target-python-version 3.10 \
  --use-schema-description \
  --disable-timestamp \
  --openapi-scopes paths parameters schemas \
  --use-standard-collections \
  --use-union-operator

# Post-processing: Remove 'V1' prefix from class names (e.g. V1EmailsPostRequest -> EmailsPostRequest)
# matches "V1" at start of word followed by an uppercase letter
# using perl for consistent cross-platform regex support (\b works)
perl -pi -e 's/\bV1([A-Z])/$1/g' "$OUTPUT_PATH"

echo "Done. Models generated at ${OUTPUT_PATH}"
