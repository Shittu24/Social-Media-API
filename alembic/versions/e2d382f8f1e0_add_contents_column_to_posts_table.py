"""add contents column to posts table

Revision ID: e2d382f8f1e0
Revises: bedd798204ea
Create Date: 2022-09-02 10:31:04.932334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2d382f8f1e0'
down_revision = 'bedd798204ea'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
