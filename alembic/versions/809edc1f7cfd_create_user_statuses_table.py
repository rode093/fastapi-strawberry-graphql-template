"""create user statuses table

Revision ID: 809edc1f7cfd
Revises: 0cc377db1551
Create Date: 2023-07-09 15:38:44.814361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '809edc1f7cfd'
down_revision = '0cc377db1551'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('user_statuses',
                    sa.Column(
                        'code', sa.String(16), primary_key=True),
                    sa.Column('label', sa.String(32), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('user_statuses')
