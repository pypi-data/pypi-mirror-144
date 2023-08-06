# Copyright (c) 2022-present, Ethan Henderson
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import annotations

import re

import requests
from packaging.version import Version

from deputil import BASE_URL


class Versioneer:
    def fetch_latest(
        self, package: str, *, include_prereleases: bool = False
    ) -> Version:
        if "[" in package:
            # Remove extras to allow parsing.
            package = re.sub("\[.*\]", "", package)

        if include_prereleases:
            return self.fetch_all(package)[-1]

        with requests.get(BASE_URL.format(package)) as resp:
            if not resp.ok:
                resp.raise_for_status()

            data = resp.json()

        return Version(data["info"]["version"])

    def fetch_all(self, package: str) -> list[Version]:
        if "[" in package:
            # Remove extras to allow parsing.
            package = re.sub("\[.*\]", "", package)

        with requests.get(BASE_URL.format(package)) as resp:
            if not resp.ok:
                resp.raise_for_status()

            data = resp.json()

        return [Version(release) for release in data["releases"].keys()]
