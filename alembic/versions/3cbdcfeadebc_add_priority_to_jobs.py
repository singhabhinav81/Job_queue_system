"""add priority to jobs

Revision ID: 3cbdcfeadebc
Revises: 501a095f1621
Create Date: 2025-05-28 23:17:58.744568

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3cbdcfeadebc'
down_revision: Union[str, None] = '501a095f1621'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
