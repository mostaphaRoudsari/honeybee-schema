# coding=utf-8
from __future__ import division

from honeybee_energy.lib.constructionsets import generic_construction_set, \
    construction_set_by_name

import honeybee_energy_standards  # make sure the standards data is there

import os
import json


def constructionset_complete(directory):
    dest_file = os.path.join(directory, 'constructionset_complete.json')
    with open(dest_file, 'w') as fp:
        json.dump(generic_construction_set.to_dict(True, False), fp, indent=4)


def constructionset_partial_exterior(directory):
    exterior_set = construction_set_by_name('2013::ClimateZone5::SteelFramed')
    dest_file = os.path.join(directory, 'constructionset_partial_exterior.json')
    with open(dest_file, 'w') as fp:
        json.dump(exterior_set.to_dict(True, True), fp, indent=4)


# run all functions within the file
master_dir = os.path.split(os.path.dirname(__file__))[0]
sample_directory = os.path.join(master_dir, 'honeybee_schema', 'samples')

constructionset_complete(sample_directory)
constructionset_partial_exterior(sample_directory)
