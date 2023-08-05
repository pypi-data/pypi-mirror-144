# Copyright 2021 AI Redefined Inc. <dev+cogment@ai-r.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class CogmentError(Exception):
    """Cogment specific exception class. All exceptions raised by Cogment are of this type."""

    def __init__(self, msg):
        super().__init__(msg)


class CogmentGenerateError(Exception):
    """Cogment generate specific exception class. All exceptions raised by Cogment generate are of this type."""

    def __init__(self, msg):
        super().__init__(msg)
