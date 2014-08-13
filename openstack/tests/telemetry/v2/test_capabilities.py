# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import testtools

from openstack.telemetry.v2 import capabilities

EXAMPLE = {
    "api": {"123": False,
            "135": True,
            "246": True, },
}


class TestMeter(testtools.TestCase):
    def test_basic(self):
        sot = capabilities.Capabilities()
        self.assertEqual('capabilities', sot.resource_key)
        self.assertEqual('capabilities', sot.resources_key)
        self.assertEqual('/v2/capabilities', sot.base_path)
        self.assertEqual('metering', sot.service.service_type)
        self.assertFalse(sot.allow_create)
        self.assertFalse(sot.allow_retrieve)
        self.assertFalse(sot.allow_update)
        self.assertFalse(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = capabilities.Capabilities(EXAMPLE)
        self.assertEqual(EXAMPLE['api'], sot.capabilities)
        self.assertFalse(sot.capabilities['123'])
        self.assertTrue(sot.capabilities['135'])
        self.assertTrue(sot.capabilities['246'])
