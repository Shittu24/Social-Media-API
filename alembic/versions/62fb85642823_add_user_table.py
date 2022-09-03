"""add user table

Revision ID: 62fb85642823
Revises: e2d382f8f1e0
Create Date: 2022-09-02 16:59:09.470632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62fb85642823'
down_revision = 'e2d382f8f1e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
