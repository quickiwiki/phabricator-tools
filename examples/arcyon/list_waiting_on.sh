# List out the revisions that require another user to act next.

# exit with error message if anything returns error status
trap 'echo FAILED; exit 1' ERR

echo Revisions you have authored, waiting on others:
arcyon query "$@" --author-me --status-type open --statuses 'Needs Review'

echo

echo Revisions you are reviewing, waiting on others:
arcyon query "$@" --reviewer-me --status-type open --statuses 'Needs Revision'
# -----------------------------------------------------------------------------
# Copyright (C) 2013-2014 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------ END-OF-FILE ----------------------------------
