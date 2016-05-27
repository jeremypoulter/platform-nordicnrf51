# Copyright 2014-present Ivan Kravets <me@ikravets.com>
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

from platformio.managers.platform import BasePlatform


class Nordicnrf51Platform(BasePlatform):

    def is_embedded(self):
        return True

    def configure_default_packages(self, variables, targets):
        if (variables.get("board") != "rfduino" and
                "tool-rfdloader" in self.get_packages()):
            del self.get_packages()['tool-rfdloader']

        return BasePlatform.configure_default_packages(
            self, variables, targets)