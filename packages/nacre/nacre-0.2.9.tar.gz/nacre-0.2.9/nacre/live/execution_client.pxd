# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2021 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

from libc.stdint cimport int64_t
from nautilus_trader.common.providers cimport InstrumentProvider
from nautilus_trader.execution.client cimport ExecutionClient
from nautilus_trader.live.execution_client cimport LiveExecutionClient as NautilusLiveExecutionClient
from nautilus_trader.model.c_enums.oms_type cimport OMSType
from nautilus_trader.model.identifiers cimport AccountId
from nautilus_trader.model.identifiers cimport Venue
from nautilus_trader.model.events.account cimport AccountState

from nacre.model.report_position cimport ReportedAccount


cdef class LiveExecutionClient(NautilusLiveExecutionClient):
    cpdef void _set_venue(self, Venue venue) except *
    cpdef void _set_account_id(self, AccountId account_id) except *
    cpdef void generate_account_snapshot(self, AccountState account_state) except *

    cpdef void generate_reported_account(self, list positions, list balances, int64_t ts_event) except *
    cpdef void _send_reported_position_state(self, ReportedAccount account) except *
