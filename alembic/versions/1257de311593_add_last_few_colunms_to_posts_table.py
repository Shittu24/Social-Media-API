"""add last few colunms to posts table

Revision ID: 1257de311593
Revises: d413ef3519c1
Create Date: 2022-09-02 17:29:20.717438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1257de311593'
down_revision = 'd413ef3519c1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'created_at')
    opdrop_column('posts', 'published')
    pass
