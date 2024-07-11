# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.review package is deprecated, please change your
    imports to import from stripe directly.
    From:
      from stripe.api_resources.review import Review
    To:
      from stripe import Review
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe._review import (  # noqa
        Review,
    )
