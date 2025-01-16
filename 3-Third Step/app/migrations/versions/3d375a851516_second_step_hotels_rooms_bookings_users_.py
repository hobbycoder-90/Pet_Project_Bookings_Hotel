"""Second Step Hotels Rooms Bookings Users models

Revision ID: 3d375a851516
Revises: 2adba8c4c014
Create Date: 2025-01-10 04:32:03.467105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d375a851516'
down_revision: Union[str, None] = '2adba8c4c014'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
