#!/usr/bin/env python3

import json
import os
import re
import sys

from mozilla_schema_generator.glean_ping import GleanPing


glean_mapping = dict((id.replace('-', '_'), name) for (name, id) in GleanPing.get_repos())


os.chdir(os.path.join(sys.argv[1], 'schemas'))
tables = []
for root, dirs, files in os.walk('.'):
    if 'metadata' in root:
        # metadata is some weird other thing
        # FIXME: figure out what it is
        continue
    try:
        bq_file = next(f for f in files if f.endswith('.bq'))
    except StopIteration:
        # if there is no bq file, not in BigQuery?
        # FIXME: interrogate this assumption
        continue
    (dataset_name, table_name) = root[2:].replace('-', '_').split('/')
    path = "/".join([root[2:], bq_file])
    version = re.sub(r'.*([0-9]+).bq', r"\1", bq_file)
    bq_definition = 'https://github.com/mozilla-services/mozilla-pipeline-schemas/blob/generated-schemas/schemas/' + path
    bq_definition_raw_json = 'https://raw.githubusercontent.com/mozilla-services/mozilla-pipeline-schemas/generated-schemas/schemas/' + path
    table = {'name': table_name, 'dataset': dataset_name, 'version': version, 'bq_definition': bq_definition, 'bq_definition_raw_json': bq_definition_raw_json }
    if glean_mapping.get(dataset_name):
        table['glean_app'] = glean_mapping[dataset_name]
    tables.append(table)

print(json.dumps(tables))
"""
Some implementation notes


Main:

JSON Schema: https://github.com/mozilla-services/mozilla-pipeline-schemas/blob/master/schemas/telemetry/main/main.4.schema.json
BigQuery definition: https://github.com/mozilla-services/mozilla-pipeline-schemas/blob/generated-schemas/schemas/telemetry/main/main.4.bq
Stable table: telemetry_stable.main_v4
Live table: telemetry_live.main_v4
View: telemetry.main

mozregression usage:

JSON Schema: N/A
BigQuery definition: https://github.com/mozilla-services/mozilla-pipeline-schemas/blob/generated-schemas/schemas/org-mozilla-mozregression/usage/usage.1.bq
Stable table: org_mozilla_mozregression_stable.usage_v1
Live: org_mozilla_mozregression_live.usage_v1
View: org_mozilla_mozregression.usage
"""
