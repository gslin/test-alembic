"""create foo table

Revision ID: 99048941a2f6
Revises: f161ae372cf7
Create Date: 2025-04-14 17:30:20.552093

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99048941a2f6'
down_revision: Union[str, None] = 'f161ae372cf7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'foo',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('bar', sa.String(100), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('foo')
