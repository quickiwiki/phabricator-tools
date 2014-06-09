"""Wrapper around 'git diff-index'.

Compares the content and mode of the blobs found via a tree object with the
content of the current index and, optionally ignoring the stat state of the
file on disk. When paths are specified, compares only those named paths.
Otherwise all entries in the index are compared.

"""
# =============================================================================
# CONTENTS
# -----------------------------------------------------------------------------
# phlgit_diffindex
#
# Public Functions:
#   is_index_dirty
#
# -----------------------------------------------------------------------------
# (this contents block is generated, edits will be lost)
# =============================================================================

from __future__ import absolute_import


def is_index_dirty(repo):
    """Return True if there are staged changes, False otherwise.

    :repo: a callable supporting git commands, e.g. repo("status")
    :returns: Bool

    """
    result = True
    if not repo("diff-index", "--cached", "HEAD", "--name-only"):
        result = False
    return result


# -----------------------------------------------------------------------------
# Copyright (C) 2014 Bloomberg Finance L.P.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# ------------------------------ END-OF-FILE ----------------------------------