# SPDX-FileCopyrightText: 2023 Phu Hung Nguyen <phuhnguyen@outlook.com>
# SPDX-License-Identifier: LGPL-2.1-or-later

import copy
import logging
import os
from typing import List

from markdown_it import MarkdownIt

from .extraction_utils import Entry, I18NEnv


def i12ize_content_file(i18n_env: I18NEnv):
    with open(i18n_env.src_path) as f_content:
        # copy to a new object so that one file's env isn't carried over to that of another
        i18n_env.mdi.render(f_content.read(), copy.copy(i18n_env.__dict__))


def i12ize_content_domain(domain_paths: List[str], entries: List[Entry], mdi: MarkdownIt):
    for src_path in domain_paths:
        if os.path.isfile(src_path):
            i12ize_content_file(I18NEnv(src_path, entries, mdi))
            logging.info(src_path)
